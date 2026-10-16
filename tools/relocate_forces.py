#!/usr/bin/env python3
"""Move each army's force entries out of the game system and into that army's own catalogue,
so a faction only offers its own compositions. Leaves one neutral root force ("Army") in the game system.
Usage: python3 relocate_forces.py <outdir>    (run LAST, after build_wab2.py, rb_build.py and hb_build.py; idempotent)."""
import sys, os, re, hashlib

OUT = sys.argv[1]
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))

def target(name):
    if name.startswith('Hannibal: '):
        base = name[len('Hannibal: '):].split(' - ')[0]
        return {'Carthaginian': 'Carthaginian_Hannibal.cat', 'Republican Roman': 'Republican_Roman_Hannibal.cat',
                'Spanish': 'Spanish_Hannibal.cat', 'Numidian': 'Numidian_Hannibal.cat',
                'Ligurian': 'Ligurian_Hannibal.cat', 'Gallic': 'Gallic_Hannibal.cat'}[base]
    if name.startswith('Early Imperial Roman'): return 'Early_Imperial_Roman.cat'
    return {'Gallic': 'Gallic.cat', 'Parthian': 'Parthian.cat', 'Medieval English': 'Medieval_English.cat',
            'Roman Army List': 'Roman_Army_List.cat', 'Barbarian Army List': 'Barbarian_Army_List.cat'}[name]

s = open(GST, encoding='utf8').read()
blocks = re.findall(r'    <forceEntry id="[^"]*" name="([^"]*)".*?    </forceEntry>\n', s, flags=re.S)
whole = re.findall(r'(    <forceEntry id="[^"]*" name="[^"]*".*?    </forceEntry>\n)', s, flags=re.S)
ROOT_NAME = 'Army'
moved = {}
for blk in whole:
    name = re.match(r'    <forceEntry id="[^"]*" name="([^"]*)"', blk).group(1).replace('&amp;', '&')
    if name == ROOT_NAME: continue
    moved.setdefault(target(name), []).append(blk)
    s = s.replace(blk, '', 1)

# neutral root force with every category and no limits
cats = re.findall(r'<categoryEntry id="([^"]*)" name="([^"]*)"', s)
rid = hid('force', 'Army root')
if f'id="{rid}"' not in s:
    root = f'    <forceEntry id="{rid}" name="{ROOT_NAME}" hidden="false">\n      <categoryLinks>\n'
    for cid, cn in cats:
        root += f'        <categoryLink id="{hid("rootlink", cn)}" name="{cn}" hidden="false" targetId="{cid}" primary="false"/>\n'
    root += '      </categoryLinks>\n    </forceEntry>\n'
    s = s.replace('  <forceEntries>\n', '  <forceEntries>\n' + root, 1)
open(GST, 'w', encoding='utf8').write(s)

n = 0
for fn, blks in moved.items():
    p = os.path.join(OUT, fn)
    c = open(p, encoding='utf8').read()
    fresh = [b for b in blks if re.match(r'    <forceEntry id="([^"]*)"', b).group(1) not in c]
    if not fresh: continue
    text = '  <forceEntries>\n' + ''.join(fresh) + '  </forceEntries>\n'
    if '  <forceEntries>' in c:
        c = c.replace('  </forceEntries>', ''.join(fresh) + '  </forceEntries>', 1)
    else:
        c = c.replace('  <selectionEntries>', text + '  <selectionEntries>', 1)
    open(p, 'w', encoding='utf8').write(c)
    n += len(fresh)
print('moved', n, 'force entries into', len(moved), 'catalogues; game system keeps 1 root force')
