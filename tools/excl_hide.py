#!/usr/bin/env python3
"""Either/or choices (alternative generals, 'King or Marshal', mounted vs dismounted versions, Hypaspists vs Royal Guard Phalanx ...):
the unit that is excluded by another unit already in the army is HIDDEN, in addition to failing validation, so it cannot be added by mistake
and no confusing "too many of X (max 0)" error appears.  The Requirements note ("Not with") is unchanged.
Usage: python3 excl_hide.py <outdir>   (run after the *_limits scripts; idempotent)"""
import sys, re, glob, os
OUT = sys.argv[1]
SKIP = ('carth-', 'roman-', 'limit-', 'size-', 'need', 'prereq', 'min-', 'hide-', 'spanish-', 'req-')
total = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); orig = s
    units = {m.group(1) for m in re.finditer(r'^    <selectionEntry id="([^"]*)" name="[^"]*"[^>]*type="unit">', s, re.M)}
    def do_unit(um):
        global total
        blk = um.group(0)
        if '<!-- hide-excl -->' in blk: return blk
        head = blk[:blk.find('<categoryLinks>')]
        cons = set(re.findall(r'<constraint field="selections" scope="force" value="-?\d+"[^>]*id="([^"]*)" type="max"/>', head))
        found = []; tag = ''
        for lb in re.finditer(r'(?:^ *<!-- ([^>]*) -->\n)|(<modifier type="set" field="([^"]*)" value="0">\n(.*?)</modifier>\n)', head, re.S | re.M):
            if lb.group(1) is not None: tag = lb.group(1); continue
            if lb.group(3) not in cons or tag.startswith(SKIP) or '<conditionGroup' in lb.group(4): continue
            ids = re.findall(r'childId="([^"]*)" type="atLeast"', lb.group(4))
            if ids and all(i in units for i in ids) and 'lessThan' not in lb.group(4): found.append(lb.group(4))
        if not found: return blk
        ind = re.search(r'^( *)<modifiers>\n', head, re.M)
        if not ind: return blk
        pad = ind.group(1) + '  '
        add = f'{pad}<!-- hide-excl -->\n' + ''.join(f'{pad}<modifier type="set" field="hidden" value="true">\n{b.rstrip(" ")}{pad}</modifier>\n' for b in found)
        total += len(found)
        return blk.replace(ind.group(0), ind.group(0) + add, 1)
    s = re.sub(r'^    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S | re.M)
    if s != orig: open(path, 'w', encoding='utf8').write(s)
print('exclusion hide modifiers added:', total)
