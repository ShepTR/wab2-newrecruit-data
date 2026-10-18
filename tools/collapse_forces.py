#!/usr/bin/env python3
"""Replace the per-army force entries with ONE neutral force ("Army") in the game system, the way Badab War / the
40k 3rd Edition data set scopes factions: the faction is the catalogue, and the percentage limits on the force's category
links are changed by modifiers that test the primary catalogue (single-composition lists) or a required
"Army composition" picker (lists with several wars/campaigns).
Usage: python3 collapse_forces.py <outdir>   (run LAST; idempotent: variants are cached in variants.json).
Replaces relocate_forces.py (catalogue-level forceEntries are pooled by New Recruit, so they did not scope)."""
import sys, os, re, glob, json, hashlib

OUT = sys.argv[1]
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
CACHE = os.path.join(OUT, 'tools', 'variants.json')
PICKER = 'Army composition'

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def q(s): return '"' + str(s).replace('&', '&amp;').replace('"', '&quot;').replace('<', '&lt;') + '"'
def unesc(s): return s.replace('&quot;', '"').replace('&lt;', '<').replace('&amp;', '&')

# 1. collect variants: {catalogue file: [{'name', 'limits': {category: {'min'|'max': value}}}]}
data = {}
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    whole = re.findall(r'(    <forceEntry id="[^"]*" name="[^"]*".*?    </forceEntry>\n)', s, flags=re.S)
    if not whole: continue
    vs = []
    for blk in whole:
        name = unesc(re.match(r'    <forceEntry id="[^"]*" name="([^"]*)"', blk).group(1))
        lim = {}
        for m in re.finditer(r'<categoryLink id="[^"]*" name="([^"]*)"[^>]*>(.*?)</categoryLink>', blk, flags=re.S):
            cat = unesc(m.group(1))
            for c in re.finditer(r'<constraint field="limit::points"[^>]*value="([^"]*)"[^>]*type="(min|max)"', m.group(2)):
                lim.setdefault(cat, {})[c.group(2)] = float(c.group(1)) if '.' in c.group(1) else int(c.group(1))
        vs.append({'name': name, 'limits': lim})
    data[os.path.basename(path)] = vs
    s = re.sub(r'  <forceEntries>\n.*?  </forceEntries>\n', '', s, flags=re.S)
    open(path, 'w', encoding='utf8').write(s)
os.makedirs(os.path.dirname(CACHE), exist_ok=True)
if data:
    old = json.load(open(CACHE, encoding='utf8')) if os.path.exists(CACHE) else {}
    old.update(data)
    json.dump(old, open(CACHE, 'w', encoding='utf8'), indent=1)
variants = json.load(open(CACHE, encoding='utf8'))

# 2. catalogue ids
cat_id = {}
for fn in variants:
    c = open(os.path.join(OUT, fn), encoding='utf8').read()
    cat_id[fn] = re.search(r'<catalogue id="([^"]*)"', c).group(1)

def label(fn, vname):
    """Picker label: the part after ' - ' for a multi-composition list."""
    base = vname.split(': ', 1)[-1]
    return base.split(' - ', 1)[1] if ' - ' in base else base

s = open(GST, encoding='utf8').read()

# optional extra rule: a category limit changes when a given unit is in the army (tools/cond_limits.json: [{file, category, kind, value, unit}])
CONDF = os.path.join(OUT, 'tools', 'cond_limits.json')
CONDS = json.load(open(CONDF, encoding='utf8')) if os.path.exists(CONDF) else []
def unit_id(fn, name):
    c = open(os.path.join(OUT, fn), encoding='utf8').read()
    return re.search(r'<selectionEntry id="([^"]*)" name="%s"[^>]*type="unit"' % re.escape(name.replace('&', '&amp;')), c).group(1)

# 3. remove every existing force and rebuild one
s = re.sub(r'  <forceEntries>\n.*?  </forceEntries>\n', '', s, flags=re.S)
s = re.sub(r'  <selectionEntries>\n.*?  </selectionEntries>\n', '', s, flags=re.S)   # old pickers, if re-run
cats = re.findall(r'<categoryEntry id="([^"]*)" name="([^"]*)"', s)
pid = hid('cat', PICKER)
if not any(c[0] == pid for c in cats):
    s = s.replace('  </categoryEntries>', f'    <categoryEntry id="{pid}" name={q(PICKER)} hidden="false"/>\n  </categoryEntries>', 1)
cats = [(i, unesc(n)) for i, n in re.findall(r'<categoryEntry id="([^"]*)" name="([^"]*)"', s) if i != pid]

def cond_cat(fn):
    return (f'<condition field="selections" scope="primary-catalogue" value="1" percentValue="false" shared="true" '
            f'includeChildSelections="true" includeChildForces="true" childId="{cat_id[fn]}" type="instanceOf"/>')
def cond_pick(vid):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" '
            f'includeChildSelections="true" includeChildForces="false" childId="{vid}" type="atLeast"/>')

rid = hid('force', 'Army root')
multi = [fn for fn, vs in variants.items() if len(vs) > 1]
pickers = ''
vid_of = {}
for fn in multi:
    for v in variants[fn]:
        vid = hid('picker', fn, v['name']); vid_of[(fn, v['name'])] = vid
        pickers += (f'    <selectionEntry id="{vid}" name={q(label(fn, v["name"]))} hidden="true" collective="false" import="true" type="upgrade">\n'
                    f'      <comment>{fn}</comment>\n'
                    f'      <modifiers>\n        <modifier type="set" field="hidden" value="false">\n          <conditions>\n            {cond_cat(fn)}\n          </conditions>\n        </modifier>\n      </modifiers>\n'
                    f'      <categoryLinks>\n        <categoryLink id="{hid(vid, "cat")}" name={q(PICKER)} hidden="false" targetId="{pid}" primary="true"/>\n      </categoryLinks>\n'
                    f'    </selectionEntry>\n')

root = f'    <forceEntry id="{rid}" name="Army" hidden="false">\n      <categoryLinks>\n'
PICK_FIRST = ''   # the Army composition picker link is placed first so it shows at the top of the list
for cid, cn in cats:
    kinds = {}      # kind -> default
    for fn, vs in variants.items():
        for v in vs:
            for k in v['limits'].get(cn, {}): kinds[k] = 100 if k == 'max' else 0
    link = f'        <categoryLink id="{hid("rootlink", cn)}" name={q(cn)} hidden="false" targetId="{cid}" primary="false"'
    if not kinds:
        root += link + '/>\n'; continue
    cons = ''; mods = ''
    for k, dflt in sorted(kinds.items()):
        conid = hid('rootcon', cn, k)
        cons += (f'            <constraint field="limit::points" scope="roster" value="{dflt}" percentValue="true" shared="false" '
                 f'includeChildSelections="true" includeChildForces="false" id="{conid}" type="{k}"/>\n')
        for fn, vs in variants.items():
            single = len(vs) == 1
            for v in vs:
                val = v['limits'].get(cn, {}).get(k)
                if val is None: continue
                c = cond_cat(fn) if single else cond_pick(vid_of[(fn, v['name'])])
                mods += (f'            <modifier type="set" field="{conid}" value="{val}">\n              <conditions>\n                {c}\n              </conditions>\n            </modifier>\n')
        for ce in CONDS:
            if ce['category'] != cn or ce['kind'] != k: continue
            uc = (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="false" '
                  f'includeChildForces="false" childId="{unit_id(ce["file"], ce["unit"])}" type="atLeast"/>')
            mods += (f'            <modifier type="set" field="{conid}" value="{ce["value"]}">\n              <conditions>\n                {cond_cat(ce["file"])}\n                {uc}\n              </conditions>\n            </modifier>\n')
    root += link + f'>\n          <constraints>\n{cons}          </constraints>\n          <modifiers>\n{mods}          </modifiers>\n        </categoryLink>\n'
# picker link: at most one choice; one is required for lists that have several compositions
if multi:
    conds = ''.join(f'                {cond_cat(fn)}\n' for fn in multi)
    root += (f'        <categoryLink id="{hid("rootlink", PICKER)}" name={q(PICKER)} hidden="false" targetId="{pid}" primary="false">\n'
             f'          <constraints>\n'
             f'            <constraint field="selections" scope="parent" value="1" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="{hid("pick", "max")}" type="max"/>\n'
             f'            <constraint field="selections" scope="parent" value="0" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" id="{hid("pick", "min")}" type="min"/>\n'
             f'          </constraints>\n          <modifiers>\n            <modifier type="set" field="{hid("pick", "min")}" value="1">\n'
             f'              <conditionGroups>\n                <conditionGroup type="or">\n                  <conditions>\n{conds}                  </conditions>\n                </conditionGroup>\n              </conditionGroups>\n'
             f'            </modifier>\n          </modifiers>\n        </categoryLink>\n')
if multi and PICK_FIRST == '':
    m_ = re.search(r'        <categoryLink id="[^"]*" name="Army composition".*?        </categoryLink>\n', root, re.S)
    root = root.replace(m_.group(0), '', 1).replace('      <categoryLinks>\n', '      <categoryLinks>\n' + m_.group(0), 1)
root += '      </categoryLinks>\n    </forceEntry>\n'
s = s.replace('  <sharedRules>', f'  <forceEntries>\n{root}  </forceEntries>\n' + (f'  <selectionEntries>\n{pickers}  </selectionEntries>\n' if pickers else '') + '  <sharedRules>', 1)
open(GST, 'w', encoding='utf8').write(s)
print('one force; limit modifiers for', sum(len(v) for v in variants.values()), 'compositions;', len(multi), 'catalogues with a picker')
