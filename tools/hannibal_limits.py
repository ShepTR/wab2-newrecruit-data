#!/usr/bin/env python3
"""Hannibal & the Punic Wars: cross-unit limits as validation constraints (unit-count ratios, total-figure limits, "at least one" rules).
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

def ratio(cat, A, Bs, per=1, extra=(), tag=None, unless_none=False):
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

C = Cat('Carthaginian_Hannibal.cat')
ratio(C, 'Spanish Caetrati', ['Spanish Scutarii'])
ratio(C, 'Oscan Hoplites', ['Oscan Warriors'])
ratio(C, 'Artillery (Heavy Bolt Ballista)', ['Citizen Infantry', 'Levy Africans', 'Trained Africans'])
for a in ('Balearic Slingers', 'Ligurian Slingers', 'Sardinian Archers', 'Moorish Archers'):
    ratio(C, a, ['Skirmishers'], tag=f'limit-{a}-skirm')
C.save()

R = Cat('Republican_Roman_Hannibal.cat')
vel = R.unit('Velites')[0]
ratio(R, 'Principes', ['Hastati', 'Raw Hastati'])
# Triarii: one unit per Principes unit; after the reorganisation (Velites in the army) two Principes units per Triarii unit
def tri(cid):
    pr = R.unit('Principes')[0]
    return [mod('increment', cid, 1, conds=[cond(vel, 'lessThan')], repeat=(pr, 1, 'false')),
            mod('increment', cid, 1, conds=[cond(vel, 'atLeast')], repeat=(pr, 2, 'false'))]
R.add_unit_limit('Triarii', 'limit-triarii-per-principes', 'max', 0, tri)
R.add_unit_limit('Triarii', 'min-triarii', 'min', 1, lambda cid: [])
# Leves: at least one unit unless Velites replace them (First Punic War, Second Punic War in Spain / Italy)
def leves(cid):
    wars = ['Hannibal: Republican Roman - First Punic War', 'Hannibal: Republican Roman - Second Punic War in Spain', 'Hannibal: Republican Roman - Second Punic War in Italy']
    return [mod('set', cid, 1, conds=[cond(vel, 'lessThan'), cond(R.vid(w), 'atLeast')]) for w in wars]
R.add_unit_limit('Leves', 'min-leves', 'min', 0, leves)
# Italian Extraordinarii may not outnumber the smallest unit of Italian Spearmen (exact with one Spearmen unit)
sp_u, sp_m, _ = R.unit('Italian Spearmen')
def extra(cid):
    return [mod('set', cid, 0, conds=[cond(sp_u, 'atLeast')]), mod('increment', cid, 1, conds=[cond(sp_u, 'atLeast')], repeat=(sp_m, 1, 'true'))]
R.add_model_limit('Italian Extraordinarii', 'limit-extraordinarii-size', 'parent', BIG, extra)
R.save()

S = Cat('Spanish_Hannibal.cat')
ib = S.vid('Hannibal: Spanish - Iberians')
scu_u, scu_m, _ = S.unit('Scutarii')
# Iberians: one Caetrati unit per two Scutarii units (unless no Scutarii are used); no Caetrati unit may outnumber the smallest Scutarii unit
def caet_units(cid):
    return [mod('set', cid, 0, conds=[cond(ib, 'atLeast'), cond(scu_u, 'atLeast')]),
            mod('increment', cid, 1, conds=[cond(ib, 'atLeast'), cond(scu_u, 'atLeast')], repeat=(scu_u, 2, 'false')),
            mod('set', cid, BIG, conds=[cond(ib, 'atLeast'), cond(scu_u, 'lessThan')])]
S.add_unit_limit('Caetrati', 'limit-caetrati-per-scutarii', 'max', BIG, caet_units)
def caet_size(cid):
    return [mod('set', cid, 0, conds=[cond(ib, 'atLeast'), cond(scu_u, 'atLeast')]),
            mod('increment', cid, 1, conds=[cond(ib, 'atLeast'), cond(scu_u, 'atLeast')], repeat=(scu_m, 1, 'true'))]
S.add_model_limit('Caetrati', 'limit-caetrati-vs-scutarii-size', 'parent', BIG, caet_size)
S.save()

N = Cat('Numidian_Hannibal.cat')
w_u, w_m, _ = N.unit('Warriors')
def figs(cid):      # total figures of this unit type may not exceed the total figures of Warriors
    return [mod('set', cid, 0), mod('increment', cid, 1, repeat=(w_m, 1, 'true'))]
N.add_model_limit('Trained Infantry', 'limit-figures-vs-warriors', 'force', BIG, figs)
N.add_model_limit('Imitation Legionaries (optional)', 'limit-figures-vs-warriors', 'force', BIG, figs)
N.save()

G = Cat('Gallic_Hannibal.cat')
ch_u = G.unit('Chariots')[0]; gw_m = G.unit('Warriors')[1]
G.add_unit_limit('Fanatics', 'need-chariots', 'max', 0, lambda cid: [mod('set', cid, BIG, conds=[cond(ch_u, 'atLeast')])])
def gfigs(cid): return [mod('set', cid, 0), mod('increment', cid, 1, repeat=(gw_m, 1, 'true'))]
G.add_model_limit('Fanatics', 'limit-figures-vs-warriors', 'force', BIG, gfigs)
G.save()
print('limits added')
