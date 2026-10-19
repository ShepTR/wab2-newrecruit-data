#!/usr/bin/env python3
"""Stage 2 for Armies of Antiquity v2 (unofficial, M. Gibbins): turn the extracted docx (aoa2_extract.py -> JSON) into tools/aoa2_data.py.
The generated data file is meant to be hand-corrected afterwards (re-running this script overwrites it).
Usage: python3 tools/aoa2_gen.py <ex.json> [gst]   (writes tools/aoa2_data.py and issues/Armies_of_Antiquity_v2.txt)"""
import sys, os, re, json, pprint
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
ex = json.load(open(sys.argv[1], encoding='utf8'))
gst = open(sys.argv[2] if len(sys.argv) > 2 else os.path.join(ROOT, 'Warhammer_Ancient_Battles_2.gst'), encoding='utf8').read()
GSTRULES = {n.replace('&amp;', '&') for n in re.findall(r'<rule id="[^"]*" name="([^"]*)"', gst)}
DEFS = {k: v for k, v in ex['rules'].items() if k}

def clean(t): return re.sub(r'\s+', ' ', t.replace(' ', ' ')).strip()
NUMW = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}

# ------------------------------------------------------------------ rules
RULE_TERMS = {   # text term -> gst rule name
 'Skirmishers': 'Skirmishers (Art of War)', 'Light Infantry': 'Light Troops', 'Light Cavalry': 'Light Troops', 'Light Camelry': 'Light Troops', 'Light Troops': 'Light Troops',
 'Combined Formation': 'Combined Formations', 'Combined Formations': 'Combined Formations', 'Combined Units': 'Combined Units',
 'Expert Horseman': 'Expert Horsemen', 'Expert Horsemen': 'Expert Horsemen', 'Army General': 'Army General', 'Army Standard': 'Army Standard',
 'Shock Cavalry': 'Shock Cavalry', 'Eastern Shock Cavalry': 'Eastern Shock Cavalry', 'Feigned Flight': 'Feigned Flight', 'Parthian Shot': 'Parthian Shot',
 'Nomad Cavalry': 'Nomad Cavalry', 'Stubborn': 'Stubborn', 'Veteran': 'Veteran', 'Drilled': 'Drilled', 'Phalanx': 'Phalanx', 'Levies': 'Levies', 'Warband': 'Warband',
 'Open Order': 'Open Order', 'Mixed Weapons': 'Mixed Weapons', 'Mixed Armour': 'Mixed Armour', 'Different Weapons': 'Different Weapons', 'Stealth': 'Stealth',
 'Special Deployment': 'Special Deployment', 'Oracles': 'Oracles', 'Xyston': 'Xyston', 'Wedge': 'Wedge', 'Strategem': 'Strategem', 'Stakes': 'Stakes',
 'Tethered Camels': 'Tethered Camels', 'Used to Elephants': 'Used to elephants', 'Used to elephants': 'Used to elephants', 'Rocket Artillery': 'Rocket Artillery',
 'Cataphracts': 'Cataphracts', 'Light Chariots': 'Light Chariots', 'Chariots': None, 'Unreliable': 'Allies and Mercenaries (Unreliable)',
 'Frenzy': 'Frenzy', 'Fierce': None, 'Impetuous': 'Impetuous', 'Hatred': 'Hatred', 'Ambush': 'Ambush', 'Camels': None, 'Massed Cavalry': 'Massed Cavalry',
}
GLOW = {n.lower(): n for n in GSTRULES}
RULE_TERMS['Stratagem'] = 'Strategem'
def rname(k): return re.sub(r'\s*\((?:page|p\.)\s*\d+\)', '', k).strip()
for k, v in DEFS.items():
    k2 = rname(k)
    if k2 not in RULE_TERMS and k2.lower() in GLOW: RULE_TERMS[k2] = GLOW[k2.lower()]
NEWRULES = {}   # rules defined by the AoA2 document that the gst does not have
for k, v in DEFS.items():
    k2 = rname(k)
    if k2.lower() not in GLOW and k2 not in ('Bow', 'Characters') and RULE_TERMS.get(k2, 0) == 0:
        NEWRULES[k2] = v; RULE_TERMS[k2] = k2
TERM_RE = [(t, re.compile(r'(?<![A-Za-z])' + re.escape(t) + r'(?![A-Za-z])')) for t in sorted(RULE_TERMS, key=len, reverse=True) if RULE_TERMS[t]]

# ------------------------------------------------------------------ weapons
WEAP = [
 (r'hand weapons?', 'Hand Weapon'), (r'improvised weapons?', 'Improvised Weapon'), (r'heavy throwing spears?', 'Heavy Throwing Spear'),
 (r'thrusting spears?', 'Thrusting Spear'), (r'throwing spears?', 'Throwing Spear'), (r'javelins?', 'Javelin'),
 (r'composite bows?', 'Bow'), (r'short ?bows?', 'Short Bow'), (r'long ?bows?', 'Long Bow'), (r'light crossbows?', 'Light Crossbow'),
 (r'repeating crossbows?', 'Repeating Crossbow'), (r'crossbows?', 'Crossbow'), (r'staff slings?', 'Staff Sling'), (r'slings?', 'Sling'), (r'handguns?', 'Handgun'),
 (r'halberds?', 'Halberd'), (r'(?:double|two)[- ]?handed (?:weapons?|swords?|axes?)', 'Double-handed Weapon'), (r'lances?', 'Lance'), (r'pikes?', 'Pike'),
 (r'daggers?', 'Dagger'), (r'darts?', 'Dart'), (r'kontos', 'Kontos'), (r'bows?', 'Bow'),
 (r'lamellar armou?r', 'Lamellar Armour'), (r'cataphract armou?r', 'Cataphract Armour'), (r'full plate armou?r', 'Full Plate Armour'), (r'partial plate armou?r', 'Partial Plate Armour'), (r'heavy armou?r', 'Heavy Armour'), (r'light armou?r', 'Light Armour'),
 (r'large shields?', 'Large Shield'), (r'bucklers?', 'Buckler'), (r'shields?', 'Shield'),
]
WEAP_RE = [(re.compile(r'(?<![A-Za-z])' + p + r'(?![A-Za-z])', re.I), n) for p, n in WEAP]
def weapons_in(seg):
    out = []; s = seg
    for rx, n in WEAP_RE:
        m = rx.search(s)
        if m:
            out.append((m.start(), n)); s = rx.sub(' ' * 3, s)
    # keep textual order
    out.sort(); res = []
    for _, n in out:
        if n not in res: res.append(n)
    return res

def split_sentences(t): return [x.strip() for x in re.split(r'(?<=[.!?])\s+', t) if x.strip()]

# ------------------------------------------------------------------ headings / kinds
def is_head(t):
    t = t.strip()
    return bool(t) and t.upper() == t and re.search(r'[A-Z]', t) and len(t) <= 70 and not t.startswith('NOTE') and not t.endswith(':') and not re.match(r'^\W+$', t)
KW = [('char', r'CHARACTER|GENERAL|OFFICER|COMMANDER|HERO|WARLORD|CAPTAIN|LEADER|EMPEROR|LORD|KING|SULTAN|CALIPH|SHAH|CHIEF'),
      ('ally', r'ALLIES|ALLY|MERCENAR'),
      ('chariot', r'CHARIOT'), ('ele', r'ELEPHANT'),
      ('mach', r'MACHINE|ARTILLERY|WAGON|ENGINE|CANNON|ORDNANCE|BOMBARD|BALLISTA|CATAPULT|SIEGE|TABOR'),
      ('cav', r'CAVALRY|KNIGHT|HORSE|MOUNTED|CAMEL|LANCER|DRUZHINA|COMPANION|CHIVALRY|HUSSAR|SIPAHI|CATAPHRACT'),
      ('inf', r'INFANTRY|MISSILE|ARCHER|SKIRMISH|LIGHT (?:TROOPS|INFANTRY|SKIRM)|FOOT|SPEAR|MILITIA|LEVY|LEVIES|WARRIOR|HOPLITE|PEASANT|COMMONER|TROOP|PIKE|SLING|CROSSBOW|HANDGUN|BOWMEN|MOB|TRIBES')]
def kinds(text):
    t = text.upper(); return [k for k, rx in KW if re.search(rx, t)]
def kind_of_section(h):
    ks = kinds(h)
    for pref in ('char', 'ally', 'chariot', 'ele', 'mach', 'cav', 'inf'):
        if pref in ks: return pref
    return None
CANON = {'char': 'Characters', 'chariot': 'Chariotry', 'cav': 'Cavalry', 'inf': 'Infantry', 'ele': 'Elephants', 'mach': 'War Machines', 'ally': 'Allies and Mercenaries'}
def title(t):
    r = re.sub(r"\b([A-Za-z])([A-Za-z']*)", lambda m: m.group(1).upper() + m.group(2).lower(), clean(t).replace('&', 'and')).replace('0-1 ', '').strip()
    return re.sub(r'\b(And|Of|The|In|For|Or|At|On|To)\b', lambda m: m.group(1).lower() if m.start() else m.group(1), r)

def parse_limit(txt):
    t = txt.lower(); d = {}
    if re.search(r'\bnone\b|\bnot allowed\b|\bno\b', t) and not re.search(r'\d+\s*%', t): return {'max': 0}
    m = re.search(r'(?:up to|max(?:imum)?(?: of)?|no more than|not more than)\s*(\d+)\s*%', t)
    if m: d['max'] = int(m.group(1))
    m = re.search(r'(?:at least|min(?:imum)?(?: of)?|no less than)\s*(\d+)\s*%', t)
    if m: d['min'] = int(m.group(1))
    if not d:
        m = re.search(r'(\d+)\s*%', t)
        if m: d['max'] = int(m.group(1))
    return d

# ------------------------------------------------------------------ one army
issues = {}
def issue(a, msg): issues.setdefault(a, []).append(msg)

def pts_of(c):
    m = re.search(r'\d+', c or ''); return int(m.group(0)) if m else None
def stats_of(r):
    s = []
    for c in r[1:10]:
        c = clean(c); s.append(c if c else '-')
    s += ['-'] * (9 - len(s)); return s

VERBS = re.compile(r'\b(?:have|has|had|are|is|were|may|can|could|ride|rides|riding|fight|fights|fought|carry|carries|wear|wears|use|uses|comprise|must|should|will|replace|exchange|count|counts|form|forms|take|takes|add|get|gets|receive|cannot|do|does|not|only|upgrade|upgrades)\b', re.I)
GENERIC = {'cavalry', 'infantry', 'troops', 'troop', 'units', 'unit', 'the', 'and', 'with', 'light', 'heavy'}
def row_keys(name):
    n = re.sub(r'\([^)]*\)', ' ', re.sub(r'^0-\d+\s*', '', name)).lower().replace('\n', ' ')
    full = set(); words = set()
    for part in re.split(r'/|\bor\b', n):
        p = clean(part)
        if not p: continue
        full.add(p)
        if p.endswith('es'): full.add(p[:-2])
        if p.endswith('s'): full.add(p[:-1])
        full.add(p + 's')
        for w in re.findall(r'[a-z]{4,}', p):
            if w not in GENERIC: words.add(w); words.add(w.rstrip('s'))
    return full, words
def assign_sentences(text, rows):
    """returns (list of per-row text, list of rows that got nothing)"""
    names = [clean(r[0]) for r in rows]; keys = [row_keys(n) for n in names]
    sents = split_sentences(text); per = [[] for _ in rows]; cur = None   # cur = None (shared) or list of row indexes
    nrows = len(rows)
    for s in sents:
        m = VERBS.search(s); subj = (s[:m.start()] if m else s[:60]).lower()
        # a sentence that starts with an option word has no subject
        sel = []
        if m and m.start() > 0 and not re.match(r'(?i)^(?:may|if|up to|one|any|additional|every|at least|there may|there must|note|to represent|all|each|both|none)\b', s):
            cands = []
            for i, (full, words) in enumerate(keys):
                best = None
                for f in full:
                    if f and re.search(r'(?<![a-z])' + re.escape(f) + r'(?:e?s)?(?![a-z])', subj):
                        if best is None or len(f) > best[2]: best = (2, f, len(f))
                if best is None:
                    for w in words:
                        if re.search(r'(?<![a-z])' + re.escape(w) + r'(?:e?s)?(?![a-z])', subj):
                            if best is None or len(w) > best[2]: best = (1, w, len(w))
                if best: cands.append((best[0], best[2], best[1], i))
            cands.sort(reverse=True)
            remaining = subj; chosen = []
            for sc, ln, key, i in cands:
                mm = re.search(r'(?<![a-z])' + re.escape(key) + r'(?:e?s)?(?![a-z])', remaining)
                if mm:
                    chosen.append((sc, i)); remaining = remaining[:mm.start()] + ' ' * (mm.end() - mm.start()) + remaining[mm.end():]
            if chosen:
                multi = bool(re.search(r'\band\b|,|/', subj))
                top = max(sc for sc, i in chosen)
                cur = sorted(i for sc, i in chosen if multi or sc == top)
        elif re.match(r'(?i)^(?:all|each|both)\b', s): cur = None
        targets = range(nrows) if cur is None else cur
        for i in targets: per[i].append(s)
    return [' '.join(p) for p in per], [i for i, p in enumerate(per) if not p]

LABEL_SPLIT = re.compile(r'(?i)\.|;|,|\bbe (?:exchanged|replaced|swapped|upgraded)\b(?: for| with| to)?|\bfielded\b|\balternatively\b|\binstead of\b|\bfor\b|\bby\b|\bmay\b|\bhave\b|\bhas\b|\btake\b|\bbe given\b|\bupgrade (?:\w+ )?to\b|\bexchange\b.*?\bfor\b|\breplace\b.*?\bwith\b|\bswap\b.*?\bfor\b|\bor\b|\band\b|\bcan\b|\bin which case\b|\bwith\b|\badd\b|\bbuy\b|\bgain\b|\bchoose\b|\bonly\b|\bup to\b|\bis\b|\bthey\b|\bunits?\b')
COST_RE = re.compile(r'\(\s*(?:([+\-–−])\s*)?(\d+)\s*(?:pts?|points?)?\s*(?:each|per model|per figure)?\s*\)|\(\s*free\s*\)|\bfree\b|\bat no (?:extra )?(?:cost|points)\b', re.I)
def label_clean(s):
    s = clean(s)
    s = re.sub(r'(?i)^(?:a|an|the|their|his|its|one|any|additional|extra|them|up to \w+)\s+', '', s)
    s = re.sub(r'(?i)^be\s+', '', s)
    s = re.sub(r'(?i)\s+(?:for|at|a cost of|costing|cost|to|of)$', '', s)
    s = re.sub(r'[\s(\[\-,:]+$', '', s).strip(' -,:')
    if len(s) > 45: s = ' '.join(s.split()[:5])
    return s
def parse_options(text, base_weapons):
    """options = every cost-bearing phrase after the first 'may' in the chunk"""
    opts = []; seen = set()
    sents = split_sentences(text)
    rest = ' '.join(sents) if sents else text
    m0 = re.search(r'\b[Mm]ay\b|\b[Ee]xchange\b|\bupgrade\b', rest)
    start = m0.start() if m0 else len(rest)
    seg = rest[start:]
    last = 0
    for m in COST_RE.finditer(seg):
        before = seg[last:m.start()]
        parts = LABEL_SPLIT.split(before)
        lab = label_clean(parts[-1]) if parts else ''
        if not lab and len(parts) > 1: lab = label_clean(parts[-2])
        last = m.end()
        if m.group(0).lower().startswith('(free') or m.group(0).lower() in ('free',) or 'no ' in m.group(0).lower(): cost = 0
        else: cost = (-1 if m.group(1) in ('-', '–', '−') else 1) * int(m.group(2))
        if not lab or len(lab) < 3: continue
        low = lab.lower()
        if re.search(r'\bwar ?horse', low) and 'barding' not in low: lab = 'Ride a warhorse'
        elif re.search(r'\bhorses?\b', low) and not re.search(r'barding|dismount|armour|warhorse', low): lab = 'Ride a horse'
        else: lab = lab[0].upper() + lab[1:]
        lab = lab.replace('"', "'")
        if lab.lower() in seen: continue
        seen.add(lab.lower()); opts.append((lab, cost))
    return opts

def parse_chunk(text, row_name, kind, issues_key):
    # base segment: up to the first sentence that starts an option list
    low = text
    m0 = re.search(r'\b[Mm]ay\b|\b[Ee]xchange\b|\bupgrade\b|\bIf\b', low)
    base = low[:m0.start()] if m0 else low
    base_w = weapons_in(base)
    alt = []
    m = re.search(r'either ([^.]*)', base, re.I)
    if m:
        ws = weapons_in(m.group(1))
        if len(ws) > 1:
            for w in ws[1:]:
                if w in base_w: base_w.remove(w)
            alt = [(f'{w} (instead of {ws[0]})', 0) for w in ws[1:]]
    if 'Hand Weapon' not in base_w and 'Improvised Weapon' not in base_w: base_w.insert(0, 'Hand Weapon')
    opts = parse_options(text, base_w)
    opts = alt + [o for o in opts if o[0] not in [a[0] for a in alt]]
    rules = []
    for s in split_sentences(text):
        if re.match(r'(?i)^(?:may|if|they may|he may|it may|each may|up to|any)\b', s):
            if 'Army General' in s and 'Army General' not in rules and not re.search(r'(?i)(?:become|be) (?:the )?army general', s): rules.append('Army General')
            continue
        if re.search(r'(?i)\b(?:if|when|unless|while|those|only)\b|\bwith [a-z ]+ (?:are|is|have|may)\b', s): continue
        for t, rx in TERM_RE:
            if rx.search(s):
                r = RULE_TERMS[t]
                if r and r not in rules: rules.append(r)
    if re.search(r'Army Standard Bearer', text) and 'Army Standard' not in rules: rules.append('Army Standard')
    return base_w, opts, rules

NOSTD = {}
UNIT_HEADS = re.compile(r'^(?:0-\d\s*)?(?:CHARACTERS?|GENERALS?|SENIOR OFFICERS|COMMANDERS?)\b')
def is_unit_head(t): return bool(UNIT_HEADS.match(t.upper().replace('0-1GENERAL','0-1 GENERAL')))
def build_army(idx, a):
    NOSTD['v'] = False
    key = f'A{idx:03d}'; atitle = title(a['title']); bl = a['blocks']
    # ---- composition
    n = len(bl); intro = []; comps = []; cur = None
    LABEL = re.compile(r'^[A-Za-z][^:]{1,59}:\s*\S')
    ps = [(k, clean(x['text'])) for k, x in enumerate(bl) if x['t'] == 'p' and clean(x['text'])]
    start = None
    for k, t in ps:
        if t.upper().startswith('ARMY COMPOSITION'): start = k + 1; break
    if start is None:
        for j, (k, t) in enumerate(ps):
            if re.match(r'(?i)^characters:', t):
                start = ps[j - 1][0] if j > 0 and ':' not in ps[j - 1][1] and len(ps[j - 1][1]) < 60 else k
                break
    if start is None: start = n; issue(a['title'], 'no composition found')
    for k, t in ps:
        if k < start - (1 if bl[start - 1:start] and bl[start - 1]['t'] == 'p' and clean(bl[start - 1]['text']).upper().startswith('ARMY COMP') else 0) and not t.upper().startswith('ARMY COMPOSITION'): intro.append(t)
    i = start
    def next_text(k):
        seen = 0
        for q in range(k + 1, n):
            if bl[q]['t'] == 'tbl': return None
            tt = clean(bl[q]['text'])
            if not tt: continue
            if LABEL.match(tt): return tt
            seen += 1
            if seen >= 3 or is_head(tt): return tt if seen == 1 else None
        return None
    while i < n:
        b = bl[i]
        if b['t'] == 'tbl': break
        t = clean(b['text'])
        if not t: i += 1; continue
        nt = next_text(i)
        if ':' not in t[:60] and len(t) < 50 and not t.endswith('.') and len(t.split()) <= 8 and not re.search(r'(?i)\b(?:may|are|is|must|have)\b', t) and nt and LABEL.match(nt) and not is_unit_head(t):
            cur = {'name': title(t) if t.upper() == t else t, 'lines': []}; comps.append(cur); i += 1; continue
        if is_head(t) and not (nt and LABEL.match(nt)) :
            break
        if cur is None: cur = {'name': atitle, 'lines': []}; comps.append(cur)
        cur['lines'].append(t); i += 1
    if not comps: comps = [{'name': atitle, 'lines': []}]; issue(a['title'], 'no ARMY COMPOSITION lines found')
    # ---- sections
    secs = []   # (heading, subheading, in_allies, table rows..., texts)
    heading = ''; sub = ''; in_allies = False; units_raw = []; pend_max1 = False
    cur_tbl = None
    while i < n:
        b = bl[i]; i += 1
        if b['t'] == 'p':
            t = clean(b['text'])
            if not t or t == '.': continue
            if is_head(t):
                if cur_tbl: units_raw.append(cur_tbl); cur_tbl = None
                if kind_of_section(t) == 'ally' or (re.search(r'ALLIES|MERCENAR', t)): in_allies = True; heading = t; sub = ''
                elif re.match(r'^0-\d', t) or (kind_of_section(t) == 'char' and heading and kind_of_section(heading) == 'char'):
                    sub = t
                    if not heading: heading = t
                elif in_allies: sub = t
                else: heading = t; sub = ''
                pend_max1 = bool(re.match(r'^0-1\s*GENERAL', t.upper().replace(' ', '')) or re.match(r'^0-1\s*GENERAL', t.upper()))
                continue
            t2 = re.sub(r'\s{2,}', '. ', re.sub(r'(?<=[.!?])\s{2,}', ' ', b['text'].replace('\u00a0', ' ').strip()))
            t2 = re.sub(r'\s+', ' ', t2.replace('. .', '.'))
            if cur_tbl is not None: cur_tbl['text'].append(t2)
            else: units_raw.append({'heading': heading, 'sub': sub, 'allies': in_allies, 'rows': [], 'text': [t], 'orphan': True})
        else:
            if cur_tbl: units_raw.append(cur_tbl)
            cur_tbl = {'heading': heading, 'sub': sub, 'allies': in_allies, 'rows': b['rows'][1:], 'text': [], 'max1': pend_max1}
            pend_max1 = False
    if cur_tbl: units_raw.append(cur_tbl)
    # attach orphan texts (e.g. text following a heading with no table) to the army notes
    army_notes = []; tables = []
    for u in units_raw:
        if u.get('orphan'): army_notes.append(f"{u['heading'].title()}: " + ' '.join(u['text']))
        else: tables.append(u)
    # ---- category mapping from composition labels
    labels = []
    for c in comps:
        for ln in c['lines']:
            m = re.match(r'^([^:]{2,60}):\s*(.*)$', ln)
            if m and not ln.lower().startswith('note'): labels.append(m.group(1).strip())
    def wset(t): return {w.rstrip('s') for w in re.findall(r'[a-z]{4,}', t.lower())} - {'troop', 'unit', 'army'}
    custom = [lb for lb in dict.fromkeys(labels) if not kinds(lb)]
    def cat_for(h, is_ally):
        for lb in custom:
            if wset(lb) & wset(h): return title(lb)
        k = 'ally' if is_ally else kind_of_section(h)
        if k is None: return title(h) or 'Other Troops'
        cands = [lb for lb in dict.fromkeys(labels) if k in kinds(lb)]
        if cands:
            best = max(cands, key=lambda lb: len(wset(lb) & wset(h)))
            return title(best)
        return CANON[k]
    comp_out = {}
    for c in comps:
        lim = {}; txt = []
        for ln in c['lines']:
            m = re.match(r'^([^:]{2,60}):\s*(.*)$', ln)
            if not m or ln.lower().startswith('note'): txt.append(ln); continue
            lab, rest = m.group(1).strip(), m.group(2)
            ks = kinds(lab)
            kk = kind_of_section(lab) if ks else None
            if kk is None:
                d = parse_limit(rest)
                if d and not ks: lim.setdefault(title(lab), {}).update(d)
                else: issue(a['title'], f'composition line not mapped: {ln[:80]}')
                txt.append(ln); continue
            cat = cat_for(lab, kk == 'ally')
            d = parse_limit(rest)
            if d:
                if cat in lim and 'max' in lim[cat] and lim[cat]['max'] == 0 and 'max' in d: pass
                lim.setdefault(cat, {}).update({k: v for k, v in d.items() if not (k == 'max' and lim.get(cat, {}).get('max', 0) > v and v == 0)})
            txt.append(ln)
        comp_out[c['name']] = (lim, ' '.join(txt))
    # ---- units
    units = []; used = {}
    for tb in tables:
        rows = [r + [''] * (11 - len(r)) for r in tb['rows'] if any(clean(c) for c in r)]
        if not rows: continue
        text = ' '.join(tb['text'])
        # group rows into units
        groups = []
        for r in rows:
            if pts_of(r[10]) is not None or not groups: groups.append([r])
            else: groups[-1].append(r)
        # chunk assignment on the main rows
        mains = [g[0] for g in groups]
        per_texts, missing = assign_sentences(text, mains)
        if missing: issue(a['title'], f"no description for {[clean(mains[i][0]) for i in missing]} in table [{tb['heading']}]")
        for gi, g in enumerate(groups):
            r = g[0]; raw = clean(r[0]); mx = None
            m = re.match(r'^0-(\d+)\s*(?:units?\s+)?(.*)$', raw)
            if m: mx = int(m.group(1)); raw = m.group(2)
            if not raw: raw = tb['sub'] or tb['heading']
            if tb.get('max1') and mx is None: mx = 1
            chunk = per_texts[gi] or ''
            k = 'ally' if tb['allies'] else kind_of_section(tb['heading'])
            ksub = kind_of_section(tb['sub']) if tb['sub'] else None
            cat = cat_for(tb['heading'] or tb['sub'], tb['allies'])
            nm = title(raw) if raw.upper() == raw else raw
            nm = nm.replace('"', "'")
            if tb['allies'] and tb['sub'] and not re.match(r'^0-\d', tb['sub']): nm = f"{title(tb['sub'])} - {nm}"
            if nm in used: used[nm] += 1; nm = f"{nm} ({title(tb['heading'])})" if f"{nm} ({title(tb['heading'])})" not in used else f'{nm} {used[nm]}'
            used[nm] = 1
            st = stats_of(r); pts = pts_of(r[10])
            ismach = st[0] == '-' and st[1] == '-'
            ischar = (k == 'char') or (ksub == 'char' and not tb['allies'])
            isch = 'chariot' in raw.lower() and not ischar
            isele = raw.lower().startswith('elephant') or k == 'ele'
            base_w, opts, rules = parse_chunk(chunk, nm, k, a['title'])
            if tb['allies'] and 'Allies and Mercenaries (Unreliable)' not in rules: rules.append('Allies and Mercenaries (Unreliable)')
            vehicle = ismach or isch or isele
            if ischar or vehicle: mn = 1
            else: mn = 5
            if ismach:
                st = ['-', '-', '-', '-', st[4], st[5], '-', '-', '-']
                base_w = []; mach_opts = [o for o in opts if re.search(r'armour|shield', o[0].lower()) and 'additional' not in o[0].lower()]; opts = []
            models = []; mach_opts = []
            if vehicle and not ismach and not isele and not isch: pass
            musters = not (NOSTD.get('v') or ischar or vehicle or 'Skirmishers (Art of War)' in rules or re.search(r'(?i)not have a standard|no standard|may not (?:take|have) (?:a )?(?:standard|musician|unit standard)|may not have a (?:standard|musician)', chunk))
            if ischar: lst_ups = []
            else: lst_ups = [('Standard bearer', 5), ('Musician', 5), ('Leader', 5)] if musters else []
            kkey = 'machine' if ismach else ('el' if isele else None)
            if ismach: base_w = []
            models.append(dict(name=nm, stats=' '.join(st), pts=pts or 0, mn=mn, mx=(1 if (vehicle or ischar) else None), weapons=base_w, rules=rules, options=opts + lst_ups, key=kkey))
            if pts is None: issue(a['title'], f'no points value for {nm}')
            for si, sup in enumerate(g[1:]):
                sn = clean(sup[0]) or 'Crew'; ss = stats_of(sup)
                lowsn = sn.lower()
                cnt = None
                mm = re.search(r'(?i)\b(one|two|three|four|five|six|seven|eight|\d+)\s+(?:\w+\s+){0,2}' + re.escape(lowsn.split()[-1]) + r'(?:s|men|man)?\b', chunk)
                if mm: cnt = NUMW.get(mm.group(1).lower()) or (int(mm.group(1)) if mm.group(1).isdigit() else None)
                if cnt is None: cnt = 1 if re.search(r'mahout|driver|rider|master', lowsn) else 2
                sw = weapons_in(chunk) if False else ['Hand Weapon']
                sopt = []
                models.append(dict(name=sn.replace('"', "'"), stats=' '.join(ss), pts=0, mn=cnt, mx=cnt, weapons=sw, rules=[], options=(mach_opts if (ismach and si == 0) else []), key=('crew' if si == 0 else f'crew{si+1}')))
            units.append(dict(cat=cat, name=nm, models=models, notes=(chunk or text)[:1500], mx=(mx if mx else (1 if (ischar and tb.get('max1')) else None)), page=None))
            if ischar and 'Army General' in rules and mx is None: units[-1]['mx'] = None
    # ---- cat flags: generals 0-1
    for u in units:
        if 'Army General' in u['models'][0]['rules'] or 'Army Standard' in u['models'][0]['rules']:
            if u['mx'] is None and u['cat'] == 'Characters': u['mx'] = 1
    ucats = {u['cat'] for u in units}
    for cn, (lim, txt) in comp_out.items():
        for ck in list(lim):
            if ck not in ucats:
                issue(a['title'], f'composition limit for {ck} dropped (no units in that category): {lim[ck]}'); del lim[ck]
    return key, atitle, units, comp_out, army_notes, intro

# ------------------------------------------------------------------ run
out = ['# Armies of Antiquity v2 (unofficial, Martin Gibbins) - GENERATED by tools/aoa2_gen.py, then hand-corrected where noted.',
       '# Model stats order: M WS BS S T W I A Ld',
       'import copy', 'from rb_data import M, U', 'LISTS = []; VAR = {}; AVAIL = []; UNAV = []; OPTAV = []; OPTRULE = []; OPTSTAT = []; RATIOS = []; OPT_ONCE = []; PAIRS = []',
       'SECOND = {}; UNIT_MAX_IN = []; GEN = {}; COND_CHARS = []; COSTV = []; STATV = []; EXCL = []', 'FLAT = []; PTSLIM = []; MODLIM = []; HIRDMEN_LE_BONDIR = []',
       "PUB = 'Armies of Antiquity v2'", '',
       'def variants(key, title, comps):', '    VAR[key] = {}; out = []', '    for c, (lim, txt) in comps.items():',
       "        VAR[key][c] = f'{PUB}: {title}' if len(comps) == 1 else f'{PUB}: {title} - {c}'", '        out.append((VAR[key][c], lim, txt))', '    return out', '']
rules_seen = {}
FILE_TITLE = {'Medieval Spanish and Portugese': 'Medieval Spanish'}
for idx, a in enumerate(ex['armies'], 1):
    try:
        key, atitle, units, comps, anotes, intro = build_army(idx, a)
    except Exception as e:
        print('FAILED', a['title'], repr(e)); raise
    fn = re.sub(r'[^A-Za-z0-9]+', '_', FILE_TITLE.get(atitle, atitle)).strip('_') + '_AoA2.cat'
    out.append(f'# ====================================================================== {idx}. {a["title"]} {a.get("dates","")}')
    out.append(f'U_{key} = []')
    for u in units:
        ms = []
        for m in u['models']:
            kw = f"weapons={m['weapons']!r}, rules={m['rules']!r}, options={m['options']!r}"
            if m['mx'] is not None: kw = f"mx={m['mx']}, " + kw
            if m['key']: kw += f", key={m['key']!r}"
            ms.append(f"M({m['name']!r}, {m['stats']!r}, {m['pts']}, mn={m['mn']}, {kw})")
        for r in u['models'][0]['rules']: rules_seen[r] = rules_seen.get(r, 0) + 1
        out.append(f"U_{key}.append(U({u['cat']!r}, {u['name']!r}, [{', '.join(ms)}],\n    {u['notes']!r}, mx={u['mx']!r}))")
    cdict = {n: (lim, txt) for n, (lim, txt) in comps.items()}
    out.append(f'{key}V = variants({key!r}, {atitle!r}, {pprint.pformat(cdict, width=200)})')
    intro_t = ' '.join(intro)[:900]
    out.append(f"LISTS.append(({key!r}, {atitle + ' (AoA2)'!r}, {fn!r}, U_{key}, {key}V,\n    {('ARMIES OF ANTIQUITY v2 #' + str(idx) + ' (unofficial, Martin Gibbins). ' + intro_t + ' ' + ' '.join(anotes))[:1800]!r}))")
    out.append('')
open(os.path.join(HERE, 'aoa2_data.py'), 'w', encoding='utf8').write('\n'.join(out) + '\n')
json.dump(NEWRULES, open('/tmp/aoa2/newrules.json', 'w'), indent=1)
os.makedirs(os.path.join(ROOT, 'issues'), exist_ok=True)
json.dump(issues, open('/tmp/aoa2/gen_issues.json', 'w'), indent=1)
print(len(ex['armies']), 'armies; units:', sum(1 for l in open(os.path.join(HERE, 'aoa2_data.py')) if '.append(U(' in l), '; new rules:', list(NEWRULES))
print('issues:', sum(len(v) for v in issues.values()), 'in', len(issues), 'armies')
