#!/usr/bin/env python3
"""Add The Age of Arthur (Warhammer Historical) army lists. Book page = printed page number.
Usage: python3 arthur_build.py <outdir>   (then sh tools/arthur_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import arthur_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'arthur')
REV = '16'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Javelins': 'Javelin', 'Short bow': 'Short Bow', 'Shortbow': 'Short Bow'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('The Age of Arthur ' + page, txt)

ADV = {
 'Angones et Franciscae': ('p.17', 30, 'The character may lead a single unit of Franci or Pueri. The unit counts as armed with heavy throwing spears. Characters may not take heavy throwing spears themselves. If the character is killed, the advantage cannot be used from the next battle onwards.'),
 'Boats': ('p.18', 10, 'An army including a character with Boats can have up to three boat models (+10 pts per boat). Boats are used only if the scenario features a coastline or tidal estuary. Each boat may carry a single unit of up to 30 models (including characters); no mounted or chariot models. After both armies have deployed, before the first turn, a player using boats may land his waterborne warriors (before Concealed troops are deployed). The unit is placed on the shore touching its boat, no figure more than 6" from it. Units that have just landed move normally and may be charged; a unit forced to flee or fall back in good order into the water is destroyed. If both players have boats, roll a dice each: the highest scorer chooses whether to deploy first or second.'),
 'Born to the Purple': ('p.18', 30, 'Army General only. When the character is fielded as Army General his Leadership range is increased from 12" to 18".'),
 'Chieftain Chariot': ('p.18', 50, 'Army General only (Picts and Scots-Irish). The Chieftain rides a light chariot (see the WAB rulebook p.57; chariot stats are in the character entry). He is assumed to fulfil the roles of Army General and Army Standard Bearer (the army may not also take a separate Army Standard Bearer). His Leadership range and the Battle Standard range are increased from 12" to 18" (cannot be increased further by a Bard). If he dismounts from the chariot he is only a normal Army General with a 12" range and the Army Standard ability is lost.'),
 'Fabricae': ('p.18', 15, 'Any units of Milites, Pedyt, Duguth, Geoguth, Frankish Milites and Pueri in the character\'s army may have Light Armour at +2 points per model. If the character is killed, Fabricae cannot be used to provide armour from the next battle onwards.'),
 'Fearsome Blow': ('p.18', 20, 'Once per game the character can declare he is using the Fearsome Blow in combat (before any character attacks). His attacks are made at +1 Strength. They cannot be made in conjunction with any re-roll ability (Veteran, Saxon Buckler, Throwing Spear) but can be used with a Strength benefit from a particular weapon such as a heavy throwing spear. Cannot be used in the same round as Hail of Blows or Salmon Leap.'),
 'Finest Armour': ('p.19', 15, 'The character and any one unit that he leads may exchange their Light Armour for Heavy Armour (only units that already have Light Armour can do this). Units wearing heavy armour and carrying shields have their movement reduced by 1". If the character is killed, Finest Armour cannot be fielded by the unit from the next battle onwards.'),
 'Finest Horses': ('p.19', 20, 'The character and any one mounted unit that he leads may exchange their Horses (Move 7") for Finest Horses (Move 8"). Only units that already have Horses can do this. If the character is killed, Finest Horses cannot be fielded by the unit from the next battle onwards.'),
 'Goad': ('p.19', 15, 'Once per game the character can declare that he is using Goad when issuing a challenge (WAB rulebook p.42). The goading character can specify which enemy character he wishes to fight. The challenged character can only refuse if he passes a Leadership test on 3D6; otherwise he must accept the challenge and fight. If he successfully refuses he must retire to the rear ranks as usual.'),
 'Hail of Blows': ('p.19', 20, 'Once per game the character can declare he is using Hail of Blows in combat (before any character attacks). He attacks with an extra two attacks, but all his attacks are made with a -1 to hit modifier. Cannot be made in conjunction with any re-roll ability (Veteran, Saxon Buckler, Throwing Spear). Cannot be used in the same round as Fearsome Blow or Salmon Leap.'),
 'Javelin Hurling': ('p.19', 10, 'Once per game, in the Shooting phase, the character may hurl three javelins (declared before his shooting attack): range 8", Strength 3. Cannot be combined with any re-roll ability (e.g. Veteran). May be used as a stand & shoot response if charged (each javelin still at -1 to hit). Cannot be used in the same round as Piercing Dart.'),
 'Knight Commander': ('p.19', 20, 'The character may lead a mounted unit. The unit can claim a Rank Bonus of up to +1 in combat and loses its Light Cavalry status. If he leaves the unit or is slain the Rank Bonus is lost and the unit reverts to normal Light Cavalry (except when he leaves the unit to fight a single combat; the bonus is restored if he rejoins).'),
 'Loyalty': ('p.20', 40, 'Army General only. The character may lead a single unit. This unit becomes Stubborn (WAB rulebook p.53). Only formed infantry units may use the Stubborn ability (not in skirmish formation or mounted). If the character leaves the unit or is slain the Stubborn ability is lost (restored if he rejoins after a single combat).'),
 'Man of the People': ('p.20', 40, 'Army General only. All units in the army (including skirmishers, but not allies) may take all their Leadership tests as if they had a Leadership of 7 (they may use their own Ld if it is higher). All other normal Leadership rules apply (only units within 12" can use the General\'s Leadership and the Battle Standard; Break tests are still taken with the usual modifiers). Lost instantly if the character is slain; a Man of the People who flees the field regains the advantage in time for the next game.'),
 'Mounted Raider': ('p.20', 20, 'The character may lead a Light Cavalry unit. This unit can use the Feigned Flight ability: if the cavalry choose to flee or fire & flee as a charge reaction they rally immediately at the end of their move and may reform facing in any direction. If the charging enemy encounters them they are not destroyed and may fight in the Close Combat phase; their opponents still count as charging. Lost if the character leaves the unit or is slain (restored after a single combat if he rejoins).'),
 'Piercing Dart': ('p.20', 5, 'Once per game, in the Shooting phase, the character may hurl a single javelin that strikes with Strength 5 and a -2 saving throw modifier, range 8". Declared before the shooting attack; cannot be combined with any re-roll ability. Only one javelin may be thrown. May be used as a stand & shoot response (-1 to hit). Cannot be used in the same round as Javelin Hurling.'),
 'Professional': ('p.20', 25, 'The character may lead a single unit. This unit becomes Drilled (WAB rulebook p.120). It cannot use the Drilled ability in skirmish formation. Lost instantly if the character leaves the unit or is slain (restored after a single combat if he rejoins).'),
 'Salmon Leap': ('p.20', 15, 'Once per game, in the Close Combat phase and before any To Hit dice are rolled, the character leaps into the air and strikes first, regardless of charging or Initiative. He makes all his attacks before his opponent. Cannot be used in conjunction with any re-roll ability (Veteran, Throwing Spear). Cannot be used in the same round as Hail of Blows or Fearsome Blow.'),
 'Veteran': ('p.20', 10, 'Once per game the character may re-roll all his To Hit dice, either for combat or for shooting. He must re-roll all his dice (not just the misses) and must abide by the re-roll.'),
}
RULES = {
 'Allies (Arthur)': R('p.15', 'Allied units may be led only by certain characters from their own list and get no benefit from the Army General or Army Standard Bearer. The first time an allied unit moves, charges or shoots, roll a D6 for reliability: on a 1 the unit remains stationary until a 2-6 is rolled; on a 2+ it is reliable for the rest of the game.'),
 'Bard (Arthur)': R('p.15', 'A Bard may re-roll ONE failed Panic test per battle. He may accompany the Army General, adding D6" to the General\'s command range while within 2".'),
 'Christian Priest (Arthur)': R('p.15', 'Christian Priest: the unit he leads may re-roll any failed Panic test throughout the battle (and must abide by the re-roll).'),
 'Pagan Priest (Arthur)': R('p.16', 'Pagan Priest: the unit he leads becomes Stubborn and Fierce, even if mounted.'),
 'Concealment (Arthur)': R('p.15', 'Concealed units are placed after all on-table enemy units, anywhere not within 12" of an enemy unit. They may never take a free 4" skirmisher move.'),
 'Fierce (Arthur)': R('p.15', 'Fierce: as Warband Rule 2, but the unit fails on a 1 or 2. A Fierce unit must always pursue.'),
 'Mixed Weapons (Arthur)': R('p.15', 'Mixed weapons count as javelins and hand weapons. The unit may re-roll failed to-hit rolls in the first round of each combat.'),
 'Shieldwall (Arthur)': R('p.16', 'Shieldwall: -1 to be hit from the front while stationary and not losing a combat round.'),
 'Skirmishers (Arthur)': R('p.27', 'Skirmishers fight in skirmish formation (WAB rulebook).'),
 'Run for the Woods (Arthur)': R('p.39', 'Any unit with Run for the Woods may re-roll any failed Leadership or Break test taken in woods or difficult terrain. Even if the unit is only partially in the woods or difficult terrain it is still allowed. A failed Leadership test may not be re-rolled more than once (for example if the Army Standard is present).'),
 'Saxon Buckler': R('p.48', 'Figures armed with a Saxon Buckler and fighting on foot may re-roll all unmodified to-hit rolls of 1 (cannot be combined with any other re-roll benefits; available in any round of combat; mounted troops cannot use it offensively). Saxon Bucklers confer a +1 save modifier in close combat for all troops (like an ordinary buckler, only skirmishers may use it against missile fire). Infantry with Saxon Bucklers are always Light Troops and have a Movement characteristic of 5.'),
 'The Age of Arthur Common Rules': R('p.14', 'The minimum size of a unit is five models unless stated otherwise. One model in each unit may be upgraded to a Leader, Standard Bearer and Musician (+5 pts each) as listed. Percentage limits are by points. Ponies: M6, pursue/flee 2D6; Horses: M7, pursue/flee 3D6; Finest Horses: M8 (Character Advantage only). Warband rule 1: close-combat rank bonus is added to the Leadership of the unit (+1 per rank after the first up to +3). Warband rule 2: roll a D6 at the start of each turn: on a 1 the unit surges forward and charges. Warbands use their own Leadership or that of a character. Allied units are documented only (see Allies).'),
}
for n, (pg, c, txt) in ADV.items(): RULES[n + ' (Arthur)'] = R(pg, f'Character Advantage ({c} pts): ' + txt)
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
    RB.PUB = SPUB; RB.SRC = 'The Age of Arthur'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="The Age of Arthur" shortName="AA" publisher="Warhammer Historical Wargames" publicationDate="2005"/>\n  </publications>', 1)
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
        first['models'][0]['rules'].append('The Age of Arthur Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the The Age of Arthur army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'AA {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
