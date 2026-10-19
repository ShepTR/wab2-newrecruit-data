#!/usr/bin/env python3
"""One-off migration: Leader / Standard bearer / Musician options on units cost a flat amount once per unit (they had been multiplied by the number of models).
Usage: python3 fix_command_costs.py <outdir>   (idempotent)"""
import sys, os, re, glob
OUT = sys.argv[1]; n = 0
PAT = re.compile(r'(^        <selectionEntry id="[^"]*" name="(?:Leader|Standard bearer|Musician)"[^>]*type="upgrade">\n)(.*?)(^        </selectionEntry>\n)', re.S | re.M)
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def fix(m):
        global n
        body = m.group(2)
        mm = re.search(r'          <modifiers>\n            <modifier type="increment" field="points" value="([^"]*)">\n              <repeats>\n.*?</repeats>\n            </modifier>\n          </modifiers>\n', body, re.S)
        if not mm: return m.group(0)
        body = body.replace(mm.group(0), '', 1)
        body = re.sub(r'(<cost name="pts" typeId="points" value=")[^"]*(")', lambda k: k.group(1) + mm.group(1) + k.group(2), body, count=1)
        n += 1
        return m.group(1) + body + m.group(3)
    s2 = PAT.sub(fix, s)
    if s2 != s: open(path, 'w', encoding='utf8').write(s2)
print('command options made flat-cost:', n)
