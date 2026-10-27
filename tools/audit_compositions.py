#!/usr/bin/env python3
"""Read-only audit of the Army composition pickers.  For every catalogue with several compositions it works out which units are AVAILABLE
(visible and not capped at 0) once each composition is picked, and compares that with the unit names written in that composition's text
(the 'ARMY COMPOSITIONS' note).  It prints, per composition:
   MENTIONED-NOT-AVAILABLE   unit names found in the composition text that cannot be added (often a deliberate "no X" in the text)
   AVAILABLE-NOT-MENTIONED   units that can be added but are not named in the text (possible "left unrestricted" errors)
   NEVER AVAILABLE           units that no composition allows
Usage: python3 audit_compositions.py [<outdir>] [catalogue.cat ...]   (outdir defaults to the repo root)"""
import sys, os, re, json, hashlib
import xml.etree.ElementTree as ET
args = [a for a in sys.argv[1:] if a != '--review']
REVIEW = '--review' in sys.argv[1:]
REPO = args.pop(0) if args and os.path.isdir(args[0]) else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NS = '{http://www.battlescribe.net/schema/catalogueSchema}'
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
V = json.load(open(os.path.join(REPO, 'tools', 'variants.json'), encoding='utf8'))

def cond_true(c, picked):
    if c.get('field') != 'selections': return False
    n = 1 if c.get('childId') == picked else 0
    val = float(c.get('value'))
    return {'atLeast': n >= val, 'lessThan': n < val, 'greaterThan': n > val, 'equalTo': n == val, 'notEqualTo': n != val, 'atMost': n <= val}[c.get('type')]
def group_true(g, picked):
    parts = [cond_true(c, picked) for c in g.findall(NS + 'conditions/' + NS + 'condition')]
    parts += [group_true(x, picked) for x in g.findall(NS + 'conditionGroups/' + NS + 'conditionGroup')]
    if not parts: return True
    return all(parts) if g.get('type', 'and') == 'and' else any(parts)
def mod_true(m, picked):
    parts = [cond_true(c, picked) for c in m.findall(NS + 'conditions/' + NS + 'condition')]
    parts += [group_true(g, picked) for g in m.findall(NS + 'conditionGroups/' + NS + 'conditionGroup')]
    return all(parts) if parts else True
def unit_state(u, picked):
    hidden = u.get('hidden') == 'true'
    cons = {c.get('id'): float(c.get('value')) for c in u.findall(NS + 'constraints/' + NS + 'constraint')
            if c.get('type') == 'max' and c.get('field') == 'selections' and c.get('scope') in ('force', 'roster')}
    ratio = set()    # constraints that a ratio rule (repeat modifier) raises once the composition is picked
    for m in u.findall(NS + 'modifiers/' + NS + 'modifier'):
        if not mod_true(m, picked): continue
        f, t, v = m.get('field'), m.get('type'), m.get('value')
        if m.find(NS + 'repeats') is not None:
            if f in cons and t == 'increment' and float(v) > 0: ratio.add(f)
            continue
        if f == 'hidden' and t == 'set': hidden = (v == 'true')
        elif f in cons and t == 'set': cons[f] = float(v)
    for f in ratio:
        if cons[f] == 0: cons[f] = -2     # conditionally available (depends on other units in the army)
    return hidden, cons   # max -1 = no limit, -2 = only through a ratio rule, 0 = not allowed

def stem(w):
    w = w.lower()
    for a, b in (('ies', 'y'), ('es', ''), ('s', '')):
        if w.endswith(a) and len(w) > 4: return w[:-len(a)] + b
    return w
def words(t): return [stem(w) for w in re.findall(r"[A-Za-z']+", t)]
def mentioned(name, text_words, text_low):
    base = re.sub(r'\s*\(.*?\)', '', name.replace('&amp;', '&')).strip()
    if base.lower() in text_low: return True
    bw = words(base)
    if not bw: return False
    for i in range(len(text_words) - len(bw) + 1):
        if text_words[i:i + len(bw)] == bw: return True
    return False

def comp_texts(root):
    """composition name -> text, from the 'ARMY COMPOSITIONS' note"""
    s = ET.tostring(root, encoding='unicode')
    m = re.search(r'ARMY COMPOSITIONS[^\n]*\n(.*?)(?:</|$)', s, re.S)
    out = {}
    if not m: return out
    cur = None
    for line in m.group(1).split('\n'):
        mm = re.match(r'\[(.+)\]\s*$', line)
        if mm: cur = mm.group(1); out[cur] = ''; continue
        if cur and line.strip() and not re.match(r'\s*[A-Z][A-Za-z &;]*: (up to|at least)', line): out[cur] += ' ' + line.strip()
    return out

def audit(fn):
    vs = V[fn]
    root = ET.parse(os.path.join(REPO, fn)).getroot()
    units = [e for e in root.findall(NS + 'selectionEntries/' + NS + 'selectionEntry') if e.get('type') == 'unit']
    texts = comp_texts(root)
    res = []
    ever = set()
    for v in vs:
        pid = hid('picker', fn, v['name'])
        avail = []
        for u in units:
            h, cons = unit_state(u, pid)
            if not h and not any(x == 0 for x in cons.values()): avail.append(u.get('name'))
        ever |= set(avail)
        key = v['name'].replace('Hannibal: ', '')
        txt = texts.get(v['name']) or texts.get(key) or ''
        if not txt:
            for k, t in texts.items():
                if k.endswith(key) or key.endswith(k): txt = t
        tw, tl = words(txt), txt.lower()
        ment = {u.get('name') for u in units if mentioned(u.get('name'), tw, tl)}
        cat = {}
        for u in units:
            cl = u.find(NS + 'categoryLinks/' + NS + 'categoryLink')
            cat[u.get('name')] = cl.get('name') if cl is not None else ''
        flags = []
        for n in avail:
            if n in ment:
                base = re.sub(r'\s*\(.*?\)', '', n.replace('&amp;', '&')).strip().lower()
                for mm in re.finditer(re.escape(base.rstrip('s')) + r's?\b', tl):
                    before = tl[max(0, mm.start() - 60):mm.start()]
                    if re.search(r'\b(no|not|without|never|none|excluding|except|exclude[sd]?|may not (?:include|have|take|use))\b[^.;]*$', before):
                        flags.append(f'{n}  <- "...{tl[max(0, mm.start() - 45):mm.end() + 15].strip()}..."'); break
        zero = [c for c, lim in v.get('limits', {}).items() if lim.get('max') == 0]
        for n in avail:
            if cat[n] in zero: flags.append(f'{n}  <- category {cat[n]} is capped at 0%')
        res.append((v['name'], avail, sorted(ment - set(avail)), sorted(n for n in avail if n not in ment and cat[n] != 'Characters'), bool(txt), flags, txt, [u.get('name') for u in units if u.get('name') not in avail]))
    never = [u.get('name') for u in units if u.get('name') not in ever]
    return res, never, [u.get('name') for u in units]

if __name__ == '__main__':
    fns = args or sorted(k for k, v in V.items() if len(v) > 1)
    for fn in fns:
        if len(V.get(fn, [])) < 2: continue
        res, never, allu = audit(fn)
        print(f'== {fn}  ({len(allu)} units, {len(res)} compositions)')
        if never: print('   NEVER AVAILABLE:', '; '.join(never))
        for name, avail, mna, anm, hastext, flags, txt, unavail in res:
            print(f'   [{name}] available {len(avail)}{"" if hastext else "  (no composition text found)"}')
            for f in flags: print('      EXCLUDED-BUT-AVAILABLE?', f)
            if REVIEW:
                print('      TEXT:', re.sub(r'\s+', ' ', txt).strip()[:700])
                print('      UNAVAILABLE:', '; '.join(unavail) or '-')
            if mna: print('      mentioned-not-available:', '; '.join(mna))
            if anm: print('      available-not-mentioned:', '; '.join(anm))
