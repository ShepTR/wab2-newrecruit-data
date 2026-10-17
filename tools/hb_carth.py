# Hannibal & the Punic Wars (Warhammer Historical, 2005) - Carthaginian army list, book pp.20-27.
# Stats order M WS BS S T W I A Ld.  Book page = pdf page - 2.
from rb_data import M, U
P = '22'
CHO = [('Light armour', 3), ('Shield', 2), ('Large shield (on foot only)', 3), ('Horse', 0)]

C = []
C.append(U('Characters', 'Army General', [M('Army General', '4 5 5 4 3 3 6 2 9', 140, weapons=['Hand Weapon'], options=CHO[:3] + [('Horse (free)', 0)])],
    'Sword. Light armour +3, shield +2 or (on foot) large shield +3. May ride a horse (free). Army General. Carthaginian characters\' Leadership and Army Battle Standard re-rolls may be used by all troops in this list, including mercenaries.', mx=1, page='22'))
C.append(U('Characters', 'Army Battle Standard', [M('Army Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon'], options=CHO[:3] + [('Horse (free)', 0)])],
    'Sword. Light armour +3, shield +2 or (on foot) large shield +3. May ride a horse (free). Army Standard Bearer.', mx=1, page='22'))
C.append(U('Characters', 'Subordinate General', [M('Subordinate General', '4 4 4 4 3 2 5 2 8', 63, weapons=['Hand Weapon', 'Light Armour'], options=[('Shield', 2), ('Large shield (on foot only)', 3), ('Horse (free)', 0), ('May be Army General if none taken', 25)])],
    'Sword and light armour. Shield +2 or (on foot) large shield +3. May ride a horse (free). May be Army General if the Army General is not taken (+25 pts).', page='22'))
C.append(U('Characters', 'Mercenary General', [M('Mercenary General', '4 5 4 4 3 2 5 2 8', 85, weapons=['Hand Weapon'], options=[('Light armour', 3), ('Thrusting spear', 2), ('Shield', 2), ('Large shield', 3), ('Horse (free)', 0), ('May be Army General if none taken', 25)])],
    'Sword. Light armour +3, thrusting spear +2 and shield +2 or large shield +3. May ride a horse (free); if mounted may not have a thrusting spear or large shield. May be Army General if the Army General is not taken (+25 pts), unless otherwise specified for the period. 0-1.', mx=1, page='22'))
C.append(U('Common Troops', 'Citizen Infantry', [M('Citizen', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'])],
    'Sword, throwing spear, shield. Light Infantry. Early citizens (incl. the Sacred Band) may be heavily armoured; use the Trained African profile to represent that.', page='22'))
AF = ['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Large Shield']
C.append(U('Common Troops', 'Levy Africans', [M('Levy African', '4 2 2 3 3 1 2 1 5', 6, mn=5, weapons=AF, rules=['Levies (Hannibal)'])],
    'Sword, thrusting spear, light armour, large shield. Levies. Libyan peasant levies; may also represent hastily raised, poorly trained levies in later wars.', page='23'))
C.append(U('Common Troops', 'Trained Africans', [M('Trained African', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=AF)],
    'Sword, thrusting spear, light armour, large shield. Fought in a fairly close formation: when they charge they can fight in two ranks with their thrusting spears (front only).', page='23'))
C.append(U('Common Troops', 'Veterans', [M('Veteran', '4 4 4 3 3 1 4 1 8', 17, mn=5, weapons=AF, rules=['Stubborn'],
    options=[('Throwing spear (replaces thrusting spear)', -2), ('Drilled', 2)])],
    'Sword, thrusting spear, light armour, large shield. May replace thrusting spear with throwing spear (-2 pts). Stubborn. May be Drilled (+2 pts). When they charge they can fight in two ranks with their thrusting spears (front only).', page='23'))
C.append(U('Common Troops', 'Mercenary Hoplites', [M('Mercenary Hoplite', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Phalanx (Hannibal)'], options=[('Light armour', 1)])],
    'Sword, thrusting spear, large shield. Light armour +1. Phalanx.', page='23'))
C.append(U('Uncommon Troops', 'Peltasts', [M('Peltast', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=[('Shield (replaces buckler)', 1)])],
    'Sword, javelins, buckler. Light Infantry.', page='23'))
C.append(U('Uncommon Troops', 'Thureophoroi', [M('Thureophoros', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Thrusting spear', 1)])],
    'Sword, javelins, shield. Light Infantry.', page='23'))
C.append(U('Common Troops', 'Oscan Hoplites', [M('Oscan Hoplite', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Phalanx (Hannibal)'], options=[('Light armour', 1)])],
    'Sword, thrusting spear, large shield. Light armour +1. Phalanx. May have one unit per Oscan Warrior unit.', page='23'))
C.append(U('Common Troops', 'Oscan Warriors', [M('Oscan Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 1), ('Large shield', 2)])],
    'Sword, throwing spear, shield. Light armour +1, large shield +2. Light Infantry.', page='23'))
C.append(U('Common Troops', 'Italian Infantry', [M('Italian Spearman', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 1)])],
    'Sword, throwing spear, shield. Light armour +1. Light Infantry.', page='23'))
C.append(U('Common Troops', 'Bruttian Veterans', [M('Bruttian Veteran', '5 4 4 3 3 1 4 1 8', 14, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'])],
    'Sword, throwing spear, light armour, shield. Light Infantry.', page='24'))
C.append(U('Common Troops', 'Gallic Warriors', [M('Gallic Warrior', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'])],
    'Mixed weapons and shield. Warband. Stealth.', page='24'))
C.append(U('Common Troops', 'Gallic Veterans', [M('Gallic Veteran', '4 4 3 3 3 1 4 1 5', 10, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield', 'Light Armour'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'])],
    'Mixed weapons, shield, light armour. Warband. Stealth. (Movement 4 as printed; Gallic Warriors are M5.)', page='24'))
C.append(U('Common Troops', 'Spanish Scutarii', [M('Scutarius', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear)', 2), ('Javelins', 1), ('Light armour', 1)])],
    'Sword, throwing spear, shield. Stealth.', page='24'))
C.append(U('Common Troops', 'Spanish Caetrati', [M('Caetratus', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'])],
    'Sword, javelins, buckler. Skirmishers. May have one unit per unit of Scutarii.', page='24'))
C.append(U('Common Troops', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Dagger', 'Javelin', 'Buckler'])],
    'Knife, javelins, buckler. Skirmishers. There must be at least one unit of these skirmishers for every other skirmisher unit in the army.', page='24'))
C.append(U('Uncommon Troops', 'Punic Heavy Cavalry', [M('Punic Cavalryman', '8 3 3 3 3 1 3 1 7', 21, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'])],
    'Sword, throwing spear, light armour, shield. Uncommon in the First and Third Punic Wars, Common in the Second Punic War in Africa.', page='24'))
C.append(U('Uncommon Troops', 'Campanian Cavalry', [M('Campanian Cavalryman', '8 4 3 3 3 1 4 1 7', 20, mn=5, weapons=['Hand Weapon', 'Javelin'],
    options=[('Light armour', 2), ('Shield', 1), ('Thrusting spear (replaces javelins)', 0)])],
    'Sword and javelins. Light Cavalry. May not outnumber any other unit of cavalry in the army.', page='24'))
C.append(U('Common Troops', 'Numidian Cavalry', [M('Numidian Cavalryman', '8 3 4 3 3 1 4 1 7', 21, mn=5, weapons=['Dagger', 'Javelin', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'],
    options=[('Shield (replaces buckler)', 1)])],
    'Knife, javelins, buckler. Light Cavalry, Feigned Flight, Parthian Shot.', page='24'))
C.append(U('Uncommon Troops', 'Spanish Heavy Cavalry', [M('Spanish Heavy Cavalryman', '8 4 4 3 3 1 3 1 7', 23, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'],
    options=[('Javelins', 1), ('Thrusting spear (replaces throwing spear)', 0), ('Light armour', 2)])],
    'Sword, throwing spear, shield. May not outnumber any other unit of cavalry in the army.', page='24'))
C.append(U('Uncommon Troops', 'Spanish Light Cavalry', [M('Spanish Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], options=[('Javelins', 1)])],
    'Sword, throwing spear, buckler. Light Cavalry. May not outnumber any other unit of cavalry in the army.', page='24'))
C.append(U('Uncommon Troops', 'Gallic Cavalry', [M('Gallic Noble Cavalryman', '8 4 4 3 3 1 4 1 6', 19, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Mixed Weapons (Hannibal)'], options=[('Light armour', 2)])],
    'Mixed weapons and shield. Warband. May not outnumber any other unit of cavalry in the army.', page='25'))
EL = '4 3 3 3 3 1 3 1 7'
C.append(U('Uncommon Troops', 'Elephants', [
    M('African Elephant', '6 4 0 6 5 5 3 4 4', 120, mn=1, mx=1, key='el', options=[('Fighting tower (5+ save for crew)', 15), ('Shields on tower (+1 save for crew)', 4)]),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', EL, 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon', 'Javelin']),
    M('Third Crewman', EL, 8, mn=0, mx=1, key='crew3', weapons=['Hand Weapon', 'Javelin'])],
    'Unarmed mahout and two crew with sword and javelins. Fighting tower +15 (5+ save for crew); shields on the tower +4 (+1 save for crew); third crewman +8. Elephant: may stampede; causes fear in infantry and terror in cavalry; African elephants fear all elephants of Indian origin.', page='25'))
C.append(U('Uncommon Troops', 'Untrained Elephants', [
    M('African Elephant', '6 4 0 6 5 5 3 4 4', 90, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 5', 0, mn=1, mx=1, key='mahout')],
    'Unarmed mahout only. Elephant: may stampede; causes fear in infantry and terror in cavalry.', page='25'))
C.append(U('Uncommon Troops', 'Balearic Slingers', [M('Balearic', '5 3 4 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Warband'], options=[('Buckler', 1)])],
    'Sword and sling. Warband, Skirmishers. May not be the largest unit of infantry skirmishers in the army.', page='25'))
C.append(U('Uncommon Troops', 'Celtiberian Scutarii', [M('Celtiberian', '5 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Warband', 'Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear)', 2), ('Light armour', 1)])],
    'Sword, throwing spear, shield. Warband. Stealth.', page='25'))
C.append(U('Uncommon Troops', 'Roman Deserters', [M('Deserter', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Large Shield'], rules=['Hatred'],
    options=[('Thrusting spear', 2), ('Pilum', 3), ('Light armour', 2)])],
    'Sword and large shield. Hate Romans: apply Hatred rules 2 and 3 (WAB rulebook p.52) when fighting Republican Roman armies.', page='25'))
C.append(U('Uncommon Troops', 'Ligurian Slingers', [M('Ligurian Slinger', '5 2 3 3 3 1 3 1 6', 5, mn=5, weapons=['Sling'])],
    'Sling. Skirmishers. May not be the largest unit of infantry skirmishers in the army. Counts as Ligurian Infantry.', page='25'))
C.append(U('Uncommon Troops', 'Ligurian Warriors', [M('Ligurian Warrior', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'], options=[('Light armour', 2)])],
    'Mixed weapons and shield. Warband. Light Infantry. Stealth. Counts as Ligurian Infantry.', page='26'))
C.append(U('Uncommon Troops', 'Sardinian Archers', [M('Sardinian', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Bow'])],
    'Bow. Skirmishers. May not be the largest unit of infantry skirmishers in the army.', page='26'))
C.append(U('Uncommon Troops', 'Moorish Archers', [M('Moor', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Bow'])],
    'Bow. Skirmishers. May not be the largest unit of infantry skirmishers in the army.', page='26'))
C.append(U('Uncommon Troops', 'Artillery (Heavy Bolt Ballista)', [
    M('Heavy Bolt Ballista', '- - - - 6 2 - - -', 42, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour (per crewman)', 2), ('Large shield (per crewman)', 2)]),
    M('Third Crewman', '4 3 3 3 3 1 3 1 7', 6, mn=0, mx=1, key='crew3', weapons=['Hand Weapon'], options=[('Light armour', 2), ('Large shield', 2)])],
    'Two crew with swords; third crewman +6. Bolt Thrower as per WAB rulebook: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. One Ballista per unit of Punic Citizens or African Infantry in the army.', page='26'))

# Variants: (name, {category: (type, pct)}, composition text)
VARIANTS = [
 ('Carthaginian - First Punic War', {'Characters': ('max', 25), 'Common Troops': ('min', 50), 'Uncommon Troops': ('max', 33)},
  'Common: Levy Africans; Mercenary Hoplites; Gallic Warriors (R: Mercenary Hoplites); Spanish Infantry (R: Mercenary Hoplites); Skirmishers; Numidian Cavalry (R: Punic Heavy Cavalry).\n'
  'Uncommon: Peltasts and Thureophoroi (R: Mercenary Hoplites); Punic Heavy Cavalry; Campanian Cavalry (R: Mercenary Hoplites); Elephants; Balearic Slingers; Ligurian Infantry; Sardinian Archers; Artillery.'),
 ('Carthaginian - Second Punic War in Spain', {'Characters': ('max', 25), 'Common Troops': ('min', 50), 'Uncommon Troops': ('max', 25)},
  'The Army General may not be a Mercenary General.\n'
  'Common: Trained Africans; Gallic Warriors; Spanish Infantry; Skirmishers; Numidian Cavalry (R: Trained Africans); Celtiberian Scutarii (R: Spanish Infantry).\n'
  'Uncommon: Spanish Cavalry; Gallic Cavalry; Elephants (R: Trained Africans); Balearic Slingers; Artillery.'),
 ('Carthaginian - Second Punic War in Italy', {'Characters': ('max', 25), 'Common Troops': ('min', 50), 'Uncommon Troops': ('max', 33)},
  'The Army General may not be a Mercenary General.\n'
  'Common: Trained Africans; Veterans; Oscan Infantry; Italian Infantry; Gallic Warriors (R: Trained Africans, Veterans); Gallic Veterans (R: Trained Africans, Veterans); Spanish Infantry (R: Trained Africans, Veterans); Skirmishers; Numidian Cavalry (R: Trained Africans, Veterans, Oscan Infantry, Italian Infantry).\n'
  'Uncommon: Campanian Cavalry (R: Oscan Infantry, Italian Infantry); Spanish Cavalry; Gallic Cavalry; Elephants (R: only one, and only with Trained Africans, Veterans); Balearic Slingers; Celtiberian Scutarii (R: Trained Africans, Veterans); Roman Deserters; Ligurian Infantry; Artillery.'),
 ('Carthaginian - Second Punic War in Africa', {'Characters': ('max', 25), 'Common Troops': ('min', 50), 'Uncommon Troops': ('max', 33)},
  'The Army General may not be a Mercenary General.\n'
  'Common: Citizens; Trained Africans; Levy Africans (R: Citizens); Veterans; Oscan Infantry; Bruttian Veterans (R: Veterans); Skirmishers; Numidian Cavalry (R: Trained Africans, Levy Africans, Veterans); Punic Heavy Cavalry.\n'
  'Uncommon: Spanish Cavalry (R: Trained Africans, Veterans); Gallic Cavalry (R: Trained Africans, Veterans); Elephants; Balearic Slingers; Celtiberian Scutarii (R: Trained Africans, Veterans); Ligurian Infantry; Moorish Archers; Artillery.'),
 ('Carthaginian - Third Punic War in Africa', {'Characters': ('max', 25), 'Common Troops': ('min', 75), 'Uncommon Troops': ('max', 25)},
  'The Army General may not be a Mercenary General.\n'
  'Common: Citizens; Trained Africans; Levy Africans; Skirmishers; Numidian Cavalry (R: Trained Africans, Levy Africans).\n'
  'Uncommon: Punic Heavy Cavalry; Artillery.'),
]
CARTH_NOTES = ('CARTHAGINIAN ARMY LIST (Hannibal & the Punic Wars, pp.20-27)\n'
  'Characters up to 25% of points; at least one character must be the Army General. Common and Uncommon Troop limits and membership depend on the chosen war (force entry). "R:" means restricted: at least one unit of the listed type must be taken first (not enforced).\n'
  'Mercenary Army General: only in the First Punic War, and optionally elsewhere as listed in the unit entry.\n'
  'ALLIES (p.26; not enforced): Gallic, Sicilian Greek, Syracusan, Campanian/Bruttian/Lucanian, Samnite, Spanish, Numidian. Allies do not gain the benefit of the Army General or other Carthaginian characters.\n'
  'OPTIONAL RULES (p.27): Pikes, Un-Crewed Elephants, Mercenaries, Fortified Camp (with opponent permission).\n'
  'Mounted models may ride a horse (M8, free) or a Warhorse (M8 WS3 BS0 S3 I3 A1). All bows are composite bows with range 24".')
CARTH_RULES = {
 'Phalanx (Hannibal)': ('Hannibal p.7', 'Mercenary Hoplites fight in phalanx; as in Alexander the Great, but phalanx units may have standards and benefit from an army standard bearer. May wheel normally; may About Face and Adjust Ranks only (no Right/Left Face). May never change facing when engaged on its flank or rear. To gain phalanx combat benefits the unit must have at least 16 models and at least a +1 combat rank bonus. A phalanx may charge and still fight in two ranks to the front. All enemy attacks (shooting and hand-to-hand) against the front of a phalanx suffer -1 to hit. Mounted units (cavalry, camelry, light chariots) may not willingly charge the front of a phalanx (elephants, scythed and heavy chariots may). A unit with pikes or spears fights in two ranks only. Only one rank may fight to flank or rear. A phalanx attacking across obstacles or difficult terrain loses both combat ranks and phalanx benefits.'),
 'Levies (Hannibal)': ('Hannibal p.8', 'Levy troops fear enemy units they do not outnumber by at least 2:1. Levies do not fear other Levies, fleeing troops or skirmishers.'),
 'Stealth': ('Hannibal p.8', 'Stealthy troops may move through difficult ground (e.g. woods) and obstacles at a normal pace even if formed, but do not retain combat rank bonuses when fighting in difficult ground or across obstacles. They must be able to see their foe before charging, may not march, and pay normal movement costs when charging in difficult ground or across obstacles.'),
 'Mixed Weapons (Hannibal)': ('Hannibal p.8', 'Celtic and Gallic barbarians fought with a mix of weapons: javelins and a hand weapon (sword, axe or short spear). Troops armed with mixed weapons may re-roll any failed to-hit roll once in the first round of combat. Applies to both cavalry and foot.'),
}
