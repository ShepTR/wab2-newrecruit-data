#!/usr/bin/env python3
"""Tag the catalogue names of the core-rulebook army lists like the other books ("Carthaginian (Hannibal)"):
Roman Army List -> "Roman Army List (Main Rulebook)", Barbarian Army List -> "Barbarian Army List (Main Rulebook)".
Only the catalogue's display name changes (ids and pickers are untouched).  Run after rb_build.py.
Also drops a leading "The " from catalogue names (it broke the alphabetical sorting): "The Swiss (Armies of Chivalry)" -> "Swiss (Armies of Chivalry)".
Usage: python3 catalogue_tags.py <outdir>   (idempotent)"""
import sys, os, re
OUT = sys.argv[1]
TAG = 'Main Rulebook'
for fn, name in (('Roman_Army_List.cat', 'Roman Army List'), ('Barbarian_Army_List.cat', 'Barbarian Army List')):
    p = os.path.join(OUT, fn); s = open(p, encoding='utf8').read()
    new = re.sub(r'(<catalogue id="[^"]*" name=")%s(" )' % re.escape(name), r'\g<1>%s (%s)\2' % (name, TAG), s, count=1)
    if new != s: open(p, 'w', encoding='utf8').write(new); print('tagged', fn)
import glob
n = 0
for p in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(p, encoding='utf8').read()
    m = re.search(r'<catalogue id="[^"]*" name="(The [^"]*)"', s)
    if not m: continue
    old = m.group(1); new_name = old[4:]
    open(p, 'w', encoding='utf8').write(s.replace(old, new_name)); n += 1
print('leading "The" dropped from', n, 'catalogue names')
