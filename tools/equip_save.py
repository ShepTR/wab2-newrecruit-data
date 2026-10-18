#!/usr/bin/env python3
"""Armour Save line + encumbrance on Move, computed from the equipment chosen (WAB2 rulebook pp.95-98).
Each model gets an 'Armour Save' profile (Save, With conditional bonuses, Notes). Modifiers on that profile and on the Model profile's M
change the values for every combination of the unit's armour / shield / barding / mount options.
Usage: python3 equip_save.py <outdir>   (idempotent; run after equip_defs.py)"""
import sys, os, re, glob, hashlib, html, itertools
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
g = open(GST, encoding='utf8').read()
PT = hid('ptype', 'Armour Save')
CT = {k: hid('ctype', k) for k in ('Save', 'With conditional bonuses', 'Notes')}
if f'id="{PT}"' not in g:
    pt = (f'    <profileType id="{PT}" name="Armour Save">\n      <characteristicTypes>\n' +
          ''.join(f'        <characteristicType id="{v}" name="{k}"/>\n' for k, v in CT.items()) + '      </characteristicTypes>\n    </profileType>\n')
    g = g.replace('  </profileTypes>', pt + '  </profileTypes>', 1)
    open(GST, 'w', encoding='utf8').write(g)
PROFILES = set(re.findall(r'<profile id="[^"]*" name="([^"]*)"', re.search(r'<sharedProfiles>(.*?)</sharedProfiles>', g, re.S).group(1)))
M_CT = '35a2-714d-db3e-3738'

ARMOUR = ['Light Armour', 'Heavy Armour', 'Cataphract Armour', 'Partial Plate Armour', 'Full Plate Armour']
SHIELDS = ['Shield', 'Large Shield', 'Buckler', 'Pavise']
BARD = ['Full Metal Barding', 'Half Metal Barding', 'Full Cloth Barding', 'Half Cloth Barding']
EQ = set(ARMOUR + SHIELDS + BARD)
MAP = {'light armour': 'Light Armour', 'light': 'Light Armour', 'heavy armour': 'Heavy Armour', 'shield': 'Shield', 'large shield': 'Large Shield',
       'buckler': 'Buckler', 'cataphract armour': 'Cataphract Armour', 'partial plate armour': 'Partial Plate Armour', 'full plate armour': 'Full Plate Armour',
       'pavise': 'Pavise', 'barding': 'Full Metal Barding', 'cloth barding': 'Full Cloth Barding', 'cloth barded': 'Full Cloth Barding'}
HORSE = re.compile(r'^(horse|ride a horse|riding horses|mounted on horses|warhorse|ride a warhorse|mounted on a warhorse)', re.I)
def effect(label):
    l = html.unescape(label).lower(); add, rem, horse = [], [], False
    if HORSE.match(l): return [], [], True
    m = re.match(r'exchange (.+?) for (?:a |an )?(.+)$', l)
    if m:
        rem += [MAP.get(t.strip()) for t in re.split(r' and ', m.group(1))]; add.append(MAP.get(re.sub(r'\s*\(.*', '', m.group(2))))
    else:
        r = re.search(r'replaces ([a-z ]+?)[;)]', l)
        if r: rem.append(MAP.get(r.group(1).strip()))
        for t in re.split(r' and ', re.sub(r'\s*\(.*', '', l)): add.append(MAP.get(t.strip()))
    return [a for a in add if a in EQ], [x for x in rem if x in EQ], False

INF = {'None': 7, 'Light Armour': 6, 'Heavy Armour': 5, 'Cataphract Armour': 4, 'Partial Plate Armour': 4, 'Full Plate Armour': 3}
CAV = {'None': 6, 'Light Armour': 5, 'Heavy Armour': 4, 'Cataphract Armour': 3, 'Partial Plate Armour': 3, 'Full Plate Armour': 3}
def calc(cav, armour, shields, bard, skirm):
    base = (CAV if cav else INF)[armour]
    nobonus = armour in ('Cataphract Armour', 'Full Plate Armour') or (cav and armour == 'Partial Plate Armour')
    unc = cnd = 0; notes = []
    sp = {'Shield': 1, 'Large Shield': 2, 'Buckler': 1, 'Pavise': 2}
    if not nobonus:
        for s in shields:
            if s == 'Buckler' and not skirm: cnd = max(cnd, 1); notes.append('Buckler +1 in hand-to-hand only')
            elif s == 'Pavise': cnd = max(cnd, 2); notes.append('Pavise +2 when shot at from the front only')
            else: unc = max(unc, sp[s])
    cu = cc = 0
    if cav:
        for b in bard:
            if b == 'Full Metal Barding': cu = 1
            elif b == 'Half Metal Barding': cc = 1; notes.append('Half metal barding +1 when hit from the front')
            elif b == 'Full Cloth Barding': cc = 1; notes.append('Cloth barding +1 in hand-to-hand only')
            elif b == 'Half Cloth Barding': cc = 1; notes.append('Half cloth barding +1 in hand-to-hand from the front only')
    cap = 2 if (cav and bard) else 3
    gen = max(cap, base - unc - cu)
    best = max(cap, base - max(unc, cnd) - max(cu, cc))
    metal = cav and any(b in bard for b in ('Full Metal Barding', 'Half Metal Barding'))
    pen = 0
    if not cav and gen <= 4: pen += 1
    if cav and max(3, base - unc) <= 3: pen += 1       # save of 3+ ignoring barding
    if metal: pen += 1
    return gen, best, notes, pen
def fmt(v): return 'None' if v >= 7 else f'{v}+'
CAVRX = re.compile(r'cavalry|camel|cataphract|horsemen|horse archer|riders|equites|hobilar|lancer|praefectus equitum|tarentine', re.I)
SKIPU = re.compile(r'elephant|chariot|warhound|ballista|scorpio|bolt thrower|machine|artillery|crew|catapult', re.I)
NOTE = ('Armour save from armour, shield and barding bonus pips (rulebook pp.95-98); maximum 3+ (2+ for barded cavalry). '
        'M already includes encumbrance for armour/barding (p.96). Conditional pips are in the next column.')
cavlist = []; done = 0; capped = 0
def cond(scope, oid, on, incl):
    return (f'<condition field="selections" scope="{scope}" value="1" percentValue="false" shared="true" includeChildSelections="{incl}" '
            f'includeChildForces="false" childId="{oid}" type="{"atLeast" if on else "lessThan"}"/>')
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(m):
        global done, capped
        blk = m.group(0)
        if 'armour-save' in blk: return blk
        uname = html.unescape(re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1))
        uid = re.match(r'    <selectionEntry id="([^"]*)"', blk).group(1)
        ischar = 'name="Characters"' in blk.split('<selectionEntries>')[0]
        if SKIPU.search(uname) or 'name="Crew"' in blk: return blk
        notes = ' '.join(html.unescape(x) for x in re.findall(r'name="Equipment and options[^"]*"[^>]*>.*?<characteristic[^>]*>(.*?)</characteristic>', blk, re.S))
        skirm = bool(re.search(r'skirmish', notes, re.I))
        out = blk
        for mm in re.finditer(r'        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="model">\n.*?\n        </selectionEntry>\n', blk, flags=re.S):
            mblk = mm.group(0); mid = mm.group(1); mname = html.unescape(mm.group(2))
            if re.search(r'elephant|mahout|crew|chariot', mname, re.I): continue
            base_blk = re.sub(r'<selectionEntries>.*</selectionEntries>\n', '', mblk, flags=re.S)   # equipment options' definition links are not base equipment
            links = re.findall(r'<infoLink id="[^"]*" name="([^"]*)" hidden="false"[^>]*type="profile"', base_blk)
            armour = next((a for a in ARMOUR if a in links), 'None')
            shields = {x for x in SHIELDS if x in links}; bard = {x for x in BARD if x in links}
            basecav = bool(CAVRX.search(uname + ' ' + mname))
            # options belonging to this model
            if ischar:
                optblk = mblk; ind = 12; scope = mid; incl = 'true'
                opts = re.findall(r'^            <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade">\n(.*?)\n            </selectionEntry>\n', mblk, re.M | re.S)
            else:
                scope = uid; incl = 'false'
                opts = re.findall(r'^        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade">\n(.*?)\n        </selectionEntry>\n', blk, re.M | re.S)
                opts = [o for o in opts if not (re.search(r'childId="([^"]*)" repeats', o[2]) and re.search(r'childId="([^"]*)" repeats', o[2]).group(1) != mid)]
            R = []
            for oid, oname, ob in opts:
                a, r, h = effect(oname)
                if a or r or h: R.append((oid, oname, a, r, h))
            if not ischar and any(a_ and any(x in BARD for x in a_) for _, _, a_, _, _ in R): basecav = True
            if len(R) > 6: capped += 1; R = R[:6]
            if not R and armour == 'None' and not shields and not bard and not ischar: continue
            states = {}
            for k in range(len(R) + 1):
                for sub in itertools.combinations(range(len(R)), k):
                    ar, sh, bd, cv = armour, set(shields), set(bard), basecav
                    for i in sub:
                        oid, on, a, r, h = R[i]
                        for x in r:
                            if x in ARMOUR and ar == x: ar = 'None'
                            sh.discard(x); bd.discard(x)
                        for x in a:
                            if x in ARMOUR: ar = x
                            elif x in SHIELDS: sh.add(x)
                            elif x in BARD: bd.add(x)
                        if h: cv = True
                    gen, best, nt, pen = calc(cv, ar, sh, bd, skirm)
                    states[sub] = (gen, best, nt, pen, any(R[i][4] for i in sub))
            base = states[()]
            if basecav: cavlist.append(f'{os.path.basename(path)}: {uname}/{mname}')
            def conds(sub):
                return ''.join(f'                {cond(scope, R[i][0], i in sub, incl)}\n' for i in range(len(R)))
            def cond_text(st):
                gen, best, nt, pen, hz = st
                return (f'{fmt(best)} with ' + '; '.join(dict.fromkeys(nt))) if best != gen else '-'
            mods = ''
            for sub, st in states.items():
                if sub == () : continue
                if st[0] != base[0]:
                    mods += f'              <modifier type="set" field="{CT["Save"]}" value="{fmt(st[0])}">\n                <conditions>\n{conds(sub)}                </conditions>\n              </modifier>\n'
                if cond_text(st) != cond_text(base):
                    mods += f'              <modifier type="set" field="{CT["With conditional bonuses"]}" value="{esc(cond_text(st))}">\n                <conditions>\n{conds(sub)}                </conditions>\n              </modifier>\n'
            prof = (f'            <profile id="{hid(mid, "armour-save")}" name="Armour Save" hidden="false" typeId="{PT}" typeName="Armour Save">\n'
                    f'              <characteristics>\n                <characteristic name="Save" typeId="{CT["Save"]}">{fmt(base[0])}</characteristic>\n'
                    f'                <characteristic name="With conditional bonuses" typeId="{CT["With conditional bonuses"]}">{esc(cond_text(base))}</characteristic>\n'
                    f'                <characteristic name="Notes" typeId="{CT["Notes"]}">{esc(NOTE)}</characteristic>\n              </characteristics>\n'
                    + (f'              <modifiers>\n                <!-- armour-save -->\n{mods}              </modifiers>\n' if mods else '              <!-- armour-save -->\n') + '            </profile>\n')
            # Move modifiers for encumbrance
            mm_ = re.search(r'<characteristic name="M" typeId="' + M_CT + r'">([^<]*)</characteristic>', mblk)
            mmods = ''
            if mm_ and re.fullmatch(r'\d+', mm_.group(1).strip()):
                m0 = int(mm_.group(1).strip())
                for sub, st in states.items():
                    # a horse or warhorse raises Movement to 8" (Hannibal p.7); encumbrance is then taken off that
                    val = max(0, (8 if st[4] else m0) - st[3])
                    if val != m0:
                        mmods += f'              <modifier type="set" field="{M_CT}" value="{val}">\n                <conditions>\n{conds(sub)}                </conditions>\n              </modifier>\n'
            if not R: mmods = mmods.replace('                <conditions>\n                </conditions>\n', '')
            m2 = mblk
            pm = re.search(r'(            <profile id="[^"]*" name="[^"]*"[^>]*typeId="a802-40b5-d980-cabc"[^>]*>.*?)(            </profile>\n)', m2, re.S)
            if pm and mmods:
                inner = pm.group(1)
                m2 = m2.replace(pm.group(0), inner + f'              <modifiers>\n                <!-- encumbrance -->\n{mmods}              </modifiers>\n' + pm.group(2), 1)
            m2 = m2.replace('          </profiles>\n', prof + '          </profiles>\n', 1)
            out = out.replace(mblk, m2, 1); done += 1
        return out
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('armour save added to', done, 'models;', capped, 'models had more than 6 relevant options (first 6 used)')
if cavlist: open(os.path.join(OUT, 'tools', 'cavalry_units.txt'), 'w').write('\n'.join(sorted(set(cavlist))) + '\n')
print('cavalry treated models:', len(set(cavlist)))
