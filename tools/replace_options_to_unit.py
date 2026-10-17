#!/usr/bin/env python3
"""'(replaces x)' equipment options must apply to EVERY model in the unit, so they become all-or-nothing unit-level checkboxes.
The points cost is the per-model cost x the number of models (cost modifier repeated once per model selection).
Usage: python3 replace_options_to_unit.py <outdir>   (idempotent)."""
import sys, os, re, glob
OUT = sys.argv[1]
moved = 0
def q(s): return s
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(m):
        global moved
        blk = m.group(0)
        new = ''
        def do_model(mm):
            global moved
            mblk = mm.group(0)
            mid = re.match(r'        <selectionEntry id="([^"]*)"', mblk).group(1)
            out = [mblk]
            def grab(o):
                global moved
                nonlocal new
                name = o.group(2)
                if not re.search(r'replace', name, re.I): return o.group(0)
                ent = o.group(1)
                cost = re.search(r'<cost name="pts" typeId="points" value="(-?[0-9.]+)"', ent).group(1)
                cons = re.search(r'<constraints>.*?</constraints>\n', ent, flags=re.S).group(0)
                cons = '\n'.join(l[4:] if l.startswith('    ') else l for l in cons.split('\n'))
                head = re.match(r'( *)(<selectionEntry id="[^"]*" name="[^"]*") hidden="false" collective="true"( import="true" type="upgrade">)', ent)
                mod = ''
                if float(cost) != 0:
                    mod = (f'          <modifiers>\n            <modifier type="increment" field="points" value="{cost}">\n              <repeats>\n'
                           f'                <repeat field="selections" scope="parent" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="{mid}" repeats="1" roundUp="false"/>\n'
                           f'              </repeats>\n            </modifier>\n          </modifiers>\n')
                new += (f'        {head.group(2)} hidden="false" collective="false"{head.group(3)}\n{cons}{mod}'
                        f'          <costs>\n            <cost name="pts" typeId="points" value="0"/>\n          </costs>\n        </selectionEntry>\n')
                moved += 1
                return ''
            mblk = re.sub(r'(            <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="upgrade">\n.*?\n            </selectionEntry>\n)', grab, mblk, flags=re.S)
            mblk = re.sub(r'          <selectionEntries>\n          </selectionEntries>\n', '', mblk)
            return mblk
        blk2 = re.sub(r'        <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="model">\n.*?\n        </selectionEntry>\n', do_model, blk, flags=re.S)
        if not new: return blk
        return blk2.replace('      <selectionEntries>\n', '      <selectionEntries>\n' + new, 1)
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda m: f' revision="{int(m.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('moved', moved, 'replace options to unit level')
