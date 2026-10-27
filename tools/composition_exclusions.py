#!/usr/bin/env python3
"""Per-composition unit exclusions (idempotent; run after the book's own pipeline and catalogue_tags).
Where a composition's text bans a whole unit ("May not take X", "Artillery: none", "Cavalry: none", "No Muslim troops"), the unit is hidden
once that composition is picked, so it can no longer be added.  The table below is deliberately limited to unambiguous bans; every other
case (partial limits, "only one unit of X", city-state labels, leaders) is listed in issues/Composition_review.txt instead.
The match on the composition is a substring of the picker's name; a table entry that matches nothing stops the script.
Usage: python3 composition_exclusions.py <outdir>"""
import sys, os, re, json, hashlib
from xml.sax.saxutils import escape
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
V = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'variants.json'), encoding='utf8'))

# catalogue -> [(composition substring, [unit names], reason)]
X = {
 'Warring_States_Art_of_War.cat': [('Army of Yan', ['Military Strategist (Jun Shi Jia)'], 'may not take a Military Strategist')],
 'Al_Andalus_and_Granada_AoA2.cat': [
    ('Al Andalus (755', ['Lancers', 'Crossbowmen', 'Crossbowmen (Infantry)'], 'may not take lancers or crossbowmen'),
    ('Taifa', ['Lancers', 'Crossbowmen'], 'may not take lancers or crossbowmen (cavalry); infantry crossbowmen limited to one unit, not enforced'),
    ('Nasrid', ['Noble Cavalry'], 'may not take Nobles')],
 'Christian_Spanish_AoA2.cat': [
    ('Early (711', ['Noble Cavalry', 'Military Orders'], 'may not take noble cavalry or military orders'),
    ('Middle (1040', ['Military Orders'], 'may not take military orders')],
 'Crusaders_AoA2.cat': [('Later Crusades', ['Pilgrims'], 'no Pilgrims may be taken')],
 'Late_Imperial_Roman_AoA2.cat': [('Romano-British', ['Imperator'], 'the army may not include an Imperator')],
 'Medieval_Hungarian_AoA2.cat': [('Early Hungarians', ['Royal Banderium', 'Cannon', 'Wagon'], 'may not take the Royal Banderium; Artillery & War Wagons: none')],
 'Muslim_Indian_AoA2.cat': [('Lodi', ['Handgunners'], 'may not take handgunners'), ('Tughluq', ['Handgunners'], 'may not take handgunners')],
 'North_African_Berbers_AoA2.cat': [('Other North African', ['Christian Captain'], 'may not take Christian captains')],
 'Ottoman_Turks_AoA2.cat': [
    ('Early Army', ['Bandsman', 'Guard Cavalry', 'Janissaries', 'Cannon', 'Mortar (Hayavi)'], 'may not take Bandsmen; Guards and Janissaries: none; Artillery: stone thrower only'),
    ('Later Army', ['Imam'], 'may not take Imams')],
 'Rus_AoA2.cat': [('Christianised', ['Berserker'], 'may not take Berserkers'), ('Pagan Rus', ['Druzhina'], 'Cavalry: none')],
 'Rus_Byzantium.cat': [('Era of the Princes', ['Grid Druzhina', 'Chernye Klobuki (Black Hoods)'], 'no Grid Druzhina or Chernye Klobuki')],
 'Russian_AoA2.cat': [('Post-Mongol', ['Aga', 'Militia Cavalry'], 'no Aga; no Militia Cavalry')],
 'Polish_AoA2.cat': [
    ('Early Polish', ['Cannon', 'Lithuanians', 'Cumans', 'Russians', 'Rycerz', 'Strzelcy'], 'Artillery, Mercenaries and Allies: none; cavalry may only be Druzhina'),
    ('Feudal Polish', ['Cannon'], 'War Wagons & Artillery: none'),
    ('Later Polish', ['Russians'], 'Mercenaries may not have Russians')],
 'Hindu_India_AoA2.cat': [
    ('Orissa', ['Elite Cavalry', 'Muslim Cavalry', 'Muslim Infantry'], 'only one unit of Hindu cavalry, no other cavalry; no Muslim troops'),
    ('Rajput', ['Rocket launcher', 'Muslim Cavalry', 'Muslim Infantry'], 'Artillery: none; Muslim troops may not be used'),
    ('Standard Army', ['Elite Cavalry', 'Muslim Infantry'], 'Elite cavalry may not be used; Muslim infantry may not be used')],
 'Italian_City_States_AoA2.cat': [('Early Italians', ['Cannon', 'Organ Gun', 'Balkan Light Cavalry (F, P, N, V)', 'Stradioti (V)'],
                                   'Artillery: none; no unit labelled F, M, P, N or V in an early army')],
 'Late_Barbarian_Fall_of_the_West.cat': [('Sea Raiders', ['Barbarian Shock Cavalry', 'Barbarian Light Cavalry'], 'no cavalry')],
}

# Units whose name ends in composition codes, e.g. "Light Chariots (E)", "Spearmen (A, B, S, M)": available only in the compositions of those codes.
# catalogue -> {composition substring: code}  (a composition that is not listed here, e.g. the generic 'Japanese' entry, hides nothing)
CODED = {
 'Assyrian_AoA2.cat': {'Early Army 900': 'E', 'Later Army 745': 'L'},
 'Japanese_AoA2.cat': {'Early Army 794': 'E', 'Middle Army 1041': 'M', 'Late Army 1392': 'L'},
 'Medieval_Balkan_States_AoA2.cat': {'Albanian': 'A', 'Bulgaria': 'B', 'Moldavia': 'M', 'Serbia': 'S'},
}
for fn, comps in CODED.items():
    path = os.path.join(OUT, fn)
    if not os.path.exists(path): continue
    names = [n.replace('&amp;', '&') for n in re.findall(r'^    <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="unit">', open(path, encoding='utf8').read(), re.M)]
    rows = []
    for comp, code in comps.items():
        hide = []
        for n in names:
            cs = set()
            for g in re.findall(r'\(([A-Z](?:\s*,\s*[A-Z])*)\s*\)', n): cs |= set(re.findall(r'[A-Z]', g))
            if cs and code not in cs: hide.append(n)
        rows.append((comp, hide, f'units coded for other compositions are not available (this one is {code})'))
    X.setdefault(fn, []).extend(rows)

def esc(n): return re.escape(escape(n))
changed = 0
for fn, rows in X.items():
    path = os.path.join(OUT, fn)
    if not os.path.exists(path): continue
    s = open(path, encoding='utf8').read(); orig = s
    for comp, units, why in rows:
        vs = [v for v in V[fn] if comp in v['name']]
        assert len(vs) == 1, f'{fn}: composition "{comp}" matches {len(vs)} pickers'
        pid = hid('picker', fn, vs[0]['name'])
        tag = f'<!-- unavailable-in:{pid} -->'
        for un in units:
            m = re.search(r'^    <selectionEntry id="[^"]*" name="%s"[^>]*type="unit">\n.*?\n    </selectionEntry>\n' % esc(un), s, re.S | re.M)
            assert m, f'{fn}: unit "{un}" not found'
            blk = m.group(0)
            if tag in blk: continue
            mod = (f'        {tag}\n'
                   f'        <modifier type="set" field="hidden" value="true">\n          <conditions>\n'
                   f'            <condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
                   f'includeChildForces="false" childId="{pid}" type="atLeast"/>\n          </conditions>\n        </modifier>\n')
            head, sep, rest = blk.partition('\n      <categoryLinks>')
            assert sep, f'{fn}/{un}: no categoryLinks'
            if '\n      <modifiers>\n' in head + '\n':
                # existing unit-level modifiers block: append before its closing tag (the last one before categoryLinks)
                i = head.rindex('\n      </modifiers>') + 1
                new = head[:i] + mod + head[i:] + sep + rest
            else:
                new = head + '\n      <modifiers>\n' + mod + '      </modifiers>' + sep + rest
            s = s.replace(blk, new, 1)
    if s != orig:
        s = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s, count=1)
        open(path, 'w', encoding='utf8').write(s); changed += 1
print(f'Composition exclusions applied to {changed} catalogue(s)' if changed else 'Composition exclusions already applied')
