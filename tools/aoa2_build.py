#!/usr/bin/env python3
"""Add the unofficial Armies of Antiquity v2 (Martin Gibbins) army lists (generated data in aoa2_data.py).
Usage: python3 aoa2_build.py <outdir>   (then sh tools/aoa2_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import aoa2_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'aoa2')
REV = '18'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})

RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('Armies of Antiquity v2 ' + page, txt)
COMMON = ('Armies of Antiquity v2 Common Rules', R('intro', 'Unofficial army lists by Martin Gibbins (Armies of Antiquity v2). Army size: 2,800 points is roughly equivalent to 2,000 points of a period supplement. The Army General is optional; a Senior Officer may become the Army General for +50. Unit leaders, standard bearers and musicians cost +5 each; skirmishing Light Infantry may not take a standard or musician. War machines: one per 1,200 points unless the list says otherwise. Allies and Mercenaries (Unreliable): at the start of the first turn roll a D6 for each such unit; on a 1 the unit will not move or shoot. Allied units may bring their own characters and general. A character mounted on a chariot or elephant: both models fight and shoot. Percentage limits are by points. These lists were generated from the source document by a script and have not been checked unit by unit; see issues/Armies_of_Antiquity_v2.txt.'))
import json as _json
RULES = {COMMON[0]: COMMON[1]}
_NR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'aoa2_newrules.json')
if os.path.exists(_NR):
    for _k, _v in _json.load(open(_NR, encoding='utf8')).items(): RULES[_k] = R('rules', _v)
FIRSTCHAR = None
def comp_text(variants):
    out = ['ARMY COMPOSITIONS (pick one in the Army composition list):'] if len(variants) > 1 else ['ARMY COMPOSITION:']
    for vn, lim, txt in variants:
        out.append(f'[{vn.split(": ", 1)[-1]}]')
        for c, d in lim.items():
            out.append(f"  {c}: " + ', '.join(('at least' if k == 'min' else 'up to') + f' {v}%' for k, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = SPUB; RB.SRC = 'Armies of Antiquity v2'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Armies of Antiquity v2" shortName="A2" publisher="Martin Gibbins (unofficial)" publicationDate="2020"/>\n  </publications>', 1)
    s = re.sub(r'gameSystemRevision="\d+"', f'gameSystemRevision="{REV}"', s, count=1) if 'gameSystemRevision' in s else s
    s = re.sub(r'(<gameSystem [^>]*?)revision="\d+"', lambda m: m.group(1) + f'revision="{REV}"', s, count=1)
    pools = sorted({c for (_, _), cs in D.SECOND.items() for c in cs})
    for c in pools:
        if f'id="{hid("cat", c)}"' not in s:
            s = s.replace('  </categoryEntries>', f'    <categoryEntry id="{hid("cat", c)}" name="{c}" hidden="false"/>\n  </categoryEntries>', 1)
    open(gst, 'w', encoding='utf8').write(s)
    cache = os.path.join(OUT, 'tools', 'variants.json')
    variants = json.load(open(cache, encoding='utf8')) if os.path.exists(cache) else {}
    allunits = [u for _, _, _, us, _, _ in D.LISTS for u in us]
    CW.clean(allunits)
    for key, name, fn, units, vs, notes in D.LISTS:
        for u in units:
            for m in u['models']:
                m['rules'] = [RULE_MAP.get(r, r) for r in m['rules']]
        first = units[0]
        first['models'][0]['rules'].append(COMMON[0])
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the unofficial Armies of Antiquity v2 army lists (Martin Gibbins).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'A2 {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
