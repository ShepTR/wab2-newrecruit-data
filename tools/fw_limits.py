#!/usr/bin/env python3
"""Fall of the West: availability limits (copy of the hannibal_limits.py helpers); Hannibal as validation constraints (unit-count ratios, total-figure limits, "at least one" rules).
 - unit ratios:  A may be taken once per N units of B  (constraint max on A = floor(count(B)/N), 0 when there is no B)
 - figure limits: total figures of A may not exceed the total figures of B (Numidian, Gallic, Spanish)
 - minimums:  Triarii, Leves (unless Velites)
Not expressible in New Recruit and therefore NOT enforced: "may not outnumber any other unit of cavalry", "may not be the largest unit of
infantry skirmishers", "no X unit may outnumber the smallest Y unit" where several Y units may exist (with one Y unit the limit is exact;
with several it is the total of their figures, which is lenient).
Usage: python3 hannibal_limits.py <outdir>   (run after the *_restrictions.py scripts; idempotent)"""
import sys, os, re, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
from ratiolib import ratio, size_limit
BIG = 1000
def cond(child, op, scope='force', incl='true'):
    return (f'<condition field="selections" scope="{scope}" value="1" percentValue="false" shared="true" includeChildSelections="{incl}" '
            f'includeChildForces="false" childId="{child}" type="{op}"/>')
def mod(kind, field, value, conds=(), repeat=None, groups=()):
    x = f'<modifier type="{kind}" field="{field}" value="{value}">\n'
    if repeat:
        child, per, incl = repeat
        x += (f'  <repeats>\n    <repeat field="selections" scope="force" value="{per}" percentValue="false" shared="true" includeChildSelections="{incl}" '
              f'includeChildForces="false" childId="{child}" repeats="1" roundUp="false"/>\n  </repeats>\n')
    if conds:
        x += '  <conditions>\n' + ''.join(f'    {c}\n' for c in conds) + '  </conditions>\n'
    x += '</modifier>\n'
    return x

class Cat:
    def __init__(self, fn):
        self.fn = fn; self.path = os.path.join(OUT, fn); self.s = open(self.path, encoding='utf8').read()
        self.cid = re.search(r'<catalogue id="([^"]*)"', self.s).group(1); self.changed = False
    def unit(self, name):
        m = re.search(r'    <selectionEntry id="([^"]*)" name="%s"[^>]*type="unit">\n(.*?)\n    </selectionEntry>\n' % re.escape(name.replace('&', '&amp;')), self.s, re.S)
        if not m: raise SystemExit(f'{self.fn}: no unit {name}')
        mid = re.search(r'        <selectionEntry id="([^"]*)" name="[^"]*"[^>]*type="model">', m.group(2)).group(1)
        return m.group(1), mid, m
    def vid(self, label):   # war / sub-list picker id
        return hid('picker', self.fn, label)
    def add_unit_limit(self, name, tag, ctype, base, mods):
        """constraint (min/max on the unit selections in the force) + modifiers, inserted into the unit entry"""
        uid, mid, m = self.unit(name)
        if f'<!-- {tag} -->' in m.group(0): return
        cid = hid(uid, tag)
        con = (f'        <constraint field="selections" scope="force" value="{base}" percentValue="false" shared="true" includeChildSelections="false" '
               f'includeChildForces="false" id="{cid}" type="{ctype}"/>\n')
        blk = m.group(0); head, rest = blk.split('\n', 1)
        modxml = f'        <!-- {tag} -->\n' + ''.join(mods(cid)).replace('\n', '\n').rstrip('\n') + '\n'
        modxml = '\n'.join(('        ' + l if l.strip() and not l.startswith('        <!--') else l) for l in modxml.split('\n'))
        if re.search(r'^      <constraints>\n', rest, re.M):
            rest = re.sub(r'^      <constraints>\n', '      <constraints>\n' + con, rest, count=1, flags=re.M); cons = ''
        else:
            cons = '      <constraints>\n' + con + '      </constraints>\n'
        if re.search(r'^      <modifiers>\n', rest, re.M):
            rest = re.sub(r'^      <modifiers>\n', '      <modifiers>\n' + modxml + '\n', rest, count=1, flags=re.M)
            rest = rest.replace('      <categoryLinks>', cons + '      <categoryLinks>', 1) if cons else rest
        else:
            rest = rest.replace('      <categoryLinks>', cons + '      <modifiers>\n' + modxml + '\n      </modifiers>\n      <categoryLinks>', 1)
        self.s = self.s.replace(blk, head + '\n' + rest, 1); self.changed = True
    def add_model_limit(self, name, tag, scope, base, mods):
        """max figures of this unit's model entry (scope 'parent' = this unit, 'force' = all units of the entry)"""
        uid, mid, m = self.unit(name)
        if f'<!-- {tag} -->' in m.group(0): return
        cid = hid(mid, tag)
        mm = re.search(r'        <selectionEntry id="%s"[^>]*type="model">\n.*?\n        </selectionEntry>\n' % mid, m.group(2), re.S)
        mblk = mm.group(0)
        con = (f'            <constraint field="selections" scope="{scope}" value="{base}" percentValue="false" shared="true" includeChildSelections="false" '
               f'includeChildForces="false" id="{cid}" type="max"/>\n')
        modxml = f'          <!-- {tag} -->\n' + ''.join(mods(cid))
        modxml = '\n'.join(('          ' + l if l.strip() and not l.startswith('          <!--') else l) for l in modxml.split('\n'))
        new = mblk.replace('          </constraints>\n', con + '          </constraints>\n', 1)
        if new == mblk: raise SystemExit('no model constraints in ' + name)
        if '          <modifiers>\n' in new.split('<profiles>')[0]:
            new = new.replace('          <modifiers>\n', '          <modifiers>\n' + modxml + '\n', 1)
        else:
            new = new.replace('          </constraints>\n', '          </constraints>\n          <modifiers>\n' + modxml + '\n          </modifiers>\n', 1)
        self.s = self.s.replace(mblk, new, 1); self.changed = True
    def save(self):
        if self.changed:
            self.s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', self.s, count=1)
            open(self.path, 'w', encoding='utf8').write(self.s)

def _ratio_old(cat, A, Bs, per=1, extra=(), tag=None, unless_none=False):
    """A units <= floor(units of Bs / per); `extra` conditions apply to the whole rule"""
    ids = [cat.unit(b)[0] for b in Bs]
    def mods(cid):
        out = []
        for b in ids:
            out.append(mod('increment', cid, 1, conds=[*extra], repeat=(b, per, 'false')))
        if unless_none:
            out.append(mod('set', cid, BIG, conds=[cond(b, 'lessThan') for b in ids] + list(extra)))
        return out
    cat.add_unit_limit(A, tag or f'limit-{A}-per-{"-".join(Bs)}', 'max', 0, mods)


def pair(cat, names, tag):
    """0-1 across several units (e.g. General = King or Prince): each is capped at 1 and at 0 once another of the group is taken"""
    ids = [cat.unit(n)[0] for n in names]
    for n, me in zip(names, ids):
        others = [i for i in ids if i != me]
        cat.add_unit_limit(n, tag, 'max', 1, lambda cid, others=others: [mod('set', cid, 0, conds=[cond(o, 'atLeast')]) for o in others])


FW = '_Fall_of_the_West.cat'

# ---------------------------------------------------------------------------------------------------------------------------
# Tormenta: one stone thrower per two bolt shooters (rulebook p.181): T <= (Scorpio units + Ballista units) - T  <=>  2T <= S+B
def tormenta(cat):
    from ratiolib import ratio
    ratio(cat, 'Small Stone Thrower (Tormenta)', ['Light Bolt Thrower (Scorpio)', 'Bolt Thrower (Ballista)'], per=2, tag='tormenta-per-two-bolt-shooters')

# Skirmish formation (free) and "one soldier in four may take a bow" (Fall of the West p.46, p.48)
LT = '5be5-5832-c8fb-3a19'     # Light Troops rule
SHIELD = 'b513-5c2a-34df-6a1d'; BOW = '5d29-ba1e-8299-8085'
def ent(blk, name, indent):
    m = re.search(r'^%s<selectionEntry id="([^"]*)" name="%s"[^>]*type="(?:upgrade|model)">\n.*?\n^%s</selectionEntry>\n' % (indent, re.escape(name), indent), blk, re.S | re.M)
    return m
def cond_sel(scope, child):
    return (f'<condition field="selections" scope="{scope}" value="1" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" type="atLeast"/>')
def add_mod(block, modxml, anchor_re):
    """insert a modifier into the first <modifiers> of `block` (or create one before the anchor)"""
    if '<modifiers>\n' in block:
        return block.replace('<modifiers>\n', '<modifiers>\n' + modxml, 1)
    return re.sub(anchor_re, lambda m: '<modifiers>\n' + modxml + '</modifiers>\n' + m.group(0), block, count=1)

def skirmish(cat, unit, archer=None, force_limit=False, block=(), shield_swap=False):
    """block: option names hidden/disabled in skirmish formation; archer: (model name, archer model name)"""
    uid, mid, m = cat.unit(unit)
    blk = m.group(0)
    if '<!-- skirmish -->' in blk: return
    T = hid(uid, 'skirmish')
    on = lambda: cond_sel(uid, T)
    # --- options disabled in skirmish formation
    for n in block:
        em = ent(blk, n, '        ')
        if not em: raise SystemExit(f'{cat.fn}: {unit}: no option {n}')
        e = em.group(0)
        mx = re.search(r'<constraint [^>]*id="([^"]*)" type="max"/>', e).group(1)
        mm = (f'                <modifier type="set" field="hidden" value="true">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n'
              f'                <modifier type="set" field="{mx}" value="0">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n')
        e2 = add_mod(e, mm, r'          <!-- def-link -->|          <infoLinks>|          <costs>')
        blk = blk.replace(e, e2, 1)
    # --- archer model
    if archer:
        base, arch = archer
        bm = ent(blk, base, '        ')
        b = bm.group(0)
        A = hid(mid, 'archer')
        c = re.sub(r'(?<=\s)id="([^"]*)"', lambda k: 'id="%s"' % hid(k.group(1), 'archer'), b)
        c = c.replace(f'name="{base}"', f'name="{arch}"')
        c = re.sub(r'<cost name="pts" typeId="points" value="([0-9.]+)"/>', lambda k: '<cost name="pts" typeId="points" value="%g"/>' % (float(k.group(1)) + 1), c)
        for ln in ('Throwing Spear', 'Large Shield', 'Javelin', 'Heavy Throwing Spear', 'Shield Wall (Fall of the West)'):
            c = re.sub(r'            <infoLink [^>]*name="%s"[^>]*?(?:/>|>\n.*?\n            </infoLink>)\n' % re.escape(ln), '', c, flags=re.S)
        c = c.replace('          <infoLinks>\n', f'          <infoLinks>\n            <infoLink id="{hid(A, "bow")}" name="Bow" hidden="false" targetId="{BOW}" type="profile"/>\n', 1)
        c = re.sub(r'            <profile id="[^"]*" name="Equipment and options[^"]*".*?</profile>\n', '', c, flags=re.S)
        c = re.sub(r'<!-- encumbrance -->.*?</modifier>\n', '', c, count=1, flags=re.S)       # no armour/shield -> no encumbrance
        c = re.sub(r'              <modifiers>\n                \n?\s*</modifiers>\n', '', c)
        # armour save: light armour only -> 6+
        c = re.sub(r'(name="Armour Save"[^>]*>\n.*?<characteristic name="Save" typeId="[^"]*">)[^<]*(</characteristic>)', r'\1None\2', c, count=1, flags=re.S)
        c = re.sub(r'<!-- armour-save -->.*?(?=              </modifiers>\n            </profile>)', '', c, count=1, flags=re.S)
        la = ent(blk, 'Light armour', '        ').group(1)
        sv = re.search(r'name="Armour Save".*?<characteristic name="Save" typeId="([^"]*)"', c, re.S).group(1)
        c = re.sub(r'(name="Armour Save"[^>]*>.*?</characteristics>\n)(?:              <modifiers>\n.*?              </modifiers>\n)?',
                   lambda k: k.group(1) + f'              <modifiers>\n                <modifier type="set" field="{sv}" value="6+">\n                  <conditions>\n                    {cond_sel(uid, la)}\n                  </conditions>\n                </modifier>\n              </modifiers>\n', c, count=1, flags=re.S)
        # constraints: min 0, max = one per three base models (a <= (base+a)/4), none in skirmish formation
        c = re.sub(r'(<constraint [^>]*value=")[0-9]+("[^>]*type="min"/>)', r'\g<1>0\2', c, count=1)
        mxid = hid(A, 'max')
        c = c.replace('          </constraints>\n', f'            <constraint field="selections" scope="parent" value="0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{mxid}" type="max"/>\n          </constraints>\n', 1)
        rep = (f'                <modifier type="increment" field="{mxid}" value="1">\n                  <repeats>\n                    <repeat field="selections" scope="parent" value="3" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="{mid}" repeats="1" roundUp="false"/>\n                  </repeats>\n                </modifier>\n'
               f'                <modifier type="set" field="{mxid}" value="0">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n')
        c = re.sub(r'(          </infoLinks>\n)', lambda k: k.group(1) + f'          <modifiers>\n{rep}          </modifiers>\n', c, count=1)
        blk = blk.replace(b, b + c, 1)
        # unit-level per-model options also apply to the archers (light armour, drilled)
        for n in ('Light armour', 'Drilled'):
            em = ent(blk, n, '        ')
            if not em: continue
            e = em.group(0)
            mo = re.search(r'                <modifier type="increment" field="points" value="[^"]*">\n.*?\n                </modifier>\n|            <modifier type="increment" field="points" value="[^"]*">\n.*?\n            </modifier>\n', e, re.S)
            if mo:
                dup = mo.group(0).replace(f'childId="{mid}"', f'childId="{A}"')
                e2 = e.replace(mo.group(0), mo.group(0) + dup, 1)
                blk = blk.replace(e, e2, 1)
    # --- toggle entry
    cons = (f'        <constraint field="selections" scope="parent" value="1" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(T, "max")}" type="max"/>\n'
            f'        <constraint field="selections" scope="parent" value="0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(T, "min")}" type="min"/>\n')
    if force_limit:
        cons += f'        <constraint field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="{hid(T, "fmax")}" type="max"/>\n'
    tog = (f'        <selectionEntry id="{T}" name="Skirmish formation (free; Light Infantry)" hidden="false" collective="false" import="true" type="upgrade">\n'
           f'          <comment>Skirmishers replace their equipment with shield, hand weapon, javelins and darts and may take no other options (Fall of the West p.46, p.48); no extra cost.</comment>\n'
           f'          <constraints>\n{cons}          </constraints>\n'
           f'          <infoLinks>\n            <infoLink id="{hid(T, "lt")}" name="Light Troops" hidden="false" targetId="{LT}" type="rule"/>\n          </infoLinks>\n'
           f'          <costs>\n            <cost name="pts" typeId="points" value="0"/>\n          </costs>\n        </selectionEntry>\n        <!-- skirmish -->\n')
    blk = blk.replace('      <selectionEntries>\n', '      <selectionEntries>\n' + tog, 1)
    if shield_swap:   # Roman infantry: shield and hand weapon, javelins and darts; armour save 6+
        # hide large shield / throwing spear, show shield / javelin on every model of the unit
        def swap(mb):
            def hide(n):
                return re.sub(r'(            <infoLink id="[^"]*" name="%s"[^>]*type="profile")/>\n' % n,
                              lambda k: k.group(1) + f'>\n              <modifiers>\n                <modifier type="set" field="hidden" value="true">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n              </modifiers>\n            </infoLink>\n', mb)
            def hide2(n):
                nonlocal mb
                m_ = re.search(r'(            <infoLink id="[^"]*" name="%s"[^>]*type="profile">\n              <modifiers>\n)' % n, mb)
                if m_:
                    mb = mb.replace(m_.group(1), m_.group(1) + f'                <modifier type="set" field="hidden" value="true">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n', 1)
                else:
                    mb = hide(n)
            def show(n):
                nonlocal mb
                m_ = re.search(r'(            <infoLink id="[^"]*" name="%s"[^>]*type="profile">\n              <modifiers>\n)' % n, mb)
                if m_:
                    mb = mb.replace(m_.group(1), m_.group(1) + f'                <modifier type="set" field="hidden" value="false">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n', 1)
            hide2('Large Shield'); hide2('Throwing Spear'); show('Javelin')
            mb = mb.replace('          </infoLinks>\n', f'            <infoLink id="{hid(T, "shield", len(mb))}" name="Shield" hidden="true" targetId="{SHIELD}" type="profile">\n              <modifiers>\n                <modifier type="set" field="hidden" value="false">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n              </modifiers>\n            </infoLink>\n          </infoLinks>\n', 1)
            sv = re.search(r'name="Armour Save"[^>]*>.*?<characteristic name="Save" typeId="([^"]*)"', mb, re.S).group(1)
            mb = re.sub(r'(name="Armour Save".*?<modifiers>\n(?:.*?\n)?)(              </modifiers>\n            </profile>)',
                        lambda k: k.group(1) + f'                <modifier type="set" field="{sv}" value="6+">\n                  <conditions>\n                    {on()}\n                  </conditions>\n                </modifier>\n' + k.group(2), mb, count=1, flags=re.S)
            return mb
        base = ent(blk, mname[unit], '        ')
        b0 = base.group(0)
        blk = blk.replace(b0, swap(b0), 1)
    cat.s = cat.s.replace(m.group(0), blk, 1); cat.changed = True

mname = {'Pedes': 'Pedes', 'Palantina': 'Palantine', 'Veterans': 'Veteran'}

R = Cat('Late_Roman' + FW)
lim = R.vid('Fall of the West: Roman Army - Limitanei')
R.add_unit_limit('Palantina', 'no-palantina-limitanei', 'max', BIG, lambda cid: [mod('set', cid, 0, conds=[cond(lim, 'atLeast')])])
# Militia or Bacaudae: no standards or musicians (book p.46) -> remove those options from the unit (idempotent)
uid, mid, m = R.unit('Militia or Bacaudae')
blk = m.group(0)
nb = re.sub(r'            <selectionEntry id="[^"]*" name="(?:Standard bearer|Musician)"[^>]*type="upgrade">\n.*?\n            </selectionEntry>\n', '', blk, flags=re.S)
if nb != blk: R.s = R.s.replace(blk, nb, 1); R.changed = True
for u, force in (('Pedes', True), ('Palantina', False), ('Veterans', False)):
    skirmish(R, u, archer=(mname[u], mname[u] + ' Archer'), force_limit=force, shield_swap=True,
             block=['Light armour', 'Javelins and darts', 'Heavy throwing spear (replaces throwing spear)', 'Drilled'])
tormenta(R)
R.save()
Bb = Cat('Late_Barbarian' + FW)
cen = Bb.vid('Fall of the West: Barbarian Army - Central Barbarians'); eas = Bb.vid('Fall of the West: Barbarian Army - Eastern Barbarians'); naf = Bb.vid('Fall of the West: Barbarian Army - North African')
for n in ('Steppe Cavalry', 'Noble Steppe Cavalry'):
    Bb.add_unit_limit(n, 'steppe-central-eastern-only', 'max', 0, lambda cid: [mod('set', cid, BIG, conds=[cond(cen, 'atLeast')]), mod('set', cid, BIG, conds=[cond(eas, 'atLeast')])])
Bb.add_unit_limit('North African Camelry', 'north-african-only', 'max', 0, lambda cid: [mod('set', cid, BIG, conds=[cond(naf, 'atLeast')])])
wl = Bb.unit('Barbarian Warlord')[0]
Bb.add_unit_limit('Comitatus', 'needs-warlord', 'max', 0, lambda cid: [mod('set', cid, BIG, conds=[cond(wl, 'atLeast')])])
skirmish(Bb, 'Warrior', force_limit=True, block=['Heavy throwing spear (replaces mixed weapons)'])
Bb.save()
W = Cat('Warlord' + FW)
pair(W, ['Roman Army General', 'Barbarian Warlord'], 'one-general')
wl = W.unit('Barbarian Warlord')[0]
W.add_unit_limit('Comitatus', 'needs-warlord', 'max', 0, lambda cid: [mod('set', cid, BIG, conds=[cond(wl, 'atLeast')])])
for u, force in (('Pedes', True), ('Palantina', False), ('Veterans', False)):
    skirmish(W, u, archer=(mname[u], mname[u] + ' Archer'), force_limit=force, shield_swap=True,
             block=['Light armour', 'Javelins and darts', 'Heavy throwing spear (replaces throwing spear)', 'Drilled'])
skirmish(W, 'Warrior', force_limit=True, block=['Heavy throwing spear (replaces mixed weapons)'])
tormenta(W)
W.save()
print('fall of the west limits added')
