#!/usr/bin/env python3
"""Additional / extra / third crew are folded into the existing crew entry: the crew entry's maximum becomes base + extra and the extra crewmen's points are charged
on the unit once the crew count passes the base number.  New Recruit then shows one crew line whose count follows the number of crewmen ("Crew (x3)").
The separate 'Additional ...' entry is removed.  (Also undoes the earlier name-modifier approach.)
Usage: python3 crew_merge.py <outdir>   (idempotent)"""
import sys, os, re, glob
OUT = sys.argv[1]
ADD = re.compile(r'^(additional|extra|third)\b', re.I)
n_units = 0
ENT = r'^        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="(?:model|upgrade)">\n.*?\n        </selectionEntry>\n'
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); orig = s
    def do_unit(um):
        global n_units
        blk = um.group(0); uid = re.match(r'    <selectionEntry id="([^"]*)"', blk).group(1)
        ents = [(m.group(1), m.group(2), m.group(0)) for m in re.finditer(ENT, blk, re.S | re.M)]
        out = blk
        for aid, aname, ablk in ents:
            if not ADD.match(aname) or not re.search(r'crew', aname, re.I): continue
            core = re.sub(r'\s*\(.*\)$', '', ADD.sub('', aname)).strip().lower()
            base = next((e for e in ents if e[1].lower() == core and not ADD.match(e[1])), None) or next((e for e in ents if e[1].lower() in ('crew', 'crewman', 'crewmen') and not ADD.match(e[1])), None)
            if not base: continue
            bid, bname, bblk = base
            bmin = re.search(r'<constraint field="selections" scope="parent" value="(\d+)"[^>]*type="min"', bblk)
            bmax = re.search(r'( *<constraint field="selections" scope="parent" value=")(\d+)("[^>]*type="max"/>)', bblk)
            amax = re.search(r'<constraint field="selections" scope="parent" value="(\d+)"[^>]*type="max"', ablk)
            cost = re.search(r'<cost name="pts" typeId="points" value="(-?[0-9.]+)"', ablk)
            if not (bmin and bmax and amax and cost): continue
            n0, extra, c = int(bmin.group(1)), int(amax.group(1)), cost.group(1)
            nb = bblk
            nb = re.sub(r'(<profile id="[^"]*" name="[^"]*?) \(\d+x\)("[^>]*typeName="Model")', r'\1\2', nb)           # undo the earlier "Crew (Nx)" names
            nb = re.sub(r'^ *<!-- crew-line -->\n(?: *<modifier type="set" field="name" [^\n]*\n.*?</modifier>\n)+', '', nb, flags=re.M | re.S)
            nb = re.sub(r'^ *<modifiers>\n *</modifiers>\n', '', nb, flags=re.M)
            nb = nb.replace(bmax.group(0), bmax.group(1) + str(n0 + extra) + bmax.group(3), 1)
            mods = ''
            if float(c) != 0:
                for k in range(1, extra + 1):
                    mods += (f'        <modifier type="increment" field="points" value="{c}">\n          <conditions>\n'
                             f'            <condition field="selections" scope="{uid}" value="{n0 + k}" percentValue="false" shared="true" includeChildSelections="false" '
                             f'includeChildForces="false" childId="{bid}" type="atLeast"/>\n          </conditions>\n        </modifier>\n')
            out = out.replace(ablk, '', 1).replace(bblk, nb, 1)
            # per-model option costs that repeated over the extra crewman now count the crew entry (once)
            def fixmod(k):
                b = k.group(0)
                if f'childId="{aid}"' not in b: return b
                reps = re.findall(r'^ *<repeat [^\n]*/>\n', b, re.M)
                mine = [r for r in reps if f'childId="{aid}"' in r]
                if len(reps) > len(mine): return b.replace(mine[0], '', 1)
                return b.replace(f'childId="{aid}"', f'childId="{bid}"')
            out = re.sub(r'^ *<modifier [^\n]*>\n(?: *<[^\n]*\n)*? *</modifier>\n', fixmod, out, flags=re.M)
            if mods:
                mods = '      <!-- crew-merge -->\n' + mods
                if re.search(r'^      <modifiers>\n', out, re.M): out = re.sub(r'^( *<modifiers>\n)', lambda k: k.group(1) + mods, out, count=1, flags=re.M)
                else: out = out.replace('      <categoryLinks>', '      <modifiers>\n' + mods + '      </modifiers>\n      <categoryLinks>', 1)
                if not re.search(r'^      <costs>\n', out, re.M):
                    out = re.sub(r'\n    </selectionEntry>\n$', '\n      <costs>\n        <cost name="pts" typeId="points" value="0"/>\n      </costs>\n    </selectionEntry>\n', out)
            n_units += 1
        return out
    s = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    if s != orig: open(path, 'w', encoding='utf8').write(s)
print('crew entries merged in', n_units, 'units')
