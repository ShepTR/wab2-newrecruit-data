#!/usr/bin/env python3
"""Armies of Antiquity v2 (unofficial, Martin Gibbins): extract the army lists from the .docx into JSON (structure only).
Usage: python3 aoa2_extract.py <path to "02_Armies of Antiquity v 2.0.docx"> <out.json>"""
import sys, re, json, docx
from docx.table import Table
from docx.text.paragraph import Paragraph

def blocks_of(path):
    d = docx.Document(path); out = []
    for el in d.element.body.iterchildren():
        tag = el.tag.split('}')[1]
        if tag == 'p':
            p = Paragraph(el, d)
            out.append({'t': 'p', 'style': p.style.name, 'text': p.text.replace('\xa0', ' ').strip(),
                        'ital': [r.text.strip() for r in p.runs if r.italic and r.text.strip()],
                        'runs': [(r.text, bool(r.italic)) for r in p.runs]})
        elif tag == 'tbl':
            t = Table(el, d); rows = []
            for r in t.rows:
                cells = []; prev = None
                for c in r.cells:
                    if c._tc is prev: continue
                    prev = c._tc; cells.append(c.text.replace('\xa0', ' ').strip())
                rows.append(cells)
            out.append({'t': 'tbl', 'rows': rows})
    return out

ARMY = re.compile(r'^(\d{1,3})\.\s+([A-Z][A-Z ,&\'()/-]+?)\s*(\d.*)?$')
def split_armies(b):
    start = next(i for i, x in enumerate(b) if x['t'] == 'p' and x['text'] == 'ARMY LISTS')
    armies = []; cur = None
    for x in b[start + 1:]:
        if x['t'] == 'p':
            m = ARMY.match(x['text'])
            if m and not x['text'].upper().startswith('APPENDIX'):
                cur = {'num': m.group(1), 'title': m.group(2).strip(), 'dates': (m.group(3) or '').strip(), 'blocks': []}
                armies.append(cur); continue
            if x['text'] == 'APPENDIX': break
        if cur is not None: cur['blocks'].append(x)
    return armies

def rule_defs(b):
    """Heading 1 sections of the additional rules chapter -> {name: text}"""
    s = next(i for i, x in enumerate(b) if x['t'] == 'p' and x['text'].startswith('ADDITIONAL RULES'))
    e = next(i for i, x in enumerate(b) if x['t'] == 'p' and x['text'] == 'ARMY LISTS')
    defs = {}; cur = None
    for x in b[s + 1:e]:
        if x['t'] != 'p': continue
        if x['style'] == 'Heading 1' or (x['runs'] and all(not r[1] for r in x['runs']) and x['text'] and len(x['text']) < 60 and not x['text'].endswith('.') and x['text'][0].isupper() and False):
            cur = re.sub(r'\s*\(p+\.? ?\d+\)\s*$', '', x['text']).strip(); defs[cur] = []
        elif cur and x['text']: defs[cur].append(x['text'])
    return {k: ' '.join(v) for k, v in defs.items()}

if __name__ == '__main__':
    b = blocks_of(sys.argv[1]); armies = split_armies(b)
    json.dump({'armies': armies, 'rules': rule_defs(b)}, open(sys.argv[2], 'w'), indent=0)
    print(len(armies), 'armies;', len(rule_defs(b)), 'rule definitions')
