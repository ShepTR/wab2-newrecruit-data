#!/usr/bin/env python3
"""Build a BattleScribe/New Recruit data set for Warhammer Ancient Battles 2.0
from the AoA2 .docx (army lists) + the 2.0 rulebook reference data (wab_data.py)."""
import sys, os, re, hashlib
from xml.sax.saxutils import escape, quoteattr
import docx
from docx.table import Table
from docx.text.paragraph import Paragraph
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import wab_data as D

DOCX = sys.argv[1]
OUT = sys.argv[2]
PILOT = [a.upper() for a in sys.argv[3:]] or ['EARLY IMPERIAL ROMAN','GALLIC','PARTHIAN','MEDIEVAL ENGLISH']

GS_NAME = "Warhammer Ancient Battles 2.0"
AUTHOR = "WAB2 New Recruit pilot"
STATS = ['M','WS','BS','S','T','W','I','A','Ld']

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i+4] for i in range(0,16,4))
def q(s): return quoteattr(str(s))
def t(s): return escape(str(s))
GS_ID = hid('gamesystem', GS_NAME)
PUB_RB = hid('pub','rulebook'); PUB_AOA = hid('pub','aoa2')

# ---------------------------------------------------------------- docx parsing
def load_items(path):
    d = docx.Document(path)
    items = []
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            p = Paragraph(el, d); txt = p.text.strip()
            if txt: items.append(('p', re.sub(r'\s+',' ',txt), p.style.name if p.style is not None else ''))
        elif tag == 'tbl':
            tb = Table(el, d)
            rows = [[re.sub(r'\s+',' ',c.text).strip() for c in r.cells] for r in tb.rows]
            items.append(('t', rows, ''))
    return items

def clean_title(n):
    n = n.replace('&amp;','&')
    small = {'and','of','at','the','de'}
    words = n.lower().split()
    return ' '.join(w if (i and w in small) else w.capitalize() for i,w in enumerate(words))

def norm_cat(n):
    n = n.replace('&amp;','&').replace('&','and').strip().lower()
    n = re.sub(r'\s+',' ',n)
    if n in ('allies','allies and mercenaries','allies and mercenary'): return 'Allies and Mercenaries'
    if n in ('characters','character','general','generals','senior officers'): return 'Characters'
    return clean_title(n)

DATE_RE = re.compile(r'(BC|AD)|^\d{3,4}\s*(AD)?\s*-\s*\d{3,4}', re.I)
def is_upper_heading(s):
    letters = re.sub(r'[^A-Za-z]','',s)
    return len(letters) >= 4 and s == s.upper() and re.match(r'^[A-Z0-9][A-Z0-9 &;\-/’\']+$', s.replace('&amp;','&')) is not None

def parse_armies(items):
    start = [i for i,(k,v,s) in enumerate(items) if k=='p' and v=='ARMY LISTS' and s.startswith('Heading')][0]
    armies = []
    heads = []
    for j in range(start+1, len(items)):
        k,v,s = items[j]
        m = re.match(r'^(\d{1,3})\.\s+([A-Z][A-Z &;’\'\-]+?)\s*$', v) if k=='p' else None
        if m and j+1 < len(items) and items[j+1][0]=='p' and DATE_RE.search(items[j+1][1]) and len(items[j+1][1])<60:
            heads.append(j)
    heads.append(len(items))
    for a,b in zip(heads, heads[1:]):
        armies.append(parse_army(items[a:b]))
    return armies

def parse_army(block):
    m = re.match(r'^(\d{1,3})\.\s+(.+)$', block[0][1])
    army = dict(num=int(m.group(1)), key=m.group(2).replace('&amp;','&').strip(), name=clean_title(m.group(2)),
                dates=block[1][1], intro=[], comp_raw=[], variants=[], sections=[], other=[])
    state = 'intro'; sec = None; pending = []; last_table = None
    for k,v,s in block[2:]:
        if k=='p' and v == 'ARMY COMPOSITION':
            state = 'comp'; continue
        if k=='p' and is_upper_heading(v):
            state = 'sec'
            title = v.replace('&amp;','&')
            restr = None
            mm = re.match(r'^0-(\d+)\s+(.*)$', title)
            if mm: restr = int(mm.group(1)); title = mm.group(2)
            sec = dict(title=title, restr=restr, tables=[], free=[])
            army['sections'].append(sec); pending = []; last_table = None
            continue
        if state == 'intro':
            army['intro'].append(v if k=='p' else ' | '.join(v[0]))
        elif state == 'comp':
            if k=='p': army['comp_raw'].append(v)
        elif state == 'sec':
            if k=='t':
                rows = v
                if not rows or len(rows[0]) < 4 or [c.strip().upper() for c in rows[0][1:4]] != ['M','WS','BS']:
                    army['other'].append(rows); continue
                tb = dict(rows=[], pre=pending, post=[]); pending = []
                for r in rows[1:]:
                    nm = r[0].strip()
                    if not nm: continue
                    tb['rows'].append(dict(name=nm, stats=r[1:10], pts=(r[10] if len(r)>10 else '')))
                sec['tables'].append(tb); last_table = tb
            else:
                if last_table is not None: last_table['post'].append(v)
                else: pending.append(v); sec['free'].append(v)
    variants = []; curv = dict(name=None, limits={}, notes=[])
    for line in army['comp_raw']:
        if ':' not in line:
            if curv['limits'] or curv['notes'] or curv['name']: variants.append(curv)
            curv = dict(name=line, limits={}, notes=[]); continue
        lab, rest = line.split(':',1)
        if lab.strip().lower() == 'note':
            curv['notes'].append(line); continue
        cat = norm_cat(lab)
        mm = re.search(r'(up to|at least|no more than|a maximum of|maximum of)\s*(\d+)\s*%', rest, re.I)
        if mm:
            kind = 'min' if mm.group(1).lower()=='at least' else 'max'
            curv['limits'][cat] = (kind, int(mm.group(2)))
            extra = rest[mm.end():].strip(' :.')
            if extra: curv['notes'].append(f'{lab.strip()}: {extra}')
        elif re.search(r'\bnone\b', rest, re.I):
            curv['limits'][cat] = ('max', 0)
        else:
            curv['limits'].setdefault(cat, None)
            curv['notes'].append(line.strip())
    if curv['limits'] or curv['notes'] or curv['name']: variants.append(curv)
    army['variants'] = variants or [dict(name=None, limits={}, notes=[])]
    return army

def parse_extra_rules(items):
    a = [i for i,(k,v,s) in enumerate(items) if k=='p' and v=='CREATING ARMIES' and s.startswith('Heading')][0]
    b = [i for i,(k,v,s) in enumerate(items) if k=='p' and v=='ARMY LISTS' and s.startswith('Heading')][0]
    rules = {}; name = None; buf = []
    def flush():
        if name and buf: rules[name] = '\n\n'.join(buf)
    for k,v,s in items[a+1:b]:
        if k=='p' and re.match(r'^Heading ?1$', s):
            flush(); name = re.sub(r'\s*\((?:p\.?|page)\s*\d+\)','',v).strip(); buf = []
        elif name:
            if k=='p': buf.append(v)
            else: buf.append('\n'.join(' | '.join(c for c in r) for r in v))
    flush()
    return rules

# ---------------------------------------------------------------- text analysis
WEAPON_PATTERNS = [
 ('Heavy Throwing Spear', r'heavy throwing spears?'), ('Throwing Spear', r'(?<!heavy )throwing spears?'),
 ('Thrusting Spear', r'thrusting spears?'), ('Hand Weapon', r'hand weapons?'), ('Dagger', r'\bdaggers?\b'),
 ('Improvised Weapon', r'improvised weapons?'), ('Double-handed Weapon', r'double[- ]handed weapons?'),
 ('Halberd', r'\bhalberds?\b'), ('Pike', r'\bpikes?\b'), ('Kontos', r'\bkontos\b'), ('Lance', r'\blances?\b'),
 ('Staff Sling', r'staff slings?'), ('Sling', r'(?<!staff )\bslings?\b'), ('Javelin', r'\bjavelins?\b'),
 ('Dart', r'\bdarts?\b'), ('Short Bow', r'short bows?'), ('Long Bow', r'long ?bows?'),
 ('Light Crossbow', r'light crossbows?'), ('Crossbow', r'(?<!light )crossbows?'), ('Handgun', r'\bhandguns?\b'),
 ('Bow', r'(?<!short )(?<!long )\bbows?\b'),
 ('Light Armour', r'light armour'), ('Heavy Armour', r'heavy armour'), ('Cataphract Armour', r'cataphract armour'),
 ('Partial Plate Armour', r'partial plate'), ('Full Plate Armour', r'full plate'),
 ('Large Shield', r'large shields?'), ('Buckler', r'\bbucklers?\b'), ('Pavise', r'\bpavise\b'),
 ('Shield', r'(?<!large )\bshields?\b'),
]
def detect_weapons(sentence):
    s = sentence.lower()
    s = re.sub(r'(throwing or thrusting|thrusting or throwing) spears?', 'throwing spear thrusting spear', s)
    found = []
    for name, pat in WEAPON_PATTERNS:
        if re.search(pat, s) and name not in found: found.append(name)
    return found

def singular(w):
    w = w.lower()
    return w[:-1] if w.endswith('s') and not w.endswith('ss') else w

def row_phrases(name):
    n = re.sub(r'^0-\d+\s+','',name).lower()
    out = []
    for part in re.split(r'\s+or\s+|/', n):
        part = ' '.join(singular(w) for w in part.split())
        if part: out.append(part)
    toks = [singular(w) for w in re.findall(r'[a-z]+', n) if len(w) >= 6]
    if ' of ' in n: toks.append(n.split()[0])
    return out, toks

def split_sentences(par):
    return [s.strip() for s in re.split(r'(?<=[.;])\s+(?=[A-Z(])', par) if s.strip()]

def named_rows(sentence, rows_ph):
    head = sentence.lower()[:48]
    head_s = ' '.join(singular(w) for w in head.split())
    hit = []
    # bare fragments such as "Army General." or "Light Cavalry." are labels, not subjects
    if not re.search(r'\b(?:have|has|are|is|as|may|can|must|should)\b', sentence.lower()[:70]): return []
    for idx,(ph,tk) in enumerate(rows_ph):
        if any(p in head_s for p in ph): hit.append(idx)
    # token fallback only when the sentence is "<subject> have/has/as ..." (not a bare fragment such as "Light Cavalry.")
    if re.match(r"^(?:the |a |an )?[\w\s/&',-]{2,45}?\b(?:have|has|as)\b", sentence.lower()):
        for idx,(ph,tk) in enumerate(rows_ph):
            if idx not in hit and any(re.search(r'\b'+re.escape(x)+r'\b', head_s) for x in tk): hit.append(idx)
    if len(hit) > 1:   # longest phrase wins
        longest = {i: (max(rows_ph[i][0], key=len) if rows_ph[i][0] else '') for i in hit}
        keep = [i for i in hit if not any(j != i and longest[i] and longest[i] != longest[j] and longest[i] in longest[j] for j in hit)]
        hit = keep or hit
    return hit

COST_GROUP = re.compile(r'\(([^()]*)\)')
def extract_options(sentence):
    """Return list of (label, cost) from '(+N)', '(-N)', '(free)' groups in one sentence."""
    out = []; prev = 0
    for m in COST_GROUP.finditer(sentence):
        inner = m.group(1)
        cm = re.search(r'(?<![\w])([+-]\d+)(?!\d)(?:\s*each)?|(?<![\w])(free)(?![\w])', inner, re.I)
        if not cm: continue
        cost = 0 if cm.group(2) else int(cm.group(1))
        extra = (inner[:cm.start()] + inner[cm.end():]).strip(' ,;')
        raw = sentence[prev:m.start()].strip()
        prev = m.end()
        mays = list(re.finditer(r'\b(?:may|can)\s+', raw, flags=re.I))
        if mays: raw = raw[mays[-1].end():]
        label = re.sub(r'^(?:[,;]\s*|(?:and|or|they|he|may|can|also|only|have|be|then|a|an|the)\s+)+', '', raw, flags=re.I).strip(' ,;')
        label = re.sub(r'\s+',' ',label)
        if not label or re.search(r'purchased|additional crew|extra crew', label, re.I): continue
        label = label[0].upper() + label[1:]
        if extra: label += f' ({extra})'
        out.append((label[:90], cost))
    return out

# ---------------------------------------------------------------- XML builders
def profile_xml(pid, name, type_id, type_name, chars, pub=None, page=None, indent='        '):
    pa = (f' publicationId="{pub}"' if pub else '') + (f' page={q(page)}' if page else '')
    s = f'{indent}<profile id="{pid}" name={q(name)}{pa} hidden="false" typeId="{type_id}" typeName={q(type_name)}>\n{indent}  <characteristics>\n'
    for cname, cval in chars:
        s += f'{indent}    <characteristic name={q(cname)} typeId="{hid("ctype",type_name,cname)}">{t(cval)}</characteristic>\n'
    s += f'{indent}  </characteristics>\n{indent}</profile>\n'
    return s

PT_CHARS = {
 'Model': STATS, 'Missile Weapon': ['Range','Strength','Save Modifier','Notes'], 'Hand-to-Hand Weapon': ['Effects'],
 'Armour': ['Infantry Save','Cavalry Save','Notes'], 'Shield or Barding': ['Bonus','Note'], 'Equipment and Notes': ['Text'],
}
PT = {n: hid('ptype', n) for n in PT_CHARS}

def constraint(field, scope, value, ctype, cid, pct=False, shared=False, inc_child=False):
    return (f'<constraint field="{field}" scope="{scope}" value="{value}" percentValue="{"true" if pct else "false"}" '
            f'shared="{"true" if shared else "false"}" includeChildSelections="{"true" if inc_child else "false"}" '
            f'includeChildForces="false" id="{cid}" type="{ctype}"/>')

# ---------------------------------------------------------------- main build
CAT_HEADS = {'infantry','cavalry','skirmishers','artillery','archers','men at arms','cavalry and chariots','allies','allies and mercenaries',
             'special troops','war machines','chariots','elephants','characters','general','generals','senior officers'}

def main():
    items = load_items(DOCX)
    armies_all = parse_armies(items)
    by_key = {a['key']: a for a in armies_all}
    missing = [p for p in PILOT if p not in by_key]
    if missing: sys.exit(f'Armies not found: {missing}')
    armies = [by_key[p] for p in PILOT]
    extra_rules = parse_extra_rules(items)

    rules = {}
    for n,(pg,tx) in D.RULES.items(): rules[n] = dict(page=pg, text=tx, pub=PUB_RB, detect=(n != 'Chariots'))
    for n,tx in extra_rules.items():
        amend = n in ('Bow','Characters')
        nm = f'{n} (AoA2 amendment)' if amend else n
        rules[nm] = dict(page=None, text=tx, pub=PUB_AOA, detect=not amend)
    rule_detect = {n.lower(): n for n,r in rules.items() if r['detect']}
    for a_,c_ in D.ALIASES.items(): rule_detect[a_.lower()] = c_
    rule_detect['unreliable'] = 'Allies and Mercenaries (Unreliable)'
    names_sorted = sorted(rule_detect, key=len, reverse=True)
    def detect_rules(sentence):
        s = sentence.lower(); found = []
        for ln in names_sorted:
            if re.search(r'(?<![\w-])'+re.escape(ln)+r'(?![\w])', s):
                c = rule_detect[ln]
                if c in rules and c not in found: found.append(c)
        return found

    cats = {}
    def cat(name):
        if name not in cats: cats[name] = hid('cat', name)
        return cats[name]

    sp = []; prof_ids = {}
    for (n,rng,st,sm,nt) in D.MISSILE:
        prof_ids[n] = hid('prof',n)
        sp.append(profile_xml(prof_ids[n], n, PT['Missile Weapon'], 'Missile Weapon', [('Range',rng),('Strength',st),('Save Modifier',sm),('Notes',nt)], PUB_RB, D.MISSILE_PAGE, '    '))
    for (n,fx) in D.HAND:
        prof_ids[n] = hid('prof',n)
        sp.append(profile_xml(prof_ids[n], n, PT['Hand-to-Hand Weapon'], 'Hand-to-Hand Weapon', [('Effects',fx)], PUB_RB, D.HAND_PAGE, '    '))
    for (n,inf,cav) in D.ARMOUR:
        prof_ids[n] = hid('prof',n)
        sp.append(profile_xml(prof_ids[n], n, PT['Armour'], 'Armour', [('Infantry Save',inf),('Cavalry Save',cav),('Notes',D.ARMOUR_NOTE)], PUB_RB, D.ARMOUR_PAGE, '    '))
    for (n,b,nt) in D.SHIELDS:
        prof_ids[n] = hid('prof',n)
        sp.append(profile_xml(prof_ids[n], n, PT['Shield or Barding'], 'Shield or Barding', [('Bonus',b),('Note',nt)], PUB_RB, D.ARMOUR_PAGE, '    '))

    forces = []; cat_files = {}; report = []
    for a in armies:
        cat_files[a['name']] = build_catalogue(a, cat, detect_rules, prof_ids, forces, report)

    g = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n',
         f'<gameSystem id="{GS_ID}" name={q(GS_NAME)} revision="1" battleScribeVersion="2.03" authorName={q(AUTHOR)} '
         f'xmlns="http://www.battlescribe.net/schema/gameSystemSchema" type="gameSystem" library="true">\n',
         '  <readme>Pilot data set: Warhammer Ancient Battles 2nd Edition, built from the 2.0 rulebook reference pages and Armies of Antiquity v2.0.</readme>\n  <publications>\n',
         f'    <publication id="{PUB_RB}" name="Warhammer Ancient Battles 2nd Edition" shortName="WAB2" publisher="Warhammer Historical Wargames" publicationDate="2010"/>\n',
         f'    <publication id="{PUB_AOA}" name="Armies of Antiquity v2.0" shortName="AoA2" publisher="Warhammer Historical Wargames" publicationDate="2011"/>\n',
         '  </publications>\n  <costTypes>\n    <costType id="points" name="pts" defaultCostLimit="-1" hidden="false"/>\n  </costTypes>\n  <profileTypes>\n']
    for pn, chars in PT_CHARS.items():
        g.append(f'    <profileType id="{PT[pn]}" name={q(pn)}>\n      <characteristicTypes>\n')
        for c in chars: g.append(f'        <characteristicType id="{hid("ctype",pn,c)}" name={q(c)}/>\n')
        g.append('      </characteristicTypes>\n    </profileType>\n')
    g.append('  </profileTypes>\n  <categoryEntries>\n')
    for n,i in sorted(cats.items()): g.append(f'    <categoryEntry id="{i}" name={q(n)} hidden="false"/>\n')
    g.append('  </categoryEntries>\n  <forceEntries>\n')
    for (fname, fid, limits, usedcats) in forces:
        g.append(f'    <forceEntry id="{fid}" name={q(fname)} hidden="false">\n      <categoryLinks>\n')
        for cn in sorted(set(list(limits.keys())+list(usedcats))):
            lim = limits.get(cn)
            g.append(f'        <categoryLink id="{hid("flink",fid,cn)}" name={q(cn)} hidden="false" targetId="{cat(cn)}" primary="false"')
            if lim:
                g.append(f'>\n          <constraints>\n            {constraint("limit::points","roster",lim[1],lim[0],hid("lc",fid,cn),pct=True,inc_child=True)}\n          </constraints>\n        </categoryLink>\n')
            else:
                g.append('/>\n')
        g.append('      </categoryLinks>\n    </forceEntry>\n')
    g.append('  </forceEntries>\n  <sharedRules>\n')
    for n,r in sorted(rules.items()):
        pa = f' page={q(r["page"])}' if r['page'] else ''
        g.append(f'    <rule id="{hid("rule",n)}" name={q(n)} publicationId="{r["pub"]}"{pa} hidden="false">\n      <description>{t(r["text"])}</description>\n    </rule>\n')
    g.append('  </sharedRules>\n  <sharedProfiles>\n'+''.join(sp)+'  </sharedProfiles>\n</gameSystem>\n')

    os.makedirs(OUT, exist_ok=True)
    open(os.path.join(OUT,'Warhammer_Ancient_Battles_2.gst'),'w',encoding='utf8').write(''.join(g))
    for name, xml in cat_files.items():
        fn = re.sub(r'[^A-Za-z0-9 _\-]','',name).replace(' ','_')+'.cat'
        open(os.path.join(OUT,fn),'w',encoding='utf8').write(xml)
    open(os.path.join(OUT,'_build_report.txt'),'w',encoding='utf8').write('\n'.join(report))
    print('wrote', 1+len(cat_files), 'files;', len(rules), 'rules;', len(forces), 'force entries;', len(cats), 'categories')

def build_catalogue(a, cat, detect_rules, prof_ids, forces, report):
    cid = hid('catalogue', a['name'])
    notes_rule_name = f"{a['name']} - List Notes"
    notes_rule_id = hid('rule', cid, 'notes')
    comp_cats = set()
    for v in a['variants']: comp_cats |= set(v['limits'].keys())
    cur = None
    for sec in a['sections']:
        nt = norm_cat(sec['title']); low = sec['title'].lower().replace('&','and')
        if nt == 'Characters': cur = 'Characters'
        elif nt in comp_cats or low in CAT_HEADS: cur = nt
        elif cur is None: cur = nt
        sec['cat'] = cur; cat(cur)
    for c in comp_cats: cat(c)
    used = sorted({s['cat'] for s in a['sections'] if s['tables']} | comp_cats)
    for v in a['variants']:
        vname = a['name'] if not v['name'] else f"{a['name']} - {v['name']}"
        forces.append((vname, hid('force', vname), {k:val for k,val in v['limits'].items() if val}, used))

    lines = [f"{a['name']} ({a['dates']})", ''] + a['intro'] + ['', 'ARMY COMPOSITION (as printed in AoA2):']
    for v in a['variants']:
        if v['name']: lines.append(f"[{v['name']}]")
        for k,val in v['limits'].items():
            lines.append(f"  {k}: " + ('no percentage limit' if not val else (('at least ' if val[0]=='min' else 'up to ')+str(val[1])+'%')))
        for nt in v['notes']: lines.append('  ' + nt)
    for s in a['sections']:
        if norm_cat(s['title']) == 'Allies and Mercenaries' and s['free']:
            lines += ['', 'ALLIES: ' + ' '.join(s['free'])]
    notes_text = '\n'.join(lines)

    units = []
    for sec in a['sections']:
        for tbi, tb in enumerate(sec['tables']):
            units.append(build_table_units(a, cid, sec, tbi, tb, cat, detect_rules, prof_ids, (notes_rule_id, notes_rule_name), report))
    x = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n',
         f'<catalogue id="{cid}" name={q(a["name"])} revision="1" battleScribeVersion="2.03" authorName={q(AUTHOR)} library="false" '
         f'gameSystemId="{GS_ID}" gameSystemRevision="1" xmlns="http://www.battlescribe.net/schema/catalogueSchema" type="catalogue">\n',
         f'  <readme>{t(a["name"])}: units and points from Armies of Antiquity v2.0 (list no. {a["num"]}).</readme>\n  <selectionEntries>\n']
    x += units
    x.append('  </selectionEntries>\n  <sharedRules>\n')
    x.append(f'    <rule id="{notes_rule_id}" name={q(notes_rule_name)} publicationId="{PUB_AOA}" hidden="false">\n      <description>{t(notes_text)}</description>\n    </rule>\n')
    x.append('  </sharedRules>\n</catalogue>\n')
    return ''.join(x)

def build_table_units(a, cid, sec, tbi, tb, cat, detect_rules, prof_ids, notes_rule, report):
    rows = tb['rows']; cname = sec['cat']
    paras = tb['pre'] + tb['post']
    rows_ph = [row_phrases(r['name']) for r in rows]
    claimed = set()
    for p in paras:
        first = split_sentences(p)[:1]
        if first and re.search(r'\b(have|has)\b', first[0]):
            claimed |= set(named_rows(first[0], rows_ph))
    unclaimed = [i for i in range(len(rows)) if i not in claimed] or list(range(len(rows)))
    per_row = {i: dict(weapons=[], rules=[], options=[]) for i in range(len(rows))}
    for p in paras:
        ctx = None
        for s in split_sentences(p):
            named = named_rows(s, rows_ph)
            if named: ctx = named
            elif ctx is None: ctx = unclaimed
            for i in ctx:
                for w in detect_weapons(s):
                    if w not in per_row[i]['weapons']: per_row[i]['weapons'].append(w)
                for r in detect_rules(s):
                    if r not in per_row[i]['rules']: per_row[i]['rules'].append(r)
                for lab, cost in extract_options(s):
                    if (lab,cost) not in per_row[i]['options']: per_row[i]['options'].append((lab,cost))
    notes_txt = '\n\n'.join(paras)
    names = [r['name'] for r in rows]
    crew_i = [i for i,n in enumerate(names) if n.strip().lower()=='crew']
    has_crew = bool(crew_i)
    is_char = (cname == 'Characters')
    out = []
    for i, r in enumerate(rows):
        if has_crew and i in crew_i: continue
        nm = re.sub(r'^0-\d+\s+','',r['name']); mx = None
        mm = re.match(r'^0-(\d+)\s+', r['name'])
        if mm: mx = int(mm.group(1))
        if sec['restr'] and sec['title'] in ('GENERAL','GENERALS'): mx = sec['restr']
        uid = hid(cid, sec['title'], tbi, r['name'], 'unit')
        x = f'    <selectionEntry id="{uid}" name={q(nm)} hidden="false" collective="false" import="true" type="unit">\n'
        if mx: x += f'      <constraints>\n        {constraint("selections","roster",mx,"max",hid(uid,"max"),shared=True)}\n      </constraints>\n'
        x += (f'      <categoryLinks>\n        <categoryLink id="{hid(uid,"cat")}" name={q(cname)} hidden="false" targetId="{cat(cname)}" primary="true"/>\n'
              f'      </categoryLinks>\n      <selectionEntries>\n')
        gen = (notes_rule if (is_char and re.search('general|king', nm, re.I)) else None)
        x += model_xml(uid, r, nm, per_row[i], notes_txt, is_char, gen, prof_ids, mn=1, mxm=(1 if (is_char or has_crew) else None))
        if has_crew:
            ci = crew_i[0]; cr = rows[ci]
            nums = re.findall(r'(\d+)\s+crew', notes_txt)
            base = int(nums[0]) if ('light' in nm.lower() and len(nums)>1) else (int(nums[-1]) if nums else 3)
            m1 = re.search(r'up to (\d+) additional', notes_txt); m2 = re.search(r'(\d+) extra crew', notes_txt)
            ex_max = int(m1.group(1)) if m1 else (int(m2.group(1)) if m2 else 3)
            m3 = re.search(r'\+(\d+) each', notes_txt); ex_cost = m3.group(1) if m3 else '10'
            x += model_xml(uid, dict(name='Crew', stats=cr['stats'], pts='0'), 'Crew', per_row[ci], '', False, None, prof_ids, mn=base, mxm=base, key='crew')
            x += model_xml(uid, dict(name='Additional Crew', stats=cr['stats'], pts=ex_cost), 'Additional Crew', per_row[ci], '', False, None, prof_ids, mn=0, mxm=ex_max, key='xcrew')
        x += '      </selectionEntries>\n    </selectionEntry>\n'
        out.append(x)
        report.append(f"{a['name']} / {cname} / {nm}: pts={r['pts']} | rules={per_row[i]['rules']} | weapons/armour={per_row[i]['weapons']} | options={per_row[i]['options']}")
    return ''.join(out)

def model_xml(uid, r, nm, info, notes_txt, is_char, notes_rule, prof_ids, mn=1, mxm=None, key='m'):
    mid = hid(uid, key)
    stats = [(s if s.strip() else '-') for s in (list(r['stats'])+['']*9)[:9]]
    pts = re.sub(r'[^\d.]','', r['pts'].strip()) or '0'
    x = f'        <selectionEntry id="{mid}" name={q(nm)} hidden="false" collective="false" import="true" type="model">\n          <constraints>\n'
    x += f'            {constraint("selections","parent",mn,"min",hid(mid,"min"))}\n'
    if mxm is not None: x += f'            {constraint("selections","parent",mxm,"max",hid(mid,"max"))}\n'
    x += '          </constraints>\n          <profiles>\n'
    x += profile_xml(hid(mid,'prof'), nm, PT['Model'], 'Model', list(zip(STATS, stats)), PUB_AOA, None, '            ')
    if notes_txt:
        x += profile_xml(hid(mid,'notes'), 'Equipment and options (as printed in AoA2)', PT['Equipment and Notes'], 'Equipment and Notes', [('Text', notes_txt)], PUB_AOA, None, '            ')
    x += '          </profiles>\n'
    links = [f'<infoLink id="{hid(mid,"r",rn)}" name={q(rn)} hidden="false" targetId="{hid("rule",rn)}" type="rule"/>' for rn in info['rules']]
    links += [f'<infoLink id="{hid(mid,"w",wn)}" name={q(wn)} hidden="false" targetId="{prof_ids[wn]}" type="profile"/>' for wn in info['weapons'] if wn in prof_ids]
    if notes_rule:
        links.append(f'<infoLink id="{hid(mid,"nl")}" name={q(notes_rule[1])} hidden="false" targetId="{notes_rule[0]}" type="rule"/>')
    if links:
        x += '          <infoLinks>\n' + ''.join('            '+l+'\n' for l in links) + '          </infoLinks>\n'
    if info['options']:
        x += '          <selectionEntries>\n'; seen = set()
        for k,(lab,cost) in enumerate(info['options']):
            if lab.lower() in seen: continue
            seen.add(lab.lower()); oid = hid(mid,'opt',k,lab)
            x += (f'            <selectionEntry id="{oid}" name={q(lab)} hidden="false" collective="true" import="true" type="upgrade">\n'
                  f'              <constraints>\n                {constraint("selections","parent",1,"max",hid(oid,"max"))}\n                {constraint("selections","parent",0,"min",hid(oid,"min"))}\n              </constraints>\n'
                  f'              <costs>\n                <cost name="pts" typeId="points" value="{cost}"/>\n              </costs>\n            </selectionEntry>\n')
        x += '          </selectionEntries>\n'
    x += f'          <costs>\n            <cost name="pts" typeId="points" value="{pts}"/>\n          </costs>\n        </selectionEntry>\n'
    return x

if __name__ == '__main__':
    main()
