#!/usr/bin/env python3
"""Armies of Antiquity (v1, 1999) catalogues are shown as zz_old_<army> so they sort below the current lists. Idempotent.
Usage: python3 aoa_oldnames.py <outdir>"""
import sys, os, re, glob
n = 0
for f in sorted(glob.glob(os.path.join(sys.argv[1], '*_Armies_of_Antiquity.cat'))):
    s = open(f, encoding='utf8').read()
    m = re.search(r'(<catalogue [^>]*?name=")([^"]*) \(Armies of Antiquity\)(")', s)
    if m:
        s = s[:m.start()] + m.group(1) + 'zz_old_' + m.group(2) + m.group(3) + s[m.end():]
        open(f, 'w', encoding='utf8').write(s); n += 1
print('renamed', n, 'Armies of Antiquity v1 catalogues')
