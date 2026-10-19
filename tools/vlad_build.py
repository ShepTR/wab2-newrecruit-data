#!/usr/bin/env python3
"""Add the Vlad the Impaler (Warhammer Historical, 2007) army lists. Book page = printed page number.
Usage: python3 bz_build.py <outdir>   (then sh tools/vlad_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import vlad_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'vlad')
REV = '15'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Javelins': 'Javelin', 'Two-handed Weapon': 'Double-handed Weapon', 'Kontarion': 'Kontos', 'Full Plate': 'Full Plate Armour', 'Partial Plate': 'Partial Plate Armour', 'Composite Bow': 'Bow', 'Sword': 'Hand Weapon'})
RULE_MAP = {'Frenzy (Religious Personality)': 'Frenzy (Religious Personality)', 'Army General': 'Army General (Chariot Wars)', 'Expert Horsemen (if mounted)': 'Expert Horsemen', 'Feigned Flight (if mounted)': 'Feigned Flight', 'Warband Psychology (rules 1 & 2)': 'Warband Psychology (rules 1 & 2)'}
def R(page, txt): return ('Vlad the Impaler ' + page, txt)
RULES = {
 'Crusader (Vlad)': R('p.131', 'Crusader Arrogant Pride: French and Burgundian Crusaders came to the Balkans with strong ideas about how battle should be conducted. If a unit containing knights of any nationality declares a charge against an enemy unit, any friendly unit subject to Crusader Arrogant Pride within 12" of the charging unit will automatically charge their nearest enemy (or, if no such unit is within charge distance, they will move at least 4" towards the nearest enemy unit within their charge arc). This is to prevent their colleagues from gaining an advantage in military prowess and glory.'),
 'Athlete of Christ': R('p.16', 'János Hunyadi: troops under his command trust his judgment and ability implicitly. In armies he leads, no Allies and Mercenaries tests are required for allied troops deployed within his 12" command radius at the start of battle; they are considered to have automatically passed this test and may move as normal for the rest of the battle.'),
 'Leader of the Black Army': R('p.16', 'King Mátyás I Corvinus: the Black Army must be built from a New Men army list; at least 25% of its total must be taken from the Allies and Mercenaries list and up to 35% may be. The Black Army must take one War Wagon for every 1,000 points, and 2+ units of Hussite Handgunners. Mercenary troops in a Black Army led by Corvinus are not bound by the Allies and Mercenaries special rule if deployed within his 12" command radius at the start of battle.'),
 'Strategist': R('p.132', 'After choosing sides, a player fielding an army with the Strategist special rule may place one additional terrain feature anywhere on the battlefield outside the enemy deployment zone.'),
 'Scythe': R('p.27', 'A farm implement used expertly by Romanian peasants, the scythe is a double-handed weapon. Scythe-armed models gain a +1 to hit bonus against cavalry. At the same time, cavalry attacking them are at -1 to hit.'),
 'Grim Reputation': R('p.30', 'Vlad (but not his bodyguard) causes fear in enemy troops.'),
 'Pagan Hatred': R('p.30', 'Vlad has Hatred against Ottoman troops and their allies.'),
 'Loyal Bodyguard': R('p.30', 'Vlad has learned to trust no one and thus does not join any unit except his loyal bodyguard of foreign mercenaries. Vlad must be accompanied by a unit of Garda Domneasca who have Ld 8, are Veterans and wear partial plate armour at a basic cost of 16 pts for a dismounted guard model and 30 pts for a mounted guard model. Additional equipment may be bought as normal.'),
 'Beloved Leader': R('p.30', 'Stefan\'s popularity among the people and the army has never been matched by any Romanian ruler since. His Ld radius as Army General is increased by D6", roll at the start of the battle, before deployment.'),
 'Resilient': R('p.30', 'Stefan was a veteran of many campaigns and received numerous wounds. To show his resiliency, his Wounds value has been increased by 1, but the effects of his wounds and his small stature (only 5\'5") is reflected in his decreased Strength and Toughness values.'),
 'Master of Ambushes': R('p.30', 'If Stefan is the army\'s General, the 0-2 restriction for Plaiesi/Darabanti is lifted.'),
 'Permanent Mercenaries': R('p.132', 'Byzantine armies had so many mercenaries in them that it was hard for contemporary observers to find the native Greek soldiers. All units subject to the Allies and Mercenaries rule may be upgraded to Permanent Mercenaries for +2 points per model (the cost is stated in the unit entry). Permanent Mercenary units increase their Leadership value by +1. Furthermore, they automatically pass the Allies and Mercenaries test they would otherwise be required to take at the beginning of their first turn. Although they are Permanent Mercenaries, they are still mercenaries and cannot use the Leadership value of the Army General or the re-roll benefit of the Army Standard Bearer.'),
 'The Padişah is Dead!': R('p.38', 'If the Padişah is killed, each unit in the army takes its Panic test at -1 to its Leadership.'),
 'Kapikulu': R('p.38', 'Kapikulu, literally Slaves of the Gate, are a completely professional body. Kapikulu units may re-roll their first failed Panic test.'),
 'Mehterhane': R('p.38', 'If used, Mehterhane models must be deployed together and with the Army General. The Mehterhane and Army General may accompany a unit, but while the Army General must be placed in the front rank of the unit, the Mehterhane bandsmen - unlike other characters - may occupy the back rank of the unit if it has multiple ranks. As long as the General and Mehterhane remain with the unit, the unit led by the General and including the band is immune to panic, and each Mehterhane model in the unit adds +1" to the Leadership radius of the Army General up to a maximum of +4".'),
 'Ottoman Artillery': R('p.38', 'All artillery pieces in the Ottoman army may take a Master Gunner for only 20 pts per Cannon.'),
 'Ditch & Stakes': R('p.37', 'Ottoman units that purchase Ditch & Stakes will be -2 to hit by cavalry and their mounts in close combat. All enemy units that break an Ottoman unit behind Ditch & Stakes fortifications must subtract D6 from their pursuit roll. If a unit with Ditch & Stakes moves outside the fortification for any reason, they lose the benefits, but may attempt to retake the fortification and use them again. Azabs and certain Kapikulu units may purchase Ditch & Stakes for the front of their units only (barricade) or fully encircled (stockade). Several Kapikulu and Azab units may be deployed adjacent to each other and then combine their stockades as one fortification, but they still count as separate units. Ditch & Stakes barricades and stockades do not count as defended obstacles; units fighting over them retain their ranks and are still vulnerable to flank or rear attack. They are placed when a unit is initially deployed and must be represented by suitable models. Ditch & Stakes may not be moved once deployed.'),
 'Gazi (Vlad)': R('p.37', 'In an Ottoman Gazi State army, any infantry or cavalry unit may upgrade to Gazis for +1 pt per model. Gazis were religious warriors flush with the prospect of victory and as such may re-roll their first failed Panic test.'),
 'Grenadoes': R('p.131', 'Some armies of the period used incendiary grenades. Regardless of how many grenades a unit has purchased, it may only make a maximum of one grenade attack per the controlling player\'s Shooting phase. Grenades may not be used as part of a stand & fire or fire & flee charge response. Grenade: range 4", save modifier -2, Strength 4. Any model in the unit may be nominated as a grenadier. No To hit roll is made; the burst of the grenade covers 3" across (use the 3" template). The model directly under the centre hole is automatically hit. Models whose bases lie under the rest of the template are hit on a D6 roll of 4+. If more than half a model\'s base lies under the template it is considered to be fully under the template. Before rolling your To wound dice, roll a D6 - on a roll of 1, the Grenade is a dud and no one has been wounded; on a 6 the grenade has gone off in the thrower\'s face: roll to wound as normal, but with the template placed around the throwing model.'),
 'Guard Archers': R('p.131', 'Some bodyguard units that are limited in size have been designated Guard Archers. In these units, all figures may fire if the unit did not move during its Movement phase.'),
 'Heavy Artillery': R('p.131', 'Heavy artillery cannot be turned or pivoted, and is therefore restricted to only the 45 degree field of fire it has at time of deployment. Heavy artillery confers D6 wounds. Heavy artillery is a large target.'),
 'Mantlets': R('p.132', 'Mantlets confer a 5+ armour save to the gun and add +2 to the crew\'s armour save against missile attacks coming from the front arc of the artillery piece only. As mantlets are part of a fixed emplacement, any gun protected by a mantlet is restricted to the 90 degree field of fire it has at time of deployment (or 45 degrees in the case of Heavy Artillery) and may not pivot or be moved.'),
 'Stone Thrower': R('p.132', 'Stone Thrower. Range 60". Once deployed, these weapons may not be turned and may only shoot forward in a straight line, down the centre of the model.'),
 'Thunderbolt': R('p.43', 'Bayezit\'s legendary speed gives him and his escort extra movement on the charge. When Bayezit and any cavalry unit he accompanies charges, you may add D6" to their charge move. If the charge fails, Bayezit and his unit move forward at half their regular charge rate.'),
 'Protect the Sultan at all Costs': R('p.43', 'Mehmet is a great leader, but as the head of the Empire, his presence on the battlefield is an inherent risk. His viziers are mindful of this, and they have surrounded the Sultan with the best troops available. If taken, Mehmet must be deployed within a designated bodyguard unit - either Solaks or Kapikulu Suvarileri.'),
 'The Mighty': R('p.71', 'Stefan Dušan earned his nickname in combat as an expert fighter skilled in the use of the lance. He must re-roll his lance attacks once every battle; he must re-roll all dice and abide by the result of the re-roll.'),
 'Wealthy (Dušan)': R('p.71', 'Stefan Dušan inherited his family\'s wealth, which he compounded through taxing the output of Serbia\'s silver mines and collecting tribute from his Empire\'s member states. The restriction of this troop type is lifted; up to 100% of the mercenary allowance may be spent on Mercenary Knights.'),
 'Leader of the Resistance': R('p.80', 'Skanderbeg is leading a war of resistance against the Ottoman Empire, and his army is highly motivated, and trying to gain their independence. When fighting against Ottoman armies, Stradioti may always use Skanderbeg\'s Leadership, even if they are in skirmish formation.'),
 'Leader of the True Faith': R('p.90', 'As the leader of the Orthodox Christian Empire, Konstantinos is an inspiring presence. He allows any one non-allied or mercenary unit to automatically pass one Panic test per game - no dice roll is required.'),
 'Embodiment of the State': R('p.90', 'If Konstantinos is slain, each unit in the Byzantine army and all allied and mercenary units take the resultant Panic test at -1 to their Leadership.'),
 'Desperation': R('p.90', 'When Longo led the Byzantine army, they fought the most desperate, and last, fight in the Empire\'s life. All mercenaries under Longo knew that there was no retreat from the Turks; therefore all allied and mercenary troops count as being Permanent Mercenaries in armies led by Longo and automatically pass their Allies and Mercenaries tests when fighting against Ottomans.'),
 'The Devotion of his Men': R('p.90', 'As long as Longo led them, the troops were determined to stay by his side. If Longo is killed or leaves the field, all allies and mercenaries take their Panic test at -1 to their Leadership.'),
 'Almughavars!': R('p.97', '1. Almughavar units not designated as Skirmishers are Open Order, and may claim up to a +2 rank bonus when in open terrain. 2. They ignore any opponent\'s save bonuses for being mounted in close combat (barding still applies as normal). 3. Almughavars receive an unmodified 6+ save when in open terrain, improving to an unmodified 5+ save if the model is in difficult or very difficult terrain. 4. Almughavars may perform Feigned Flight. 5. Formed Almughavar units may re-roll failed Panic tests until the first formed Almughavar unit fails a re-roll; after that, the ability is lost for the remainder of the game.'),
 'Impressed Archers': R('p.98', 'Any Panic test that results in a natural roll of higher than a 7 is a failure regardless of character influence.'),
 'Vlad the Impaler Common Rules': R('p.131-132', 'The minimum size of a unit is five models unless stated otherwise. One model in each unit may be upgraded to a Leader, Standard Bearer and Musician as in the WAB rulebook. Units described as Allies and Mercenaries are subject to the Allies and Mercenaries rule. Mangonel (all lists): Stone Thrower, range 60", three crewmen with hand weapon (two additional crewmen +10 pts each, crew may have light armour +2 pts). Optional medieval rules (Deployment by Battles, Battle Leaders and others on pp.133-134) are not built.'),
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
    RB.PUB = SPUB; RB.SRC = 'Vlad the Impaler'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Vlad the Impaler" shortName="VL" publisher="Warhammer Historical Wargames" publicationDate="2007"/>\n  </publications>', 1)
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
        first['models'][0]['rules'].append('Vlad the Impaler Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Vlad the Impaler army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'VL {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
