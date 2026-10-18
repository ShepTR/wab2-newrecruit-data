#!/usr/bin/env python3
"""Add the Armies of Chivalry (Warhammer Historical, 2004) army lists (19 lists, see ac_data.py). Book page = printed page number.
Usage: python3 ac_build.py <outdir>   (then sh tools/ac_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import ac_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'armies of chivalry')
REV = '12'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Longbow': 'Long Bow', 'Javelins': 'Javelin', 'Two-handed Weapon': 'Double-handed Weapon'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)',
            'Open Order (if no heavy armour)': 'Open Order', 'Open Order (if not combined or mixed)': 'Open Order', 'Open Order (if not in Mixed Order)': 'Open Order', 'Open Order (when not in Mixed Order)': 'Open Order',
            'Medieval Phalanx (if not in Combined Formation)': 'Medieval Phalanx', 'Eastern Shock Cavalry (if heavy armour)': 'Eastern Shock Cavalry'}
def R(page, txt): return ('Armies of Chivalry ' + page, txt)
RULES = {
 'Armies of Chivalry Common Rules': R('pp.5-15', 'UNITS: the minimum size for a unit is five models unless stated otherwise; every unit may upgrade one model to a Leader, one to a Standard Bearer and one to a Musician (+5 pts each). Units of fewer than five models, and unattached characters, that lose a round of hand-to-hand combat are broken automatically and cannot use Psychology rules. A character must be in the front rank of a unit to affect it with a psychology rule. Units subject to Frenzy cannot Flee or Fire & Flee as a charge reaction. MOVEMENT: Movement is the unencumbered rate; deduct the armour and barding penalties. OVERRUN: if all of a unit\'s opponents are slain in the first round of combat it may make a 2D6" or 3D6" Overrun move as if it had broken them (a fresh enemy is charged automatically). FALLING BACK IN GOOD ORDER: sides with overwhelming odds (over 2:1), Drilled troops, skirmishers and cavalry may fall back in good order (no panic, rally automatically, may not charge next turn). TROOP TYPES: Close Order troops use the standard movement rules and rank bonus up to +3; Open Order infantry ignore difficult terrain and obstacles (no marching while doing so), may reform at the end of their move (then cannot shoot) and get +1 rank bonus (some +2, in open ground only); Skirmishers fear formed troops (but need no Fear test to flee or fire & flee as a charge reaction). COMBINED FORMATION, MIXED ORDER, DIFFERENT WEAPONS and MEDIEVAL PHALANX: see the individual rules. ARMOUR: Light 6+ (no penalty); Heavy 5+ (-1" with a shield); Partial plate 4+ (the shield only helps on foot; -1"); Full plate 3+ on foot, 4+ mounted (-1"); mounted models gain +1 to their armour save. Pavise: counts as a large shield (+2) against missiles. BARDING (mounted only, -1" Movement): cloth +1 save in hand-to-hand; half-barding +1 save to the front facing; plate +1 save in hand-to-hand and against missiles. MEDIEVAL MASSED FIRE: the first archer or crossbowman in each file fires at full effect and half of the other archers (rounded down) may also fire; crossbowmen and handgunners may only fire if they remain stationary; in difficult terrain only the front rank fires. Light crossbow: 24", S3, move and shoot. Handgun: 24", S4 (S3 at long range), -2 (-1) save modifier, move or shoot. STAKES: negate strength bonuses for mounted attackers and First Charge; only formed units place them, at deployment or after a free 4" move. MOUNTED & DISMOUNTED: units begin the game mounted or dismounted and cannot change; both count towards the Cavalry allocation; warhorse M8 WS3 I3 A1. ARTILLERY, WAR WAGONS and WAGON TABOR: see their rules. ALLIES & MERCENARIES: see that rule. Optional rules and the campaign/scenario material of the book are not built.'),
 'Impetuous': R('p.7', 'Roll a D6 for each Impetuous unit in the Compulsory Movement phase: on a 1 it must charge the closest enemy unit in its charge arc (or move at least its base Movement towards it). Impetuous units must always pursue defeated enemies and after an Overrun, may never disengage (but may fall back in good order), and characters that join them become Impetuous.'),
 'First Charge (Chivalry)': R('p.7', 'Mounted units only: a modified Ferocious Charge. The unit automatically breaks (1) skirmishers it defeats in any charge or counter-charge, and (2) the first formed enemy unit it successfully charges or counter-charges. Later charges against formed units still count as charges but do not auto-break. Charging stakes or a defended obstacle expends the ability. Characters with the unit share the benefit; individual characters never have it.'),
 'Allies and Mercenaries (Chivalry)': R('p.7', 'Allies & Mercenaries may have a Leader, Standard and Musician, but may not benefit from the Army General or Army Battle Standard (they may be led by an appropriate character). The first time each unit moves, charges or shoots roll a D6: on a 1 it stays put (it may still defend itself); once it has acted it is moved normally. They count as part of the army for Panic tests.'),
 'Open Order': R('p.8', 'Open Order troops move by the standard rules; infantry ignore difficult terrain and obstacles (no marching), may reform at the end of their move (then they cannot shoot), and count a +1 rank bonus in open ground and difficult terrain (some units up to +2 in open ground only). Open Order cavalry only get the rank bonus given in their list.'),
 'Skirmishers (Chivalry)': R('p.8', 'Skirmish Order: individual models need their own line of sight; skirmishers fear formed troops (but need not take a Fear test to flee or fire & flee as a charge reaction). Charging a flank or rear does not cause a Panic test.'),
 'Combined Formation (Chivalry)': R('p.8', 'Units may mix troop types (archers or retainers in the rear ranks). Archers lose Open Order and are Close Order for movement and rank bonuses; missile hits use the saving throw of the majority of models in the unit; special abilities apply until no model with them remains.'),
 'Mixed Order (Chivalry)': R('p.9', 'Missile troops form the front rank(s). On entering close combat they may stay in front (and stand & shoot, with second-rank spearmen fighting) or retire to the rear (no shooting, but up to two ranks of spearmen or one of other infantry fight). Bringing them forward again takes a whole turn. The unit uses the majority Leadership, or the accompanying character\'s if higher.'),
 'Medieval Phalanx': R('p.9', 'May wheel, About Face and adjust ranks but cannot Right/Left Face or change facing when engaged on the flank or rear. With at least 16 models and a +1 rank bonus: may charge and still fight in two ranks, hand-to-hand attacks from foot troops against its front are -1 to hit (not missiles), and mounted attackers get no strength bonuses from weapons and are -2 to hit.'),
 'Mounted Infantry': R('p.9', 'May make a regular cavalry move (not march) after deployment before Turn 1; then they abandon their horses and fight as infantry.'),
 'Hatred (Tartars and Akinjis)': R('p.46', 'Hate Tartars and Akinjis.'),
 'Stubborn (if dismounted)': R('lists', 'Stubborn while on foot.'),
 'Stubborn (if with Knights)': R('lists', 'Stubborn while with a unit of Knights.'),
 'Stubborn (if led by Kniaz)': R('p.49', 'Stubborn if led by a Kniaz.'),
 'Stubborn (if with Royal Banderium)': R('p.50', 'Stubborn if with the Royal Banderium.'),
 'Stubborn (if in Mixed Order)': R('p.56', 'Crossbowmen and Handgunners in Mixed Order are Stubborn.'),
 'Arrogant Pride': R('p.34', 'If a unit containing French Knights and/or Esquires charges an enemy unit, any unit containing mounted French Knights and/or Esquires within 12" of the charging unit automatically charges its nearest enemy (or, if none is in charge distance, moves at least 4" towards the nearest enemy within its charge arc).'),
 'Keeper of the Oriflamme': R('pp.18, 58', 'The Oriflamme may be carried as the army\'s battle standard in a King-led army (+50 pts). It may only be accompanied by a unit of Gendarmes/Knights; that unit is immune to panic; if surrendered to a victorious opponent the banner is worth 250 Victory points; its powers are lost when the Battle Standard Bearer is killed.'),
 'Plançon': R('p.39', 'The plançon confers a +1 Strength bonus on all hits.'),
 'Bishop (Chivalry)': R('p.15', 'Knights, Men-at-Arms or a Combined Formation of Knights and Men-at-Arms led by a Bishop are Stubborn; Archers or Infantry led by a Bishop may re-roll failed Panic tests.'),
 'Peasants (Chivalry)': R('lists', 'Peasants/levies fear enemies they do not outnumber by at least two to one; they do not fear other peasants/levies or skirmishers.'),
 'Noble Commander (Poland)': R('p.44', 'Substituted for unit Leaders in units of Knights; roll a D6 for each before deployment: 1 Young Hotspur (+1 Attack; Impetuous roll 1 or 2); 2 Venerable Leader (Ld 9); 3 Potential Usurper (Ld 7 for him and the unit, which cannot use the General\'s Ld); 4 Defiant/Reluctant Leader (unit is subject to Allies & Mercenaries); 5 Charismatic Leader (Knights may re-roll misses once); 6 Notable Reputation (+1 WS and fear).'),
 'Superior Shock Cavalry': R('p.49', 'Superior Shock Cavalry (Junior Druzhniks): see the Eastern Shock Cavalry rule; as the army list entry.'),
 'Hidden Ambush Force': R('p.46', 'At the start of deployment units with this rule are set up in hiding anywhere on the table out of sight and not in the opposing deployment zone, writing down their positions; they deploy at the start of the player\'s first turn.'),
 'Frenzy (Religious Personality)': R('p.56', 'The Religious Personality and his unit are subject to frenzy; frenzy is lost when he dies or the unit is broken. Other Crusading Peasant units within 12" may use his Leadership.'),
 'Ghazi': R('p.52', 'Ghazis may re-roll their first failed Panic test.'),
 'Mehterhane': R('p.52', 'Must be placed in the same unit as the Army General; the unit is immune to panic and each Mehterhane model adds 1" to the General\'s Leadership radius (max +3").'),
 'Janissary Panic': R('p.53', 'Janissaries may re-roll their first failed Panic test.'),
 'Ottoman Wagon Tabor': R('p.52', 'In Conquest Ottoman armies the Janissaries may deploy inside a Wagon Tabor in place of the regular defenders; the General, the Army Standard Bearer and all Janissaries must deploy inside.'),
 'Chicken': R('p.58', 'Francs-archers fear any formed troops with a Leadership of 7 or more.'),
 'Cantonal Standards': R('p.57', 'The Gewalthut must begin the game as the largest unit in the army; while it is in good order all formed Swiss infantry within 12" may re-roll failed Break tests; it gains +1 combat results as if it had an Army Standard; if it loses its standards they are worth 300 Victory points.'),
 'Artillery (Chivalry)': R('pp.12-14', 'Light cannons (no indirect fire). Models are based singly; crew move at their basic Movement (no marching). Guns within 5" form a battery; all artillery may have a Leader but not a Standard or Musician. Characters may join a gun or battery (never harmed by a misfire). Cannons cannot fire at chargers. Artillery dice rolled twice (misfire / bounce); misfire 1-3 malfunction, 4 damp powder, 5 gunner killed and Panic, 6 destroyed. Fewer than three crew: fires every other turn. A Master Gunner may re-roll one Artillery dice misfire. A gun passed through by enemy troops is lost.'),
 'Multi-barrelled Artillery (Chivalry)': R('p.13', 'Ribaud/organ gun: template placed in front of the gun and moved D6"; models touched are hit on 4+ at Strength 4 (-1 save). Can stand & shoot when charged.'),
 'War Wagon (Chivalry)': R('p.14', 'A wagon, 2-4 horses and six crewmen (three halberd, three missile). May never charge or fast march; halved movement if it turns. Missile crew fire twice per Shooting phase (-1 if moved); crew saves +2 as a large shield or pavise; the wagon gets no save but is immune to individual missile weapons; tall - can see and be seen over low obstacles. May be single models (no Leader, Standard or Musician) or units of at least three. A tarasnices (+20 pts) fires as a carroballista.'),
 'Wagon Tabor (Chivalry)': R('p.15', 'The Tabor is deployed as one unit, placed first, with wagons up to 3" apart and the wagons at each end touching the owner\'s table edge; it may not move after deployment. Each wagon\'s defenders (5-10) are a separate unit with Different Weapons, placed in base contact, counted as inside the wagon, and cannot leave voluntarily; defenders\' armour saves are +2 as a large shield or pavise.'),
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
    RB.PUB = SPUB; RB.SRC = 'Armies of Chivalry'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Armies of Chivalry" shortName="AC" publisher="Warhammer Historical Wargames" publicationDate="2004"/>\n  </publications>', 1)
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
        first['models'][0]['rules'].append('Armies of Chivalry Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Armies of Chivalry army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'AC {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
