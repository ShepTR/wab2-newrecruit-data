# Hannibal & the Punic Wars - Republican Roman army list, book pp.51-62 (pdf = book + 2).
from rb_data import M, U
CH3 = [('Light armour', 3), ('Shield', 2), ('Large shield (on foot only)', 3), ('Horse (free)', 0)]
LEAD = 'A unit of this type may have a Leader, Standard Bearer and Musician at no cost.'
R = []
R.append(U('Characters', 'Army General', [M('Army General', '4 5 5 4 3 3 6 2 9', 145, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=CH3)],
    'Sword. Light armour +3, shield +2 or (on foot) large shield +3. May ride a horse (free). Army General, Drilled, Stubborn, Alternative Generals: after choosing the army and before deployment roll a D6: 1-2 keep this profile; 3-4 use the Political Animal; 5-6 use the Military Man (see those entries). If you do not select an Army General the commander is the character with the highest Leadership.', mx=1, page='56'))
R.append(U('Characters', 'Alternative General - Political Animal', [M('Political Animal', '4 4 4 4 3 3 4 2 8', 145, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=CH3)],
    'Equipment as for the Army General. Army General. Must always deploy first. The enemy player rolls a D6 at the start of the game: the result is the number of times he may require the Roman player to re-roll a Leadership test (no single test more than once). In compensation the Roman player receives one free Military Tribune or Prefect of the Allies (basic 69 pts, no options). Use only via the Alternative Generals roll.', mx=1, page='56'))
R.append(U('Characters', 'Alternative General - Military Man', [
    M('Military Man', '4 6 6 4 4 3 6 3 10', 145, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=CH3[:3] + [('Horse (free)', 0), ('Warhorse (replaces horse)', 0)], key='mm'),
    ],
    'Equipment as for the Army General; if mounted may ride a Warhorse instead (M8 WS3 BS0 S3 I3 A1). Army General, Drilled, Stubborn. Always deploys second. The Roman player rolls a D6 at the start of the game: the result is the number of times he may re-roll a Leadership test (no single test more than once). Use only via the Alternative Generals roll.', mx=1, page='56'))
R.append(U('Characters', 'Army Battle Standard', [M('Army Standard Bearer', '4 4 4 4 3 2 5 2 8', 80, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=CH3)],
    'Sword. Light armour +3, shield +2 or (on foot) large shield +3. May ride a horse (free). Army Standard Bearer, Drilled, Stubborn.', mx=1, page='56'))
R.append(U('Characters', 'Consul', [M('Consul', '4 5 5 4 3 3 6 2 9', 145, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=CH3)],
    'Sword. Light armour +3, shield +2 or (on foot) large shield +3. May ride a horse (free). Army General, Drilled, Stubborn. The second Consul may only be taken if the army exceeds 2,000 points and acts as a second Army General.', mx=1, page='57'))
R.append(U('Characters', 'Cavalry Prefect', [M('Praefectus Equitum', '8 5 5 4 3 2 5 2 8', 86, weapons=['Hand Weapon', 'Light Armour', 'Shield'], options=[('Throwing spear', 2)])],
    'Sword, light armour, shield. Rides a horse. A cavalry prefect only affects the Leadership of Roman and Italian Cavalry units.', mx=1, page='57'))
R.append(U('Characters', 'Military Tribune', [M('Tribune', '4 4 4 4 3 2 5 2 8', 69, weapons=['Hand Weapon', 'Light Armour'], rules=['Drilled', 'Stubborn'], options=[('Shield', 2), ('Large shield (on foot only)', 3), ('Horse (free)', 0)])],
    'Sword and light armour. Shield +2 or (on foot) large shield +3. May ride a horse (free). Drilled, Stubborn.', page='57'))
R.append(U('Characters', 'Prefect of the Allies', [M('Praefectus Socii', '4 4 4 4 3 2 5 2 8', 69, weapons=['Hand Weapon', 'Light Armour', 'Large Shield'], rules=['Drilled'], options=[('Stubborn', 3)])],
    'Sword, light armour, large shield. Drilled. May be Stubborn (+3 pts).', page='57'))
R.append(U('Common Troops', 'Leves', [M('Leves', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Javelin'], options=[('Shield', 1), ('Thrusting spear', 0)])],
    'Javelins. May have shield (+1) and thrusting spear (free). Skirmishers. There must be at least one unit of Leves in the army, unless replaced by Velites.', page='57'))
R.append(U('Common Troops', 'Hastati', [M('Hastatus', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Heavy Throwing Spear', 'Large Shield'], rules=['Manipular Unit'], options=[('Light armour', 2), ('Drilled', 2)])],
    'Sword, pilum, large shield. Light armour +2. Manipular Unit. May be Drilled (+2). May be replaced by Raw Hastati to depict hastily-raised and very young troops levied in emergencies (added by roman_fixes.py as a unit upgrade: -2 pts per model, WS 2, Ld 5). One unit of Hastati for each unit of Principes. ' + LEAD, page='57'))
R.append(U('Common Troops', 'Principes', [M('Princeps', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Manipular Unit'],
    options=[('Light armour', 2), ('Pilum (replaces thrusting spear)', 1), ('Drilled', 2), ('Stubborn', 3)])],
    'Sword, thrusting spear, large shield. Manipular Unit. One unit of Principes for each unit of Triarii (two units of Principes per Triarii after the legion reorganisation). ' + LEAD, page='57'))
R.append(U('Common Troops', 'Triarii', [M('Triarius', '4 3 3 3 3 1 3 1 8', 13, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Drilled', 'Stubborn', 'Manipular Unit'], options=[('Light armour', 2)])],
    'Sword, thrusting spear, large shield. Manipular Unit, Drilled, Stubborn. At least one unit of Triarii in the army. ' + LEAD, page='58'))
R.append(U('Uncommon Troops', 'Rorarii (use Leves profile)', [M('Rorarii', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Javelin'], options=[('Shield', 1), ('Thrusting spear', 0)])],
    'Use the Leves profile to use them as additional skirmishers (First Punic War, Uncommon).', page='58'))
R.append(U('Uncommon Troops', 'Accensi', [M('Accensus', '4 2 2 3 3 1 3 1 5', 4, mn=5, weapons=['Thrusting Spear', 'Large Shield'])],
    'Thrusting spear, large shield. Poorly equipped heavy infantry.', page='58'))
R.append(U('Common Troops', 'Velites', [M('Velite', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Throwing spear', 1)])],
    'Sword, javelins, shield. Skirmishers. Velites may not be used if any Leves, Rorarii or Accensi are used.', page='59'))
R.append(U('Common Troops', 'Roman and Italian Cavalry', [M('Cavalryman', '6 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 2), ('Javelins', 1)])],
    'Sword, throwing spear, shield. Unbridled Charge (optional rule, p.62).', page='59'))
R.append(U('Common Troops', 'Italian Spearmen', [
    M('Spearman', '5 3 3 3 3 1 3 1 7', 7, mn=5, key='sp', weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 2), ('Large shield', 1)])],
    'Sword, throwing spear, shield. Light Infantry. Portrays Latin allies before adopting Roman arms.', page='59'))
R.append(U('Common Troops', 'Italian Extraordinarii', [M('Extraordinarius', '5 4 4 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 2), ('Large shield', 1)])],
    'Sword, throwing spear, shield. Light Infantry. 0-1; may not outnumber the smallest unit of Italian Spearmen.', mx=1, page='59'))
R.append(U('Common Troops', 'Thureophoroi', [M('Thureophoros', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Thrusting spear', 1)])],
    'Sword, javelins, shield. Light Infantry. Common in the Roman Campaigns in the East only.', page='59'))
R.append(U('Common Troops', 'Peltasts', [M('Peltast', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=[('Shield (replaces buckler)', 1)])],
    'Sword, javelins, buckler. Light Infantry. Common in the Roman Campaigns in the East only.', page='59'))
R.append(U('Uncommon Troops', 'Cretan Archers', [M('Cretan', '5 3 4 3 3 1 3 1 6', 10, mn=5, weapons=['Hand Weapon', 'Bow', 'Buckler'])],
    'Sword, composite bow, buckler. Skirmishers. May not be the largest unit of infantry skirmishers in the army.', page='59'))
R.append(U('Uncommon Troops', 'Syracusan Skirmishers', [M('Syracusan', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Sling'], options=[('Buckler', 1)])],
    'Sling. Skirmishers. May not be the largest unit of infantry skirmishers in the army.', page='59'))
R.append(U('Uncommon Troops', 'Balearic Slingers', [M('Balearic', '5 3 4 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Warband'], options=[('Buckler', 1)])],
    'Sword and sling. Warband, Skirmishers. May not be the largest unit of infantry skirmishers. Not named in any army composition on pp.51-52.', page='59'))
R.append(U('Uncommon Troops', 'Tarentine Cavalry', [M('Tarentine', '8 2 4 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Feigned Flight', 'Parthian Shot'], options=[('Large shield', 1)])],
    'Sword, javelins, shield. Light Cavalry, Feigned Flight, Parthian Shot. May not outnumber any other unit of cavalry.', page='60'))
R.append(U('Uncommon Troops', 'Numidian Cavalry', [M('Numidian', '8 3 4 3 3 1 4 1 7', 21, mn=5, weapons=['Dagger', 'Javelin', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'], options=[('Shield (replaces buckler)', 1)])],
    'Knife, javelins, buckler. Light Cavalry, Feigned Flight, Parthian Shot. May not outnumber any other unit of cavalry.', page='60'))
R.append(U('Uncommon Troops', 'Spanish Infantry', [M('Scutarius', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear)', 2), ('Javelins', 1), ('Drilled', 2)])],
    'Sword, throwing spear, shield. Stealth. May be Drilled (+2).', page='60'))
R.append(U('Uncommon Troops', 'Spanish Cavalry', [M('Spanish Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], options=[('Javelins', 1)])],
    'Sword, throwing spear, buckler. Light Cavalry. May not outnumber any other unit of cavalry.', page='60'))
R.append(U('Uncommon Troops', 'Gallic Infantry', [M('Gallic Warrior', '4 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'])],
    'Mixed weapons and shield. Warband. Stealth. (Movement 4 as printed, unlike M5 in the Carthaginian list.)', page='60'))
R.append(U('Uncommon Troops', 'Gallic Cavalry', [M('Gallic Noble Cavalryman', '8 4 4 3 3 1 4 1 6', 19, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Mixed Weapons (Hannibal)'], options=[('Light armour', 2)])],
    'Mixed weapons and shield. Warband. May not outnumber any other unit of cavalry.', page='60'))
R.append(U('Uncommon Troops', 'Illyrian Infantry', [M('Illyrian Warrior', '4 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Throwing Spear', 'Shield'], rules=['Warband', 'Stealth'])],
    'Sword, javelins, throwing spears and shield. Light Infantry. Warband. Stealth.', page='60'))
R.append(U('Uncommon Troops', 'Illyrian Cavalry', [M('Illyrian Cavalryman', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband'])],
    'Sword, javelins and shield. Light Cavalry. Warband. May not outnumber any other unit of cavalry.', page='60'))
R.append(U('Uncommon Troops', 'Ligurian Infantry', [M('Ligurian Warrior', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'])],
    'Mixed weapons and shield. Warband. Light Infantry. Stealth.', page='60'))
EL = '4 3 3 3 3 1 3 1 7'
R.append(U('Uncommon Troops', 'Numidian Elephant', [
    M('African Elephant', '6 4 0 6 5 5 3 4 4', 116, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', EL, 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon', 'Javelin']),
    M('Escorts', '5 3 3 3 3 1 3 1 7', 10, mn=0, mx=10, key='esc', options=[('Sling and buckler (up to half)', 0), ('Javelin and buckler', 0)])],
    'No more than one elephant model regardless of army size. Unarmed mahout and two crew with javelins in a fighting tower (5+ save). Up to ten escorts (Light Infantry), up to half with sling and buckler, the rest javelin and buckler; escorts may not have leader, standard bearer or musician; escorts touching an enemy model may fight if they join the engaged elephant. Elephant: may stampede; causes fear in infantry and terror in cavalry.', mx=1, page='61'))

VARIANTS = [
 ('Republican Roman - First Punic War', {'Characters': ('max', 25), 'Common Troops': ('min', 75), 'Uncommon Troops': ('max', 10)},
  'Common: Leves; Hastati; Principes; Triarii; Roman and Italian Cavalry; Italian Spearmen.\nUncommon: Rorarii; Accensi.'),
 ('Republican Roman - Second Punic War in Spain', {'Characters': ('max', 25), 'Common Troops': ('min', 75), 'Uncommon Troops': ('max', 10)},
  'Common: Leves OR Velites; Hastati; Principes; Triarii; Roman and Italian Cavalry; Italian Spearmen.\nUncommon: Spanish Infantry; Spanish Cavalry (R: Roman and Italian Cavalry).'),
 ('Republican Roman - Second Punic War in Italy', {'Characters': ('max', 25), 'Common Troops': ('min', 75), 'Uncommon Troops': ('max', 10)},
  'Common: Leves OR Velites; Hastati; Principes; Triarii; Roman and Italian Cavalry; Italian Spearmen.\nUncommon: Cretan Archers; Syracusan Skirmishers; Tarentine Cavalry (R: Roman and Italian Cavalry).'),
 ('Republican Roman - Second and Third Punic Wars in Africa', {'Characters': ('max', 25), 'Common Troops': ('min', 75), 'Uncommon Troops': ('max', 5)},
  'Common: Velites; Hastati; Principes; Triarii; Roman and Italian Cavalry.\nUncommon: Syracusan Skirmishers.'),
 ('Republican Roman - Campaigns in the West', {'Characters': ('max', 25), 'Common Troops': ('min', 65), 'Uncommon Troops': ('max', 20)},
  'Common: Velites; Hastati; Principes; Triarii; Roman and Italian Cavalry.\nUncommon: Tarentine Cavalry (R: Roman and Italian Cavalry); Numidian Cavalry (R: Roman and Italian Cavalry); Spanish Cavalry (R: Roman and Italian Cavalry); Gallic Infantry; Gallic Cavalry (R: Gallic Infantry).'),
 ('Republican Roman - Campaigns in the East', {'Characters': ('max', 25), 'Common Troops': ('min', 65), 'Uncommon Troops': ('max', 20)},
  'Common: Velites; Hastati; Principes; Triarii; Roman and Italian Cavalry; Thureophoroi and Peltasts.\nUncommon: Cretan Archers; Tarentine Cavalry (R: Roman and Italian Cavalry); Numidian Cavalry (R: Roman and Italian Cavalry); Spanish Infantry; Spanish Cavalry (R: Spanish Infantry); Gallic Infantry; Gallic Cavalry (R: Gallic Infantry); Illyrian Infantry; Illyrian Cavalry (R: Illyrian Infantry); Ligurian Infantry; 0-1 Elephant.'),
]
ROMAN_NOTES = ('REPUBLICAN ROMAN ARMY LIST (Hannibal & the Punic Wars, pp.51-62)\n'
  'Characters up to 25% of points; at least one character must be the Army General. Common and Uncommon limits and membership depend on the chosen campaign (force entry). "R:" = restricted: a unit of the listed type must be taken first (not enforced).\n'
  'Unit upgrades: minimum 5 models per unit, no maximum. One model may be upgraded to Leader, Standard Bearer and Musician (+5 each), but Hastati, Principes and Triarii get them free.\n'
  'Reorganisation (use Velites instead of Leves; two units of Principes per unit of Triarii; field one Triarii unit per two Hastati and two Principes).\n'
  'Latin allies: use the Roman profiles (or Italian Spearmen for the early Republic). Allies (p.61, not enforced): Gallic Tribes (Gallic list; one northern Italian tribe, no other allies), Spanish (with Numidians only), Numidian (with Spanish only), Hellenistic Greek (Armies of Antiquity; with Pergamenes only, no Spartans), Pergamene (Alexander and his Successors list). Allies do not gain the Roman leadership benefits.\n'
  'Optional rules (p.62): Fortified Camp, Penal and Slave Legions (use Leves and Accensi entries with mixed weapons; Hate any enemy; heavy infantry cause fear; take Leadership tests to pursue/collect heads), Unbridled Charge.')
ROMAN_RULES = {
 'Manipular Unit': ('Hannibal pp.53-55', 'Hastati, principes and triarii are manipular units. Rank support: a manipular unit with a friendly manipular unit in its rear arc (part of the supporter\'s charge arc in the rear arc of the supported unit, within 4", unengaged, not fleeing, with a rank bonus and not in difficult terrain) may count the rear unit\'s rank bonus in addition to its own, up to the normal +3 maximum. No support if in column, if its own rank bonus is lost to terrain/obstacles/flank or rear charge, or if the combat includes an elephant. Formation swap: an engaged, non-fleeing manipular unit not in column may swap places at the start of the Roman turn with an unengaged friendly manipular unit completely within its rear arc, within 8" of the front of the engaged unit, that could charge the enemy; a unit may not swap if engaged to more than one facing; the replacing unit counts as charging in the next combat round. A fleeing manipular unit with a supporting unit in its rear adds +2 to its Flee roll. Panic: Principes may re-roll Panic tests caused by broken, destroyed or fleeing friendly hastati units; Triarii may re-roll Panic tests caused by hastati or principes; Roman characters on their own may re-roll Panic tests caused by hastati or principes.'),
 'Unbridled Charge': ('Hannibal p.62 (optional)', 'A Roman or Italian cavalry unit may declare an unbridled charge in lieu of an ordinary charge, only against non-cataphract enemy cavalry (not infantry, cataphracts, camels, chariots or elephants). If it wins a round of combat the charged unit breaks automatically with no Leadership test (units that ignore Break tests roll a D6: 1-3 broken, 4-6 hold). After the charge and combat the Roman cavalry must spend one turn reforming before pursuing or moving, other than fleeing. If charged while reforming it may not fall back in good order.'),
}
