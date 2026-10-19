#!/usr/bin/env python3
"""SUPERSEDED by crew_merge.py (kept for reference; no longer run). Additional / extra / third crew are folded into the existing crew stat line instead of showing a second line:
the crew profile is named 'Crew (Nx)' and its name changes to 'Crew (N+kx)' when k additional crew are taken; the additional model's own profile is hidden.
Usage: python3 crew_lines.py <outdir>   (idempotent)"""
import sys, os, re, glob
OUT = sys.argv[1]
ADD = re.compile(r'^(additional|extra|third)\b', re.I)
CREWISH = re.compile(r'crew', re.I)
MODEL_T = 'a802-40b5-d980-cabc'
PRX = re.compile(r'( *<profile id="[^"]*" name=")([^"]*)("[^>]*typeId="' + MODEL_T + r'"[^>]*>\n)(.*?)( *</profile>\n)', re.S)
n_units = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); orig = s
    def do_unit(um):
        global n_units
        blk = um.group(0); uid = re.match(r'    <selectionEntry id="([^"]*)"', blk).group(1)
        models = [(m.group(1), m.group(2), m.group(0)) for m in re.finditer(r'^        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="model">\n.*?\n        </selectionEntry>\n', blk, re.S | re.M)]
        out = blk
        for aid, aname, ablk in models:
            if not ADD.match(aname) or not CREWISH.search(aname): continue
            if 'crew-line' in ablk: continue
            core = re.sub(r'\s*\(.*\)$', '', ADD.sub('', aname)).strip().lower()
            base = next((m for m in models if m[1].lower() == core and not ADD.match(m[1])), None) or next((m for m in models if m[1].lower() in ('crew', 'crewman', 'crewmen') and not ADD.match(m[1])), None)
            if not base: continue
            bid, bname, bblk = base
            bmin = re.search(r'<constraint field="selections" scope="parent" value="(\d+)"[^>]*type="min"', bblk)
            amax = re.search(r'<constraint field="selections" scope="parent" value="(\d+)"[^>]*type="max"', ablk)
            if not bmin or not amax: continue
            n0, extra = int(bmin.group(1)), int(amax.group(1))
            pm = PRX.search(bblk)
            if not pm or re.search(r'\(\d+x\)', pm.group(2)): continue
            label = bname
            mods = '                <!-- crew-line -->\n'
            for k in range(1, extra + 1):
                mods += (f'                <modifier type="set" field="name" value="{label} ({n0 + k}x)">\n                  <conditions>\n'
                         f'                    <condition field="selections" scope="{uid}" value="{k}" percentValue="false" shared="true" includeChildSelections="false" '
                         f'includeChildForces="false" childId="{aid}" type="atLeast"/>\n                  </conditions>\n                </modifier>\n')
            inner = pm.group(4)
            if '<modifiers>\n' in inner: inner = re.sub(r'( *<modifiers>\n)', lambda k: k.group(1) + mods, inner, count=1)
            else: inner += '              <modifiers>\n' + mods + '              </modifiers>\n'
            nb = bblk.replace(pm.group(0), pm.group(1) + f'{label} ({n0}x)' + pm.group(3) + inner + pm.group(5), 1)
            out = out.replace(bblk, nb, 1)
            # hide the additional model's own profile line
            ap = PRX.search(ablk)
            if ap:
                hid_ = ap.group(1) + ap.group(2) + re.sub(r'hidden="false"', 'hidden="true"', ap.group(3), count=1) + ap.group(4) + ap.group(5)
                na = ablk.replace(ap.group(0), hid_, 1).replace('<profiles>', '<!-- crew-line -->\n          <profiles>', 1)
                out = out.replace(ablk, na, 1)
            n_units += 1
        return out
    s = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    if s != orig: open(path, 'w', encoding='utf8').write(s)
print('crew lines merged in', n_units, 'units')
