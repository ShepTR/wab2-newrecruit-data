#!/usr/bin/env python3
"""Carthaginian list (Hannibal & the Punic Wars pp.20-21): per-war availability, Common/Uncommon tier per war,
"R:" (restricted) prerequisites, Elephants max 1 in Italy, Mercenary General only in the First Punic War.
Units stay selectable; a unit that is not on the chosen war's list, or whose "R:" prerequisite is missing, FAILS VALIDATION
(an 'availability' max constraint that a modifier relaxes when the war and prerequisites are satisfied).
Usage: python3 carth_restrictions.py <outdir>   (run after collapse_forces.py; idempotent)."""
import sys, os, re, hashlib

OUT = sys.argv[1]
FN = 'Carthaginian_Hannibal.cat'
PATH = os.path.join(OUT, FN)

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))

G = {   # list entry in the book -> catalogue units
 'Levy Africans': ['Levy Africans'], 'Trained Africans': ['Trained Africans'], 'Veterans': ['Veterans'],
 'Citizens': ['Citizen Infantry'], 'Mercenary Hoplites': ['Mercenary Hoplites'], 'Gallic Warriors': ['Gallic Warriors'],
 'Gallic Veterans': ['Gallic Veterans'], 'Spanish Infantry': ['Spanish Scutarii', 'Spanish Caetrati'],
 'Skirmishers': ['Skirmishers'], 'Numidian Cavalry': ['Numidian Cavalry'], 'Celtiberian Scutarii': ['Celtiberian Scutarii'],
 'Oscan Infantry': ['Oscan Hoplites', 'Oscan Warriors'], 'Italian Infantry': ['Italian Infantry'],
 'Bruttian Veterans': ['Bruttian Veterans'], 'Peltasts and Thureophoroi': ['Peltasts', 'Thureophoroi'],
 'Punic Heavy Cavalry': ['Punic Heavy Cavalry'], 'Campanian Cavalry': ['Campanian Cavalry'],
 'Elephants': ['Elephants', 'Untrained Elephants'], 'Balearic Slingers': ['Balearic Slingers'],
 'Ligurian Infantry': ['Ligurian Warriors', 'Ligurian Slingers'], 'Sardinian Archers': ['Sardinian Archers'],
 'Moorish Archers': ['Moorish Archers'], 'Artillery': ['Artillery (Heavy Bolt Ballista)'],
 'Spanish Cavalry': ['Spanish Heavy Cavalry', 'Spanish Light Cavalry'], 'Gallic Cavalry': ['Gallic Cavalry'],
 'Roman Deserters': ['Roman Deserters'],
}
TA, VET, MH = 'Trained Africans', 'Veterans', 'Mercenary Hoplites'
# war -> list of (tier, group, [prerequisite groups], max units or None); tier C = Common, U = Uncommon
W = {
 'First Punic War': [
  ('C', 'Levy Africans', [], None), ('C', 'Mercenary Hoplites', [], None), ('C', 'Gallic Warriors', [MH], None),
  ('C', 'Spanish Infantry', [MH], None), ('C', 'Skirmishers', [], None), ('C', 'Numidian Cavalry', ['Punic Heavy Cavalry'], None),
  ('U', 'Peltasts and Thureophoroi', [MH], None), ('U', 'Punic Heavy Cavalry', [], None), ('U', 'Campanian Cavalry', [MH], None),
  ('U', 'Elephants', [], None), ('U', 'Balearic Slingers', [], None), ('U', 'Ligurian Infantry', [], None),
  ('U', 'Sardinian Archers', [], None), ('U', 'Artillery', [], None)],
 'Second Punic War in Spain': [
  ('C', TA, [], None), ('C', 'Gallic Warriors', [], None), ('C', 'Spanish Infantry', [], None), ('C', 'Skirmishers', [], None),
  ('C', 'Numidian Cavalry', [TA], None), ('C', 'Celtiberian Scutarii', ['Spanish Infantry'], None),
  ('U', 'Spanish Cavalry', [], None), ('U', 'Gallic Cavalry', [], None), ('U', 'Elephants', [TA], None),
  ('U', 'Balearic Slingers', [], None), ('U', 'Artillery', [], None)],
 'Second Punic War in Italy': [
  ('C', TA, [], None), ('C', VET, [], None), ('C', 'Oscan Infantry', [], None), ('C', 'Italian Infantry', [], None),
  ('C', 'Gallic Warriors', [TA, VET], None), ('C', 'Gallic Veterans', [TA, VET], None), ('C', 'Spanish Infantry', [TA, VET], None),
  ('C', 'Skirmishers', [], None), ('C', 'Numidian Cavalry', [TA, VET, 'Oscan Infantry', 'Italian Infantry'], None),
  ('U', 'Campanian Cavalry', ['Oscan Infantry', 'Italian Infantry'], None), ('U', 'Spanish Cavalry', [], None),
  ('U', 'Gallic Cavalry', [], None), ('U', 'Elephants', [TA, VET], 1), ('U', 'Balearic Slingers', [], None),
  ('U', 'Celtiberian Scutarii', [TA, VET], None), ('U', 'Roman Deserters', [], None), ('U', 'Ligurian Infantry', [], None),
  ('U', 'Artillery', [], None)],
 'Second Punic War in Africa': [
  ('C', 'Citizens', [], None), ('C', TA, [], None), ('C', 'Levy Africans', ['Citizens'], None), ('C', VET, [], None),
  ('C', 'Oscan Infantry', [], None), ('C', 'Bruttian Veterans', [VET], None), ('C', 'Skirmishers', [], None),
  ('C', 'Numidian Cavalry', [TA, 'Levy Africans', VET], None), ('C', 'Punic Heavy Cavalry', [], None),
  ('U', 'Spanish Cavalry', [TA, VET], None), ('U', 'Gallic Cavalry', [TA, VET], None), ('U', 'Elephants', [], None),
  ('U', 'Balearic Slingers', [], None), ('U', 'Celtiberian Scutarii', [TA, VET], None), ('U', 'Ligurian Infantry', [], None),
  ('U', 'Moorish Archers', [], None), ('U', 'Artillery', [], None)],
 'Third Punic War in Africa': [
  ('C', 'Citizens', [], None), ('C', TA, [], None), ('C', 'Levy Africans', [], None), ('C', 'Skirmishers', [], None),
  ('C', 'Numidian Cavalry', [TA, 'Levy Africans'], None), ('U', 'Punic Heavy Cavalry', [], None), ('U', 'Artillery', [], None)],
}
CHAR_WARS = {'Mercenary General': ['First Punic War']}      # allowed only here; other characters: every war

s = open(PATH, encoding='utf8').read()
# merge the old duplicate "Common - Africa" Heavy Cavalry entry into Punic Heavy Cavalry (tier is now per war)
s = re.sub(r'    <selectionEntry id="[^"]*" name="Punic Heavy Cavalry \(Common - Africa\)".*?\n    </selectionEntry>\n', '', s, flags=re.S)
s = s.replace('(use the "Common - Africa" entry)', '').replace('Uncommon in the First and Third Punic Wars.', 'Uncommon in the First and Third Punic Wars, Common in the Second Punic War in Africa.')
cid = re.search(r'<catalogue id="([^"]*)"', s).group(1)
cat_ids = {'C': hid('cat', 'Common Troops'), 'U': hid('cat', 'Uncommon Troops')}
cat_names = {'C': 'Common Troops', 'U': 'Uncommon Troops'}
war_names = [w for w in W]
def vid(war): return hid('picker', FN, f'Hannibal: Carthaginian - {war}')
def uid(name): return hid(cid, name, 'unit')

def cond_war(war):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{vid(war)}" type="atLeast"/>')
def cond_unit(name):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{uid(name)}" type="atLeast"/>')

# per catalogue unit: {war: (tier, prereq group names, max)}
rules = {}
for war, lst in W.items():
    for tier, grp, pre, mx in lst:
        for un in G[grp]:
            rules.setdefault(un, {})[war] = (tier, pre, mx)
for un, wars in CHAR_WARS.items():
    for war in wars: rules.setdefault(un, {})[war] = (None, [], None)
ALWAYS = {'Army General', 'Army Battle Standard', 'Subordinate General'}

done = 0
def do_unit(m):
    global done
    blk = m.group(0)
    name = re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1).replace('&amp;', '&')
    if name in ALWAYS or 'carth-restrictions' in blk: return blk
    if name not in rules:
        print('NOT IN ANY WAR LIST:', name); return blk
    rl = rules[name]
    conid = hid(uid(name), 'carth-war')
    mods = ''
    base = re.search(r'<categoryLink id="[^"]*" name="([^"]*)"[^>]*primary="true"', blk).group(1)
    base_tier = 'C' if base == 'Common Troops' else 'U' if base == 'Uncommon Troops' else None
    for war in war_names:
        if war not in rl: continue
        tier, pre, mx = rl[war]
        val = mx if mx else -1
        conds = f'                {cond_war(war)}\n'
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
    modxml = '      <modifiers>\n        <!-- carth-restrictions -->\n' + mods + '      </modifiers>\n'
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
    if name in ALWAYS or name not in rules or 'carth-hide' in blk: return blk
    absent = [w for w in war_names if w not in rules[name]]
    if not absent: return blk
    conds = ''.join(f'                  {cond_war(w)}\n' for w in absent)
    mod = ('        <!-- carth-hide -->\n          <modifier type="set" field="hidden" value="true">\n            <conditionGroups>\n              <conditionGroup type="or">\n'
           f'                <conditions>\n{conds}                </conditions>\n              </conditionGroup>\n            </conditionGroups>\n          </modifier>\n')
    hid_done += 1
    return blk.replace('      </modifiers>\n', mod + '      </modifiers>\n', 1)
s = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_hide, s, flags=re.S)
open(PATH, 'w', encoding='utf8').write(s)
print('hide modifiers added to', hid_done, 'units')
