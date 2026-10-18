#!/usr/bin/env python3
"""Armies of Antiquity: availability limits (helpers in limlib.py, copied from fw_limits.py).
 - RATIOS: unit A may be taken at most once per N units of B (A <= units(B)/N)
 - FIGS:   figures of A may not exceed figures of B / N (Nomadic Noble cavalry vs horse archers)
 - EXCL:   A and B may not both be in the army;  REQ: A needs B in the army
 - NO_STANDARDS: the unit standard bearer option is removed from every unit (Greek Oracles rule)
 - OPT_PAIRS: an option may be taken once across the listed units (Sacred Band)
 - PTSLIM: "one per N points in the army": max = floor(roster points / N), minus the units sharing the allowance
Usage: python3 aoa_limits.py <outdir>   (run after the post-processing scripts; idempotent)"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from limlib import *
import aoa_data as D

def no_standards(cat):
    n = re.sub(r'^( +)<selectionEntry id="[^"]*" name="Standard bearer"[^>]*type="upgrade">\n.*?\n\1</selectionEntry>\n', '', cat.s, flags=re.S | re.M)
    if n != cat.s: cat.s = n; cat.changed = True

def points_limit(cat, unit, per, shared):
    others = [cat.unit(o)[0] for o in shared]
    def mods(cid):
        out = [f'<modifier type="increment" field="{cid}" value="1">\n  <repeats>\n    <repeat field="points" scope="roster" value="{per}" percentValue="false" shared="true" includeChildSelections="true" includeChildForces="true" repeats="1" roundUp="false"/>\n  </repeats>\n</modifier>\n']
        for o in others: out.append(mod('increment', cid, -1, repeat=(o, 1, 'false')))
        return out
    cat.add_unit_limit(unit, f'points-limit-1-per-{per}', 'max', 0, mods)

def option_once(cat, pairs, tag):
    """the same option in several units: at most one selection in the whole roster"""
    for unit, label in pairs:
        uid, mid, m = cat.unit(unit)
        mm = re.search(r'^( +)<selectionEntry id="([^"]*)" name="%s"[^>]*type="upgrade">\n.*?\n\1</selectionEntry>\n' % re.escape(label.replace('&', '&amp;')), m.group(0), re.S | re.M)
        if not mm: raise SystemExit(f'{cat.fn}: no option {label} in {unit}')
        blk, oid = mm.group(0), mm.group(2)
        cid = hid(oid, tag)
        if cid in blk: continue
        con = (f'<constraint field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" '
               f'includeChildForces="false" id="{cid}" type="max"/>\n')
        if '<constraints>\n' not in blk: raise SystemExit(f'{cat.fn}: no constraints in option {oid}')
        nb = blk.replace('<constraints>\n', '<constraints>\n' + con, 1)
        cat.s = cat.s.replace(blk, nb, 1); cat.changed = True

for key, name, fn, units, lim, notes, vs in D.LISTS:
    todo = [r for r in D.RATIOS if r[0] == key] + [r for r in D.FIGS if r[0] == key] + [r for r in D.EXCL if r[0] == key] + [r for r in D.REQ if r[0] == key] + [r for r in D.PTSLIM if r[0] == key]
    if not todo and key not in D.NO_STANDARDS and not [r for r in D.OPT_PAIRS if r[0] == key]: continue
    cat = Cat(fn)
    for _, a, bs, per in [r for r in D.RATIOS if r[0] == key]:
        ratio(cat, a, bs, per)
    for _, a, b, per in [r for r in D.FIGS if r[0] == key]:
        bm = cat.unit(b)[1]
        cat.add_model_limit(a, f'limit-figures-vs-{b}', 'force', BIG, lambda cid, bm=bm, per=per: [mod('set', cid, 0), mod('increment', cid, 1, repeat=(bm, per, 'true'))])
    for _, a, b in [r for r in D.EXCL if r[0] == key]:
        ua, ub = cat.unit(a)[0], cat.unit(b)[0]
        cat.add_unit_limit(a, f'excl-{b}', 'max', BIG, lambda cid, ub=ub: [mod('set', cid, 0, conds=[cond(ub, 'atLeast')])])
        cat.add_unit_limit(b, f'excl-{a}', 'max', BIG, lambda cid, ua=ua: [mod('set', cid, 0, conds=[cond(ua, 'atLeast')])])
    for _, a, b in [r for r in D.REQ if r[0] == key]:
        ub = cat.unit(b)[0]
        cat.add_unit_limit(a, f'needs-{b}', 'max', 0, lambda cid, ub=ub: [mod('set', cid, BIG, conds=[cond(ub, 'atLeast')])])
    for _, u, per, shared in [r for r in D.PTSLIM if r[0] == key]:
        points_limit(cat, u, per, shared)
    if key in D.NO_STANDARDS: no_standards(cat)
    for _, pairs in [r for r in D.OPT_PAIRS if r[0] == key]:
        option_once(cat, pairs, 'sacred-band-once')
    cat.save()
print('armies of antiquity limits added')
