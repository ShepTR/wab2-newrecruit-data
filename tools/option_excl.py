#!/usr/bin/env python3
"""Mutually exclusive options.  Spec: tools/option_excl.json = [{"cat": glob, "unit": name|null, "groups": [[label prefix, ...], ...]}, ...]
For every unit (or the named one) and every group, the options whose label starts with one of the prefixes (same parent) hide each other:
once one is ticked, the others of the group are hidden (modifier appended last so it wins over availability modifiers).
Usage: python3 option_excl.py <outdir>   (idempotent)"""
import sys, os, re, json, glob, hashlib
OUT = sys.argv[1]; HERE = os.path.dirname(os.path.abspath(__file__))
SPEC = json.load(open(os.path.join(HERE, 'option_excl.json'), encoding='utf8'))
TAG = '<!-- optexcl -->'
def cnd(child):
    return (f'<condition field="selections" scope="parent" value="1" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" type="atLeast"/>')
def add_mod(blk, modxml):
    pm = re.search(r'^ *<profiles>\n.*?^ *</profiles>\n', blk, re.S | re.M)
    masked = blk if not pm else blk[:pm.start()] + ' ' * (pm.end() - pm.start()) + blk[pm.end():]
    ms = [m for m in re.finditer(r'^( *)</modifiers>\n', masked, re.M)]
    if ms:
        m = ms[-1]
        return blk[:m.start()] + modxml + blk[m.start():]
    m = re.search(r'^( *)(<!-- def-link -->|<rules>|<infoLinks>|<costs>)', blk, re.M)
    ind = m.group(1)
    return blk[:m.start()] + f'{ind}<modifiers>\n' + modxml + f'{ind}</modifiers>\n' + blk[m.start():]
total = 0
for pat in sorted({sp['cat'] for sp in SPEC}):
    for path in sorted(glob.glob(os.path.join(OUT, pat))):
        s = open(path, encoding='utf8').read(); orig = s
        for sp in [x for x in SPEC if x['cat'] == pat]:
            for um in list(re.finditer(r'^    <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', s, re.S | re.M)):
                if sp.get('unit') and um.group(1) != sp['unit'].replace('&', '&amp;'): continue
                ublk = um.group(0); new = ublk
                for grp in sp['groups']:
                    opts = []   # (indent, id, name, block)
                    for om in re.finditer(r'^( *)<selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade">\n.*?\n\1</selectionEntry>\n', new, re.S | re.M):
                        if any(om.group(3).startswith(p) for p in grp): opts.append(om)
                    byind = {}
                    for om in opts: byind.setdefault(om.group(1), []).append(om)
                    for ind, oms in byind.items():
                        if len(oms) < 2: continue
                        for om in oms:
                            blk = om.group(0)
                            if TAG in blk: continue
                            others = [o.group(2) for o in oms if o.group(2) != om.group(2)]
                            mods = ind + '  ' + TAG + '\n' + ''.join(
                                f'{ind}  <modifier type="set" field="hidden" value="true">\n{ind}    <conditions>\n{ind}      {cnd(o)}\n{ind}    </conditions>\n{ind}  </modifier>\n' for o in others)
                            new = new.replace(blk, add_mod(blk, mods), 1); total += 1
                if new != ublk: s = s.replace(ublk, new, 1)
        if s != orig: open(path, 'w', encoding='utf8').write(s)
print('exclusive options:', total)
