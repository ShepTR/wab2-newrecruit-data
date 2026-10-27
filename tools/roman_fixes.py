#!/usr/bin/env python3
"""Republican Roman (Hannibal) corrections, applied in place (idempotent; run after hannibal_limits.py and sv_stat.py):
 1. Raw Hastati are not a separate unit: "Hastati may be replaced by Raw Hastati to depict hastily-raised and very young troops levied in
    emergencies" (Hannibal p.57) is a unit upgrade on Hastati: -2 pts per model, WS 3 -> 2 and Ld 7 -> 5 (Raw Hastatus 4 2 3 3 3 1 3 1 5, 7 pts).
    The separate 'Raw Hastati' unit entry (and the ratio rule that counted it) is removed.
 2. Balearic Slingers are named in no composition on pp.51-52, so they are unavailable in every composition (hidden, maximum 0).
Usage: python3 roman_fixes.py <outdir>"""
import sys, os, re, hashlib
OUT = sys.argv[1]
FN = 'Republican_Roman_Hannibal.cat'
PATH = os.path.join(OUT, FN)
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
WS, LD = 'bb04-2b70-ae79-3559', 'b6d1-0987-3a4d-d6a9'
RAW_NAME = 'Raw Hastati (hastily raised: WS 2, Ld 5)'
s = open(PATH, encoding='utf8').read()
orig = s

def unit_block(name):
    m = re.search(r'^    <selectionEntry id="([^"]*)" name="%s"[^>]*type="unit">\n.*?\n    </selectionEntry>\n' % re.escape(name), s, re.S | re.M)
    return m

# ---- 1. Raw Hastati ----
m = unit_block('Raw Hastati')
if m:
    rid = m.group(1)
    s = s.replace(m.group(0), '', 1)
    # the Hastati need-modifier that counted Raw Hastati against the Principes minimum
    s = re.sub(r'        <modifier type="increment" field="[^"]*" value="-1">\n          <repeats>\n            <repeat [^>]*childId="%s"[^>]*/>\n          </repeats>\n        </modifier>\n' % re.escape(rid), '', s)
    assert rid not in s, 'dangling reference to Raw Hastati'
m = unit_block('Hastati'); uid = m.group(1); blk = m.group(0)
if '<!-- raw-hastati -->' not in blk:
    mid = re.search(r'<selectionEntry id="([^"]*)" name="Hastatus"[^>]*type="model">', blk).group(1)
    oid = hid(uid, 'raw-hastati')
    opt = (f'        <selectionEntry id="{oid}" name="{RAW_NAME}" hidden="false" collective="false" import="true" type="upgrade">\n'
           f'          <!-- raw-hastati -->\n'
           f'          <constraints>\n'
           f'            <constraint field="selections" scope="parent" value="1" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(oid, "max")}" type="max"/>\n'
           f'            <constraint field="selections" scope="parent" value="0" percentValue="false" shared="false" includeChildSelections="false" includeChildForces="false" id="{hid(oid, "min")}" type="min"/>\n'
           f'          </constraints>\n'
           f'          <modifiers>\n'
           f'            <modifier type="increment" field="points" value="-2">\n'
           f'              <repeats>\n'
           f'                <repeat field="selections" scope="parent" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="{mid}" repeats="1" roundUp="false"/>\n'
           f'              </repeats>\n'
           f'            </modifier>\n'
           f'          </modifiers>\n'
           f'          <costs>\n'
           f'            <cost name="pts" typeId="points" value="0"/>\n'
           f'          </costs>\n'
           f'        </selectionEntry>\n')
    # after the Drilled option
    dm = re.search(r'        <selectionEntry id="[^"]*" name="Drilled"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n', blk, re.S)
    new = blk.replace(dm.group(0), dm.group(0) + opt, 1)
    # statline: WS 2, Ld 5 when taken
    cond = (f'                <condition field="selections" scope="{uid}" value="1" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{oid}" type="atLeast"/>\n')
    mods = ''.join(f'              <modifier type="set" field="{f}" value="{v}">\n                <conditions>\n{cond}                </conditions>\n              </modifier>\n'
                   for f, v in ((WS, '2'), (LD, '5')))
    mods = '                <!-- raw-hastati -->\n' + mods
    pm = re.search(r'(<profile id="[^"]*" name="Hastatus"[^>]*typeName="Model">\n.*?</characteristics>\n)(              <modifiers>\n)?', new, re.S)
    if pm.group(2):
        new = new.replace(pm.group(0), pm.group(1) + pm.group(2) + mods, 1)
    else:
        raise SystemExit('Hastatus profile has no modifiers block (run sv_stat.py first)')
    new = new.replace('May be Drilled (+2). One unit of Hastati', f'May be Drilled (+2). May be Raw Hastati (hastily raised and very young troops levied in emergencies): -2 pts per model, WS 2, Ld 5. One unit of Hastati', 1)
    s = s.replace(blk, new, 1)

# ---- 2. Balearic Slingers: unavailable in every composition ----
m = unit_block('Balearic Slingers'); blk = m.group(0)
if '<!-- unavailable -->' not in blk:
    uid = m.group(1)
    head, rest = blk.split('\n', 1)
    head = head.replace('hidden="false"', 'hidden="true"', 1)
    con = (f'      <!-- unavailable -->\n      <constraints>\n        <constraint field="selections" scope="force" value="0" percentValue="false" shared="true" includeChildSelections="false" '
           f'includeChildForces="false" id="{hid(uid, "unavailable")}" type="max"/>\n      </constraints>\n')
    assert '      <constraints>\n' not in rest.split('<categoryLinks>')[0], 'unit already has constraints'
    rest = rest.replace('      <modifiers>\n', con + '      <modifiers>\n', 1)
    new = head + '\n' + rest
    new = new.replace('Not named in any army composition on pp.51-52.', 'Not named in any army composition on pp.51-52, so it is unavailable in every composition (kept for reference).')
    s = s.replace(blk, new, 1)

if s != orig:
    s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1)
    open(PATH, 'w', encoding='utf8').write(s)
    print('Roman fixes applied')
else:
    print('Roman fixes already applied')
