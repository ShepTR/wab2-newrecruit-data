#!/usr/bin/env python3
"""Add the Byzantium: Beyond the Golden Gate (Warhammer Historical, 2005) army lists. Book page = printed page number.
Usage: python3 bz_build.py <outdir>   (then sh tools/bz_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import bz_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'byzantium')
REV = '14'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Javelins': 'Javelin', 'Two-handed Weapon': 'Double-handed Weapon', 'Kontarion': 'Kontos'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)', 'Expert Horsemen (if mounted)': 'Expert Horsemen', 'Feigned Flight (if mounted)': 'Feigned Flight', 'Warband Psychology (rules 1 & 2)': 'Warband Psychology (rules 1 & 2)'}
def R(page, txt): return ('Byzantium ' + page, txt)
RULES = {
 'Superior Byzantine Cavalry': R('p.12', 'Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of any close combat when charging or counter-charging). Superior Byzantine Cavalry may also choose to retire if they win a round of close combat but fail to force their opponents to flee or fall back: a normal Fall Back in Good Order move, the retiring unit may only be pursued by opponents with Movement equal or greater than its own and may still charge next turn. Not usable by cavalry on barded or half-barded horses.'),
 'Superior Germanic Cavalry': R('p.12', 'Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). The first formed enemy unit successfully charged or counter-charged by Superior Germanic Cavalry will automatically break if it loses the combat, but only if the enemy is outnumbered by the Superior Germanic Cavalry unit.'),
 'Superior Persian Cavalry': R('p.12', 'Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). May shoot when they charge or counter-charge and may use massed archery whilst doing so, after enemy charge reactions, counting as short range (the -1 for moving still applies). Enemy units taking 25% casualties or more must pass a Panic test or flee; these casualties do not count towards combat resolution.'),
 'Superior Turkish Cavalry': R('p.12', 'Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). During their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching. May also perform Parthian Shot.'),
 'Superior Arab Cavalry': R('p.12', 'Superior Cavalry (rank bonus up to +1; re-roll misses in the first round of combat when charging or counter-charging). During their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching.'),
 'Shieldwall (Byzantium)': R('p.13', 'May form a shieldwall instead of moving. While in a shieldwall all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit. Benefits last while the unit remains stationary and does not lose a round of close combat.'),
 'Levies (Byzantium)': R('p.13', 'Levies fear enemies they do not outnumber by at least two to one. Levies do not fear other levies or skirmishers.'),
 'Fearsome': R('p.13', 'All enemy units with a base Leadership value of 7 or less fear troops who are Fearsome. If a character or model with a higher Leadership leads the unit they still fear them but may use the leader\'s higher Leadership for the Fear test. The same applies to warbands.'),
 'Oath of Allegiance': R('p.14', 'If the Army General is killed roll a D6. On a 4+ the troops immediately move towards and charge the nearest enemy and are immune to Panic and Break tests. If they eliminate their opponent they attack the nearest enemy unit again, and so on. They must always pursue a broken enemy.'),
 'Nomad Cavalry (Byzantium)': R('p.14', 'Mad Cavalry: tribesmen living most of their lives on horseback count as Nomad Cavalry - they benefit from the Expert Horsemen, Parthian Shot, Feigned Flight and Special Deployment rules. Special Deployment: may make a march (not fast march) or double pace move after deployment but before the battle begins; may not charge or shoot after this move.'),
 'Skirmishers (Byzantium)': R('p.15', 'Skirmishers: see the WAB rulebook (pages 54-56).'),
 'Combined Formation (Byzantium)': R('p.17', 'Combined Formation: units may mix two troop types in one unit (for example spearmen with archers in the rear ranks, or cavalry with Hippo-toxotai); the proportions and equipment limits are given in the unit entry. Not enforced.'),
 'Blunt-nosed Wedge (Byzantium)': R('p.16', 'Blunt-nosed Wedge (Kataphraktoi): a unit adopting this formation at deployment pivots instead of turning or wheeling (pivoting more than 90 degrees costs a quarter of the move unless Drilled); when it charges every model may attack and for every two models fighting one extra model in the charged unit may fight too; it flattens out if charged in the flank or rear, loses a round of combat (unless it falls back in good order) or is charged without counter-charging. No rank bonus while in wedge. Needs at least seven models.'),
 'Fear Cavalry (Camels)': R('p.83', 'Camels cause fear in enemy cavalry.'),
 'Bedouin Cavalry (Phylarch)': R('p.15', 'Bedouin Cavalry: during their move may turn any number of times without penalty and change formation once by any number of ranks without penalty, even while marching. The Phylarch must lead and may not leave a unit of Ghassanid Arab Cavalry.'),
 'Basileus (Emperor)': R('p.38', 'Emperor: Leadership 10. May only be taken in armies exceeding the points value given in the unit entry.'),
 'Excubitores': R('p.40', 'Excubitores: the Bucellarii are armed with maces and led by the Emperor (Heraclian armies).'),
 'Rusticani': R('p.41', 'Rusticani: see the Early Byzantines list.'),
 'Circus Faction Mob': R('p.43', 'Green or Blue Circus Faction mob: subject to Warband Psychology Rule 1; cannot Fall Back in Good Order, cannot benefit from the Leadership of characters other than their Faction Leader, nor use the re-roll benefit of the Army Standard.'),
 'Cane Shieldwall': R('p.47', 'Spearmen with Cane Shields may form a Cane Shieldwall (as a shieldwall).'),
 'Cataphract (Sassanid)': R('p.46', 'Sassanid Cataphracts: see the Sassanid Persians list.'),
 'Elephant (Sassanid)': R('p.48', 'Indian Elephant: see the Sassanid Persians list and the WAB rulebook.'),
 'Throne (Sassanid)': R('p.46', 'The Shahanshah\'s throne with guards: see the Sassanid Persians list.'),
 'Scythed Chariots (Sassanid)': R('p.48', 'Scythed chariots may be fielded in units of less than three models. They may not have Standards, Leaders or Musicians. A Scythed Chariot counts as three models for the calculation of unit size.'),
 'Jan-avaspar': R('p.46', 'Jan-avaspar (Shahanshah\'s guards): Leadership 9; Later Sassanid armies led by the Shahanshah.'),
 'Jurz Maces': R('p.46', 'Jurz maces count as heavy maces.'),
 'Basque Light Cavalry': R('p.53', 'Basque Light Cavalry: see the Germanic Kingdoms list.'),
 'Priest (Germanic)': R('p.53', 'Units led by a priest become Stubborn when they fight enemies of a different creed than themselves.'),
 'Great Khagan': R('p.59', 'Great Khagan: Leadership 10.'),
 'Companion (Byzantium)': R('p.82', 'Companions: units led by a Companion may re-roll failed Panic tests. The Companion is not subject to Warband Psychology.'),
 'Marzban (Byzantium)': R('p.82', 'Marzban: must lead a Khurasan Cavalry unit.'),
 'Naffatun (Byzantium)': R('p.84', 'Naffatun must be incorporated in units of City Militia skirmishers (one per unit). Their incendiary projectiles are treated like javelins with Strength 4; no armour save is allowed. A unit that receives a wound from a Naffatun must take an immediate Panic test; if it panics it flees an extra D6".'),
 'Heavy Mace': R('p.82', 'Heavy Mace: see the WAB rulebook.'),
 'Imperial Army Standard': R('p.68', 'Imperial Army Standard: +1 to the Leadership of the standard bearer (Tagmata armies).'),
 'Warband Psychology (rules 1 & 2)': R('p.83', 'Subject to Warband Psychology Rules 1 and 2.'),
 'Byzantium Common Rules': R('p.12-17', 'The minimum size of a unit is five models unless stated otherwise. One model in each unit may be upgraded to a Leader, Standard Bearer and Musician as in the WAB rulebook. Stratagem (documented): armies led by an Army General of the relevant kind may use the Stratagem special rule from the Early Byzantine chapter.'),
}
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
    RB.PUB = SPUB; RB.SRC = 'Byzantium'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Byzantium: Beyond the Golden Gate" shortName="BZ" publisher="Warhammer Historical Wargames" publicationDate="2005"/>\n  </publications>', 1)
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
        first['models'][0]['rules'].append('Byzantium Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Byzantium: Beyond the Golden Gate army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'BZ {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
