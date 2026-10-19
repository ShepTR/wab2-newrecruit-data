#!/usr/bin/env python3
"""Extract the 'Armies of Antiquity v2024' PDF (Word export, pdftotext -layout) into the same JSON structure that aoa2_gen.py reads
(armies -> blocks of paragraphs / 11-column tables, plus rule definitions).
Usage: python3 aoa24_extract.py <layout.txt> <out.json> [appendix.txt]"""
import sys, re, json
src = open(sys.argv[1], encoding='utf8').read()
pages = src.split('\f')
lines = []
for p in pages:
    for ln in p.split('\n'):
        if re.match(r'^\s*Updated 01 January 2024\s+\d*\s*$', ln): continue
        if re.match(r'^\s*\d{1,3}\s*$', ln): continue
        ln = re.sub(r'\b0\s*[\u2013\-]\s*(\d)\b', r'0-\1', ln.rstrip())
        ln = ln.replace('BERBER S', 'BERBERS')
        lines.append(ln)
HDR = re.compile(r'^\s*M\s+WS\s+BS\s+S\s+T\s+W\s+I\s+A\s+Ld(?:\s+Pts)?\s*$')
TITLE = re.compile(r'^\s*(?:(\d{1,3})\.\s+)?(\S.*?)\s+(\d{2,4}\s*(?:BC|AD)\b.*|\d{2,4}\s*A\b.*)$')
def is_title(ln):
    m = TITLE.match(ln)
    if not m: return None
    t = m.group(2).strip()
    letters = [c for c in t if c.isalpha()]
    if '....' in ln or len(t) < 3 or not letters or t.startswith('0-'): return None
    up = sum(1 for c in letters if c.isupper()) / len(letters)
    if up < 0.8 or len(t) > 60: return None
    return (m.group(1), t, m.group(3).strip())
# ---- locate sections
body = None; rules_start = None; chariot_start = None; app_start = None
for i, ln in enumerate(lines):
    if ln.strip() == 'ADDITIONAL RULES' and rules_start is None and not ln.rstrip().endswith('.'): rules_start = i if rules_start is None else rules_start
    if ln.strip() == 'ARMY LISTS' and body is None: body = i
# TOC lines have dots; body lines exact. first exact 'ADDITIONAL RULES' w/o dots is the TOC?  TOC has dots so exact match is body.
app = [i for i, ln in enumerate(lines) if ln.strip() == 'APPENDIX']
app_start = app[-1] if app else len(lines)
toc_rules = []
for ln in lines[:body]:
    m = re.match(r'^   ([A-Z][A-Z0-9 /().,&\'-]+?)\s*\.{5,}\s*\d*\s*$', ln)
    if m: toc_rules.append(m.group(1).strip().lower())
def para_join(ls):
    out = []; prev = ''
    for ln in ls:
        s = ln.strip()
        if not s: out.append(None); prev = ''; continue
        if out and out[-1] is not None and len(prev) >= 130: out[-1] += ' ' + s
        else: out.append(s)
        prev = ln
    return out
# ---- rule definitions
rules = {}
cur = None
for ln in lines[rules_start + 1:body]:
    s = ln.strip()
    if s.lower() in toc_rules and len(s) < 60 and s.lower() not in ('wagon movement',):
        cur = s; rules[cur] = []; continue
    if cur and s: rules[cur].append(s)
rules = {k: ' '.join(v) for k, v in rules.items()}
# ---- armies
armies = []; cur = None; i = body + 1
def cols_of(h):
    return [(m.start() + m.end()) / 2 for m in re.finditer(r'\S+', h)]
pending = []   # raw lines of current army
def flush_army():
    global cur
    if cur is None: return
    cur['blocks'] = build_blocks(pending[:])
    armies.append(cur); cur = None
def assign(nums, hc):
    n = len(nums); m = len(hc); cells = [''] * m
    if n >= m: 
        for j in range(m): cells[j] = nums[j][2]
        return cells
    INF = 1e9
    cs = [(t[0] + t[1]) / 2 for t in nums]
    dp = [[INF] * (m + 1) for _ in range(n + 1)]; ch = [[None] * (m + 1) for _ in range(n + 1)]
    for j in range(m + 1): dp[0][j] = 0
    for i in range(1, n + 1):
        for j in range(i, m + 1):
            skip = dp[i][j - 1]; use = dp[i - 1][j - 1] + abs(hc[j - 1] - cs[i - 1])
            if use <= skip: dp[i][j] = use; ch[i][j] = 'u'
            else: dp[i][j] = skip; ch[i][j] = 's'
    i, j = n, m
    while i > 0 and j > 0:
        if ch[i][j] == 'u': cells[j - 1] = nums[i - 1][2]; i -= 1; j -= 1
        else: j -= 1
    return cells
def build_blocks(ls):
    blocks = []; para = []; prev = ''; tbl = None; hc = None; lastrow_or_cont = False
    def endpara():
        nonlocal para
        if para:
            txt = ' '.join(para)
            m = re.match(r'^([A-Z][^.:;,()]{1,40}?)\s{3,}((?:Hand|Driver|Two|One|Rides|Armed|Light|Heavy|Javelin|Bow|Sling|Option)\b.*)$', txt)
            if m: txt = m.group(1).strip() + ' have ' + m.group(2)
            blocks.append({'t': 'p', 'style': 'Normal', 'text': txt, 'ital': [], 'runs': []}); para = []
    for ln in ls:
        if HDR.match(ln):
            endpara(); hc = cols_of(ln); tbl = {'t': 'tbl', 'rows': [['', 'M', 'WS', 'BS', 'S', 'T', 'W', 'I', 'A', 'Ld', 'Pts']]}
            blocks.append(tbl); lastrow_or_cont = False; prev = ''; continue
        s = ln.strip()
        if tbl is not None:
            if not s: tbl = None; prev = ''; continue
            toks = [(m.start(), m.end(), m.group()) for m in re.finditer(r'\S+', ln)]
            isnum = lambda t: re.fullmatch(r"[-\u2013\u2014*]|\d+(?:/\d+)?\*?|\d+\+?|[A-Za-z]?\d+", t)
            k0 = None
            for k, t in enumerate(toks):
                if (t[0] + t[1]) / 2 >= hc[0] - 4 and isnum(t[2]) and all(isnum(u[2]) for u in toks[k:]): k0 = k; break
            if k0 is not None and k0 > 0:
                namepart = ln[:toks[k0][0]].strip(); nums = toks[k0:]
                if len(namepart) <= 48 and len(namepart.split()) <= 7 and len(ln) - len(ln.lstrip()) < 12:
                    cells = assign(nums, hc)
                    tbl['rows'].append([namepart] + cells); lastrow_or_cont = True; continue
            nums = [t for t in toks if isnum(t[2]) and (t[0] + t[1]) / 2 >= hc[0] - 4]
            if lastrow_or_cont and len(s) <= 32 and not re.search(r'[.,:;]$', s) and not nums and len(ln) - len(ln.lstrip()) < 12:
                tbl['rows'][-1][0] += ' ' + s; continue
            tbl = None; lastrow_or_cont = False
        if not s: endpara(); prev = ''; continue
        if para and len(prev) >= 130: para[-1] += ' ' + s
        else:
            endpara(); para.append(s)
        prev = ln
    endpara()
    return blocks
skip = False
for i in range(body + 1, app_start):
    ln = lines[i]
    if ln.strip().startswith('WAB 2.0 CHARIOT WARS ARMY LISTS'):
        flush_army(); skip = True; continue
    t = is_title(ln)
    if t:
        flush_army(); pending = []; skip = False
        cur = {'num': t[0] or '', 'title': t[1], 'dates': t[2], 'blocks': []}; continue
    if cur is not None and not skip: pending.append(ln)
flush_army()
json.dump({'armies': armies, 'rules': rules}, open(sys.argv[2], 'w'), indent=1)
if len(sys.argv) > 3: open(sys.argv[3], 'w').write('\n'.join(lines[app_start:]))
print(len(armies), 'armies;', len(rules), 'rule definitions;', sum(1 for a in armies for b in a['blocks'] if b['t'] == 'tbl'), 'tables')
