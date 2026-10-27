#!/usr/bin/env python3
"""Fractional loadouts ("up to half the figures exchange thrusting spear for composite bow", "up to a third ...") as separate model lines.
Generalises mix_models.py: the unit keeps its base model line and gets one extra model line per loadout (e.g. "Themata (Infantry) (bow)"):
  - the loadout line costs the base price plus the price difference of the option it replaces (the option is removed from the unit)
  - it is capped at (base figures) / (n-1)  =  at most 1/n of the unit (n=2 half, n=3 a third, n=4 a quarter)
  - the base line's minimum is reduced by the loadout figures, so the unit still has at least the normal minimum in total
  - loadouts of one unit share the allowance (bow OR crossbow)
  - the unit's other per-model options (armour, darts ...) are charged on the loadout figures too, unless the loadout is `locked`
    ("may take no further equipment") or the option is listed in `excl`
The table lives in tools/loadout_split.json: [{cat, unit, n, locked?, loadouts:[{name, opt?, delta?, drop?, add?, excl?, sv?}]}]
  name   suffix of the model line            opt    option entry the loadout replaces (price difference and weapon link come from it)
  delta  price difference when there is no option (or to override it)
  drop   weapon links removed from the loadout line (Thrusting Spear, Shield, Large Shield ...)   add  weapon links the line shows
  excl   options not charged on this line      sv     {"base": "-", "opt": "Light armour", "with": "6+"}: static save instead of the copied modifiers
  model  name of an existing model line that already is the loadout (only the cap is added)
Usage: python3 loadout_split.py <outdir>   (idempotent)"""
import sys, os, re, json, hashlib, glob
OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = json.load(open(os.path.join(HERE, 'loadout_split.json'), encoding='utf8'))
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def esc(n): return re.escape(n.replace('&', '&amp;'))
IDRE = re.compile(r'(\bid=")([0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4})(")')

def rep(child, per=1, scope='parent'):
    return (f'<repeat field="selections" scope="{scope}" value="{per}" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" repeats="1" roundUp="false"/>')
def fmt(x): return str(int(x)) if x == int(x) else str(x)

_LINKS = {}
def link_map():
    if not _LINKS:
        for f in glob.glob(os.path.join(OUT, '*.cat')) + glob.glob(os.path.join(OUT, '*.gst')):
            for m in re.finditer(r'<infoLink id="[^"]*" name="([^"]*)"[^>]*targetId="([^"]*)" type="profile"', open(f, encoding='utf8').read()):
                _LINKS.setdefault(m.group(1), m.group(2))
    return _LINKS

def strip_modifiers_with(block, oid):
    """remove every <modifier> element whose text mentions option id `oid`"""
    return re.sub(r'\n? *<modifier [^>]*>(?:(?!</modifier>).)*?%s(?:(?!</modifier>).)*?</modifier>' % re.escape(oid), '', block, flags=re.S)

def split_unit(s, sp):
    um = re.search(r'^    <selectionEntry id="([^"]*)" name="%s"[^>]*type="unit">\n.*?\n    </selectionEntry>\n' % esc(sp['unit']), s, re.S | re.M)
    if not um: raise SystemExit(f'{sp["cat"]}: no unit {sp["unit"]}')
    U, uid = um.group(0), um.group(1)
    if '<!-- loadout-split -->' in U: return s, False
    models = list(re.finditer(r'^        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="model">\n.*?\n        </selectionEntry>\n', U, re.S | re.M))
    if not models: raise SystemExit(f'{sp["cat"]}: {sp["unit"]} has no model')
    M, sid = models[0].group(0), models[0].group(1)
    mname = models[0].group(2)
    n = sp['n']; locked = sp.get('locked', False)
    per = n - 1                                                      # one loadout figure per `per` base figures
    mcons = re.search(r'<constraint [^>]*id="([^"]*)" type="min"/>', M)
    mcid = mcons.group(1)
    NU, newM, lids = U, M, []
    removed_opts = []
    built = []
    for lo in sp['loadouts']:
        label = lo['name']
        if 'model' in lo:                                           # existing model line: only the cap is added
            em = re.search(r'^        <selectionEntry id="([^"]*)" name="%s"[^>]*type="model">\n.*?\n        </selectionEntry>\n' % esc(lo['model']), NU, re.S | re.M)
            if not em: raise SystemExit(f'{sp["cat"]}: {sp["unit"]}: no model {lo["model"]}')
            built.append({'existing': em.group(0), 'id': em.group(1), 'lo': lo}); lids.append(em.group(1)); continue
        opt = None
        if lo.get('opt'):
            om = re.search(r'^        <selectionEntry id="([^"]*)" name="%s"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n' % esc(lo['opt']), NU, re.S | re.M)
            if not om: raise SystemExit(f'{sp["cat"]}: {sp["unit"]}: no option {lo["opt"]}')
            opt = om
        delta = lo.get('delta')
        if delta is None:
            if opt is None: delta = 0
            else:
                dm = re.search(r'<modifier type="increment" field="points" value="(-?[0-9.]+)"', opt.group(0))
                delta = float(dm.group(1)) if dm else float(re.search(r'<cost name="pts" typeId="points" value="(-?[0-9.]+)"', opt.group(0)).group(1))
        lid = hid(sid, 'loadout', label)
        B = IDRE.sub(lambda k: k.group(1) + hid(k.group(2), 'ls', label) + k.group(3), M)
        B = re.sub(r'^(        <selectionEntry id=")[^"]*(" name=")%s(")' % esc(mname), lambda k: k.group(1) + lid + k.group(2) + f'{mname} ({label})' + k.group(3), B, count=1, flags=re.M)
        B = re.sub(r'(<profile id="[^"]*" name=")%s(" [^>]*typeName="Model">)' % esc(mname), lambda k: k.group(1) + f'{mname} ({label})' + k.group(2), B, count=1)
        base = float(re.search(r'<cost name="pts" typeId="points" value="(-?[0-9.]+)"', B).group(1))
        B = re.sub(r'(<cost name="pts" typeId="points" value=")[^"]*(")', lambda k: k.group(1) + fmt(base + delta) + k.group(2), B, count=1)
        for lab in lo.get('drop', []):
            B, k = re.subn(r' *<infoLink id="[^"]*" name="%s"[^>]*?(?:/>|>.*?</infoLink>)\n' % re.escape(lab), '', B, flags=re.S)
        # weapon links: the option's own link becomes a permanent link on the loadout line, every other link tied to the option goes
        oid = opt.group(1) if opt else None
        for lab in lo.get('add', []):
            lm = re.search(r'( *)<infoLink id="([^"]*)" name="%s"([^>]*?)targetId="([^"]*)" type="profile"(?:/>|>.*?</infoLink>)\n' % re.escape(lab), B, re.S)
            if lm:
                B = B.replace(lm.group(0), f'{lm.group(1)}<infoLink id="{lm.group(2)}" name="{lab}" hidden="false" targetId="{lm.group(4)}" type="profile"/>\n', 1)
            else:
                tid = link_map().get(lab)
                if not tid: raise SystemExit(f'{sp["cat"]}: no profile link "{lab}"')
                x = f'            <infoLink id="{hid(lid, "link", lab)}" name="{lab}" hidden="false" targetId="{tid}" type="profile"/>\n'
                B = B.replace('          </infoLinks>\n', x + '          </infoLinks>\n', 1) if '          </infoLinks>\n' in B else B.replace('          <costs>\n', '          <infoLinks>\n' + x + '          </infoLinks>\n          <costs>\n', 1)
        if opt:             # the option's own note (rule entry) stays with the loadout line
            rm = re.search(r'^ *<rules>\n.*?\n *</rules>\n', opt.group(0), re.S | re.M)
            if rm:
                blk = IDRE.sub(lambda k: k.group(1) + hid(k.group(2), 'ls', label) + k.group(3), rm.group(0))
                B = B.replace('          <infoLinks>\n', blk + '          <infoLinks>\n', 1) if '          <infoLinks>\n' in B else B.replace('          <costs>\n', blk + '          <costs>\n', 1)
        built.append({'B': B, 'id': lid, 'lo': lo, 'opt': opt, 'oid': oid, 'label': label})
        lids.append(lid)
    # ---- caps and static saves on the loadout lines
    for b in built:
        lo = b['lo']
        if 'existing' in b:
            continue
        B = b['B']
        others = [x for x in built if x is not b]
        bcid = hid(b['id'], 'cap')
        # other options tied to this loadout in the copied block (hidden weapon-swap links referencing the removed option) must go
        for xo in [x['oid'] for x in built if x.get('oid')]:
            B = re.sub(r' *<infoLink id="[^"]*" name="[^"]*" hidden="true"[^>]*>(?:(?!</infoLink>).)*?%s(?:(?!</infoLink>).)*?</infoLink>\n' % re.escape(xo), '', B, flags=re.S)
            B = strip_modifiers_with(B, xo)
        if 'sv' in lo:
            sv = lo['sv']
            B = re.sub(r'(<characteristic name="Sv" typeId="[^"]*">)[^<]*(<)', lambda k: k.group(1) + sv['base'] + k.group(2), B)
            B = re.sub(r'(<characteristic name="Save" typeId="[^"]*">)[^<]*(<)', lambda k: k.group(1) + sv['base'] + k.group(2), B)
            B = re.sub(r'\n? *<!-- (?:sv-stat|encumbrance|armour-save) -->(?:\n *<modifier .*?</modifier>)+', '', B, flags=re.S)
            B = re.sub(r'\n *<modifiers>\s*</modifiers>', '', B)
            if sv.get('opt') and not locked and sv['opt'] not in lo.get('excl', []):   # the armour option still applies to these figures
                am = re.search(r'^        <selectionEntry id="([^"]*)" name="%s"[^>]*type="upgrade">' % esc(sv['opt']), U, re.M)
                if not am: raise SystemExit(f'{sp["cat"]}: {sp["unit"]}: no option {sv["opt"]}')
                def armour_mod(k):
                    cid = k.group(2)
                    x = (f'\n              <modifiers>\n                <!-- loadout-sv -->\n                <modifier type="set" field="{cid}" value="{sv["with"]}">\n'
                         f'                  <conditions>\n                    <condition field="selections" scope="{uid}" value="1" percentValue="false" shared="true" includeChildSelections="false" '
                         f'includeChildForces="false" childId="{am.group(1)}" type="atLeast"/>\n                  </conditions>\n                </modifier>\n              </modifiers>')
                    return k.group(0) + x
                B = re.sub(r'(<characteristic name="(?:Sv|Save)" typeId="([^"]*)">[^<]*</characteristic>\n(?: *<characteristic [^\n]*\n)* *</characteristics>)', armour_mod, B)
        # constraint: min -> max 0, raised by one per `per` base figures
        minre = re.compile(r'<constraint field="selections" scope="parent" value="\d+"([^>]*?) id="([^"]*)" type="min"/>')
        mc = minre.search(B)
        ncid = mc.group(2)
        B = minre.sub(lambda k: f'<constraint field="selections" scope="parent" value="0"{k.group(1)} id="{k.group(2)}" type="max"/>', B, count=1)
        mods = f'            <modifier type="increment" field="{ncid}" value="1">\n              <repeats>\n                {rep(sid, per)}\n              </repeats>\n            </modifier>\n'
        if len(built) > 1:                                          # shared allowance: this line + the others may not pass the cap
            scid = hid(b['id'], 'shared')
            B = B.replace('          </constraints>\n', f'            <constraint field="selections" scope="parent" value="0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{scid}" type="max"/>\n          </constraints>\n', 1)
            mods += f'            <modifier type="increment" field="{scid}" value="1">\n              <repeats>\n                {rep(sid, per)}\n              </repeats>\n            </modifier>\n'
            for o in others:
                mods += f'            <modifier type="decrement" field="{scid}" value="1">\n              <repeats>\n                {rep(o["id"], 1)}\n              </repeats>\n            </modifier>\n'
        if b['opt']:        # availability rules attached to the option (composition conditions) move to the line
            hm = re.findall(r'<modifier type="set" field="hidden" value="true">(?:(?!</modifier>).)*?</modifier>', b['opt'].group(0), flags=re.S)
            for x in hm: mods += '            ' + x + '\n'
        B = B.replace('          </constraints>\n', '          </constraints>\n          <!-- loadout-cap -->\n          <modifiers>\n' + mods + '          </modifiers>\n', 1)
        b['B'] = B
    # ---- base line: minimum reduced by every loadout figure, links tied to the replaced options removed
    mods = ''.join(f'            <modifier type="decrement" field="{mcid}" value="1">\n              <repeats>\n                {rep(i)}\n              </repeats>\n            </modifier>\n' for i in lids)
    newM = M
    for b in built:
        if b.get('oid'):
            newM = re.sub(r' *<infoLink id="[^"]*" name="[^"]*" hidden="true"[^>]*>(?:(?!</infoLink>).)*?%s(?:(?!</infoLink>).)*?</infoLink>\n' % re.escape(b['oid']), '', newM, flags=re.S)
            newM = strip_modifiers_with(newM, b['oid'])
    newM = newM.replace('          </constraints>\n', '          </constraints>\n          <!-- loadout-base -->\n          <modifiers>\n' + mods + '          </modifiers>\n', 1)
    # an existing line that already is the loadout: just cap it
    for b in built:
        if 'existing' in b:
            E = b['existing']
            ec = re.search(r'<constraint field="selections" scope="parent" value="\d+"([^>]*?) id="([^"]*)" type="(?:min|max)"/>', E)
            if not ec: raise SystemExit(f'{sp["cat"]}: existing model {b["lo"]["model"]} has no constraint')
            E2 = re.sub(r'<constraint field="selections" scope="parent" value="\d+"([^>]*?) id="([^"]*)" type="(?:min|max)"/>', lambda k: f'<constraint field="selections" scope="parent" value="0"{k.group(1)} id="{k.group(2)}" type="max"/>', E, count=1)
            E2 = E2.replace('          </constraints>\n', '          </constraints>\n          <!-- loadout-cap -->\n          <modifiers>\n' + f'            <modifier type="increment" field="{ec.group(2)}" value="1">\n              <repeats>\n                {rep(sid, per)}\n              </repeats>\n            </modifier>\n          </modifiers>\n', 1)
            NU = NU.replace(E, E2, 1)
    # ---- unit: drop the replaced option entries, other per-model options are charged on the loadout lines too
    for b in built:
        if b.get('opt'):
            NU = NU.replace(b['opt'].group(0), '', 1)
    def addrep(k):
        blk = k.group(0)
        name = k.group(1)
        if locked or f'childId="{sid}"' not in blk: return blk
        extra = ''.join('\n                ' + rep(b['id']) for b in built if name not in b['lo'].get('excl', []) and 'existing' not in b)
        if name in sp.get('base_excl', []):
            return blk.replace(rep(sid), extra.strip() if extra else '', 1)
        return blk.replace(rep(sid), rep(sid) + extra, 1) if extra else blk
    NU = re.sub(r'^        <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n', addrep, NU, flags=re.S | re.M)
    NU = NU.replace(M, newM + ''.join(b['B'] for b in built if 'B' in b), 1)
    for b in built:
        if b.get('oid') and b['oid'] in NU: raise SystemExit(f'{sp["cat"]}: {sp["unit"]}: option "{b["lo"]["opt"]}" is still referenced after the split')
    head, rest = NU.split('\n', 1)
    NU = head + '\n      <!-- loadout-split -->\n' + rest
    return s.replace(U, NU, 1), True

count = 0; files = set()
for sp in SPEC:
    path = os.path.join(OUT, sp['cat'])
    if not os.path.exists(path): continue
    s = open(path, encoding='utf8').read()
    s, ch = split_unit(s, sp)
    if ch:
        s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1) if sp['cat'] not in files else s
        files.add(sp['cat']); count += 1
        open(path, 'w', encoding='utf8').write(s)
print(f'Loadout lines added to {count} unit(s) in {len(files)} catalogue(s)' if count else 'Loadouts already applied')
