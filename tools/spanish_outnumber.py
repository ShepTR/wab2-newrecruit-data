#!/usr/bin/env python3
"""Spanish list: "no Caetrati unit may outnumber the smallest Celtiberian (or Lusitanian) unit" (Hannibal p.70), as a validation constraint.
A max-size constraint on the Caetrati model entry: unlimited until a Celtiberian (Lusitanian) unit is in the army, then limited to the model
count of those units. New Recruit cannot compare against the smallest of several units, so with two or more Celtiberian (Lusitanian)
units the limit is the TOTAL of their models, which is lenient; with one unit it is exact.
Usage: python3 spanish_outnumber.py <outdir>   (run after spanish_restrictions.py; idempotent)"""
import sys, os, re, hashlib
OUT = sys.argv[1]; FN = 'Spanish_Hannibal.cat'; PATH = os.path.join(OUT, FN)
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
s = open(PATH, encoding='utf8').read()
if 'spanish-outnumber' in s: sys.exit('already applied')
def unit(name):
    m = re.search(r'    <selectionEntry id="([^"]*)" name="%s"[^>]*type="unit">\n(.*?)\n    </selectionEntry>\n' % re.escape(name), s, re.S)
    mid = re.search(r'        <selectionEntry id="([^"]*)" name="[^"]*"[^>]*type="model">', m.group(2)).group(1)
    return m.group(1), mid
cu, cm = unit('Caetrati')
def vid(war): return hid('picker', FN, f'Hannibal: Spanish - {war}')
def c(kind, cid, war=None):
    if war: return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="{vid(war)}" type="atLeast"/>')
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="{cid}" type="{kind}"/>')
conid = hid(cm, 'outnumber')
mods = '        <!-- spanish-outnumber -->\n'
for war, unitname in (('Celtiberians', 'Celtiberian Warriors'), ('Lusitanians', 'Lusitanians')):
    u, m = unit(unitname)
    mods += (f'          <modifier type="set" field="{conid}" value="0">\n            <conditionGroups>\n              <conditionGroup type="and">\n                <conditions>\n'
             f'                  {c("atLeast", None, war)}\n                  {c("atLeast", u)}\n                </conditions>\n              </conditionGroup>\n            </conditionGroups>\n          </modifier>\n'
             f'          <modifier type="increment" field="{conid}" value="1">\n            <repeats>\n'
             f'              <repeat field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="false" childId="{m}" repeats="1" roundUp="false"/>\n'
             f'            </repeats>\n            <conditions>\n              {c("atLeast", None, war)}\n            </conditions>\n          </modifier>\n')
constraint = (f'            <constraint field="selections" scope="parent" value="1000" percentValue="false" shared="false" includeChildSelections="false" '
              f'includeChildForces="false" id="{conid}" type="max"/>\n')
i = s.index(f'<selectionEntry id="{cm}"'); j = s.index('</constraints>\n', i)
s = s[:j] + constraint + '          ' + s[j:]
j2 = s.index('</constraints>\n', i) + len('</constraints>\n')
s = s[:j2] + '          <modifiers>\n' + mods + '          </modifiers>\n' + s[j2:]
s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1)
open(PATH, 'w', encoding='utf8').write(s); print('ok')
