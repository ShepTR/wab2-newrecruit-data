#!/usr/bin/env python3
"""Prerequisites ("R:" restrictions, "needs X first") as a MINIMUM on the prerequisite unit instead of a 'max 0' on the dependent unit.
Before: the dependent unit had an availability max of 0 that a modifier lifted once a prerequisite was in the army, so adding it first
showed "too many of <unit> (max 0)".  After: the dependent unit is freely addable (war availability is unchanged) and the first
prerequisite unit gets a minimum of 1 while the dependent unit is in the army (reduced by one per unit of the other prerequisites), so the
error names the unit to add, in any order.
Handles (1) war-specific 'or' groups inside carth/roman restriction modifiers and (2) the plain 'needs-...' unlock modifiers.
Marker comments  <!-- prereq:A -->  <!-- prereqalt:A -->  inside the prerequisite unit let req_notes rebuild the Requirements text.
Usage: python3 prereq_min.py <outdir>   (run after the *_restrictions / *_limits scripts and before req_notes; idempotent)"""
import sys, re, glob, os
from limlib import Cat, mod, cond, hid
OUT = sys.argv[1]
GRP = re.compile(r'( *)<conditionGroups>\n *<conditionGroup type="or">\n *<conditions>\n(.*?)\n *</conditions>\n *</conditionGroup>\n *</conditionGroups>\n(?=( *)</conditionGroup>\n *</conditionGroups>\n)', re.S)
CONDRE = re.compile(r'<condition [^>]*/>')
def child(c): return re.search(r'childId="([^"]*)"', c).group(1)
total = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    fn = os.path.basename(path)
    cat = Cat(fn)
    units = {m.group(1): m.group(2).replace('&amp;', '&') for m in re.finditer(r'^    <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="unit">', cat.s, re.M)}
    plan = {}     # (P1 name, A name) -> list of modifier xml strings
    for aid, aname in list(units.items()):
        m = cat.unit(aname)
        blk = m[2].group(0)
        head = blk[:blk.find('<categoryLinks>')]
        new = head
        # (1) war-specific prerequisite groups inside restriction modifiers
        out = []; pos = 0
        for mm in re.finditer(r'<modifier type="set" field="[^"]*" value="-?\d+">\n.*?</modifier>\n', new, re.S):
            body = mm.group(0)
            g = GRP.search(body)
            if g:
                prereq = [child(c) for c in CONDRE.findall(g.group(2)) if 'atLeast' in c]
                prereq = [p for p in prereq if p in units]
                if prereq:
                    warconds = CONDRE.findall(body[:g.start()])
                    p1, alts = prereq[0], prereq[1:]
                    lst = plan.setdefault((units[p1], aname), [])
                    base = warconds + [cond(aid, 'atLeast')]
                    lst.append('<!-- prereq:%s -->\n' % aname + mod('increment', '%CID%', 1, conds=base))
                    for o in alts:
                        lst.append('<!-- prereqalt:%s -->\n' % aname + mod('increment', '%CID%', -1, conds=base, repeat=(o, 1, 'false')))
                    total += 1
                    body = body.replace(g.group(0), '', 1)
            out.append((mm.start(), mm.end(), body))
        for s_, e_, b_ in reversed(out): new = new[:s_] + b_ + new[e_:]
        # (2) plain "needs X first" unlock modifiers (needs-*, need-chariots)
        tm = re.search(r'^ *<!-- (needs?-[^>]*) -->\n((?: *<modifier type="set" field="([^"]*)" value="1000">\n.*?</modifier>\n)+)', new, re.S | re.M)
        if tm:
            cid2 = tm.group(3)
            prereq = [child(c) for c in CONDRE.findall(tm.group(2)) if 'atLeast' in c]
            prereq = [p for p in prereq if p in units]
            if prereq:
                p1, alts = prereq[0], prereq[1:]
                lst = plan.setdefault((units[p1], aname), [])
                base = [cond(aid, 'atLeast')]
                lst.append('<!-- prereq:%s -->\n' % aname + mod('increment', '%CID%', 1, conds=base))
                for o in alts:
                    lst.append('<!-- prereqalt:%s -->\n' % aname + mod('increment', '%CID%', -1, conds=base, repeat=(o, 1, 'false')))
                new = new.replace(tm.group(0), '', 1)
                new = re.sub(r'^ *<constraint [^\n]*id="%s" type="max"/>\n' % re.escape(cid2), '', new, flags=re.M)
                new = re.sub(r'^ *<constraints>\n *</constraints>\n', '', new, flags=re.M)
                new = re.sub(r'^ *<modifiers>\n\s*</modifiers>\n', '', new, flags=re.M)
                total += 1
        if new != head:
            cat.s = cat.s.replace(blk, new + blk[len(head):], 1); cat.changed = True
    for (p1, aname), mods in plan.items():
        uid = cat.unit(p1)[0]
        cid_ = hid(uid, f'prereq-{aname}')
        cat.add_unit_limit(p1, f'prereq-{aname}', 'min', 0, lambda cid, mods=mods: [x.replace('%CID%', cid) for x in mods])
    cat.save()
print('prerequisite rules converted:', total)
