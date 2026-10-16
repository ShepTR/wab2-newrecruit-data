#!/usr/bin/env python3
"""Add the Hannibal & the Punic Wars army lists (Carthaginian, Republican Roman, Spanish, Numidian, Ligurian, Gallic)
to an existing output folder. Usage: python3 hb_build.py <outdir>   (run after build_wab2.py and rb_build.py)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import hb_carth as HC, hb_roman as HR, hb_others as HO
B = RB.B
hid, q = B.hid, B.q
OUT = RB.OUT
HPUB = hid('pub', 'hannibal')

CLARIFY = ('Hannibal p.106-109 (Rules Clarifications, also published in Spartacus and Armies of Chivalry). Summary:\n'
 'UNITS: minimum size is five models unless stated; one model per unit may be a Leader, Standard Bearer and Musician (+5 each). Units under five models that lose a round of combat are broken automatically and cannot use Psychology rules. For a character to affect a unit by Psychology he must be in the front rank or engaged as part of that unit. Units subject to frenzy cannot flee or fire and flee as a charge reaction.\n'
 'CHARACTERS: unattached characters that lose a round of combat automatically break and flee but may rally normally. A character attached to a unit reduced below five models that flees cannot rally. A character may not join an engaged unit (he may charge into the combat) and may not charge an enemy in the rear if he starts his move in front of it.\n'
 'LEADERSHIP & WARBAND: if a Warband unit is joined by a character without Warband Psychology the unit uses either its own Ld or the character\'s, not both, and adds the Warband rank bonus. Warband rule 1 characters and cavalry may count a rank bonus up to 3 for a maximum Leadership of 10 (light troops count up to two ranks); no rank bonus means no benefit.\n'
 'CAVALRY COUNTER CHARGES: a charge reaction only for cavalry charged to the front by enemy cavalry. The unit counts as charging for weapon effects but does not move or strike first; cavalry with a move of less than 6" (e.g. cataphracts) cannot counter charge; cavalry cannot counter charge infantry. Camelry and light chariots count as cavalry. Also counts as charging for Ferocious Charge and Warband.\n'
 'REFORMING IN COMBAT: a unit fighting to its flank or rear may reform at the end of the Close Combat phase if it did not break and is not engaged on another facing; it faces the engaging unit with its centre in base contact. A reformed unit loses its rank bonus if charged by an enemy unit with five or more models.\n'
 'COMBINED FORMATION (not used in Hannibal lists): archers lose Light Troop status, may use Massed Archery, may stand and shoot or fire and flee; missile hits use the majority saving throw and casualties are removed in roughly equal proportions; in close combat hits fall on models in contact.\n'
 'FEROCIOUS CHARGE (not used in Hannibal lists): winning a round of combat makes opponents break automatically (Break-immune units roll a D6: 1-3 broken, 4-6 hold). FEIGNED FLIGHT: cavalry that flee or fire and flee as a charge reaction rally at the end of their move and may reform facing any direction; the charging enemy still counts as charging. PARTHIAN SHOT: a normal move immediately after shooting, in the Shooting phase only, not a charge reaction, and the unit may not march.\n'
 'MOVEMENT: movement values are unencumbered; deduct armour and barding penalties. Reforming units cannot move more than double their move. Disengaging: move away in a straight line ending with the rear facing the enemy; units fighting to more than one facing cannot disengage. Copses and orchards are difficult terrain for formed units (skirmishers unaffected); shooting through or at targets within suffers -1 to hit.\n'
 'SHOOTING: all models in a unit on an elevated position can shoot and be targeted by all models in a shooting unit (Massed Archery rules apply to missile weapons in these situations unless agreed otherwise). Crew models aboard elephants, chariots and war-wagons suffer -1 to hit for moving unless stated. Heavy and Scythed Chariots are large targets (+1 to hit).\n'
 'HAND-TO-HAND: weapons that fight in two ranks do so only to the front. Skirmishing units charging the flank or rear cause no Panic test and do not negate rank bonuses but gain the +1/+2 flank/rear combat result; skirmishers get no unit standard bonus and no musician roll-off. A unit in clear ground fighting an enemy in difficult terrain only loses rank bonus if its models are in contact with enemy models in the difficult ground.\n'
 'OVERRUN: if all of a unit\'s opponents are slain in the first round of close combat it may make an Overrun move (2D6" or 3D6" by Movement value) as if it had broken them. An overrun into a fresh enemy is a new charge (fear/terror tests apply) and combat is resolved next turn with charge bonuses.\n'
 'FALLING BACK IN GOOD ORDER: if one side outnumbers the other by over 2:1 (models, calculated at the end of the combat) and the outnumbering side loses and fails its Break test, it falls back in good order instead of fleeing. Drilled troops, skirmishers and cavalry that lose and pass their Break test may also fall back in good order. Exceptions to a flee: no Panic test for friends within 12"; rally automatically at the end of the move (a unit that was fighting to its flank or rear cannot reform); may be pursued (pursuers count as having charged next combat phase); may not charge next turn but may move and shoot; lost if it falls off the table; units may also fall back from a First Charge or Ferocious Charge.')
EXTRA = {
 'Mixed Armour (Hannibal)': ('Hannibal p.8', 'Some units have figures with different armour. In close combat use the Saving roll of the wounded figure. Against missile fire use the Saving roll of the majority of the figures in the unit. The owner of the unit decides which figures to remove as casualties.'),
 'Hannibal Rules Clarifications': ('Hannibal pp.106-109', CLARIFY),
 'Hannibal Common Rules': ('Hannibal pp.7-8', 'What you see is what you get: models must show the options taken unless the opponent agrees otherwise. Mounted models may ride a horse (Movement 8" before armour penalties) or, where stated, a Warhorse (M8 WS3 BS0 S3 I3 A1). All bows in the army lists are composite bows with a range of 24".'),
}

ARMIES = [
 ('Carthaginian (Hannibal)', HC.C, HC.VARIANTS, HC.CARTH_NOTES, HC.CARTH_RULES, 'Carthaginian_Hannibal.cat'),
 ('Republican Roman (Hannibal)', HR.R, HR.VARIANTS, HR.ROMAN_NOTES, HR.ROMAN_RULES, 'Republican_Roman_Hannibal.cat'),
 ('Spanish (Hannibal)', HO.SP, HO.SP_VARIANTS, HO.SP_NOTES, {}, 'Spanish_Hannibal.cat'),
 ('Numidian (Hannibal)', HO.NU, HO.NU_VARIANTS, HO.NU_NOTES, {}, 'Numidian_Hannibal.cat'),
 ('Ligurian (Hannibal)', HO.LG, HO.LG_VARIANTS, HO.LG_NOTES, {}, 'Ligurian_Hannibal.cat'),
 ('Gallic (Hannibal)', HO.GL, HO.GL_VARIANTS, HO.GL_NOTES, {}, 'Gallic_Hannibal.cat'),
]

def comp_text(variants):
    out = ['ARMY COMPOSITIONS:']
    for vn, lim, txt in variants:
        out.append(f'[{vn}]')
        for k, (t_, v) in lim.items():
            out.append(f"  {k}: {'at least' if t_ == 'min' else 'up to'} {v}%")
        out.append('  ' + txt.replace('\n', '\n  '))
    return '\n'.join(out)

def main():
    RB.PUB = HPUB; RB.SRC = 'Hannibal'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{HPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{HPUB}" name="Hannibal and the Punic Wars" shortName="HPW" publisher="Warhammer Historical Wargames" publicationDate="2005"/>\n  </publications>', 1)
        open(gst, 'w', encoding='utf8').write(s)
    rules = dict(EXTRA)
    forces = []
    for name, units, variants, notes, arules, fn in ARMIES:
        rules.update(arules)
        full = notes + '\n\n' + comp_text(variants)
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(RB.build_cat(name, units, full, None))
        for vn, lim, txt in variants:
            forces.append((f'Hannibal: {vn}', units, lim))
        print('wrote', fn, len(units), 'units,', len(variants), 'force entries')
    RB.patch_gst(gst, forces, rules)
    print('patched gst with', len(forces), 'force entries and', len(rules), 'rules')

if __name__ == '__main__':
    main()
