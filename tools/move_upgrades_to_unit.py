#!/usr/bin/env python3
"""One-off migration: Leader / Standard bearer / Musician / Centurion options were generated on the model entry, so New Recruit
charged them per model. Move them up to the unit entry (flat cost once per unit). Idempotent.
Usage: python3 move_upgrades_to_unit.py <outdir>"""
import sys, os, re, glob
OUT = sys.argv[1]
NAMES = re.compile(r'^(Leader|Standard bearer|Musician|Centurion\b.*)$')
moved = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(m):
        global moved
        blk = m.group(0)
        found, seen = [], set()
        def grab(mm):
            name = mm.group(2)
            if not NAMES.match(name.replace('&amp;', '&')): return mm.group(0)
            if name not in seen:
                seen.add(name); found.append(mm.group(1))
            return ''
        # upgrade entries nested at model level are indented 12 spaces
        blk2 = re.sub(r'(            <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="upgrade">\n.*?\n            </selectionEntry>\n)', grab, blk, flags=re.S)
        if not found: return blk
        # drop model-level <selectionEntries> blocks left empty
        blk2 = re.sub(r'          <selectionEntries>\n          </selectionEntries>\n', '', blk2)
        ins = ''.join(re.sub(r'(?m)^    ', '', f) if False else f for f in found)
        ins = ''.join('\n'.join(l[4:] if l.startswith('    ') else l for l in f.split('\n')) for f in found)
        moved += len(found)
        return blk2.replace('      <selectionEntries>\n', '      <selectionEntries>\n' + ins, 1)
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s: open(path, 'w', encoding='utf8').write(s2)
print('moved', moved, 'upgrade entries to unit level')
