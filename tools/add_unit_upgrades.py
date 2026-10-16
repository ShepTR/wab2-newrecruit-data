#!/usr/bin/env python3
"""Give every non-character troop unit Leader / Standard bearer / Musician options (+5 pts each; free for the
Republican Roman manipular units, per Hannibal p.55). Skips units that already have the option, war machines and crews,
elephants and war-hound packs. Idempotent. Usage: python3 add_unit_upgrades.py <outdir>   (run after the build scripts)."""
import sys, os, re, glob, hashlib

OUT = sys.argv[1]
def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def q(s): return '"' + str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;') + '"'

FREE = {'Hastati', 'Raw Hastati', 'Principes', 'Triarii'}          # Hannibal p.55: free for the manipular units
UPGRADES = [('Leader', r'leader|centurion'), ('Standard bearer', r'standard bearer'), ('Musician', r'musician')]
SKIP_UNIT = re.compile(r'elephant|warhound', re.I)

def opt_xml(mid, label, cost):
    oid = hid(mid, 'upg', label)
    return (f'            <selectionEntry id="{oid}" name={q(label)} hidden="false" collective="true" import="true" type="upgrade">\n'
            f'              <constraints>\n'
            f'                <constraint field="selections" scope="parent" value="1" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(oid,"max")}" type="max"/>\n'
            f'                <constraint field="selections" scope="parent" value="0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(oid,"min")}" type="min"/>\n'
            f'              </constraints>\n'
            f'              <costs>\n                <cost name="pts" typeId="points" value="{cost}"/>\n              </costs>\n            </selectionEntry>\n')

total = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    added = 0
    def do_unit(m):
        global total
        nonlocal_added = 0
        blk = m.group(0)
        uname = re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1)
        if 'name="Characters"' in blk.split('<selectionEntries>')[0]: return blk
        if SKIP_UNIT.search(uname) or 'name="Crew"' in blk: return blk
        mm = re.search(r'(        <selectionEntry id="([^"]*)" name="[^"]*"[^>]*type="model">\n.*?\n {8}</selectionEntry>\n)', blk, flags=re.S)
        if not mm: return blk
        model, mid = mm.group(1), mm.group(2)
        if re.search(r'name="[^"]*elephant', model, re.I): return blk
        low = ' '.join(re.findall(r'<selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="upgrade"', model)).lower()
        new = ''
        for label, pat in UPGRADES:
            if re.search(pat, low): continue
            new += opt_xml(mid, label, 0 if uname.replace('&amp;', '&') in FREE else 5)
        if not new: return blk
        if '          </selectionEntries>\n          <costs>' in model:
            nm = model.replace('          </selectionEntries>\n          <costs>', new + '          </selectionEntries>\n          <costs>', 1)
        else:
            nm = model.replace('          <costs>', '          <selectionEntries>\n' + new + '          </selectionEntries>\n          <costs>', 1)
        total += new.count('type="upgrade"')
        return blk.replace(model, nm, 1)
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s: open(path, 'w', encoding='utf8').write(s2)
print('added', total, 'upgrade options')
