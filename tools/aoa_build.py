#!/usr/bin/env python3
"""Add the Armies of Antiquity (Warhammer Historical, 1999) army lists: 22 lists, each as its own catalogue named "(Armies of Antiquity)".
Book page = pdf page - 2. Usage: python3 aoa_build.py <outdir>   (then sh tools/aoa_all.sh <outdir> for the post-processing chain)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import aoa_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
APUB = hid('pub', 'armies of antiquity')

CW.WEAPON_MAP.update({'Pilum': 'Heavy Throwing Spear', 'Longbow': 'Long Bow', 'Two-handed Weapon': 'Double-handed Weapon'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)', 'Warband (psychology rules 1 & 2)': 'Warband Psychology (rules 1 & 2)'}
def R(page, txt): return ('Armies of Antiquity ' + page, txt)
RULES = {
 'Hittite Three-man Chariots': R('p.7', 'Hittite chariots are sturdier than those of other nations: Movement 7 and Strength 4. They may have three crewmen, or the three-man chariot may represent a two-man chariot giving a lift to a chariot runner. If the chariot model has three crewmen fixed in the chariot, use it as a three-man chariot (the runner is a permanent crew member and does not dismount): +1 Attacks and +5 pts. If the third crewman can be detached, or a runner can be placed in the chariot or on its base, transport runners as described in the rulebook; if the runner joins its chariot unit when the unit is engaged in hand-to-hand combat, any runners touching a chariot or enemy model may fight as well.'),
 'Hurrian Chariots': R('p.7', 'Hurrian, Syrian and Canaanite chariots do not suffer -1 to hit for moving while shooting.'),
 'Warriors of Legend': R('pp.8, 45', 'Generals and Heroes chosen from this list are mighty warriors of near legendary ability. They may re-roll one failed to-hit and one failed to-wound roll in each combat phase. In addition they may re-roll a failed armour save if the wound suffered is their last one remaining.'),
 'Independent Character': R('p.9', 'The character is independent: he moves and fights as a lone character and is not required to join a unit.'),
 'Terrifying Reputation': R('p.10', 'The Assyrians cause fear in all units in an enemy army with a Leadership value of 7 or less, after any modifications have been applied. This rule no longer applies once an Assyrian chariot, cavalry or infantry unit has been broken in combat.'),
 'Highly Professional (Armies of Antiquity)': R('p.10', 'The Assyrians may always choose who moves first in a battle if this would normally be decided randomly. In battles where who moves first is not determined by a dice roll, the Assyrians follow the normal rules.'),
 'Spara': R('p.12', 'Infantry units in the Persian army may be equipped with large shields called spara, stood up to form a barrier in the same way as medieval pavises. Spara bearers count as having a shield unless the spara is set up. A spara may be set up instead of the bearer moving. While set up the unit counts as being behind hard cover to its front against missile fire, and behind a defended obstacle if attacked by opponents to their front in hand-to-hand combat. The spara barrier is knocked down if the unit moves or loses a round of combat.'),
 'Parthian Shot': R('p.30', 'Nomadic cavalry make a normal move immediately after shooting. This is only allowed in the shooting phase, is not a charge reaction, and the unit may not march.'),
 'Feigned Flight': R('p.30', 'If Nomadic cavalry choose to flee or fire & flee as a charge reaction, they rally immediately at the end of their move and may reform facing in any direction. Should the charging enemy encounter them, the Nomadic cavalry are not destroyed and may instead fight in the close combat phase. Their opponents still count as charging.'),
 'Expert Horsemen': R('p.30', 'Nomadic cavalry do not suffer the -1 to hit modifier to their shooting if they moved in the same turn. This does not allow them to shoot if they charge or make a march move.'),
 'Nomad Cavalry': R('p.30', 'Special Deployment: Nomadic horse archers may make a free march move after both sides have deployed (not a charge; no shooting afterwards). Expert Horsemen, Parthian Shot and Feigned Flight apply (see those rules). Hidden Ambush Force: the Nomadic player may set up one unit in hiding, out of sight of the opponent\'s deployment zone, to be deployed at the start of his first turn.'),
 'Wedge Formation': R('p.16', 'Shock cavalry units drawn from the army list that have between five and ten models may fight in a wedge formation: one model in the first rank, two in the second, etc. The unit\'s front, flank and rear arcs are based on the models in the rear rank. As long as at least one model is in contact with the enemy, all models in the unit may fight, even if not in base contact; for every two unengaged models in the wedge that this allows to fight, one enemy model in the unit touching the wedge, but not in base contact, may fight. This applies even if the wedge is charged or attacked to the front or rear.'),
 'Phalanx (Armies of Antiquity)': R('p.14', 'As long as the unit has at least 16 models and a rank bonus of at least +1: cavalry may not charge the front of the phalanx; models in a phalanx may charge and still fight in two ranks; all enemy attacks (shooting and hand-to-hand) at the front of the phalanx suffer -1 to hit. The only formation change allowed is an about face (180 degrees). Phalanxes may wheel but may not march or charge if they do; they may slide one inch to the right when they march or charge. When reduced below 16 models or losing the rank bonus (including when attacked in the flank or rear) these rules no longer apply. The Carthaginian phalanx may have unit standards and an Army Standard Bearer (the Oracles rule does not apply).'),
 'Warband Psychology (rule 1)': R('p.15', 'Subject to Warband psychology rule 1: a D6 test at the start of each turn; 2-6 pass, on a 1 the unit surges forward towards the nearest visible enemy by at least its basic move and charges if within range.'),
 'Allies & Mercenaries (Carthaginian)': R('p.23', 'The first time a unit wishes to move, charge or shoot, roll a D6. On a 1 the unit stays stationary and may not shoot. Once a unit has passed the test it need not test again.'),
 'Shield Wall (Late Roman)': R('p.24', 'Units of heavy infantry may form a shield wall instead of moving. While in a shield wall all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer -1 to hit. The unit benefits from the shield wall as long as it does not move or lose a round of close combat.'),
 'Cataphracts (Armies of Antiquity)': R('p.26', 'Cataphract cavalry count their rank bonus, up to a maximum bonus of +3, and may not march.'),
 'City Militia (Cataphract)': R('p.27', 'Militia cause fear in all enemy troops apart from skirmishers.'),
 'Byzantine Cataphracts': R('p.29', 'Count a rank bonus of +1 when charging. May combine with Cataphract Archers (the archers making up the rear ranks; casualties are taken against the front rank models first).'),
 'Strategicon': R('p.28', 'If the army includes a General, choose one at the start of battle: Flank March (play the Flank Attack scenario with the Byzantines as the flankers); Hidden Ambush Force (one unit set up in hiding out of sight of the opponent\'s deployment zone, deployed at the start of your first turn); Scouts (your opponent must set up first).'),
 'Bedouin and Turkish Cavalry': R('p.32', 'Cavalry in the list may turn during their move without penalty and may change formation once during their move by any number of ranks with no penalty (including while marching). Bow-armed Turkish cavalry may make a normal move immediately after shooting in the shooting phase (Parthian Shot; not a charge reaction; may not march).'),
 'Huscarls (Armies of Antiquity)': R('p.34', 'A Saxon army may include a single unit of Huscarls, alone or split up and added to Fyrd units in the front rank only. While at least half (rounding up) of the front rank are Huscarls the unit is not subject to Warband psychology, has Leadership 9 and is stubborn; below 50% it is subject to Warband psychology with Leadership 6 (Select Fyrd) or 5 (Fyrd). Half of missile casualties on a combined unit fall on Huscarls; enemy models in base contact with a Huscarl must fight him. If the General is slain, Huscarls (and units where they make up at least half of the front rank) become subject to hatred for the rest of the battle.'),
 'Shield Wall (Saxon)': R('p.34', 'Units of Huscarls and Fyrd spearmen may form a shield wall instead of moving. While in a shield wall all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit, as long as the unit does not move or lose a round of close combat.'),
 'Fyrd Warband Psychology': R('p.35', 'Subject to Warband psychology unless within 12" of the army\'s General.'),
 'Viking Huscarls': R('p.37', 'Cause fear in enemy troops with Leadership of 7 or less. Different models may be armed with different weapons in the same unit. A unit of Huscarls can contain up to three Beserkers.'),
 'Beserkers': R('p.36', 'Beserkers are not hidden in the unit and are represented by ferocious models in the front rank. They may be removed as casualties at the player\'s choice. If an enemy unit is within 12" of the unit at the start of a Viking turn, roll 2D6 for each Beserker: if the roll is equal to or greater than the distance to the nearest enemy he charges immediately (automatically if the unit is within 2" of an enemy or in close combat). They always charge the closest enemy (random if tied). The Beserker causes D6 automatic Strength 5 hits and is then removed from play.'),
 'Frenzy': R('p.37', 'Frenzied.'),
 'Ferocious Charge': R('p.38', 'If a unit noted as having a ferocious charge charges and wins the round of combat, its opponent automatically breaks with no Leadership test. Enemy units that normally ignore Break tests roll a D6: on 1-3 they are broken anyway, on 4-6 they hold.'),
 'Knights Rank Bonus': R('pp.39, 43', 'May count a rank bonus of up to +1 even though cavalry.'),
 'Honourable': R('p.44', 'Samurai characters in a position to charge an enemy character must do so, and must accept a challenge issued by an enemy character (if several are eligible, any one may be chosen). Infantry units in the army may not declare a charge until after a Samurai unit has declared a charge or fought a round of combat as a defender; they may declare in the same turn, after the Samurai.'),
 'Katana': R('p.44', 'A character or Samurai armed with a katana counts as having a shield as well (it can parry), and the katana adds +1 Strength if he is on foot (a mounted Samurai uses the sword one-handed and gets no bonus). With an additional hand weapon he loses the +1 Strength bonus but may still parry. Samurai armour gives a 5+ armour save but counts as light armour for movement; a naginata is treated as a halberd on foot and a thrusting spear when mounted; Samurai count as armed with a longbow (infantry have ordinary bows). Any Samurai or Ashigaru unit may carry Sashimonos for +15 pts per unit and may re-roll a failed Break test.'),
 'Warrior Monks Dodge': R('p.45', 'Warrior monks receive a 5+ special dodge save that is not modified by the strength of their opponent\'s attack.'),
 'Ninja Scouts': R('p.45', 'Ninja scouts always set up last. They may deploy anywhere on the table outside the enemy\'s deployment zone and out of sight of the enemy.'),
 'Peasants (Samurai)': R('p.45', 'May only declare a charge if led by a Samurai Hero.'),
}

def lim_d(lim): return {c: {k: v} for c, (k, v) in lim.items()}

def comp_text(lim):
    out = ['ARMY COMPOSITION (percentages by points):']
    for c, (k, v) in lim.items():
        out.append(f"  {c}: {'at least' if k == 'min' else 'up to'} {v}%")
    return '\n'.join(out)

def main():
    RB.PUB = APUB; RB.SRC = 'Armies of Antiquity'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{APUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{APUB}" name="Armies of Antiquity" shortName="AoA" publisher="Warhammer Historical Wargames" publicationDate="1999"/>\n  </publications>', 1)
        open(gst, 'w', encoding='utf8').write(s)
    cache = os.path.join(OUT, 'tools', 'variants.json')
    variants = json.load(open(cache, encoding='utf8')) if os.path.exists(cache) else {}
    CW.clean([u for _, _, _, us, _, _, _ in D.LISTS for u in us])
    for u in [u for _, _, _, us, _, _, _ in D.LISTS for u in us]:
        for m in u['models']:
            m['rules'] = [RULE_MAP.get(r, r) for r in m['rules']]
    for key, name, fn, units, lim, notes, vs in D.LISTS:
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(lim), None)
        x = x.replace('gameSystemRevision="1"', 'gameSystemRevision="7"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Armies of Antiquity army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': f'Armies of Antiquity: {name.replace(" (Armies of Antiquity)", "")}', 'limits': lim_d(lim)}]
        print('wrote', fn, len(units), 'units')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'AoA {n}', u, {}) for k, n, fn, u, l, nt, v in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
