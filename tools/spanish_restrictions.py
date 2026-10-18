#!/usr/bin/env python3
"""Spanish list (Hannibal & the Punic Wars pp.70-71): which units each sub-list (Iberians, Celtiberians, Lusitanians) may use, Celtiberian Warriors
Infantry in the Celtiberians and Special Units in the Iberians, one Lusitanian unit per two Caetrati units. Same mechanism as carth_restrictions.py.
Units stay selectable; a unit that is not on the chosen war's list, or whose "R:" prerequisite is missing, FAILS VALIDATION
(an 'availability' max constraint that a modifier relaxes when the war and prerequisites are satisfied).
Usage: python3 spanish_restrictions.py <outdir>   (run after collapse_forces.py; idempotent)."""
import sys, os, re, hashlib

OUT = sys.argv[1]
FN = 'Spanish_Hannibal.cat'
PATH = os.path.join(OUT, FN)

def hid(*parts):
    h = hashlib.md5('|'.join(str(p) for p in parts).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))

G = {n: [n] for n in ['Heavy Cavalry', 'Light Cavalry', 'Scutarii', 'Tribesmen', 'Caetrati', 'Celtiberian Warriors', 'Lusitanians', 'Slingers', 'Balearic Slingers']}
CAV = [('V', 'Heavy Cavalry', [], None, []), ('V', 'Light Cavalry', [], None, [])]
# sub-list -> (tier/category I = Infantry, S = Special Units, V = Cavalry, group, prerequisites, max, absent)
W = {
 'Iberians': [('I', 'Scutarii', [], None, []), ('I', 'Tribesmen', [], None, []), ('I', 'Caetrati', [], None, []),
   ('S', 'Celtiberian Warriors', [], None, []), ('S', 'Slingers', [], None, []), ('S', 'Balearic Slingers', [], None, [])] + CAV,
 'Celtiberians': [('I', 'Celtiberian Warriors', [], None, []), ('I', 'Tribesmen', [], None, []), ('I', 'Caetrati', [], None, []),
   ('S', 'Slingers', [], None, [])] + CAV,
 'Lusitanians': [('I', 'Lusitanians', [], None, []), ('I', 'Caetrati', [], None, []), ('S', 'Slingers', [], None, [])] + CAV,
}
CHAR_WARS = {}

s = open(PATH, encoding='utf8').read()
cat_ids = {'I': hid('cat', 'Infantry'), 'S': hid('cat', 'Special Units')}
s = re.sub(r'    <selectionEntry id="[^"]*" name="Celtiberian Warriors \(Special - Iberians\)".*?\n    </selectionEntry>\n', '', s, flags=re.S)
# "Common - Africa" Heavy Cavalry entry into Punic Heavy Cavalry (tier is now per war)
cid = re.search(r'<catalogue id="([^"]*)"', s).group(1)

cat_names = {'C': 'Common Troops', 'U': 'Uncommon Troops'}
war_names = [w for w in W]
def vid(war): return hid('picker', FN, f'Hannibal: Spanish - {war}')
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
ALWAYS = {'Army General', 'Army Battle Standard', 'Heroic Leaders'}

done = 0
def do_unit(m):
    global done
    blk = m.group(0)
    name = re.match(r'    <selectionEntry id="[^"]*" name="([^"]*)"', blk).group(1).replace('&amp;', '&')
    if name in ALWAYS or 'spanish-restrictions' in blk: return blk
    if name not in rules:
        print('NOT IN ANY WAR LIST:', name); return blk
    rl = rules[name]
    conid = hid(uid(name), 'spanish-war')
    mods = ''
    base = re.search(r'<categoryLink id="[^"]*" name="([^"]*)"[^>]*primary="true"', blk).group(1)
    base_tier = {'Infantry': 'I', 'Special Units': 'S', 'Cavalry': 'V'}.get(base)
    for war in war_names:
        if war not in rl: continue
        tier, pre, mx, ab = rl[war]
        val = mx if mx else -1
        tier = None if tier == 'V' else tier
        conds = f'                {cond_war(war)}\n' + ''.join(f'                {cond_absent(u)}\n' for g in ab for u in G[g])
        grp = ''
        if pre:
            members = [u for g in pre for u in G[g]]
            grp = ('                <conditionGroups>\n                  <conditionGroup type="or">\n                    <conditions>\n'
                   + ''.join(f'                      {cond_unit(u)}\n' for u in members)
                   + '                    </conditions>\n                  </conditionGroup>\n                </conditionGroups>\n')
        if name == 'Lusitanians' and war == 'Lusitanians':
            mods += (f'          <modifier type="increment" field="{conid}" value="1">\n            <repeats>\n              <repeat field="selections" scope="force" value="2" percentValue="false" shared="true" includeChildSelections="false" includeChildForces="false" childId="{uid("Caetrati")}" repeats="1" roundUp="false"/>\n            </repeats>\n'
                     f'            <conditions>\n              {cond_war(war)}\n            </conditions>\n          </modifier>\n')
            continue
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
    modxml = '      <modifiers>\n        <!-- spanish-restrictions -->\n' + mods + '      </modifiers>\n'
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
    if name in ALWAYS or name not in rules or 'spanish-hide' in blk: return blk
    absent = [w for w in war_names if w not in rules[name]]
    if not absent: return blk
    conds = ''.join(f'                  {cond_war(w)}\n' for w in absent)
    mod = ('        <!-- spanish-hide -->\n          <modifier type="set" field="hidden" value="true">\n            <conditionGroups>\n              <conditionGroup type="or">\n'
           f'                <conditions>\n{conds}                </conditions>\n              </conditionGroup>\n            </conditionGroups>\n          </modifier>\n')
    hid_done += 1
    return blk.replace('      </modifiers>\n', mod + '      </modifiers>\n', 1)
s = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_hide, s, flags=re.S)
open(PATH, 'w', encoding='utf8').write(s)
print('hide modifiers added to', hid_done, 'units')

s = open(PATH, encoding='utf8').read()
s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1)
open(PATH, 'w', encoding='utf8').write(s)
