#!/usr/bin/env python3
"""Republican Roman list (Hannibal & the Punic Wars pp.51-52): per-war availability, Common/Uncommon tier per war,
"R:" (restricted) prerequisites, Leves OR Velites, 0-1 Elephant (Campaigns in the East). Same mechanism as carth_restrictions.py.
Units stay selectable; a unit that is not on the chosen war's list, or whose "R:" prerequisite is missing, FAILS VALIDATION
(an 'availability' max constraint that a modifier relaxes when the war and prerequisites are satisfied).
Usage: python3 roman_restrictions.py <outdir>   (run after collapse_forces.py; idempotent)."""
import sys, os, re, hashlib

OUT = sys.argv[1]
FN = 'Republican_Roman_Hannibal.cat'
PATH = os.path.join(OUT, FN)

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))

G = {   # list entry in the book -> catalogue units
 'Leves': ['Leves'], 'Velites': ['Velites'], 'Hastati': ['Hastati'], 'Principes': ['Principes'], 'Triarii': ['Triarii'],
 'Roman and Italian Cavalry': ['Roman and Italian Cavalry'], 'Italian Spearmen': ['Italian Spearmen', 'Italian Extraordinarii'],
 'Rorarii': ['Rorarii (use Leves profile)'], 'Accensi': ['Accensi'], 'Spanish Infantry': ['Spanish Infantry'], 'Spanish Cavalry': ['Spanish Cavalry'],
 'Cretan Archers': ['Cretan Archers'], 'Syracusan Skirmishers': ['Syracusan Skirmishers'], 'Tarentine Cavalry': ['Tarentine Cavalry'],
 'Numidian Cavalry': ['Numidian Cavalry'], 'Gallic Infantry': ['Gallic Infantry'], 'Gallic Cavalry': ['Gallic Cavalry'],
 'Thureophoroi and Peltasts': ['Thureophoroi', 'Peltasts'], 'Illyrian Infantry': ['Illyrian Infantry'], 'Illyrian Cavalry': ['Illyrian Cavalry'],
 'Ligurian Infantry': ['Ligurian Infantry'], 'Elephant': ['Numidian Elephant'],
}
RIC = 'Roman and Italian Cavalry'
# war -> (tier, group, [prerequisite groups, any one], max units or None, [groups that must be ABSENT]); C = Common, U = Uncommon
BASE = [('C', 'Hastati', [], None, []), ('C', 'Principes', [], None, []), ('C', 'Triarii', [], None, []), ('C', RIC, [], None, [])]
W = {
 'First Punic War': BASE + [('C', 'Leves', [], None, []), ('C', 'Italian Spearmen', [], None, []), ('U', 'Rorarii', [], None, []), ('U', 'Accensi', [], None, [])],
 'Second Punic War in Spain': BASE + [('C', 'Leves', [], None, ['Velites']), ('C', 'Velites', [], None, ['Leves']), ('C', 'Italian Spearmen', [], None, []),
   ('U', 'Spanish Infantry', [], None, []), ('U', 'Spanish Cavalry', [RIC], None, [])],
 'Second Punic War in Italy': BASE + [('C', 'Leves', [], None, ['Velites']), ('C', 'Velites', [], None, ['Leves']), ('C', 'Italian Spearmen', [], None, []),
   ('U', 'Cretan Archers', [], None, []), ('U', 'Syracusan Skirmishers', [], None, []), ('U', 'Tarentine Cavalry', [RIC], None, [])],
 'Second and Third Punic Wars in Africa': BASE + [('C', 'Velites', [], None, []), ('U', 'Syracusan Skirmishers', [], None, [])],
 'Campaigns in the West': BASE + [('C', 'Velites', [], None, []), ('U', 'Tarentine Cavalry', [RIC], None, []), ('U', 'Numidian Cavalry', [RIC], None, []),
   ('U', 'Spanish Cavalry', [RIC], None, []), ('U', 'Gallic Infantry', [], None, []), ('U', 'Gallic Cavalry', ['Gallic Infantry'], None, [])],
 'Campaigns in the East': BASE + [('C', 'Velites', [], None, []), ('C', 'Thureophoroi and Peltasts', [], None, []),
   ('U', 'Cretan Archers', [], None, []), ('U', 'Tarentine Cavalry', [RIC], None, []), ('U', 'Numidian Cavalry', [RIC], None, []),
   ('U', 'Spanish Infantry', [], None, []), ('U', 'Spanish Cavalry', ['Spanish Infantry'], None, []), ('U', 'Gallic Infantry', [], None, []),
   ('U', 'Gallic Cavalry', ['Gallic Infantry'], None, []), ('U', 'Illyrian Infantry', [], None, []), ('U', 'Illyrian Cavalry', ['Illyrian Infantry'], None, []),
   ('U', 'Ligurian Infantry', [], None, []), ('U', 'Elephant', [], 1, [])],
}
CHAR_WARS = {}

s = open(PATH, encoding='utf8').read()
# (nothing to merge for the Romans)
# "Common - Africa" Heavy Cavalry entry into Punic Heavy Cavalry (tier is now per war)
cid = re.search(r'<catalogue id="([^"]*)"', s).group(1)
cat_ids = {'C': hid('cat', 'Common Troops'), 'U': hid('cat', 'Uncommon Troops')}
cat_names = {'C': 'Common Troops', 'U': 'Uncommon Troops'}
war_names = [w for w in W]
def vid(war): return hid('picker', FN, f'Hannibal: Republican Roman - {war}')
def uid(name): return hid(cid, name, 'unit')

def cond_war(war):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{vid(war)}" type="atLeast"/>')
def cond_absent(name):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{uid(name)}" type="lessThan"/>')
def cond_unit(name):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{uid(name)}" type="atLeast"/>')

# per catalogue unit: {war: (tier, prereq group names, max)}
rules = {}
for war, lst in W.items():
    for tier, grp, pre, mx, ab in lst:
        for un in G[grp]:
            rules.setdefault(un, {})[war] = (tier, pre, mx, ab)
for un, wars in CHAR_WARS.items():
    for war in wars: rules.setdefault(un, {})[war] = (None, [], None, [])
ALWAYS = {'Army General', 'Alternative General - Political Animal', 'Alternative General - Military Man', 'Army Battle Standard', 'Consul', 'Cavalry Prefect',
          'Military Tribune', 'Prefect of the Allies', 'Balearic Slingers'}   # characters; Balearic Slingers are named in no composition: made unavailable by roman_fixes.py

done = 0
def do_unit(m):
    global done
    blk = m.group(0)
    name = re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1).replace('&amp;', '&')
    if name in ALWAYS or 'roman-restrictions' in blk: return blk
    if name not in rules:
        print('NOT IN ANY WAR LIST:', name); return blk
    rl = rules[name]
    conid = hid(uid(name), 'roman-war')
    mods = ''
    base = re.search(r'<categoryLink id="[^"]*" name="([^"]*)"[^>]*primary="true"', blk).group(1)
    base_tier = 'C' if base == 'Common Troops' else 'U' if base == 'Uncommon Troops' else None
    for war in war_names:
        if war not in rl: continue
        tier, pre, mx, ab = rl[war]
        val = mx if mx else -1
        conds = f'                {cond_war(war)}\n' + ''.join(f'                {cond_absent(u)}\n' for g in ab for u in G[g])
        grp = ''
        if pre:
            members = [u for g in pre for u in G[g]]
            grp = ('                <conditionGroups>\n                  <conditionGroup type="or">\n                    <conditions>\n'
                   + ''.join(f'                      {cond_unit(u)}\n' for u in members)
                   + '                    </conditions>\n                  </conditionGroup>\n                </conditionGroups>\n')
        mods += (f'          <modifier type="set" field="{conid}" value="{val}">\n'
                 f'            <conditionGroups>\n              <conditionGroup type="and">\n                <conditions>\n{conds}                </conditions>\n{grp}'
                 f'              </conditionGroup>\n            </conditionGroups>\n          </modifier>\n')
        if tier and base_tier and tier != base_tier:
            mods += (f'          <modifier type="remove" field="category" value="{cat_ids[base_tier]}">\n            <conditions>\n              {cond_war(war)}\n            </conditions>\n          </modifier>\n'
                     f'          <modifier type="add" field="category" value="{cat_ids[tier]}">\n            <conditions>\n              {cond_war(war)}\n            </conditions>\n          </modifier>\n')
    constraint = (f'        <constraint field="selections" scope="force" value="0" percentValue="false" shared="true" includeChildSelections="false" '
                  f'includeChildForces="false" id="{conid}" type="max"/>\n')
    head, rest = blk.split('\n', 1)
    if '      <constraints>\n' in rest.split('<categoryLinks>')[0]:
        rest = rest.replace('      <constraints>\n', '      <constraints>\n' + constraint, 1)
        cons = ''
    else:
        cons = '      <constraints>\n' + constraint + '      </constraints>\n'
    modxml = '      <modifiers>\n        <!-- roman-restrictions -->\n' + mods + '      </modifiers>\n'
    rest = rest.replace('      <categoryLinks>', cons + modxml + '      <categoryLinks>', 1)
    done += 1
    return head + '\n' + rest
s = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
open(PATH, 'w', encoding='utf8').write(s)
print('restricted', done, 'units')

# ---- second pass: hide units that are not on the chosen war's list (they also still fail validation if already added) ----
s = open(PATH, encoding='utf8').read()
hid_done = 0
def do_hide(m):
    global hid_done
    blk = m.group(0)
    name = re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1).replace('&amp;', '&')
    if name in ALWAYS or name not in rules or 'roman-hide' in blk: return blk
    absent = [w for w in war_names if w not in rules[name]]
    if not absent: return blk
    conds = ''.join(f'                  {cond_war(w)}\n' for w in absent)
    mod = ('        <!-- roman-hide -->\n          <modifier type="set" field="hidden" value="true">\n            <conditionGroups>\n              <conditionGroup type="or">\n'
           f'                <conditions>\n{conds}                </conditions>\n              </conditionGroup>\n            </conditionGroups>\n          </modifier>\n')
    hid_done += 1
    return blk.replace('      </modifiers>\n', mod + '      </modifiers>\n', 1)
s = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_hide, s, flags=re.S)
open(PATH, 'w', encoding='utf8').write(s)
print('hide modifiers added to', hid_done, 'units')

s = open(PATH, encoding='utf8').read()
s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1)
open(PATH, 'w', encoding='utf8').write(s)
