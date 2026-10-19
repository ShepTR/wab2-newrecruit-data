#!/usr/bin/env python3
"""In elephant units, mahout/driver/crew entries become type="upgrade" so the unit size counts only the elephants (their profiles still show).
Usage: python3 elephant_count.py <outdir>   (idempotent)"""
import sys, os, re, glob
OUT = sys.argv[1]
CREW = re.compile(r'crew|mahout|driver|howdah', re.I)
n = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); orig = s
    def do_unit(um):
        global n
        blk = um.group(0)
        if not re.search(r'^        <selectionEntry id="[^"]*" name="[^"]*lephant[^"]*"[^>]*type="model">', blk, re.M): return blk
        def fix(m):
            global n
            if not CREW.search(m.group(2)) or 'scort' in m.group(2): return m.group(0)
            n += 1
            return m.group(1) + 'type="upgrade"' + m.group(3)
        return re.sub(r'(^        <selectionEntry id="[^"]*" name="([^"]*)"[^>]*?)type="model"(>)', fix, blk, flags=re.M)
    s = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    if s != orig: open(path, 'w', encoding='utf8').write(s)
print('crew entries excluded from count:', n)
