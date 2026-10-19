#!/usr/bin/env python3
"""Chariot Wars: cross-unit limits (copy of the hannibal_limits.py helpers); Hannibal as validation constraints (unit-count ratios, total-figure limits, "at least one" rules).
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

CWSUF = '_Chariot_Wars.cat'
E = Cat('Egyptian_New_Kingdom' + CWSUF); pair(E, ['Pharaoh/Prince (General)', 'Army General/Viceroy (General)'], 'one-general'); E.save()
S = Cat('Sumerian_Akkadian' + CWSUF); pair(S, ['Sumerian Lugal (General)', 'Akkadian King (General)'], 'one-general'); S.save()
H = Cat('Hammurabic_Babylonian' + CWSUF); pair(H, ['King (Shar) (General)', 'General (Alik-Pani) (General)'], 'one-general')
ratio(H, 'Chariot Runners', ['Chariots'])
H.save()
T = Cat('Hittite' + CWSUF); pair(T, ['Great King (General)', 'Prince or Ally King (General)'], 'one-general'); pair(T, ['Scout Cavalry', 'Hittite Successor Cavalry'], 'one-cavalry-unit'); T.save()
W = Cat('Trojan_War' + CWSUF); pair(W, ['King (Wanax) (General)', 'Lawageta (General)'], 'one-general'); W.save()
I = Cat('Israelite' + CWSUF); pair(I, ['King (General)', 'General (General)'], 'one-general'); pair(I, ['Army Standard Bearer', 'Sacred Ark'], 'one-standard')
ch = I.unit('Chariots')[0]
I.add_unit_limit('Sacred Ark', 'ark-no-chariots', 'max', 1, lambda cid: [mod('set', cid, 0, conds=[cond(ch, 'atLeast')])])
I.save()
A = Cat('Assyrian' + CWSUF); pair(A, ['King (General)', 'Turtanu (General)'], 'one-general')
asy = A.vid('Chariot Wars: Assyrian Empire - Assyrian'); bab = A.vid('Chariot Wars: Assyrian Empire - Babylonian')
for n in ('Four-horse Heavy Chariots', 'Assyrian Cavalry', 'Qurubuti Royal Guard', 'Assyrian Infantry (Kisir Sharruti)', 'Heavy Slingers', 'Urartians'):
    A.add_unit_limit(n, 'assyrian-only', 'max', BIG, lambda cid: [mod('set', cid, 0, conds=[cond(bab, 'atLeast')])])
for n in ('Babylonian Cavalry', 'Babylonian Infantry (Kisir Sharruti)', 'Elamite Chariots', 'Elamite Cavalry', 'Elamite Infantry', 'Medes', 'Greek or Lydian Hoplites'):
    A.add_unit_limit(n, 'babylonian-only', 'max', BIG, lambda cid: [mod('set', cid, 0, conds=[cond(asy, 'atLeast')])])
A.save()
print('chariot wars limits added')
