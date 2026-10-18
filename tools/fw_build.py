#!/usr/bin/env python3
"""Add the Fall of the West (Warhammer Historical, 2002) army lists: Late Roman (Limitanei / Comitatenses), Late Barbarian (Sea Raiders, Western,
Central, Eastern, North African) and Warlord. Book pp.44-48 and special rules p.58 (pdf page = book + 2).
Usage: python3 fw_build.py <outdir>   (then run the post-processing chain: sh tools/fw_all.sh <outdir>)"""
import sys, os, re, json, copy
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import fw_data as D
import cw_build as CW
B = RB.B
hid, q, t = B.hid, B.q, B.t
OUT = RB.OUT
FPUB = hid('pub', 'fall of the west')
ROMAN_CH = ['Roman Army General', 'Roman Army Standard Bearer', 'Priest', 'Senior Roman Officer', 'Junior Roman Officer']
BARB_CH = ['Barbarian Warlord', 'Comitatus', 'Barbarian Army Warbanner', 'Priest', 'Senior Barbarian Chief', 'Barbarian Chieftain (Optimates)']
ch = {u['name']: u for u in D.CH}
def pick(names): return [copy.deepcopy(ch[n]) for n in names]
ROMAN = pick(ROMAN_CH) + copy.deepcopy(D.RI) + copy.deepcopy(D.RC) + copy.deepcopy(D.SP)
BARB = pick(BARB_CH) + copy.deepcopy(D.BI) + copy.deepcopy(D.BC)
WARL = [copy.deepcopy(u) for u in D.CH] + copy.deepcopy(D.RI) + copy.deepcopy(D.BI) + copy.deepcopy(D.RC) + copy.deepcopy(D.BC) + copy.deepcopy(D.SP)
for u in WARL:
    if u['cat'] in ('Roman Infantry', 'Barbarian Infantry'): u['cat'] = 'Infantry'
    elif u['cat'] in ('Roman Cavalry', 'Barbarian Cavalry'): u['cat'] = 'Cavalry'

def L(**k): return {c: v for c, v in k.items()}
ROMAN_V = [
 ('Roman Army - Limitanei', {'Characters': {'max': 25}, 'Roman Infantry': {'min': 25}, 'Roman Cavalry': {'min': 20, 'max': 60}, 'Special Units': {'max': 25}},
  'Approximately 50% of a Limitanei force by unit would be cavalry (a cavalry unit was half to two-thirds the size of an infantry unit), half light cavalry and half Roman shock cavalry; a heavy shock cavalry unit is very rare. The infantry would not include Palatina but might include Roman veterans and Roman Sagittarii. Special Units only with the opponent\'s permission.'),
 ('Roman Army - Comitatenses', {'Characters': {'max': 25}, 'Roman Infantry': {'min': 25}, 'Roman Cavalry': {'min': 20, 'max': 50}, 'Special Units': {'max': 25}},
  'Approximately one third of a Comitatenses force by unit would be cavalry (smaller units than infantry). Two thirds of the cavalry was Roman shock cavalry; the remainder split between heavy shock cavalry and light cavalry. Special Units only with the opponent\'s permission. Roman North African armies may be entirely mounted.'),
]
BARB_V = [
 ('Barbarian Army - Sea Raiders', {'Characters': {'max': 33}, 'Barbarian Cavalry': {'max': 0}}, 'Sea Raiders (including Saxon armies in Britain): characters up to 33%, Barbarian infantry the rest; no cavalry.'),
 ('Barbarian Army - Western Barbarians', {'Characters': {'max': 33}, 'Barbarian Infantry': {'min': 50}, 'Barbarian Cavalry': {'max': 20}}, 'Western Barbarians: characters up to 33%, Barbarian infantry at least 50%, Barbarian cavalry up to 20% (not steppe cavalry).'),
 ('Barbarian Army - Central Barbarians', {'Characters': {'max': 33}, 'Barbarian Infantry': {'min': 25}, 'Barbarian Cavalry': {'max': 40}}, 'Central Barbarians: characters up to 33%, Barbarian infantry at least 25%, Barbarian cavalry up to 40% (half may be steppe cavalry; not enforced).'),
 ('Barbarian Army - Eastern Barbarians', {'Characters': {'max': 33}, 'Barbarian Infantry': {'max': 25}, 'Barbarian Cavalry': {'max': 100}}, 'Eastern Barbarians: characters up to 33%, Barbarian infantry up to 25%, Barbarian cavalry up to 100% (all may be steppe cavalry).'),
 ('Barbarian Army - North African', {'Characters': {'max': 33}, 'Barbarian Infantry': {'max': 25}, 'Barbarian Cavalry': {'max': 100}}, 'North African: characters up to 33%, Barbarian infantry up to 25%, Barbarian cavalry up to 100%.'),
]
WARL_V = [('Warlord Army', {'Characters': {'max': 33}, 'Infantry': {'min': 33}, 'Cavalry': {'max': 50}}, 'Warlord armies: characters up to 33%, infantry (any) at least 33%, cavalry (any) up to 50%. During the 5th century the distinction between Roman and Barbarian armies broke down; a warlord\'s army could contain almost any mix of troops.')]

NOTES_ROMAN = 'LATE ROMAN ARMY LIST (Fall of the West, pp.44-48). Percentages are by points. Special rules p.58. Skirmish option, archers mixed into infantry units (one in four) and the Militia standard/musician restriction are rules text only.'
NOTES_BARB = 'LATE BARBARIAN ARMY LIST (Fall of the West, pp.44-48). Percentages are by points. Special rules p.58.'
NOTES_WARL = 'WARLORD ARMY LIST (Fall of the West, pp.44-48). Any Roman or Barbarian troops may be mixed. A Warlord army may be led by a Roman Army General or a Barbarian Warlord (not both).'
LISTS = [('Late Roman (Fall of the West)', ROMAN, ROMAN_V, NOTES_ROMAN, 'Late_Roman_Fall_of_the_West.cat'),
         ('Late Barbarian (Fall of the West)', BARB, BARB_V, NOTES_BARB, 'Late_Barbarian_Fall_of_the_West.cat'),
         ('Warlord (Fall of the West)', WARL, WARL_V, NOTES_WARL, 'Warlord_Fall_of_the_West.cat')]

def comp_text(variants):
    out = ['ARMY COMPOSITIONS:']
    for vn, lim, txt in variants:
        out.append(f'[{vn}]')
        for k, d in lim.items():
            out.append(f"  {k}: " + ', '.join(('at least' if kk == 'min' else 'up to') + f' {v}%' for kk, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = FPUB; RB.SRC = 'Fall of the West'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{FPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{FPUB}" name="Fall of the West" shortName="FotW" publisher="Warhammer Historical Wargames" publicationDate="2002"/>\n  </publications>', 1)
        open(gst, 'w', encoding='utf8').write(s)
    cache = os.path.join(OUT, 'tools', 'variants.json')
    variants = json.load(open(cache, encoding='utf8')) if os.path.exists(cache) else {}
    CW.clean([u for _, us, _, _, _ in LISTS for u in us])
    for name, units, vars_, notes, fn in LISTS:
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vars_), None)
        x = x.replace('gameSystemRevision="1"', 'gameSystemRevision="6"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Fall of the West army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': f'Fall of the West: {vn}', 'limits': lim} for vn, lim, txt in vars_]
        print('wrote', fn, len(units), 'units,', len(vars_), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    rules = dict(D.RULES)
    RB.patch_gst(gst, [(f'FW {n}', u, {}) for n, u, v, nt, fn in LISTS], rules)

if __name__ == '__main__':
    main()
