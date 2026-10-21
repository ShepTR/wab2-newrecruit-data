#!/usr/bin/env python3
"""Tag the catalogue names of the core-rulebook army lists like the other books ("Carthaginian (Hannibal)"):
Roman Army List -> "Roman Army List (Main Rulebook)", Barbarian Army List -> "Barbarian Army List (Main Rulebook)".
Only the catalogue's display name changes (ids and pickers are untouched).  Run after rb_build.py.
Usage: python3 catalogue_tags.py <outdir>   (idempotent)"""
import sys, os, re
OUT = sys.argv[1]
TAG = 'Main Rulebook'
for fn, name in (('Roman_Army_List.cat', 'Roman Army List'), ('Barbarian_Army_List.cat', 'Barbarian Army List')):
    p = os.path.join(OUT, fn); s = open(p, encoding='utf8').read()
    new = re.sub(r'(<catalogue id="[^"]*" name=")%s(" )' % re.escape(name), r'\g<1>%s (%s)\2' % (name, TAG), s, count=1)
    if new != s: open(p, 'w', encoding='utf8').write(new); print('tagged', fn)
