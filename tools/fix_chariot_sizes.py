#!/usr/bin/env python3
"""Chariot squadrons need at least 3 chariots, so a maximum of 1-2 chariot models is dropped (Armies of Antiquity v2: ~40 units started invalid).
A character's own chariot crew model ("Chariot", fixed size) keeps min = max.
Usage: python3 fix_chariot_sizes.py <outdir>   (idempotent)"""
import sys, os, re, glob
OUT = sys.argv[1]; n = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(um):
        global n
        blk = um.group(0); char = 'name="Characters"' in blk.split('<selectionEntries>')[0]
        def do_model(mm):
            global n
            b = mm.group(0)
            c = re.search(r'<constraints>\n(.*?)</constraints>', b, re.S).group(1)
            mn = re.search(r'value="(\d+)"[^>]*type="min"', c); mx = re.search(r'( *<constraint [^>]*value="(\d+)"[^>]*type="max"/>\n)', c)
            if not mn or not mx or int(mx.group(2)) >= int(mn.group(1)) or '<modifier' in b.split('<profiles>')[0]: return b
            if not re.search(r'Chariot|Eqeta', mm.group(1)): return b
            n += 1
            if char: return b.replace(mn.group(0), mn.group(0).replace(f'value="{mn.group(1)}"', f'value="{mx.group(2)}"'), 1)
            return b.replace(mx.group(1), '', 1)
        return re.sub(r'^        <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="model">\n.*?\n        </selectionEntry>\n', do_model, blk, flags=re.S | re.M)
    s2 = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    if s2 != s: open(path, 'w', encoding='utf8').write(s2)
print('chariot size constraints fixed:', n)
