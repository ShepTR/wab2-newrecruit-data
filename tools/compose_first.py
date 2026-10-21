#!/usr/bin/env python3
"""Lists with several wars / periods have a required "Army composition" picker.  Until one is chosen every unit of such a list is HIDDEN,
so it is obvious that the composition has to be picked first (before: the units were listed and failed validation with "max 0").
Usage: python3 compose_first.py <outdir>   (run after collapse_forces and the restriction scripts; idempotent)"""
import sys, os, re, glob, json, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
V = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'variants.json'), encoding='utf8'))
TAG = '<!-- hide-until-composition -->'
n = 0
for fn, vs in sorted(V.items()):
    path = os.path.join(OUT, fn)
    if len(vs) < 2 or not os.path.exists(path): continue
    s = open(path, encoding='utf8').read()
    if TAG in s: continue
    conds = ''.join(f'            <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
                    f'includeChildForces="false" childId="{hid("picker", fn, v["name"])}" type="lessThan"/>\n' for v in vs)
    mod = (f'        {TAG}\n        <modifier type="set" field="hidden" value="true">\n          <conditions>\n{conds}          </conditions>\n        </modifier>\n')
    def do_unit(m):
        global n
        blk = m.group(0); cut = blk.find('      <categoryLinks>')
        head, tail = blk[:cut], blk[cut:]
        if '      <modifiers>\n' in head: head = head.replace('      <modifiers>\n', '      <modifiers>\n' + mod, 1)
        else:
            i = min([k for k in (head.find('      <profiles>'), head.find('<!-- req-notes -->')) if k >= 0] or [len(head)])
            head = head[:i] + '      <modifiers>\n' + mod + '      </modifiers>\n' + head[i:]
        n += 1
        return head + tail
    s = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    s = s.replace('  <selectionEntries>\n', f'  <selectionEntries>\n', 1)
    open(path, 'w', encoding='utf8').write(s)
print('units hidden until a composition is chosen:', n)
