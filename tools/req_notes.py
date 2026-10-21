#!/usr/bin/env python3
"""Adds a visible "Requirements" profile (Take first / Limit / Not with, shown like Armour Save) to every unit whose availability depends on another unit in the force.
Read from the unit's own constraints/modifiers (as built by the limits scripts):
 - ratio:    max raised by N per unit of B            -> "Requires at least one of: B. One per N unit(s) of B."
 - unlock:   max set to >0 when X is in the force     -> "Requires at least one of: X, Y."
 - exclude:  max set to 0 / hidden when X is in force  -> "Cannot be taken if the force has: X, Y."
Idempotent (marker comment). Usage: python3 req_notes.py <outdir>"""
import sys, os, re, glob, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def esc(t): return t.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
MARK = '<!-- req-notes -->'
import json
_V = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'variants.json'), encoding='utf8'))
def pickers(fn):
    return {hid('picker', fn, e['name']): re.sub(r'^.*? - ', '', e['name']) if ' - ' in e['name'] else e['name'] for e in _V.get(fn, [])}
def join(names):
    names = list(dict.fromkeys(names))
    return ', '.join(names[:-1]) + (' or ' if len(names) > 1 else '') + names[-1] if len(names) > 1 else names[0]
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
PT = hid('ptype', 'Requirements'); CT = {k: hid('ctype', 'req-' + k) for k in ('Take first', 'Limit', 'Not with')}
_g = open(GST, encoding='utf8').read()
if f'id="{PT}"' not in _g:
    pt = (f'    <profileType id="{PT}" name="Requirements">\n      <characteristicTypes>\n' + ''.join(f'        <characteristicType id="{v}" name="{k}"/>\n' for k, v in CT.items()) +
          '      </characteristicTypes>\n    </profileType>\n')
    open(GST, 'w', encoding='utf8').write(_g.replace('  </profileTypes>', pt + '  </profileTypes>', 1))
tot = 0; per = {}
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    if MARK in s: s = s.replace(MARK + '\n', '')   # rebuild notes from scratch each time
    s = re.sub(r'      <rules>\n        <rule id="[^"]*" name="Requirements"[^>]*>.*?</rules>\n', '', s, flags=re.S)
    s = re.sub(r'      <profiles>\n        <profile id="[^"]*" name="Requirements"[^>]*>.*?</profile>\n      </profiles>\n', '', s, flags=re.S)
    units = {m.group(1): m.group(2).replace('&amp;', '&') for m in re.finditer(r'^    <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="unit">', s, re.M)}
    anyent = pickers(os.path.basename(path))
    # ratio rules built as a minimum on the base unit (ratiolib): <!-- need:A --> modifiers
    need_a, need_b = {}, {}
    for bm in re.finditer(r'^    <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', s, re.S | re.M):
        for nm in re.finditer(r'<!-- need:([^>]*?) -->\n\s*<modifier type="increment" field="[^"]*" value="(\d+)">', bm.group(0)):
            need_a.setdefault(nm.group(1), {})[bm.group(1).replace('&amp;', '&')] = int(nm.group(2)); need_b.setdefault(bm.group(1).replace('&amp;', '&'), {})[nm.group(1).replace('&amp;', '&')] = int(nm.group(2))
    # prerequisites written as a minimum on the prerequisite unit (prereq_min.py): <!-- prereq:A --> increment (+ <!-- prereqalt:A --> alternatives)
    prereq = {}   # A -> [(war picker names, [prerequisite unit names])]
    for bm in re.finditer(r'^    <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', s, re.S | re.M):
        cur = None
        for pm in re.finditer(r'<!-- (prereq|prereqalt):([^>]*?) -->\n\s*<modifier type="increment" field="[^"]*" value="-?1">\n(.*?)</modifier>', bm.group(0), re.S):
            kind_, an, body_ = pm.groups(); an = an.replace('&amp;', '&')
            if kind_ == 'prereq':
                wars_ = [anyent[c].replace('&amp;', '&') for c in re.findall(r'childId="([^"]*)" type="atLeast"', body_) if c not in units and c in anyent]
                cur = (wars_, [bm.group(1).replace('&amp;', '&')]); prereq.setdefault(an, []).append(cur)
            elif cur is not None:
                rid = re.search(r'<repeat [^>]*childId="([^"]*)"', body_)
                if rid and rid.group(1) in units: cur[1].append(units[rid.group(1)])
    need_alt = {}   # A -> other base units whose units also count toward A's ratio (several-base rules)
    for bm in re.finditer(r'^    <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', s, re.S | re.M):
        bn = bm.group(1).replace('&amp;', '&')
        for nm in re.finditer(r'<!-- needalt:([^>]*?) -->\n\s*<modifier type="increment" field="[^"]*" value="-1">\n\s*<repeats>\n\s*<repeat [^>]*childId="([^"]*)"', bm.group(0)):
            need_alt.setdefault(nm.group(1).replace('&amp;', '&'), []).append(nm.group(2))
    ids2name = {}
    for m_ in re.finditer(r'^    <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="unit">', s, re.M): ids2name[m_.group(1)] = m_.group(2).replace('&amp;', '&')
    out = s; n = 0
    for um in list(re.finditer(r'^    <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', s, re.S | re.M)):
        blk = um.group(0); uid, uname = um.group(1), um.group(2)
        cut = blk.find('<categoryLinks>')
        head = blk[:cut] if cut > 0 else blk
        cons = {m.group(2): (m.group(1), m.group(3)) for m in re.finditer(r'<constraint field="selections" scope="[^"]*" value="(-?\d+)"[^>]*id="([^"]*)" type="(max|min)"/>', head)}
        maxids = {cid: int(v) for cid, (v, t) in cons.items() if t == 'max'}
        ratio, unlock, excl, cunlock, wunlock = {}, [], [], {}, []
        pool, pts = [], []
        for mm in re.finditer(r'<modifier type="(\w+)" field="([^"]*)" value="([^"]*)">\n(.*?)</modifier>', head, re.S):
            kind, field, val, body = mm.groups()
            conds = re.findall(r'<condition field="selections" scope="force"[^>]*childId="([^"]*)" type="(\w+)"/>', body)
            names = [units[c] for c, t in conds if c in units and t == 'atLeast']
            lt = [units[c] for c, t in conds if c in units and t == 'lessThan']
            pick = [anyent[c].replace('&amp;', '&') for c, t in conds if c not in units and c in anyent and t == 'atLeast']
            if field in maxids:
                reps = re.findall(r'<repeat field="selections" scope="force" value="(\d+)"[^>]*childId="([^"]*)"', body)
                preps = re.findall(r'<repeat field="points" scope="roster" value="(\d+)"', body)
                if kind == 'increment' and preps:
                    pts.append(preps[0])
                elif kind == 'increment' and reps and val.startswith('-'):
                    pool += [units[c] for _, c in reps if c in units]      # shared pool: each of these units uses up one of the allowance
                elif kind == 'increment' and reps:
                    for per_n, c in reps:
                        if c in units: ratio[units[c]] = int(per_n)
                elif kind == 'set' and not names and pick and val not in ('0',):
                    wunlock += pick
                elif kind == 'set' and names and val not in ('0',):
                    if pick: cunlock.setdefault(tuple(names), []).extend(pick)
                    else: unlock += names
                elif kind == 'set' and names and val == '0':
                    excl += names
            elif field == 'hidden' and val == 'true':
                excl += names
                if lt and not names: unlock += lt
        req, lim, notw = [], [], []
        for wars_, names_ in prereq.get(uname.replace('&amp;', '&'), []):
            if wars_: cunlock.setdefault(tuple(names_), []).extend(wars_)
            else: unlock += names_
        ratio.update(need_a.get(uname.replace('&amp;', '&'), {}) or need_a.get(uname, {}))
        if uname in need_b:
            grp = {}
            for k, v in need_b[uname].items(): grp.setdefault(v, []).append(k)
            alts = sorted({ids2name.get(o, o) for k in need_b[uname] for o in need_alt.get(k, [])})
            lim.append('Need at least ' + '; and '.join(f'{v} unit{"s" if v > 1 else ""} for each unit of ' + ', '.join(k.replace('&amp;', '&') for k in ks) for v, ks in grp.items())
                       + (f' (units of {join(alts)} count toward this)' if alts else ''))
        combined = None
        if uname.replace('&amp;', '&') in need_alt and ratio:
            first = next(iter(ratio)); n_ = ratio[first]
            combined = (n_, [first] + [ids2name.get(o, o) for o in need_alt[uname.replace('&amp;', '&')]])
            ratio = {k: n_ for k in combined[1]}
        if ratio:
            allb = list(ratio)
            req.append('At least one of: ' + join(allb))
            if combined: lim.append(f'1 per {"" if combined[0] == 1 else str(combined[0]) + " units of "}{"unit of " if combined[0] == 1 else ""}' + join(combined[1]).replace(' or ', ' and ') + ' combined')
            else: lim.append('; '.join(f'1 per {"" if v == 1 else str(v) + " units of "}{k}' if v != 1 else f'1 per unit of {k}' for k, v in ratio.items()))
        if pts:
            lim.append(f'1 per {pts[0]} points in the army' + (f' (shared with {join(pool)})' if pool else ''))
        if unlock:
            req.append('At least one of: ' + join(unlock))
        wunlock = [w for w in dict.fromkeys(wunlock) if not any(w in v for v in cunlock.values())]
        if cunlock and wunlock:
            req.append('Available in: ' + join(wunlock))
        for nm, wars in cunlock.items():
            req.append('In ' + join(wars) + ': at least one of: ' + join(list(nm)))
        if excl:
            notw.append(join(list(dict.fromkeys(excl))))
        if not (req or lim or notw): continue
        def ch(name, v): return f'              <characteristic name="{name}" typeId="{CT[name]}">{esc(v) if v else "-"}</characteristic>\n'
        rule = (f'      <profiles>\n        <profile id="{hid(uid, "req-notes")}" name="Requirements" hidden="false" typeId="{PT}" typeName="Requirements">\n'
                f'          <characteristics>\n' + ch('Take first', '. '.join(req)) + ch('Limit', '. '.join(lim)) + ch('Not with', '. '.join(notw)) +
                '          </characteristics>\n        </profile>\n      </profiles>\n')
        nb = blk.replace('      <categoryLinks>', MARK + '\n' + rule + '      <categoryLinks>', 1) if '      <categoryLinks>' in blk else blk
        if nb != blk: out = out.replace(blk, nb, 1); n += 1
    if n: open(path, 'w', encoding='utf8').write(out); per[os.path.basename(path)] = n; tot += n
print('requirement notes added:', tot, 'in', len(per), 'catalogues')
