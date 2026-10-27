#!/usr/bin/env python3
"""Table-driven army-list limits that the books state in words (idempotent; run after the book's own pipeline and composition_exclusions).
The rules live in tools/rules_limits.json, a list of objects {"cat": "X.cat", "type": ..., ...}.  Types:
  unit_max   {unit, n, comps?}              at most n units of this entry in the force            ("0-1 Elite Cavalry")
  unit_min   {unit, n, comps?}              at least n units                                      ("at least one unit of Phalangites")
  ratio      {unit, per_units, per, comps?} unit may be taken once per `per` units of the entries in per_units  (min on the base unit, like Hannibal)
  points     {unit, per, plus?, minus?, comps?} one unit per `per` army points, plus `plus` extra (minus: other entries that share the allowance)
  opt_max    {unit, option, n, comps?}      the option may be taken on at most n units in the force ("one unit may upgrade to Royal Guard")
  opt_every  {unit, option, k, comps?, of?} the option may be taken on at most ceil(units/k) units ("every second unit"); `of` lists the entries
                                           whose units are counted (default: the unit itself; 'Unit::Option' counts units that took that option)
  (opt_max / opt_every also take `share`: other options of the same unit that draw on the same allowance, e.g. sling OR short bow)
  opt_need   {unit, option, needs}          the option is available only while a unit of one of `needs` is in the force ("only with chariots")
`comps` = list of substrings of the Army composition picker names the rule applies to (default: every composition).
Rounding: "every second / third unit" and "up to half the units" allow ceil(units / k) (the first unit may have it).
Usage: python3 rules_limits.py <outdir>"""
import sys, os, re, json, hashlib
OUT = sys.argv[1]
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from limlib import Cat, mod, cond, hid, BIG
from ratiolib import ratio
SPEC = json.load(open(os.path.join(HERE, 'rules_limits.json'), encoding='utf8'))
VAR = json.load(open(os.path.join(HERE, 'variants.json'), encoding='utf8'))

def esc(n): return re.escape(n.replace('&', '&amp;'))
def pickers(cat, comps):
    out = []
    for c in comps or []:
        vs = [v for v in VAR[cat.fn] if c in v['name']]
        if len(vs) != 1: raise SystemExit(f'{cat.fn}: composition "{c}" matches {len(vs)} pickers')
        out.append(cat.vid(vs[0]['name']))
    return out
def tag_of(r):
    return r.get('tag') or ('rl-' + hashlib.md5(json.dumps(r, sort_keys=True).encode()).hexdigest()[:8])

def find_option(cat, unit, option):
    uid, mid, m = cat.unit(unit)
    blk = m.group(0)
    hits = list(re.finditer(r'^( *)<selectionEntry id="([^"]*)" name="%s"[^>]*type="upgrade">\n.*?\n\1</selectionEntry>\n' % esc(option), blk, re.S | re.M))
    if len(hits) != 1: raise SystemExit(f'{cat.fn}: unit "{unit}" option "{option}" matches {len(hits)} entries')
    return uid, hits[0].group(2), hits[0], blk

def add_option_limit(cat, unit, option, tag, base, mods):
    """force-scope max on an option entry (counts the option over every unit of the force) + modifiers"""
    uid, oid, om, blk = find_option(cat, unit, option)
    o = om.group(0)
    if f'<!-- {tag} -->' in o: return
    ind = om.group(1)
    cid = hid(oid, tag)
    con = (f'{ind}  <constraint field="selections" scope="force" value="{base}" percentValue="false" shared="true" includeChildSelections="false" '
           f'includeChildForces="false" id="{cid}" type="max"/>\n')
    if f'{ind}  </constraints>\n' not in o: raise SystemExit(f'{cat.fn}: option {option} of {unit} has no constraints')
    new = o.replace(f'{ind}  </constraints>\n', con + f'{ind}  </constraints>\n', 1)
    mx = ''.join(mods(cid))
    if mx:
        modxml = f'{ind}    <!-- {tag} -->\n' + ''.join((f'{ind}    ' + l if l.strip() else l) for l in mx.splitlines(True))
        if f'{ind}  <modifiers>\n' in new:
            new = new.replace(f'{ind}  <modifiers>\n', f'{ind}  <modifiers>\n' + modxml, 1)
        else:
            new = new.replace(f'{ind}  </constraints>\n', f'{ind}  </constraints>\n{ind}  <modifiers>\n' + modxml + f'{ind}  </modifiers>\n', 1)
    if not mx:
        new = new.replace(f'{ind}  </constraints>\n', f'{ind}  </constraints>\n{ind}  <!-- {tag} -->\n', 1)
    cat.s = cat.s.replace(o, new, 1); cat.changed = True

def rep(child, per, round_up):
    return (f'  <repeats>\n    <repeat field="selections" scope="force" value="{per}" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" repeats="1" roundUp="{"true" if round_up else "false"}"/>\n  </repeats>\n')

def cond_n(child, op, n):
    return cond(child, op).replace('value="1"', f'value="{n}"', 1)

def ref_id(cat, ref):
    """'Unit' -> unit entry id; 'Unit::Option' -> option entry id"""
    if '::' in ref:
        u, o = ref.split('::', 1)
        return find_option(cat, u, o)[1]
    return cat.unit(ref)[0]

def apply(cat, r):
    t, tag = r['type'], tag_of(r)
    ps = pickers(cat, r.get('comps'))
    if t in ('unit_max', 'unit_min'):
        ctype = 'max' if t == 'unit_max' else 'min'
        if ps:
            base = BIG if ctype == 'max' else 0
            mods = lambda cid: [mod('set', cid, r['n'], conds=[cond(p, 'atLeast')]) for p in ps]
        else:
            base, mods = r['n'], (lambda cid: [])
        cat.add_unit_limit(r['unit'], tag, ctype, base, mods)
    elif t == 'ratio':
        if ps: raise SystemExit('ratio rules with comps are not supported; write them in a book script')
        ratio(cat, r['unit'], r['per_units'], per=r.get('per', 1), tag=tag)
    elif t == 'points':
        others = [cat.unit(o)[0] for o in r.get('minus', [])]
        plus = r.get('plus', 0)
        def pts_mod(cid, conds):
            x = (f'<modifier type="increment" field="{cid}" value="1">\n  <repeats>\n    <repeat field="points" scope="roster" value="{r["per"]}" percentValue="false" shared="true" '
                 f'includeChildSelections="true" includeChildForces="true" repeats="1" roundUp="false"/>\n  </repeats>\n')
            if conds: x += '  <conditions>\n' + ''.join(f'    {c}\n' for c in conds) + '  </conditions>\n'
            return x + '</modifier>\n'
        def mods(cid):
            out = []
            for p in (ps or [None]):
                cs = [cond(p, 'atLeast')] if p else []
                if p: out.append(mod('set', cid, plus, conds=cs))
                out.append(pts_mod(cid, cs))
                out += [mod('increment', cid, -1, conds=cs, repeat=(o, 1, 'false')) for o in others]
            return out
        cat.add_unit_limit(r['unit'], tag, 'max', BIG if ps else plus, mods)
    elif t == 'opt_max':
        share = [ref_id(cat, o if '::' in o else r['unit'] + '::' + o) for o in r.get('share', [])]
        n = r['n']
        if share and not (n == 1 or (n == 2 and len(share) == 1)):
            print(f"  note: {cat.fn}: {r['unit']} / {r['option']}: allowance shared with {len(share)} other options is not enforced, each option is limited to {n} unit(s)")
            share = []
        assert not (ps and share), 'comps together with share is not supported'
        def mods(cid):
            out = [mod('set', cid, n, conds=[cond(p, 'atLeast')]) for p in ps]
            # no arithmetic on the other options' counts: a negative maximum would mean "no limit" in the program
            if n == 1:
                out += [mod('set', cid, 0, conds=[cond(o, 'atLeast')]) for o in share]
            elif share:
                out += [mod('set', cid, 1, conds=[cond_n(share[0], 'atLeast', 1)]), mod('set', cid, 0, conds=[cond_n(share[0], 'atLeast', 2)])]
            return out
        add_option_limit(cat, r['unit'], r['option'], tag, BIG if ps else n, mods)
    elif t == 'opt_every':
        counted = [ref_id(cat, u) for u in r.get('of', [r['unit']])]
        share = [ref_id(cat, o if '::' in o else r['unit'] + '::' + o) for o in r.get('share', [])]
        if len(share) > 1:
            print(f"  note: {cat.fn}: {r['unit']} / {r['option']}: allowance shared with {len(share)} other options is not enforced, each option is limited on its own")
            share = []
        def mods_base(cid):
            out = []
            if ps:
                for p in ps:
                    out.append(mod('set', cid, 0, conds=[cond(p, 'atLeast')]))
                    for u in counted:
                        out.append(mod_rep('increment', cid, 1, u, r['k'], [cond(p, 'atLeast')]))
            else:
                for u in counted: out.append(mod_rep('increment', cid, 1, u, r['k'], []))
            return out
        base = BIG if ps else 0
        add_option_limit(cat, r['unit'], r['option'], tag, base, lambda cid: mods_base(cid) + [mod('increment', cid, -1, repeat=(o, 1, 'false')) for o in share])
        if share:   # the shared limit alone could go negative (= no limit) when the other option is overused, so each option also keeps its own limit
            add_option_limit(cat, r['unit'], r['option'], tag + 'o', base, mods_base)
    elif t == 'opt_need':
        needs = [cat.unit(u)[0] for u in r['needs']]
        # max 0 until a unit of one of `needs` is in the force
        add_option_limit(cat, r['unit'], r['option'], tag, 0, lambda cid: [mod('set', cid, BIG, conds=[cond(n, 'atLeast')]) for n in needs])
    else:
        raise SystemExit('unknown rule type ' + t)

def mod_rep(kind, field, value, child, per, conds):
    x = f'<modifier type="{kind}" field="{field}" value="{value}">\n' + rep(child, per, True)
    if conds: x += '  <conditions>\n' + ''.join(f'    {c}\n' for c in conds) + '  </conditions>\n'
    return x + '</modifier>\n'

cats = {}
for r in SPEC:
    fn = r['cat']
    if not os.path.exists(os.path.join(OUT, fn)): continue
    cat = cats.setdefault(fn, Cat(fn))
    apply(cat, r)
n = 0
for cat in cats.values():
    if cat.changed: n += 1
    cat.save()
print(f'Rules applied to {n} catalogue(s)' if n else 'Rules already applied')
