# Armies of Antiquity (Warhammer Historical, 1999) army lists. Book page = pdf page - 2. Percentages are by points.
# Model stats order: M WS BS S T W I A Ld
from rb_data import M, U
LISTS = []     # (key, display name, catalogue file, units, limits, notes, variants-or-None)

# ------------------------------------------------------------------ SUMERIAN (book pp.2-3)
SU = []
SU.append(U('Characters', 'General', [M('General', '4 5 5 4 3 3 6 2 9', 145, weapons=['Hand Weapon', 'Javelins', 'Light Armour'], rules=['Army General'], options=[('Ride in a four-ass heavy chariot (cost of chariot extra)', 0)])],
    'Hand weapon, javelins and light armour. May ride in a four-ass heavy chariot bought at additional cost from the list. Any unit within 12" of the General may use his Leadership. 0-1.', mx=1, page='3'))
SU.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 78, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'])],
    'Hand weapon and light armour. Any unit within 12" of the Army Standard may re-roll any failed Break tests. 0-1.', mx=1, page='3'))
SU.append(U('Chariotry', 'Chariots', [M('4-Ass Chariot', '6 4 4 3 3 1 4 1 8', 30, weapons=['Hand Weapon', 'Light Armour'], rules=['Onager Chariots'], options=[('Javelins', 2)])],
    'One crewman armed with hand weapons and light armour riding in a heavy chariot pulled by four wild asses (onagers), with a driver. The crewman may throw javelins (+2). Special rule: Onagers.', page='3'))
SU.append(U('Infantry', 'Royal Guard', [M('Royal Guard', '4 4 3 3 3 1 4 1 8', 13, mn=5, weapons=['Double-handed Weapon', 'Light Armour'], options=[('Throw sticks', 1)])],
    'Double-handed weapon and light armour. May have throw sticks (+1 pt). 0-1 unit.', mx=1, page='3'))
SU.append(U('Infantry', 'Spearman', [M('Spearman', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], options=[('Light armour (Ur-style)', 2), ('Large shield (Lagash-style)', 2)])],
    'Hand weapon and thrusting spear. Ur-style spearmen may have light armour (+2); Lagash-style spearmen may have large shields (+2). Akkadians may be armed in either fashion.', page='3'))
SU.append(U('Infantry', 'Akkadian Archers', [M('Archer', '4 2 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[])],
    'Hand weapon and bow. Light Infantry.', page='3'))
SU.append(U('Infantry', 'Javelin Men', [M('Javelin man', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[])],
    'Nicknamed Nim (flies). Hand weapon and javelins. Skirmishers.', page='3'))
SU.append(U('Infantry', 'Peasant Slingers', [M('Slinger', '4 2 2 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=[])],
    'Hand weapon and sling. Skirmishers.', page='3'))
SU.append(U('Allies & Tribal Mercenaries', 'Amorites', [M('Amorite', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins', 'Buckler'], rules=['Warband (psychology rules 1 & 2)'])],
    'Hand weapon, javelins and buckler. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='3'))
SU.append(U('Allies & Tribal Mercenaries', 'Gutians', [M('Gutian', '5 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Double-handed Weapon', 'Javelins'], rules=['Warband (psychology rules 1 & 2)'])],
    'Double-handed weapons and throw sticks (count as javelins). Light Infantry. Subject to Warband psychology rules 1 & 2.', page='3'))
SU.append(U('Allies & Tribal Mercenaries', 'Tribal Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=[], options=[('Sling instead of short bow', 0)])],
    'Hand weapons and short bow or sling. Skirmishers.', page='3'))
SU.append(U('Allies & Tribal Mercenaries', 'Elamites', [M('Elamite', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[])],
    'Hand weapon and bow. Light Infantry.', page='3'))
SU_LIM = {'Chariotry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Tribal Mercenaries': ('max', 25)}
SU_NOTES = ('SUMERIAN ARMY LIST (Armies of Antiquity, pp.2-3), Sumerian and Akkadian armies, c.3000-2000 BC.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Chariotry up to a quarter of the points; Infantry at least a quarter; Allies & Tribal Mercenaries up to a quarter.\n'
  'Special rules: Throw sticks (same effect as a javelin) and Onagers (see the rule).')
LISTS.append(('SU', 'Sumerian (Armies of Antiquity)', 'Sumerian_Armies_of_Antiquity.cat', SU, SU_LIM, SU_NOTES, None))

RATIOS = []    # (list key, unit, [limiting units], per)   "A may be taken once per `per` units of B"
PAIRS = []     # (list key, [units], tag)                  0-1 across several units

# ------------------------------------------------------------------ ANCIENT EGYPTIAN (book pp.4-5)
EG = []
EG.append(U('Characters', 'Army General', [M('General', '4 5 5 4 3 3 6 2 9', 150, weapons=['Hand Weapon', 'Bow', 'Javelin', 'Shield', 'Light Armour'], rules=['Army General'], options=[('Ride in a light chariot with a driver (cost of chariot extra)', 0)])],
    'Hand weapon, bow, javelin, shield and light armour. May ride in a light chariot with a driver (bought at additional cost from the list). 0-1.', mx=1, page='5'))
EG.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 78, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Ride in a light chariot with a driver (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. May ride in a light chariot with a driver (bought at additional cost from the list). 0-1.', mx=1, page='5'))
EG.append(U('Chariotry', 'Chariots', [M('Light Chariot', '8 4 4 3 4 1 4 2 8', 40, weapons=['Hand Weapon', 'Bow', 'Javelins', 'Shield', 'Light Armour'], rules=['Egyptian Charioteers'])],
    'One crewman armed with bow, javelins, shield and light armour riding in a two-horse light chariot with driver. Egyptian charioteers do not suffer -1 to hit for shooting on the move and are able to shoot as they charge.', page='5'))
EG.append(U('Chariotry', 'Chariot Runners', [M('Chariot Runner', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=['Chariot Runners (Chariot Wars)'])],
    'Hand weapons, javelins and shield. Light Infantry. Your army may include up to one unit of chariot runners for each unit of chariots. If the runners join the chariot unit when it is engaged in hand-to-hand combat, any runners touching a chariot or enemy model may fight as well.', page='5'))
EG.append(U('Infantry', 'Shock Troops', [M('Shock Troop', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Double-handed weapon instead of throwing spear', 2), ('Light armour', 2)])],
    'Khepesh (sickle sword), axe, mace or other hand weapon, throwing spear and shield. May have a double-handed weapon such as a mace-axe instead of a throwing spear (+2 pts). May have light armour (+2 pts). Types include spearmen, mace-axe men and khepesh men.', page='5'))
EG.append(U('Infantry', 'Archers', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Light armour', 2)])],
    'Hand weapon and bow. May have light armour (+2 pts).', page='5'))
EG.append(U('Infantry', 'Marines', [M('Marine', '4 4 4 3 3 1 4 1 8', 11, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Light armour', 3), ('Javelins and shield instead of bow', 1)])],
    'Hand weapon and bow. May have light armour (+3 pts). May have javelins and shield instead of a bow (+1 pt). A unit of Marines may be made up entirely of javelin men or archers or include both, in which case the unit counts as being armed with the weapons carried by the majority of the unit at the start of the battle.', page='5'))
EG.append(U('Allies & Mercenaries', 'Sea Peoples Sherden Guard', [M('Sherden Guard', '5 4 3 3 3 1 3 1 7', 13, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband', 'Stubborn'], options=[('Javelins', 1), ('Light armour', 3)])],
    'Sword and shield. May have javelins (+1 pt) and light armour (+3 pts). Warband. Sherden Guards are stubborn. 0-1 unit.', mx=1, page='5'))
EG.append(U('Allies & Mercenaries', 'Sea Peoples Warriors', [M('Warrior', '5 4 3 3 3 1 3 1 5', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'], options=[('Javelins', 1), ('Light armour', 3)])],
    'Sword and shield. May have javelins (+1 pt) and light armour (+3 pts). Warband.', page='5'))
EG.append(U('Allies & Mercenaries', 'Nubian Skirmishers', [M('Nubian', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=[])],
    'Hand weapon and short bow. Skirmishers.', page='5'))
EG.append(U('Allies & Mercenaries', 'Libyan Skirmishers', [M('Libyan', '5 3 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=[], options=[('Javelins instead of short bow', 0)])],
    'Hand weapon and short bow. Libyans may have javelins instead of short bows. Skirmishers.', page='5'))
EG.append(U('Allies & Mercenaries', 'Syrian Skirmishers', [M('Syrian', '5 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=[], options=[('Javelins instead of short bow', 0)])],
    'Hand weapon and short bow. Syrians may have javelins instead of short bows. Skirmishers.', page='5'))
EG_LIM = {'Chariotry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)}
EG_NOTES = ('ANCIENT EGYPTIAN ARMY LIST (Armies of Antiquity, pp.4-5), the New Kingdom (XVIII-XX Dynasties), c.1570-1080 BC.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Chariotry up to a quarter of the points; Infantry at least a quarter; Allies & Mercenaries up to a quarter.\n'
  'Chariot Runners: up to one unit of runners for each unit of chariots.')
LISTS.append(('EG', 'Ancient Egyptian (Armies of Antiquity)', 'Egyptian_Armies_of_Antiquity.cat', EG, EG_LIM, EG_NOTES, None))
RATIOS.append(('EG', 'Chariot Runners', ['Chariots'], 1))

# ------------------------------------------------------------------ HITTITE (book pp.6-7)
HT = []
HT.append(U('Characters', 'General', [M('General', '4 6 6 4 4 3 6 4 9', 190, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour'], rules=['Army General'], options=[('Shield', 2), ('Ride in a Hittite chariot (cost of chariot extra)', 0)])],
    'Hand weapon, thrusting spear and light armour. May have a shield (+2 pts). May ride in a Hittite chariot (bought at an additional cost from the list).', page='7'))
HT.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 5 5 4 4 2 5 3 8', 98, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Shield', 2), ('Ride in a Hittite chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. May have a shield (+2 pts). May ride in a Hittite chariot (bought at an additional cost from the list). 0-1.', mx=1, page='7'))
HT.append(U('Chariotry', 'Hittite Chariotry', [M('3-Man Chariot', '7 4 4 4 4 1 4 2 8', 47, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Light Armour'], rules=['Hittite Three-man Chariots'], options=[('Javelins', 3), ('Third crewman fixed in the chariot (+1 A)', 5)])],
    'One or two crewmen armed with thrusting spear, shield and light armour, riding in a two-horse light chariot with a driver. Crew may have javelins (+3 pts). May have three crew (see Hittite Three-man Chariots): a fixed third crewman adds +1 Attacks and +5 pts.', page='7'))
HT.append(U('Chariotry', 'Hurrian, Syrian & Canaanite Chariotry', [M('2-Man Chariot', '8 4 4 3 4 1 4 2 7', 35, weapons=['Hand Weapon', 'Bow', 'Shield', 'Light Armour'], rules=['Hurrian Chariots'], options=[('Thrusting spear', 3), ('Javelins', 3)])],
    'One crewman armed with bow, shield and light armour, riding in a two-horse light chariot with a driver. The crewman may have a thrusting spear (+3 pts) and javelins (+3 pts). Hurrian, Syrian and Canaanite chariots do not suffer -1 to hit for moving while shooting.', page='7'))
HT.append(U('Chariotry', 'Chariot Runners', [M('Chariot Runner', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Chariot Runners (Chariot Wars)'])],
    'Hand weapons and javelins. Light Infantry. If any runners join a two-man chariot unit when it is engaged in hand-to-hand combat, any runners touching a chariot or enemy model may fight as well.', page='7'))
HT.append(U('Infantry', 'Hittite Guards', [M('Guard', '4 4 3 3 3 1 4 1 7', 11, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Double-handed weapon instead of thrusting spear and shield', 0)])],
    'Hand weapon, thrusting spear and shield, or double-handed weapon. 0-1 unit.', mx=1, page='7'))
HT.append(U('Infantry', 'Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], options=[('Shield', 1)])],
    'Hand weapon and thrusting spear. May have shields (+1 pt).', page='7'))
HT.append(U('Infantry', 'Syrian or Hurrian Archers', [M('Archer', '4 2 3 3 3 1 2 1 6', 6, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[])],
    'Hand weapon and bow. Light Infantry.', page='7'))
HT.append(U('Allies & Mercenaries', 'Lukka Mercenaries', [M('Lukka', '5 4 3 3 3 1 3 1 6', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'], options=[('Javelins', 1), ('Light armour', 3)])],
    'Sword and shield. May have javelins (+1 pt) and light armour (+3 pts). Subject to Warband psychology.', page='7'))
HT.append(U('Allies & Mercenaries', 'Habiru Mercenaries', [M('Habiru', '5 4 4 3 3 1 3 1 6', 9, mn=5, weapons=['Hand Weapon', 'Javelins', 'Buckler'], rules=[])],
    'Hand weapon, javelins and bucklers. Light Infantry.', page='7'))
HT.append(U('Allies & Mercenaries', 'Phoenician Light Infantry', [M('Phoenician', '4 3 4 3 3 1 3 1 6', 8, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[], options=[('Bows', 2)])],
    'Hand weapon and javelins. May have bows (+2 pts). Light Infantry.', page='7'))
HT.append(U('Allies & Mercenaries', 'Syrian Light Infantry', [M('Syrian', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[], options=[('Bows', 2)])],
    'Hand weapon and javelins. May have bows (+2 pts). Light Infantry.', page='7'))
HT.append(U('Allies & Mercenaries', 'Anatolian or Aramaean Tribal Scouts', [M('Anatolian/Aramaean', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[], options=[('Short bows instead of javelins (no cost)', 0), ('Bucklers (Aramaeans with javelins)', 1)])],
    'Hand weapon and javelins. May have short bows instead of javelins at no additional points cost. Aramaeans armed with javelins may have bucklers (+1 pt). Skirmishers.', page='7'))
HT.append(U('Allies & Mercenaries', 'Shosu Skirmishers', [M('Shosu', '5 2 3 3 3 1 3 1 4', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[])],
    'Hand weapon and javelins. Skirmishers. Shosu may not have short bows.', page='7'))
HT.append(U('Allies & Mercenaries', 'Slingers', [M('Slinger', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=[])],
    'Hand weapons and a sling instead of any other options. Skirmishers.', page='7'))
HT_LIM = {'Chariotry': ('min', 25), 'Infantry': ('max', 50), 'Allies & Mercenaries': ('max', 50)}
HT_NOTES = ('HITTITE ARMY LIST (Armies of Antiquity, pp.6-7), also usable for Mitannian, Syrian, Canaanite or Hyksos armies.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Chariotry at least a quarter of the points; Infantry up to half; Allies & Mercenaries up to half.\n'
  'Hittite three-man chariots: Movement 7, Strength 4. A chariot may have three crew (+1 Attacks, +5 pts) or carry a chariot runner as a passenger.')
LISTS.append(('HT', 'Hittite (Armies of Antiquity)', 'Hittite_Armies_of_Antiquity.cat', HT, HT_LIM, HT_NOTES, None))

# ------------------------------------------------------------------ TROJAN WAR (book pp.8-9)
TW = []
TW.append(U('Characters', 'General', [M('General', '4 6 6 4 4 3 6 4 9', 191, weapons=['Hand Weapon', 'Thrusting Spear', 'Heavy Armour'], rules=['Army General', 'Warriors of Legend'], options=[('Ride in a two-horse light chariot (cost of chariot extra)', 0), ('Change equipment to sword, javelins, light armour and shield', 0)])],
    'Sword, thrusting spear and heavy armour. May ride in a two-horse light chariot (bought at an additional cost from the list). May change equipment to sword, javelins, light armour and shield. Army General. Warriors of Legend. The army must have a General.', mx=1, page='9'))
TW.append(U('Characters', 'Heroes', [M('Hero', '4 5 5 4 4 1 5 2 8', 50, weapons=['Hand Weapon', 'Thrusting Spear', 'Heavy Armour'], rules=['Warriors of Legend'], options=[('Ride in a two-horse light chariot (cost of chariot extra)', 0), ('Change equipment to sword, javelins, light armour and shield', 0)])],
    'Sword, thrusting spear and heavy armour. May ride in a two-horse light chariot (bought at an additional cost from the list). May change equipment to sword, javelins, light armour and shield. Independent Characters. Warriors of Legend.', page='9'))
TW.append(U('Chariotry', 'Eqeta Chariot Warriors', [M('Eqeta', '8 4 4 3 4 1 4 2 8', 39, weapons=['Hand Weapon', 'Thrusting Spear', 'Javelins', 'Light Armour', 'Shield'], options=[('Heavy armour', 2)])],
    'One crewman armed with thrusting spear, javelins, light armour and shield riding in a two-horse light chariot with driver. Crewman may have heavy armour (+2 pts).', page='9'))
TW.append(U('Infantry', 'Tereta Spearmen', [M('Spearman', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Warband'], options=[('Change equipment to sword, javelins, light armour and shield', 1)])],
    'Sword, thrusting spear and a large shield. May change equipment to sword, javelins, light armour and shield (+1 pt). Subject to Warband psychology. Archers may be mixed into a spearmen unit armed with thrusting spears, one archer for every three spearmen (see the rule; not modelled).', page='9'))
TW.append(U('Infantry', 'Javelin Men', [M('Javelin man', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Warband'], options=[('Bucklers', 1)])],
    'Dagger and javelins. May have bucklers (+1 pt). Light Infantry. Subject to Warband psychology.', page='9'))
TW.append(U('Infantry', 'Archers', [M('Archer', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Warband'])],
    'Hand weapon and short bow. Light Infantry. Subject to Warband psychology.', page='9'))
TW.append(U('Infantry', 'Slingers', [M('Slinger', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=[])],
    'Hand weapon and sling. Skirmishers.', page='9'))
TW.append(U('Allies & Mercenaries', 'Lukka Pirates', [M('Lukka Pirate', '5 4 3 3 3 1 3 1 6', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'], options=[('Javelins', 1), ('Light armour', 2)])],
    'Sword and shield. May have javelins (+1 pt) and light armour (+2 pts). Subject to Warband psychology.', page='9'))
TW.append(U('Allies & Mercenaries', 'Libyans', [M('Libyan', '5 2 3 3 3 1 3 1 7', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[], options=[('Short bow instead of javelins', 0)])],
    'Hand weapon and javelins. May have short bow instead of javelins. Skirmishers.', page='9'))
TW_LIM = {'Characters': ('max', 25), 'Chariotry': ('max', 50), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)}
TW_NOTES = ('TROJAN WAR ARMY LIST (Armies of Antiquity, pp.8-9), for Mycenaean Greek, Minoan Cretan or Trojan armies (a Sea Peoples army can be made with modification).\n'
  'Characters: the army must have a General and may have up to a quarter of its points in Hero characters, including the General. Chariotry up to half; Infantry at least a quarter; Allies & Mercenaries up to a quarter.\n'
  'Archers mixed into spearmen units: one archer for every three spearmen (25%), counted as part of the spearmen unit, all shielded (not modelled: all models in a unit are equipped alike).')
LISTS.append(('TW', 'Trojan War (Armies of Antiquity)', 'Trojan_War_Armies_of_Antiquity.cat', TW, TW_LIM, TW_NOTES, None))

# ------------------------------------------------------------------ ASSYRIAN EMPIRE (book pp.10-11)
AS = []
AS.append(U('Characters', 'General', [M('General', '4 5 5 4 4 3 6 4 10 '.strip(), 200, weapons=['Hand Weapon', 'Bow', 'Light Armour'], rules=['Army General', 'Terrifying Reputation', 'Highly Professional (Armies of Antiquity)'], options=[('Ride in a heavy chariot (cost of chariot extra)', 0), ('Extra shield bearer in chariot (+1 Attacks, per chariot)', 5)])],
    'Sword, bow and light armour. May ride in a heavy chariot (bought at an additional cost from the list). May have an extra shield bearer in the chariot adding +1 to Attacks (+5 pts per chariot). 0-1.', mx=1, page='11'))
AS.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 4 2 4 3 9', 95, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Ride in a heavy chariot (cost of chariot extra)', 0), ('Extra shield bearer in chariot (+1 Attacks, per chariot)', 5)])],
    'Sword and light armour. May ride in a heavy chariot (bought at an additional cost from the list). May have an additional shield bearer in the chariot adding +1 Attacks (+5 pts per chariot). 0-1.', mx=1, page='11'))
AS.append(U('Chariotry & Cavalry', 'Heavy Chariots', [M('Heavy Chariot', '6 4 4 4 4 2 4 4 8', 60, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Light Armour', 'Bow'], rules=['Chariot Archers (Assyrian)'], options=[('Extra crewman (+1 Attacks)', 5), ('Darts (siltabi, count as javelins)', 2)])],
    'Two crew armed with thrusting spear, shield and light armour riding in a four-horse heavy chariot with driver. One crewman has a bow. May have an extra crewman adding +1 Attacks (+5 pts per chariot). Archer may have darts (siltabi, count as javelins), kept in quivers at the front of the chariot (+2 pts). Archers do not suffer -1 to hit for shooting on the move.', page='11'))
AS.append(U('Chariotry & Cavalry', 'Royal Guard Cavalry (Qurubuti)', [M('Royal Guard Cavalryman', '8 4 4 3 3 1 4 1 9', 34, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Bow', 'Light Armour'], rules=[])],
    'All armed with spears, bow, light armour and barding. Models in a unit can have different weapon combinations. Archers in the second rank may shoot at full effect as long as the unit does not move. 0-1 unit.', mx=1, page='11'))
AS.append(U('Chariotry & Cavalry', 'Assyrian Cavalry', [M('Assyrian Cavalryman', '8 4 4 3 3 1 4 1 8', 23, mn=5, weapons=['Hand Weapon', 'Light Armour'], rules=[], options=[('Half the unit with bows', 3), ('Half the unit with thrusting spears', 2)])],
    'Sword and light armour. Half the unit is armed with bows (+3 pts), the other half with thrusting spears (+2 pts). Models in a unit can have different weapon combinations. Archers in the second rank may shoot at full effect as long as the unit does not move.', page='11'))
AS.append(U('Infantry', 'Heavy Infantry', [M('Assyrian', '4 3 3 3 3 1 3 1 8', 14, mn=5, weapons=['Hand Weapon', 'Light Armour'], rules=['Stubborn'], options=[('Large shields (spearmen)', 1)])],
    'Half the unit may have swords, light armour and bows, the other half swords, light armour, thrusting spears and shields. Spearmen may have large shields (+1 pt). Models in a unit can have different weapon combinations. Archers in the second rank may shoot at full effect as long as the unit does not move. The unit is stubborn.', page='11'))
AS.append(U('Infantry', 'Siege Troops', [M('Siege Troop', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Light Armour'], rules=['Heavy Slingers'], options=[('Pavises instead of shields', 1)])],
    'Sword and light armour. Archers armed with bow and shield bearers armed with large shields. A unit includes equal numbers of both types. Shield bearers may swap shields for pavises (+1 pt). Models in a unit can have different weapon combinations. Archers in the second rank may shoot at full effect as long as the unit does not move. If shield bearers swap shields for pavises use the rules for Spara from the Achaemenid Persians list.', page='11'))
AS.append(U('Infantry', 'Armoured Archers & Slingers', [M('Armoured Archer/Slinger', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Light Armour'], rules=['Heavy Slingers'], options=[('Bows', 2), ('Slings', 1)])],
    'Sword and light armour. Archers can have bows (+2 pts). Slingers can have slings (+1 pt). A unit may contain archers and slingers in equal proportions or have separate units that are entirely archers or entirely slingers. Armoured slingers in the second rank may shoot at full effect as long as the unit does not move. Slingers may fire even if not in skirmish formation.', page='11'))
AS.append(U('Auxiliaries', 'Aramaeans', [M('Aramaean', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Warband'], options=[('Half the unit with bows instead of spear and shield', 0)])],
    'Half the unit has swords, thrusting spear and shields; the other half have swords and bows. Subject to Warband psychology. Models in a unit can have different weapon combinations. Archers in the second rank may shoot at full effect as long as the unit does not move.', page='11'))
AS.append(U('Auxiliaries', 'Urartians, Neo-Hittites, Phrygians & Mannai', [M('Urartian etc', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Warband'])],
    'Sword, thrusting spear and shield. Subject to Warband psychology.', page='11'))
AS.append(U('Auxiliaries', 'Tribal Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=[], options=[('Short bows instead of slings', 0), ('Javelins and bucklers instead of sling or bow', 0)])],
    'Hand weapon and sling. May have short bows instead of slings. May have javelins and bucklers instead of sling or bow. Skirmishers.', page='11'))
AS.append(U('Allies & Mercenaries', 'Cimmerians or Scythians', [M('Cimmerian', '8 3 3 3 3 1 3 1 5', 16, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[])],
    'Sword and bow. Light Cavalry. 0-1 unit.', mx=1, page='11'))
AS.append(U('Allies & Mercenaries', 'Arab Camel Riders', [M('Arab Camelry', '8 2 3 3 3 2 3 2 5', 16, mn=5, weapons=['Short Bow'], rules=['Camels'])],
    'Each camel has two riders armed with short bows. Camels cause fear in cavalry and chariots. 0-1 unit.', mx=1, page='11'))
AS_LIM = {'Chariotry & Cavalry': ('max', 50), 'Infantry': ('min', 25), 'Auxiliaries': ('max', 50), 'Allies & Mercenaries': ('max', 25)}
AS_NOTES = ('ASSYRIAN EMPIRE ARMY LIST (Armies of Antiquity, pp.10-11), from the reforms of Tiglath Pileser III to the fall of Nineveh.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Chariotry & Cavalry up to half the points; Infantry at least a quarter; Auxiliaries up to half; Allies & Mercenaries up to a quarter.\n'
  'Special rules: Terrifying Reputation (fear in enemy units with Ld 7 or less until an Assyrian chariot, cavalry or infantry unit breaks) and Highly Professional (the Assyrians choose who moves first if it would be random).')
LISTS.append(('AS', 'Assyrian Empire (Armies of Antiquity)', 'Assyrian_Armies_of_Antiquity.cat', AS, AS_LIM, AS_NOTES, None))

# ------------------------------------------------------------------ ACHAEMENID PERSIANS (book pp.12-13)
PE = []
PCH = lambda extra=(): [('Light armour', 3), ('Warhorse', 4), ('Barding (-1 M)', 4), ('Ride in a light chariot (cost of chariot extra)', 0)] + list(extra)
PE.append(U('Characters', 'Army General', [M('General', '4 3 5 3 3 3 5 2 9', 128, weapons=['Hand Weapon', 'Bow'], rules=['Army General'], options=PCH([('Thrusting spear', 1), ('Javelins', 2)]))],
    'Hand weapon and bow. May have light armour (+3 pts), thrusting spear (+1 pt), javelins (+2 pts). May ride in a light chariot (bought at an additional cost from the list) or be on a warhorse (+4 pts); if on a warhorse it may have barding (+4 pts). 0-1.', mx=1, page='12'))
PE.append(U('Characters', 'Army Standard', [M('Standard on foot', '4 3 4 3 3 2 5 2 9', 65, weapons=['Hand Weapon'], rules=['Army Standard'], options=PCH())],
    'Hand weapon. May have light armour (+3 pts). May ride in a light chariot (bought at an additional cost from the list) or be on a warhorse (+4 pts); if on a warhorse it may have barding (+4 pts). 0-1.', mx=1, page='12'))
PCAV = [('Light armour', 3), ('Shield', 2), ('Thrusting spear', 2), ('Bow', 3), ('Barding (-1 M)', 4)]
PE.append(U('Persian Troops', 'Guard Cavalry', [M('Guard Cavalryman', '8 4 4 3 3 1 4 1 8', 22, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Stubborn'], options=PCAV)],
    'Hand weapons and javelins. May have light armour (+3 pts), shield (+2 pts), thrusting spear (+2 pts), bow (+3 pts), barding (+4 pts). Every second cavalry unit may be Guard Cavalry. Guards and units with barding count rank bonus of up to +1 when charging. Guards are stubborn.', page='13'))
PE.append(U('Persian Troops', 'Persian Cavalry', [M('Persian Cavalryman', '8 3 4 3 3 1 4 1 8', 18, mn=5, weapons=['Hand Weapon', 'Javelins'], options=PCAV)],
    'Hand weapons and javelins. May have light armour (+3 pts), shield (+2 pts), thrusting spear (+2 pts), bow (+3 pts), barding (+4 pts). Units with barding count rank bonus of up to +1 when charging.', page='13'))
PINF = [('Thrusting spear', 1), ('Bow', 2), ('Shield', 1), ('Light armour', 2), ('Spara (replaces shield)', 1)]
PE.append(U('Persian Troops', 'Immortals / Guard Infantry', [M('Immortal/Guard', '4 4 4 3 3 1 4 1 8', 10, mn=5, weapons=['Hand Weapon'], rules=['Stubborn', 'Spara'], options=PINF)],
    'Hand weapons. May have thrusting spear (+1 pt), bow (+2 pts), shield (+1 pt), light armour (+2 pts). Shields may be replaced with spara (+1 pt). Models in the unit can have different weapon combinations; archers in the second rank may shoot at full effect as long as the unit does not move. Immortals/Guard are stubborn.', page='13'))
PE.append(U('Persian Troops', 'Persian Infantry', [M('Persian Infantry', '4 3 3 3 3 1 3 1 7', 5, mn=5, weapons=['Hand Weapon'], rules=['Spara'], options=PINF)],
    'Hand weapons. May have thrusting spear (+1 pt), bow (+2 pts), shield (+1 pt), light armour (+2 pts). Shields may be replaced with spara (+1 pt). Models in the unit can have different weapon combinations; archers in the second rank may shoot at full effect as long as the unit does not move.', page='13'))
PLEV = [('Light armour', 1), ('Shield', 1), ('Thrusting spear', 1), ('Bow', 2), ('Barding (-1 M)', 2)]
PE.append(U('Levies & Mercenaries', 'Bactrian / Noble Shock Cavalry', [M('Bactrian/Noble Cavalryman', '8 4 4 3 3 1 4 1 8', 17, mn=5, weapons=['Hand Weapon', 'Javelins'], options=PLEV)],
    'Hand weapons and javelins. May have light armour (+1 pt), shield (+1 pt), thrusting spear (+1 pt), bow (+2 pts), barding (+2 pts). Bactrians/Nobles and units with barding count rank bonus of up to +1 when charging. All levies & mercenaries are subject to fear against all enemy units they do not outnumber by at least 2 to 1.', page='13'))
PE.append(U('Levies & Mercenaries', 'Shock Cavalry', [M('Shock Cavalryman', '8 3 3 3 3 1 3 1 5', 13, mn=5, weapons=['Hand Weapon', 'Javelins'], options=PLEV)],
    'Hand weapons and javelins. May have light armour (+1 pt), shield (+1 pt), thrusting spear (+1 pt), bow (+2 pts), barding (+2 pts). Units with barding count rank bonus of up to +1 when charging.', page='13'))
PE.append(U('Levies & Mercenaries', 'Scythian / Dahae Skirmish Cavalry', [M('Scythian/Dahae Cavalryman', '8 2 4 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Javelins', 'Bow'], rules=['Parthian Shot'], options=[('Shield', 1)])],
    'Knife and javelins; Scythians/Dahae must be armed with bows. May have shield (+1 pt). Skirmishers. Parthian Shot.', page='13'))
PE.append(U('Levies & Mercenaries', 'Skirmish Cavalry', [M('Skirmish Cavalryman', '8 2 3 3 3 1 3 1 5', 13, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Parthian Shot'], options=[('Bow', 2), ('Shield', 1)])],
    'Knife and javelins. May have bow (+2 pts), shield (+1 pt). Skirmishers. Parthian Shot (only units armed with bows can use it).', page='13'))
PE.append(U('Levies & Mercenaries', 'Levy Infantry', [M('Levy Infantry', '4 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon'], rules=['Spara'], options=[('Thrusting spear', 1), ('Bow', 2), ('Shield', 1), ('Light armour', 2), ('Spara (replaces shield, +1/2 pt)', 1)])],
    'Hand weapons. May have thrusting spear (+1 pt), bow (+2 pts), shield (+1 pt), light armour (+2 pts). Shields may be replaced with spara (+1/2 pt per model; entered here as +1 pt, the nearest whole point). Models in the unit may be armed with different weapon combinations; archers in the second rank may shoot at full effect as long as the unit does not move.', page='13'))
PLI = [('Thrusting spear', 1), ('Double-handed weapon', 1)]
PE.append(U('Levies & Mercenaries', 'Marines', [M('Marine', '4 2 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], options=PLI + [('Bow instead of javelins and shield', 0)])],
    'Armed with javelins and shield, or bow. May have thrusting spears (+1 pt) or double-handed weapons (+1 pt). Light Infantry.', page='13'))
PE.append(U('Levies & Mercenaries', 'Light Infantry', [M('Light Infantry', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], options=PLI + [('Bow instead of javelins and shield', 0)])],
    'Armed with javelins and shield, or bow. May have thrusting spears (+1 pt) or double-handed weapons (+1 pt). Light Infantry.', page='13'))
PE.append(U('Levies & Mercenaries', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], options=[('Bow instead of javelins and shield', 0), ('Sling (no extra cost)', 0)])],
    'Armed with javelins and shield, or bow. Skirmishers may use slings at no extra cost. Skirmishers.', page='13'))
PE.append(U('Special Troops', 'Light Chariots', [M('Light Chariot', '8 3 3 3 4 1 4 2 7', 33, weapons=['Hand Weapon', 'Light Armour', 'Bow'], rules=[])],
    'All Persian chariot crewmen count as having light armour and are armed with a bow.', page='13'))
PE.append(U('Special Troops', 'Scythed Chariots', [M('Scythed Chariot', '7 3 3 5 4 1 3 1 7', 75, weapons=['Hand Weapon', 'Light Armour', 'Bow'], rules=[])],
    'All Persian chariot crewmen count as having light armour and are armed with a bow.', page='13'))
PE.append(U('Special Troops', 'Heavy Chariots', [M('Heavy Chariot', '6 4 4 4 4 2 4 4 7', 56, weapons=['Hand Weapon', 'Light Armour', 'Bow'], rules=[])],
    'All Persian chariot crewmen count as having light armour and are armed with a bow.', page='13'))
PE.append(U('Special Troops', 'War Wagon', [M('War Wagon', '5 3 4 3 4 4 6 6 7', 150, mn=1, mx=1, weapons=['Hand Weapon', 'Light Armour', 'Bow'], rules=[])],
    'All Persian chariot crewmen count as having light armour and are armed with a bow. War wagons are pulled by oxen and so do not cause impact hits when they charge; they charge at normal speed. One bolt thrower or war wagon per 500 points in the army.', page='13'))
PE.append(U('Special Troops', 'Elephants', [
    M('Indian Elephant', '6 4 0 7 6 6 3 4 4', 166, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Two Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon', 'Javelin'], options=[('Bows instead of javelins', 0)])],
    'An armed mahout and two crew armed with javelins or bows. Elephant: may stampede; causes fear in infantry and terror in cavalry. One elephant per 1,000 points in the army.', page='13'))
PE.append(U('Special Troops', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 2 3 3 3 1 3 1 7', 0, mn=3, mx=3, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. Crew armed with hand weapons. May have light armour (+2 pts). One bolt thrower or war wagon per 500 points in the army.', page='13'))
PE_LIM = {'Persian Troops': ('max', 75), 'Levies & Mercenaries': ('min', 25), 'Special Troops': ('max', 25)}
PE_NOTES = ('ACHAEMENID PERSIAN ARMY LIST (Armies of Antiquity, pp.12-13), 550-330 BC.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Persian Troops up to three quarters of the points; Levies & Mercenaries at least a quarter; Special Troops up to a quarter, with at most one bolt thrower or war wagon per 500 points and one elephant per 1,000 points.\n'
  'Spara: infantry may carry large shields (spara) that count as shields unless set up as a barrier (hard cover to the front against missiles, defended obstacle in combat; knocked down if the unit moves or loses a round).')
LISTS.append(('PE', 'Achaemenid Persian (Armies of Antiquity)', 'Persian_Armies_of_Antiquity.cat', PE, PE_LIM, PE_NOTES, None))
RATIOS.append(('PE', 'Guard Cavalry', ['Persian Cavalry'], 1))

NO_STANDARDS = []      # lists whose units may not have a standard bearer (Standard bearer option removed from every unit)
OPT_PAIRS = []         # (list key, [(unit, option label), ...]) the option may be taken once across the listed units

# ------------------------------------------------------------------ ANCIENT GREEK (book pp.14-15)
GR = []
GR.append(U('Characters', 'Army General', [M('General', '4 6 3 4 4 3 5 3 9', 157, weapons=['Hand Weapon', 'Large Shield', 'Heavy Armour'], rules=['Army General'], options=[('Thrusting spear', 0)])],
    'Hand weapon, large shield and heavy armour. May be given a thrusting spear at no additional cost. The General must lead (and may not leave) a Hoplite phalanx. 0-1.', mx=1, page='15'))
GR.append(U('Cavalry', 'Theban / Thessalian Heavy Cavalry', [M('Theban/Thessalian Cavalryman', '6 4 4 3 3 1 4 1 8', 19, mn=5, weapons=['Hand Weapon', 'Javelins'], options=[('Thrusting spear instead of javelins', 1), ('Heavy armour', 3)])],
    'Hand weapon and javelins. May replace javelins with thrusting spear (+1 pt). May have heavy armour (+3 pts). Every second heavy cavalry unit purchased may be Theban or Thessalian.', page='15'))
GR.append(U('Cavalry', 'Greek Heavy Cavalry', [M('Greek Cavalryman', '6 3 3 3 3 1 3 1 7', 14, mn=5, weapons=['Hand Weapon', 'Javelins'], options=[('Thrusting spear instead of javelins', 1), ('Heavy armour', 3)])],
    'Hand weapon and javelins. May replace javelins with thrusting spear (+1 pt). May have heavy armour (+3 pts).', page='15'))
GR.append(U('Cavalry', 'Thessalian / Thracian Light Cavalry', [M('Thessalian/Thracian Cavalryman', '6 3 4 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[])],
    'Hand weapon and javelins. Skirmishers. Every second light cavalry unit purchased may be Thessalian or Thracian.', page='15'))
GR.append(U('Cavalry', 'Greek Light Cavalry', [M('Greek Light Cavalryman', '6 2 3 3 3 1 3 1 5', 11, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=[])],
    'Hand weapon and javelins. Skirmishers.', page='15'))
GR.append(U('Phalanx', 'Spartan Hoplites', [M('Spartan', '4 4 3 3 4 1 3 1 8', 22, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Drilled', 'Stubborn', 'Phalanx (Armies of Antiquity)'], options=[('Light armour', 2), ('Heavy armour (replaces light armour)', 3), ('Sacred Band (+5 pts per model; fewer models than any other Hoplite unit)', 5)])],
    'Hand weapon, thrusting spear and large shield. May have light armour (+2 pts) or heavy armour (+3 pts). Up to one unit in the army may be upgraded to a Sacred Band at +5 pts per model; the Sacred Band must have fewer models than any other Hoplite unit in the army, is immune to psychology and will never break. Spartans are drilled and stubborn (Toughness 4 is not a typo). All units fight in phalanx formation.', page='15'))
GR.append(U('Phalanx', 'Hoplites', [M('Hoplite', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Phalanx (Armies of Antiquity)'], options=[('Light armour', 2), ('Heavy armour (replaces light armour)', 3), ('Sacred Band (+5 pts per model; fewer models than any other Hoplite unit)', 5)])],
    'Hand weapon, thrusting spear and large shield. May have light armour (+2 pts) or heavy armour (+3 pts). Up to one unit in the army may be upgraded to a Sacred Band at +5 pts per model; the Sacred Band must have fewer models than any other Hoplite unit in the army, is immune to psychology and will never break. All units fight in phalanx formation.', page='15'))
GR.append(U('Light Infantry', 'Thracian Peltasts', [M('Thracian', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Halberd', 'Javelins', 'Shield'], rules=[])],
    'Armed with a rhompahia (counts as a halberd), javelins and shields. Light Infantry.', page='15'))
GR.append(U('Light Infantry', 'Peltasts', [M('Peltast', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=[('Thrusting spear', 1)])],
    'Hand weapon, javelins and shield. May have a thrusting spear (+1 pt). Light Infantry.', page='15'))
GR.append(U('Light Infantry', 'Cretan Skirmishers', [M('Cretan', '5 2 4 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[], options=[('Shield', 1)])],
    'Hand weapon and bow (Cretans must be armed with bows). Any model may be given a shield (+1 pt). Skirmishers. 0-1 unit.', mx=1, page='15'))
GR.append(U('Light Infantry', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=[], options=[('Sling instead of javelins', 0), ('Short bow instead of javelins', 0), ('Bow instead of javelins', 1), ('Shield', 1)])],
    'Hand weapon and javelin. Every second skirmisher unit purchased may replace javelins with sling or short bow (no additional cost), or a bow (+1 pt). Any model may be given a shield (+1 pt). Skirmishers.', page='15'))
GR_LIM = {'Cavalry': ('max', 25), 'Phalanx': ('min', 50), 'Light Infantry': ('max', 25)}
GR_NOTES = ('ANCIENT GREEK ARMY LIST (Armies of Antiquity, pp.14-15), the hoplite armies of Athens, Thebes and Sparta.\n'
  'Characters: the army may have a General (no Army Standard Bearer). Cavalry up to a quarter of the points; Phalanx at least half; Light Infantry up to a quarter.\n'
  'The Oracles: Greek armies may not have unit standards or Army Standard Bearers. Instead roll 1D6 per 1,000 points at the start of the battle; each point may add +1 to a combat resolution score (maximum +2) or re-roll a failed Leadership test once; once used it is spent.\n'
  'Phalanxes: units of at least 16 models with a rank bonus of at least +1 fight as a phalanx (see the rule).')
LISTS.append(('GR', 'Ancient Greek (Armies of Antiquity)', 'Greek_Armies_of_Antiquity.cat', GR, GR_LIM, GR_NOTES, None))
RATIOS.append(('GR', 'Theban / Thessalian Heavy Cavalry', ['Greek Heavy Cavalry'], 1))
RATIOS.append(('GR', 'Thessalian / Thracian Light Cavalry', ['Greek Light Cavalry'], 1))
NO_STANDARDS.append('GR')
OPT_PAIRS.append(('GR', [('Spartan Hoplites', 'Sacred Band (+5 pts per model; fewer models than any other Hoplite unit)'), ('Hoplites', 'Sacred Band (+5 pts per model; fewer models than any other Hoplite unit)')]))

FIGS = []      # (list key, unit A, unit B, per): figures of A in the force <= figures of B / per
EXCL = []      # (list key, unit A, unit B): A and B may not both be taken
REQ = []       # (list key, unit, required unit): unit may only be taken if the required unit is in the army
PTSLIM = []    # (list key, unit, points per allowed unit, [other units that share the allowance])

# ------------------------------------------------------------------ ALEXANDER & HIS SUCCESSORS (book pp.16-17)
AL = []
ALCH = [('Light armour', 3), ('Heavy armour (replaces light armour)', 4), ('Shield or buckler', 1), ('Large shield', 2), ('Warhorse', 4), ('Barding (-1 M)', 4)]
AL.append(U('Characters', 'Army General', [M('General', '4 6 6 4 4 3 6 3 9', 175, weapons=['Hand Weapon'], rules=['Army General'], options=ALCH + [('Spear', 2), ('Pike or kontos', 3), ('Ride an elephant (cost of elephant extra)', 0)])],
    'Armed with a sword. May have light armour (+3 pts), heavy armour (+4 pts), shield or buckler (+1 pt), large shield (+2 pts), spear (+2 pts), pike or kontos (+3 pts). May ride a warhorse (+4 pts) or an elephant purchased at the additional cost from the Special Troops section. The warhorse may have barding (+4 pts). 0-1.', mx=1, page='17'))
AL.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 4 2 4 2 8', 80, weapons=['Hand Weapon'], rules=['Army Standard'], options=ALCH)],
    'Armed with a sword. May have light armour (+3 pts), heavy armour (+4 pts), shield or buckler (+1 pt), large shield (+2 pts). May ride a warhorse (+4 pts); the warhorse may have barding (+4 pts). 0-1.', mx=1, page='17'))
ALSH = [('Throwing spear and javelins instead of kontos', 1), ('Light armour', 3), ('Shield', 2), ('Barding (-1 M)', 4), ('Heavy armour (barded cavalry only)', 4)]
AL.append(U('Cavalry', 'Royal Guard Shock Cavalry', [M('Royal Guard Cavalryman', '8 4 4 3 3 1 4 1 9', 28, mn=5, weapons=['Hand Weapon', 'Kontos'], rules=['Stubborn', 'Wedge Formation'], options=ALSH)],
    'Sword and kontos. May replace kontos with throwing spear and javelins (+1 pt). May have light armour (+3 pts), shield (+2 pts), barding (+4 pts). Cavalry with barding may have heavy armour (+4 pts). May fight in Wedge formation. Royal Guard are stubborn. 0-1 unit.', mx=1, page='17'))
AL.append(U('Cavalry', 'Shock Cavalry', [M('Shock Cavalryman', '8 4 4 3 3 1 3 1 8', 25, mn=5, weapons=['Hand Weapon', 'Kontos'], rules=['Wedge Formation'], options=ALSH)],
    'Sword and kontos. May replace kontos with throwing spear and javelins (+1 pt). May have light armour (+3 pts), shield (+2 pts), barding (+4 pts). Cavalry with barding may have heavy armour (+4 pts). May fight in Wedge formation.', page='17'))
ALLC = [('Throwing spear', 1), ('Kontos instead of javelins', 1), ('Bow instead of javelins', 1)]
AL.append(U('Cavalry', 'Elite Light Cavalry', [M('Elite Light Cavalryman', '8 4 4 3 3 1 4 1 8', 24, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=ALLC)],
    'Swords, javelins and shield. May have throwing spear (+1 pt). May replace javelins with kontos or bow (+1 pt). Light Cavalry. Every second light cavalry unit may be elite.', page='17'))
AL.append(U('Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=ALLC)],
    'Swords, javelins and shield. May have throwing spear (+1 pt). May replace javelins with kontos or bow (+1 pt). Light Cavalry.', page='17'))
ALPH = [('Heavy armour instead of light armour', 1)]
AL.append(U('Infantry', 'Royal Guard Phalanx', [M('Royal Guard', '4 4 4 3 3 1 3 1 9', 20, mn=5, weapons=['Hand Weapon', 'Pike', 'Light Armour', 'Shield'], rules=['Stubborn', 'Phalanx (Armies of Antiquity)'], options=ALPH)],
    'Sword, pike, light armour and shield. May replace light armour with heavy armour (+1 pt). May fight in phalanx formation. Royal Guard may not be taken if the army includes a unit of Hypaspists. Royal Guard are stubborn. 0-1 unit.', mx=1, page='17'))
AL.append(U('Infantry', 'Veteran Phalanx', [M('Veteran', '4 3 3 3 3 1 3 1 8', 15, mn=5, weapons=['Hand Weapon', 'Pike', 'Light Armour', 'Shield'], rules=['Stubborn', 'Phalanx (Armies of Antiquity)'], options=ALPH)],
    'Sword, pike, light armour and shield. May replace light armour with heavy armour (+1 pt). May fight in phalanx formation. Veterans are stubborn.', page='17'))
AL.append(U('Infantry', 'Regular Phalanx', [M('Regular', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Pike', 'Light Armour', 'Shield'], rules=['Phalanx (Armies of Antiquity)'], options=ALPH)],
    'Sword, pike, light armour and shield. May replace light armour with heavy armour (+1 pt). May fight in phalanx formation.', page='17'))
AL.append(U('Infantry', 'Levy Phalanx', [M('Levy', '4 2 2 3 3 1 2 1 5', 5, mn=5, weapons=['Hand Weapon', 'Pike', 'Light Armour', 'Shield'], rules=['Phalanx (Armies of Antiquity)'], options=ALPH)],
    'Sword, pike, light armour and shield. May replace light armour with heavy armour (+1 pt). May fight in phalanx formation.', page='17'))
ALLI = [('Thrusting spear', 1)]
AL.append(U('Infantry', 'Hypaspists', [M('Hypaspist', '5 4 4 3 3 1 3 1 9', 14, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=ALLI)],
    'Hand weapon, javelins and shield. May have thrusting spear (+1 pt). Light Infantry. 0-1 unit.', mx=1, page='17'))
AL.append(U('Infantry', 'Thracians', [M('Thracian', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Halberd', 'Javelins', 'Shield'], rules=[])],
    'Rhomphaia (counts as a halberd), javelins and shield. Light Infantry. 0-1 unit.', mx=1, page='17'))
AL.append(U('Infantry', 'Peltasts', [M('Peltast', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=ALLI)],
    'Hand weapon, javelins and shield. May have thrusting spear (+1 pt). Light Infantry.', page='17'))
AL.append(U('Infantry', 'Levy Light Infantry', [M('Levy', '4 2 2 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=[], options=ALLI)],
    'Hand weapon, javelins and shield. May have thrusting spear (+1 pt). Light Infantry.', page='17'))
ALSK = [('Sling or short bow instead of javelin (second unit)', 0), ('Bow instead of javelin', 1), ('Shield', 1), ('Staff slings or crossbows (one unit)', 2)]
AL.append(U('Infantry', 'Mercenary Skirmishers', [M('Mercenary', '5 2 3 3 3 1 3 1 7', 5, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=[], options=ALSK)],
    'Hand weapon and javelin. Every second unit purchased may replace javelins with sling or short bow (no additional cost), or a bow (+1 pt). Any model may be given a shield (+1 pt). One unit may be given staff slings or crossbows (+2 pts). Skirmishers.', page='17'))
AL.append(U('Infantry', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=[], options=ALSK)],
    'Hand weapon and javelin. Options as for Mercenary Skirmishers. Skirmishers.', page='17'))
AL.append(U('Infantry', 'Levy Skirmishers', [M('Levy', '4 2 2 3 3 1 2 1 3', 3, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=[], options=ALSK)],
    'Hand weapon and javelin. Options as for Mercenary Skirmishers. Skirmishers.', page='17'))
AL.append(U('Special Troops & Allies', 'Scythed Chariots', [M('Scythed Chariot', '7 3 3 5 4 1 3 1 7', 75, weapons=['Dagger', 'Heavy Armour'], rules=[])],
    'Driver armed with a dagger and heavy armour. Scythed chariot. One artillery piece or scythed chariot per 500 points in the army.', page='17'))
AL.append(U('Special Troops & Allies', 'Indian Elephants', [
    M('Indian Elephant', '6 4 0 7 6 6 3 4 4', 150, mn=1, mx=1, key='el', options=[('Barding', 16)]),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 8, mn=0, mx=3, key='crew', weapons=['Hand Weapon', 'Javelin'], options=[('Bows instead of javelins', 0), ('Light armour', 2), ('Pike', 1), ('Shield', 1)])],
    'Unarmed mahout and up to three crew armed with javelins or bows at +8 pts per crewman. Any crew may have light armour (+2 pts), pike (+1 pt) or shield (+1 pt). Elephant may have barding (+16 pts). Elephants: all elephants must be either African or Indian; you cannot mix both types in the same army. One elephant per 1,000 points in the army.', page='17'))
AL.append(U('Special Troops & Allies', 'African Elephants', [
    M('African Elephant', '6 4 0 6 6 5 3 4 4', 125, mn=1, mx=1, key='el', options=[('Barding', 16)]),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 8, mn=0, mx=3, key='crew', weapons=['Hand Weapon', 'Javelin'], options=[('Bows instead of javelins', 0), ('Light armour', 2), ('Pike', 1), ('Shield', 1)])],
    'Unarmed mahout and up to three crew armed with javelins or bows at +8 pts per crewman. Any crew may have light armour (+2 pts), pike (+1 pt) or shield (+1 pt). Elephant may have barding (+16 pts). Elephants: all elephants must be either African or Indian; you cannot mix both types in the same army. One elephant per 1,000 points in the army.', page='17'))
AL.append(U('Special Troops & Allies', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=1, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Each machine has a crew of two to three men armed with swords. May have light armour (+2 pts per crewman). Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. No more than one artillery piece per infantry unit in the army. One artillery piece or scythed chariot per 500 points in the army.', page='17'))
AL.append(U('Special Troops & Allies', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=1, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Each machine has a crew of two to three men armed with swords. May have light armour (+2 pts per crewman). Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit. No more than one artillery piece per infantry unit in the army. One artillery piece or scythed chariot per 500 points in the army.', page='17'))
AL_LIM = {'Cavalry': ('max', 50), 'Infantry': ('min', 25), 'Special Troops & Allies': ('max', 50)}
AL_NOTES = ('ALEXANDER & HIS SUCCESSORS ARMY LIST (Armies of Antiquity, pp.16-17).\n'
  'Characters: the army may have a General and an Army Battle Standard. Cavalry up to half the points; Infantry at least a quarter; Special Troops & Allies up to half, with one artillery piece or scythed chariot per 500 points and one elephant per 1,000 points.\n'
  'Allies: allied units can be taken from the Barbarian, Persian, Indian, Cataphract and Ancient Greek army lists (not built here: make a separate small roster for allies).\n'
  'Wedge formation, the staff sling (treated as a crossbow) and the phalanx are explained in the rules.')
LISTS.append(('AL', 'Alexander & his Successors (Armies of Antiquity)', 'Alexander_Successors_Armies_of_Antiquity.cat', AL, AL_LIM, AL_NOTES, None))
RATIOS.append(('AL', 'Elite Light Cavalry', ['Light Cavalry'], 1))
PTSLIM.append(('AL', 'Scythed Chariots', 500, ['Bolt Thrower', 'Stone Thrower']))
PTSLIM.append(('AL', 'Bolt Thrower', 500, ['Scythed Chariots', 'Stone Thrower']))
PTSLIM.append(('AL', 'Stone Thrower', 500, ['Scythed Chariots', 'Bolt Thrower']))
PTSLIM.append(('AL', 'Indian Elephants', 1000, ['African Elephants']))
PTSLIM.append(('AL', 'African Elephants', 1000, ['Indian Elephants']))
PTSLIM.append(('PE', 'Bolt Thrower', 500, ['War Wagon']))
PTSLIM.append(('PE', 'War Wagon', 500, ['Bolt Thrower']))
PTSLIM.append(('PE', 'Elephants', 1000, []))

# ------------------------------------------------------------------ ANCIENT INDIAN (book pp.18-19)
IN = []
INMT = [('Horse (M8, free)', 0), ('Light chariot (cost of chariot extra)', 0), ('Heavy chariot (cost of chariot extra)', 0), ('Elephant (cost of elephant extra)', 0)]
IN.append(U('Characters', 'Army General', [M('Army General', '4 6 6 4 4 3 6 4 7', 140, weapons=['Hand Weapon'], rules=['Army General'], options=[('Shield', 2), ('Light armour', 3), ('Longbow', 3), ('Javelins', 2), ('Thrusting spear (on horse)', 2), ('Barding (-1 M, on horse)', 4)] + INMT)],
    'Hand weapon. May have shield (+2 pts), light armour (+3 pts), longbow (+3 pts), javelins (+2 pts). May be mounted on a horse (free, Movement 8"), or in a light chariot, heavy chariot or on an elephant (bought at additional points cost from the list). A general on a horse may have a thrusting spear (+2 pts) and horse barding (+4 pts). The army must have a General.', mx=1, page='19'))
IN.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 5 5 4 4 2 5 3 6', 88, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Shield', 2), ('Heavy armour (replaces light armour)', 3), ('Longbow', 2), ('Javelins', 2), ('Thrusting spear (on horse)', 2), ('Barding (-1 M, on horse)', 4)] + INMT)],
    'Hand weapon and light armour. May have shield (+2 pts), light armour (+3 pts; as printed, although the model already has light armour, so entered as heavy armour), longbow (+2 pts), javelins (+2 pts). May be mounted on a horse (free, Movement 8"), or in a light chariot, heavy chariot or on an elephant (bought at additional points cost from the list). A Standard Bearer on a horse may have a thrusting spear (+2 pts) and horse barding (+4 pts). 0-1.', mx=1, page='19'))
IN.append(U('Elephants, Chariots & Cavalry', 'Elephants', [
    M('Indian Elephant', '6 4 0 7 6 6 3 4 4', 182, mn=1, mx=1, key='el', options=[('Barding', 16)]),
    M('Mahout', '4 2 2 3 3 1 3 1 6', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 4 4 3 3 1 4 1 6', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon', 'Longbow', 'Javelins', 'Light Armour', 'Shield']),
    M('Additional Crewman', '4 4 4 3 3 1 4 1 6', 16, mn=0, mx=1, key='crew3', weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Longbow instead of shield', 0)])],
    'An unarmed mahout and two crew armed with hand weapon, longbow, javelins, light armour and shield. May have one additional crewman armed with hand weapon, javelin and shield or longbow (+16 pts). Elephant may have barding (+16 pts). One elephant per 500 points in the army.', page='19'))
IN.append(U('Elephants, Chariots & Cavalry', 'Light Chariots', [M('Light Chariot', '8 4 4 3 4 1 4 2 6', 40, weapons=['Hand Weapon', 'Longbow', 'Javelins', 'Light Armour', 'Shield'], rules=[])],
    'Two crewmen armed with a hand weapon, longbow, javelins, light armour and shield riding in a two-horse light chariot with driver.', page='19'))
IN.append(U('Elephants, Chariots & Cavalry', 'Heavy Chariots', [M('Heavy Chariot', '6 4 4 4 4 2 4 6 6', 75, weapons=['Hand Weapon', 'Longbow', 'Javelins', 'Light Armour', 'Shield'], rules=[])],
    'Four crewmen armed with a hand weapon, longbow, javelins, light armour and shield riding in a four-horse heavy chariot with two drivers.', page='19'))
IN.append(U('Elephants, Chariots & Cavalry', 'Indian Cavalry', [M('Indian Cavalryman', '6 3 3 3 3 1 3 1 5', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Warband Psychology (rule 1)'], options=[('Light armour', 3), ('Barding (-1 M)', 4), ('Thrusting spear instead of throwing spear', 0), ('Kontos instead of throwing spear', 1)])],
    'Sword, throwing spear and shield. May have light armour (+3 pts), barding (+4 pts). May replace throwing spear with thrusting spear (free) or kontos (+1 pt). Subject to Warband rule 1.', page='19'))
IN.append(U('Infantry', 'Maiden Guards', [M('Maiden Guard', '4 4 4 3 3 1 4 1 6', 14, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Buckler'], rules=['Stubborn', 'Warband Psychology (rule 1)'])],
    'Sword, light armour and buckler. Stubborn. Subject to Warband rule 1. 0-1 unit.', mx=1, page='19'))
IN.append(U('Infantry', 'Longbowmen', [M('Longbowman', '4 3 3 3 3 1 3 1 5', 8, mn=5, weapons=['Double-handed Weapon', 'Longbow'], rules=['Warband Psychology (rule 1)'], options=[('Light armour', 2)])],
    'Double-handed sword and longbow. May have light armour (+2 pts). Subject to Warband rule 1.', page='19'))
IN.append(U('Infantry', 'Longbowmen Militia', [M('Militia', '4 2 2 3 3 1 3 1 3', 4, mn=5, weapons=['Double-handed Weapon', 'Longbow'], rules=['Warband Psychology (rule 1)'], options=[('Light armour', 2)])],
    'Double-handed sword and longbow. May have light armour (+2 pts). Subject to Warband rule 1.', page='19'))
IN.append(U('Infantry', 'Swordsmen', [M('Swordsman', '4 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Double-handed Weapon', 'Large Shield'], rules=['Warband Psychology (rule 1)'], options=[('Javelins', 1), ('Light armour', 2)])],
    'Double-handed sword and large shield. May have javelins (+1 pt), light armour (+2 pts). Subject to Warband rule 1.', page='19'))
IN.append(U('Infantry', 'Swordsmen Militia', [M('Militia', '4 2 2 3 3 1 3 1 3', 4, mn=5, weapons=['Double-handed Weapon', 'Large Shield'], rules=['Warband Psychology (rule 1)'], options=[('Javelins', 1), ('Light armour', 2)])],
    'Double-handed sword and large shield. May have javelins (+1 pt), light armour (+2 pts). Subject to Warband rule 1.', page='19'))
IN.append(U('Infantry', 'Skirmishers', [M('Skirmisher', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Longbow'], rules=['Warband Psychology (rule 1)'], options=[('Javelins and shield instead of longbow', 0), ('Sling instead of longbow', 0), ('Double-handed sword (archers and javelin men)', 2)])],
    'Sword and longbow, or sword, javelins and shield, or sword and sling. Archers and javelin men may upgrade sword to double-handed sword (+2 pts). Skirmishers. Subject to Warband rule 1.', page='19'))
IN_LIM = {'Elephants, Chariots & Cavalry': ('max', 50), 'Infantry': ('min', 25)}
IN_NOTES = ('ANCIENT INDIAN ARMY LIST (Armies of Antiquity, pp.18-19), 500 BC - 500 AD (Mauryan, Gupta, Kushan and Bactrian Greek kingdoms).\n'
  'Characters: the army must have a General and may have an Army Standard Bearer. Elephants, Chariots & Cavalry up to half the points; Infantry at least a quarter; Allies & Mercenaries up to a quarter, with at most one elephant per 500 points (the elephant limit is applied to the Elephants unit).\n'
  'Allies: Indian armies may have allies drawn from the Cataphract (Scythian mercenaries) and Ancient Greek (Bactrian Greek allies) lists (not built here: make a separate small roster).\n'
  'Used To Elephants: Indian infantry do not fear elephants; Indian cavalry and chariots only fear them. Indian Longbow: treated as a longbow; downgrade all longbows to bows at -1 pt per model if you prefer.')
LISTS.append(('IN', 'Ancient Indian (Armies of Antiquity)', 'Indian_Armies_of_Antiquity.cat', IN, IN_LIM, IN_NOTES, None))
PTSLIM.append(('IN', 'Elephants', 500, []))

# ------------------------------------------------------------------ REPUBLICAN ROMANS (book pp.20-21)
RR = []
RRCH = [('Light armour', 3), ('Shield', 2), ('Large shield', 3), ('Warhorse', 4)]
RR.append(U('Characters', 'Army General', [M('General', '4 5 5 4 3 3 6 2 9', 142, weapons=['Hand Weapon'], rules=['Army General', 'Drilled'], options=RRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts). May ride a warhorse (+4 pts). Army General and drilled. 0-1.', mx=1, page='21'))
RR.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 77, weapons=['Hand Weapon'], rules=['Army Standard', 'Drilled'], options=RRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts). May ride a warhorse (+4 pts). Army Standard Bearer and drilled. 0-1.', mx=1, page='21'))
RR.append(U('Infantry', 'Hastati', [M('Hastati', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Hand Weapon', 'Pilum', 'Large Shield'], rules=['Drilled'], options=[('Light armour', 2)])],
    'Large shield, pilum and sword. May have light armour (+2 pts). Drilled.', page='21'))
RR.append(U('Infantry', 'Principes', [M('Principe', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], rules=['Drilled'], options=[('Light armour', 2), ('Pilum instead of thrusting spear', 1)])],
    'Large shield, thrusting spear and sword. May have light armour (+2 pts) and a pilum (+1 pt) instead of a thrusting spear. Drilled.', page='21'))
RR.append(U('Infantry', 'Triarii', [M('Triarii', '4 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield', 'Light Armour'], rules=['Drilled', 'Stubborn'])],
    'Large shield, thrusting spear, sword and light armour. Drilled. Triarii are stubborn.', page='21'))
RR.append(U('Auxiliaries', 'Roman and Italian Cavalry', [M('Cavalryman', '6 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Light armour', 2), ('Javelins', 1)])],
    'Throwing spear, sword and shield. May have light armour (+2 pts), javelins (+1 pt).', page='21'))
RR.append(U('Auxiliaries', 'Italian Spearmen', [M('Italian', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=[], options=[('Light armour', 2), ('Large shield (replaces shield)', 1)])],
    'Throwing spear, sword and shield. May have light armour (+2 pts), large shield (+1 pt). Light Infantry.', page='21'))
RR.append(U('Auxiliaries', 'Levy Light Infantry', [M('Levy', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Throwing Spear'], rules=[], options=[('Shield', 1), ('Javelins', 1)])],
    'Throwing spear and sword. May have shield (+1 pt), javelins (+1 pt). Skirmishers.', page='21'))
RR.append(U('Auxiliaries', 'Velites', [M('Velite', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear'], rules=[], options=[('Shield', 1), ('Javelins', 1)])],
    'Throwing spear and sword. May have shield (+1 pt), javelins (+1 pt). Skirmishers.', page='21'))
RR.append(U('Special Units', 'Spanish Cavalry', [M('Spanish Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear'], rules=[], options=[('Buckler or shield', 1), ('Javelins', 1), ('Light armour', 1)])],
    'Throwing spear and sword. May have buckler (+1 pt) or shield (+1 pt), javelins (+1 pt) and light armour (+1 pt). Light Cavalry.', page='21'))
RR.append(U('Special Units', 'Caetrati', [M('Caetrati', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], rules=[], options=[('Light armour', 2), ('Javelins', 1)])],
    'Throwing spear, sword and buckler. May have light armour (+2 pts) and javelins (+1 pt). Caetrati are skirmishers.', page='21'))
RR.append(U('Special Units', 'Scutarii', [M('Scutarii', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=[], options=[('Javelins', 1), ('Heavy throwing spear (replaces throwing spear)', 1)])],
    'Throwing spear, sword and shield (free, instead of the buckler). May have javelins (+1 pt) and a heavy throwing spear (+1 pt) instead of a throwing spear. Scutarii are Light Infantry.', page='21'))
RR_LIM = {'Infantry': ('min', 50), 'Auxiliaries': ('max', 50), 'Special Units': ('max', 25)}
RR_NOTES = ('REPUBLICAN ROMAN ARMY LIST (Armies of Antiquity, pp.20-21), the citizen legions from c.400 BC to c.100 BC.\n'
  'Characters: the army may have a General and an Army Battle Standard. Infantry at least half the points; Auxiliaries up to half; Special Units up to a quarter, and no more special units than the army has infantry and auxiliary units (not enforced).\n'
  'Allies as special units from other lists (not built here: make a separate small roster): Numidians (any number of Barbarian Light Cavalry, Warriors but not Fanatic Warriors, and Skirmishers from the Barbarian list), Celts (Barbarian Noble Cavalry or Warriors, not Fanatic Warriors), Greeks (Peltasts and Skirmishers from the Ancient Greek list). All are subject to the Warband rules.\n'
  'Manipular formation: a hastati, principes or triarii unit may swap places with another hastati or principes unit within 4" in its front arc (see the rule).')
LISTS.append(('RR', 'Republican Roman (Armies of Antiquity)', 'Republican_Roman_Armies_of_Antiquity.cat', RR, RR_LIM, RR_NOTES, None))

# ------------------------------------------------------------------ CARTHAGINIAN (book pp.22-23)
CA = []
CA.append(U('Characters', 'Army General', [M('General', '4 5 5 4 3 3 6 2 9', 140, weapons=['Hand Weapon'], rules=['Army General'], options=RRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts). May ride a warhorse (+4 pts). 0-1.', mx=1, page='23'))
CA.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon'], rules=['Army Standard'], options=RRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts). May ride a warhorse (+4 pts). 0-1.', mx=1, page='23'))
CA.append(U('Cavalry', 'Punic Heavy Cavalry', [M('Punic Cavalryman', '8 3 3 3 3 1 3 1 7', 19, mn=5, weapons=['Hand Weapon', 'Shield', 'Throwing Spear', 'Light Armour'])],
    'Sword, shield, throwing spear and light armour.', page='23'))
CA.append(U('Infantry', 'Punic Heavy Infantry (Citizens)', [M('Citizen', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Phalanx (Armies of Antiquity)'], options=[('Light armour', 2), ('Heavy armour (replaces light armour)', 3), ('Large shield (replaces shield)', 1), ('Throwing spear instead of thrusting spear (free)', 0)])],
    'Sword, thrusting spear and shield. May have light armour (+2 pts) or heavy armour (+3 pts), large shield (+1 pt). May have throwing spear (free) instead of thrusting spear. Phalanx. If all citizens are equipped without armour and have throwing spears, they may be fielded as Light Infantry but may then not use the Phalanx rule.', page='23'))
CA.append(U('Infantry', 'Africans', [M('African', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Shield', 'Throwing Spear', 'Light Armour'], rules=['Phalanx (Armies of Antiquity)'])],
    'Sword, shield, throwing spear and light armour. Phalanx.', page='23'))
CA.append(U('Allies & Mercenaries', 'Spanish Cavalry', [M('Spanish Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear'], rules=['Allies & Mercenaries (Carthaginian)'], options=[('Buckler or shield', 1), ('Light armour', 1), ('Javelins', 1)])],
    'Throwing spear and sword. May have buckler (+1 pt) or shield (+1 pt), light armour (+1 pt), javelins (+1 pt). Light Cavalry. Allies & Mercenaries.', page='23'))
CA.append(U('Allies & Mercenaries', 'Spanish Caetrati', [M('Caetrati', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], rules=['Allies & Mercenaries (Carthaginian)'], options=[('Light armour', 2), ('Javelins', 2)])],
    'Sword, throwing spear and buckler. May have light armour (+2 pts) and javelins (+2 pts). Caetrati are skirmishers. Subject to the Allies & Mercenaries special rule.', page='23'))
CA.append(U('Allies & Mercenaries', 'Spanish Scutarii', [M('Scutarii', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Allies & Mercenaries (Carthaginian)'], options=[('Javelins', 1), ('Heavy throwing spear (replaces throwing spear)', 1)])],
    'Sword, throwing spear and shield (free, instead of a buckler). May have javelins (+1 pt) and a heavy throwing spear (+1 pt) instead of a throwing spear. Scutarii are Light Infantry. Subject to the Allies & Mercenaries special rule.', page='23'))
CA.append(U('Allies & Mercenaries', 'Libyan Skirmishers', [M('Libyan', '5 2 3 3 3 1 3 1 7', 5, mn=5, weapons=['Hand Weapon', 'Javelins', 'Buckler'], rules=['Allies & Mercenaries (Carthaginian)'])],
    'Javelins, hand weapon and buckler. Skirmishers. Subject to the Carthaginian Allies & Mercenaries special rule.', page='23'))
CA.append(U('Special Units', 'African Elephants', [
    M('African Elephant', '6 4 0 6 6 5 3 4 4', 152, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon', 'Thrusting Spear', 'Javelins', 'Light Armour'])],
    'Unarmed mahout and two crew armed with thrusting spear, javelins, hand weapons and light armour. Elephant: may stampede; causes fear in infantry and terror in cavalry. One elephant per 1,000 points in the army.', page='23'))
CA_LIM = {'Cavalry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50), 'Special Units': ('max', 25)}
CA_NOTES = ('CARTHAGINIAN ARMY LIST (Armies of Antiquity, pp.22-23), 600-146 BC.\n'
  'Characters: the army may have a General and an Army Battle Standard. Cavalry up to a quarter of the points; Infantry at least a quarter; Allies & Mercenaries up to half; Special Units up to a quarter with one elephant per 1,000 points.\n'
  'Phalanx: Punic citizens and African infantry fight in a phalanx (see the Ancient Greek rule), but may have unit standards and an Army Standard Bearer; the Oracles rule does not apply.\n'
  'Allies from other lists (not built here: make a separate small roster): Numidians (Barbarian Light Cavalry, Warriors, Skirmishers), Celts (Barbarian Noble Cavalry or Warriors; not Fanatic Warriors) and Greeks (Hoplites including Spartans but not Sacred Band, and Skirmishers except Cretans, from the Ancient Greek list; no Oracles, no unit standards). All are subject to the Allies & Mercenaries and Warband rules.')
LISTS.append(('CA', 'Carthaginian (Armies of Antiquity)', 'Carthaginian_Armies_of_Antiquity.cat', CA, CA_LIM, CA_NOTES, None))
PTSLIM.append(('CA', 'African Elephants', 1000, []))

# ------------------------------------------------------------------ LATE ROMAN (book pp.24-25)
LR = []
LRCH = [('Light armour', 3), ('Shield or buckler', 1), ('Large shield', 3), ('Warhorse', 4), ('Barded warhorse (replaces warhorse)', 8)]
LR.append(U('Characters', 'Army General', [M('General', '4 6 6 4 4 3 6 3 9', 175, weapons=['Hand Weapon'], rules=['Army General'], options=LRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield or buckler (+1 pt), large shield (+3 pts). May ride a warhorse (+4 pts) or a barded warhorse (+8 pts). 0-1.', mx=1, page='25'))
LR.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 4 2 4 2 8', 80, weapons=['Hand Weapon'], rules=['Army Standard'], options=LRCH)],
    'Armed with a sword. May have light armour (+3 pts), shield or buckler (+1 pt), large shield (+3 pts). May ride a warhorse (+4 pts) or a barded warhorse (+8 pts). 0-1.', mx=1, page='25'))
LRHC = [('Javelins', 1), ('Darts', 1), ('Short bow', 1), ('Kontos instead of throwing spear', 1), ('Heavy armour (replaces light armour)', 2)]
LR.append(U('Cavalry', 'Guard Heavy Cavalry', [M('Guard Cavalryman', '8 4 4 3 3 1 4 1 8', 28, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield', 'Light Armour'], options=LRHC)],
    'Sword, throwing spear, shield and light armour. May have javelins (+1 pt), darts (+1 pt), short bow (+1 pt). May replace throwing spear with kontos (+1 pt). May replace light armour with heavy armour (+2 pts). Guard troops.', page='25'))
LR.append(U('Cavalry', 'Cataphracts', [M('Cataphract Cavalryman', '5 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Kontos', 'Shield', 'Light Armour'], options=[('Javelins', 1), ('Darts', 1), ('Short bow', 1), ('Heavy armour (replaces light armour)', 2)])],
    'Sword, kontos, shield and light armour; barded horses (included in the points). May have javelins (+1 pt), darts (+1 pt), short bow (+1 pt), heavy armour (+2 pts). Cataphracts: count rank bonus up to +3 and may not march (see Cataphract list). Cataphract values as printed in the Late Roman list.', page='25'))
LR.append(U('Cavalry', 'Comitatense Heavy Cavalry', [M('Comitatense Cavalryman', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield', 'Light Armour'], options=LRHC)],
    'Sword, throwing spear, shield and light armour. May have javelins (+1 pt), darts (+1 pt), short bow (+1 pt). May replace throwing spear with kontos (+1 pt). May replace light armour with heavy armour (+2 pts). 0-1.', mx=1, page='25'))
LRLC = [('Throwing spear', 2), ('Shield (replaces buckler)', 1), ('Large shield (replaces buckler)', 3), ('Kontos instead of javelins', 1), ('Bow instead of javelins', 2)]
LR.append(U('Cavalry', 'Guard Light Cavalry', [M('Guard Light Cavalryman', '8 4 4 3 3 1 4 1 8', 24, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=LRLC)],
    'Sword, javelins and buckler. May have throwing spear (+2 pts), shield (+1 pt) or large shield (+3 pts) instead of a buckler, kontos (+1 pt) or bow (+2 pts) instead of javelins. Light Cavalry. Guard troops.', page='25'))
LR.append(U('Cavalry', 'Comitatense Light Cavalry', [M('Comitatense Light Cavalryman', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=LRLC)],
    'Sword, javelins and buckler. May have throwing spear (+2 pts), shield (+1 pt) or large shield (+3 pts) instead of a buckler, kontos (+1 pt) or bow (+2 pts) instead of javelins. Light Cavalry.', page='25'))
LR.append(U('Cavalry', 'Limitanei Light Cavalry', [M('Limitanei Light Cavalryman', '8 2 3 3 3 1 3 1 5', 12, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=LRLC)],
    'Sword, javelins and buckler. May have throwing spear (+2 pts), shield (+1 pt) or large shield (+3 pts) instead of a buckler, kontos (+1 pt) or bow (+2 pts) instead of javelins. Light Cavalry.', page='25'))
LRHI = [('Light armour', 2), ('Javelins', 1), ('Darts', 1), ('Large shield (replaces shield)', 1)]
LR.append(U('Infantry', 'Guard Heavy Infantry', [M('Guard Infantryman', '4 4 4 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Shield Wall (Late Roman)'], options=LRHI)],
    'Sword, throwing spear and shield. May have light armour (+2 pts), javelins (+1 pt), darts (+1 pt). May replace shield with large shield (+1 pt). May form a shield wall. Guard troops.', page='25'))
LR.append(U('Infantry', 'Comitatense Heavy Infantry', [M('Comitatense Infantryman', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Shield Wall (Late Roman)'], options=LRHI)],
    'Sword, throwing spear and shield. May have light armour (+2 pts), javelins (+1 pt), darts (+1 pt). May replace shield with large shield (+1 pt). May form a shield wall.', page='25'))
LR.append(U('Infantry', 'Limitanei Heavy Infantry', [M('Limitanei Infantryman', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Shield Wall (Late Roman)'], options=LRHI)],
    'Sword, throwing spear and shield. May have light armour (+2 pts), javelins (+1 pt), darts (+1 pt). May replace shield with large shield (+1 pt). May form a shield wall.', page='25'))
LRLI = [('Throwing spear (with javelins)', 1), ('Darts (with javelins)', 1), ('Large shield (replaces shield)', 1), ('Light armour', 2)]
LR.append(U('Infantry', 'Guard Light Infantry', [M('Guard Light Infantryman', '4 4 4 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=LRLI)],
    'Sword, javelins and shield. If armed with javelins, may also have throwing spears (+1 pt), darts (+1 pt), and may replace shield with large shield (+1 pt). May have light armour (+2 pts). Light Infantry. Guard troops.', page='25'))
LR.append(U('Infantry', 'Auxiliary Light Infantry', [M('Auxiliary', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=LRLI)],
    'Sword, javelins and shield. If armed with javelins, may also have throwing spears (+1 pt), darts (+1 pt), and may replace shield with large shield (+1 pt). May have light armour (+2 pts). Light Infantry.', page='25'))
LR.append(U('Infantry', 'Archers', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Light armour', 2)])],
    'Sword and bow. May have light armour (+2 pts). Light Infantry. Archers may be combined with other light or heavy infantry units (see Combined Formations; not built as a single unit here).', page='25'))
LRSK = [('Buckler or shield', 1), ('Throwing spear', 1), ('Darts', 1), ('Sling instead of javelins (free)', 0), ('Bow instead of javelins', 1), ('Crossbow or staff sling instead of javelins', 2)]
LR.append(U('Infantry', 'Guard Skirmishers', [M('Guard Skirmisher', '4 4 4 3 3 1 3 1 8', 10, mn=5, weapons=['Hand Weapon', 'Javelin'], options=LRSK)],
    'Sword and javelins. May have buckler or shield (+1 pt), throwing spear (+1 pt), darts (+1 pt). May replace javelins with sling (free), bow (+1 pt) or crossbow/staff sling (+2 pts; both count as crossbows). Skirmishers. Guard troops.', page='25'))
LR.append(U('Infantry', 'Lanciarii', [M('Lanciarius', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Javelin'], options=LRSK)],
    'Sword and javelins. May have buckler or shield (+1 pt), throwing spear (+1 pt), darts (+1 pt). May replace javelins with sling (free), bow (+1 pt) or crossbow/staff sling (+2 pts; both count as crossbows). Skirmishers.', page='25'))
LR.append(U('Infantry', 'Skirmishers', [M('Skirmisher', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], options=LRSK)],
    'Sword and javelins. May have buckler or shield (+1 pt), throwing spear (+1 pt), darts (+1 pt). May replace javelins with sling (free), bow (+1 pt) or crossbow/staff sling (+2 pts; both count as crossbows). Skirmishers.', page='25'))
LR.append(U('Infantry', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Each machine has a crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. One artillery piece per 500 points in the army.', page='25'))
LR.append(U('Infantry', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Each machine has a crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit. One artillery piece per 500 points in the army.', page='25'))
LR_LIM = {'Cavalry': ('max', 75), 'Infantry': ('max', 75)}
LR_NOTES = ('LATE ROMAN ARMY LIST (Armies of Antiquity, pp.24-25), AD 285-475.\n'
  'Characters: the army may have a General and an Army Battle Standard. Cavalry up to three quarters of the points; Infantry up to three quarters; Barbarian Allies up to half; one artillery piece per 500 points in the army.\n'
  'Guard Troops: "Guard" marks any top-quality unit. The Craig Davey Option (optional): count Guard units with the characteristics of the ordinary troops in the entry below them, but drilled and stubborn, at the same points cost. Not built; use the ordinary entry and add the rules by hand.\n'
  'Shield Wall: heavy infantry may form a shield wall instead of moving; all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit while the unit has not moved or lost a round of close combat.\n'
  'Combined Formations: heavy and auxiliary infantry may be combined with archers into one regiment, the archers in the rear ranks, losing light infantry status; casualties come from the infantry models first. Not built as a combined unit (field the archers separately).\n'
  'Barbarian Allies (not built here: make a separate small roster): numeri, symmachiarii or foederati from the Barbarian and Nomadic Hordes lists, up to half the points.')
LISTS.append(('LR', 'Late Roman (Armies of Antiquity)', 'Late_Roman_Armies_of_Antiquity.cat', LR, LR_LIM, LR_NOTES, None))
PTSLIM.append(('LR', 'Bolt Thrower', 500, ['Stone Thrower']))
PTSLIM.append(('LR', 'Stone Thrower', 500, ['Bolt Thrower']))

# ------------------------------------------------------------------ CATAPHRACT (book pp.26-27)
CT = []
CT.append(U('Characters', 'Army General', [M('General', '4 3 5 3 3 3 5 2 9', 128, weapons=['Hand Weapon'], rules=['Army General'], options=[('Light armour', 3), ('Heavy armour (replaces light armour)', 4), ('Kontos', 2), ('Javelins', 2), ('Warhorse', 4), ('Barding (-1 M)', 4)])],
    'Armed with a hand weapon and bow. May have light armour (+3 pts), heavy armour (+4 pts), kontos (+2 pts), javelins (+2 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). 0-1.', mx=1, page='27'))
CT.append(U('Characters', 'Army Standard', [M('Standard Bearer', '4 3 4 3 3 2 5 2 9', 65, weapons=['Hand Weapon'], rules=['Army Standard'], options=[('Light armour', 3), ('Heavy armour (replaces light armour)', 4), ('Warhorse', 4), ('Barding (-1 M)', 4)])],
    'Armed with a hand weapon. May have light armour (+3 pts), heavy armour (+4 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). 0-1.', mx=1, page='27'))
CT.append(U('Cavalry', 'Cataphracts', [M('Cataphract Cavalryman', '5 4 4 3 3 1 3 1 8', 26, mn=5, weapons=['Hand Weapon', 'Kontos', 'Light Armour'], rules=['Cataphracts (Armies of Antiquity)'], options=[('Additional hand weapon', 2), ('Javelins or darts', 2), ('Short bow', 2), ('Buckler', 1), ('Shield', 2), ('Heavy armour (replaces light armour)', 1)])],
    'Sword, kontos and light armour on a barded horse. May have additional hand weapons (+2 pts), javelin/darts (+2 pts), short bow (+2 pts), buckler (+1 pt), shield (+2 pts) and heavy armour (+1 pt). Cataphracts count rank bonus up to +3 and may not march.', page='27'))
CTLC = [('Bow', 2), ('Throwing spear', 2), ('Shield', 2), ('Javelins', 1)]
CT.append(U('Cavalry', 'Nomad Horsemen', [M('Nomad Horseman', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon'], rules=['Feigned Flight', 'Parthian Shot', 'Expert Horsemen'], options=CTLC)],
    'Hand weapon. May have bows (+2 pts), throwing spears (+2 pts), shields (+2 pts) and javelins (+1 pt). Light Cavalry. May use the Feigned Flight, Parthian Shot and Expert Horsemen rules from the Nomadic Hordes list.', page='27'))
CT.append(U('Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon'], options=CTLC + [('Light armour', 2)])],
    'Hand weapon. May have bows (+2 pts), throwing spears (+2 pts), shields (+2 pts) and javelins (+1 pt). May have light armour (+2 pts). Light Cavalry.', page='27'))
CTSP = [('Large shield (replaces shield)', 1)]
CT.append(U('Infantry', 'Guard Spearmen', [M('Guard Spearman', '4 4 4 3 3 1 4 1 8', 12, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=CTSP + [('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. May have large shield (+1 pt), light armour (+2 pts). 0-1.', mx=1, page='27'))
CT.append(U('Infantry', 'Levy Spearmen', [M('Levy Spearman', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=CTSP + [('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. May have large shield (+1 pt), light armour (+2 pts).', page='27'))
CT.append(U('Infantry', 'City Militia', [M('Militiaman', '4 2 2 3 3 1 2 1 5', 3, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['City Militia (Cataphract)'], options=CTSP)],
    'Hand weapon, thrusting spear and shield. May have large shield (+1 pt). Militia cause fear in all enemy troops apart from skirmishers.', page='27'))
CT.append(U('Infantry', 'Guard Archers', [M('Guard Archer', '4 4 4 3 3 1 4 1 8', 11, mn=5, weapons=['Hand Weapon', 'Bow'])],
    'Hand weapon and bow. Light Infantry. 0-1.', mx=1, page='27'))
CT.append(U('Infantry', 'Levy Archers', [M('Levy Archer', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'])],
    'Hand weapon and bow. Light Infantry.', page='27'))
CT.append(U('Infantry', 'Skirmishers', [M('Skirmisher', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Javelin', 'Shield'], options=[('Bow instead of javelins and shield', 0), ('Sling instead of javelins (free)', 0)])],
    'Javelins and shield, or bow. May replace javelins with sling at no additional cost. Skirmishers. (The printed Movement is 8, apparently a misprint; entered as 4.)', page='27'))
CT.append(U('Special Troops', 'Arab Camel Riders', [M('Camel Rider', '6 3 3 3 3 1 3 1 5', 15, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Camels'], options=[('Spear', 1), ('Javelins', 1), ('Shield', 1), ('Light armour', 2), ('Barding (-1 M)', 4)])],
    'Hand weapon and bow. May have spears (+1 pt), javelins (+1 pt), shields (+1 pt), light armour (+2 pts) and barding (+4 pts). Cause fear in enemy cavalry. 0-1.', mx=1, page='27'))
CT.append(U('Special Troops', 'Elephants', [
    M('Indian Elephant', '6 4 0 7 6 6 3 4 4', 150, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 6, mn=0, mx=5, key='crew', weapons=['Hand Weapon', 'Javelin'], options=[('Light armour', 2), ('Thrusting spear', 1), ('Shield', 1)])],
    'Unarmed mahout and up to five crew armed with javelins at +6 pts per model. The crew may have light armour (+2 pts), thrusting spears or shields (+1 pt). One elephant per 1,000 points in the army.', page='27'))
CT.append(U('Special Troops', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. No more than one artillery piece per infantry unit in the army (not enforced). One artillery piece per 500 points.', page='27'))
CT.append(U('Special Troops', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit. No more than one artillery piece per infantry unit in the army (not enforced). One artillery piece per 500 points.', page='27'))
CT_LIM = {'Cavalry': ('min', 25), 'Infantry': ('max', 50), 'Special Troops': ('max', 25)}
CT_NOTES = ('CATAPHRACT ARMY LIST (Armies of Antiquity, pp.26-27): Parthian, Palmyrene and Sassanid Persian armies, 50 BC - AD 600.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Cavalry at least a quarter of the points; Infantry up to half; Special Troops up to a quarter, with one artillery piece per 500 points and one elephant per 1,000 points.\n'
  'Cataphracts: count their rank bonus up to a maximum of +3 and may not march.')
LISTS.append(('CT', 'Cataphract (Armies of Antiquity)', 'Cataphract_Armies_of_Antiquity.cat', CT, CT_LIM, CT_NOTES, None))
PTSLIM.append(('CT', 'Elephants', 1000, []))
PTSLIM.append(('CT', 'Bolt Thrower', 500, ['Stone Thrower']))
PTSLIM.append(('CT', 'Stone Thrower', 500, ['Bolt Thrower']))

# ------------------------------------------------------------------ NOMADIC HORDES (book pp.30-31)
NH = []
NHCH = [('Light armour', 3), ('Throwing spear', 2), ('Shield', 2), ('Horse (M8)', 0), ('Barding (-1 M)', 4)]
NH.append(U('Characters', 'Army General', [M('General', '4 6 6 4 4 3 6 4 10', 195, weapons=['Hand Weapon', 'Bow'], rules=['Army General'], options=NHCH)],
    'Armed with a hand weapon and bow. May have light armour (+3 pts), throwing spear (+2 pts), shield (+2 pts). May have a horse (free, increases Movement to 8"); the horse may have barding (+4 pts). If mounted, counts as Nomadic cavalry. 0-1.', mx=1, page='31'))
NH.append(U('Characters', 'Army Standard', [M('Standard Bearer', '4 5 5 4 4 2 5 3 9', 95, weapons=['Hand Weapon', 'Bow'], rules=['Army Standard'], options=NHCH)],
    'Armed with a hand weapon and bow. May have light armour (+3 pts), throwing spear (+2 pts), shield (+2 pts). May have a horse (free, increases Movement to 8"); the horse may have barding (+4 pts). If mounted, counts as Nomadic cavalry. 0-1.', mx=1, page='31'))
NH.append(U('Cavalry', 'Noble Cavalry', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Bow', 'Light Armour'], rules=['Nomad Cavalry'], options=[('Throwing spear', 2), ('Kontos', 3), ('Shield', 2), ('Barding (-1 M)', 4)])],
    'Sword, bow and light armour. May have throwing spear (+2 pts), kontos (+3 pts), shield (+2 pts), barding (+4 pts). Light Cavalry. Nomad Cavalry. There must be at least three times as many Nomadic horse archer models in the army as there are Noble cavalry models.', page='31'))
NH.append(U('Cavalry', 'Nomad Horse Archers', [M('Horse Archer', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Nomad Cavalry'], options=[('Throwing spear', 1), ('Shield', 2)])],
    'Hand weapon and bow. May have throwing spear (+1 pt), shield (+2 pts). Light Cavalry. Nomad Cavalry.', page='31'))
NH.append(U('Special Troops, Allies & Mercenaries', 'Human Shields', [M('Human Shield', '3 1 1 1 2 1 1 1 2', 1, mn=5)],
    'No equipment. Will not charge. May not have a Leader, Standard or Musician, or be joined by characters. Other units ignore Human Shields for the purposes of Panic tests.', page='31'))
NH.append(U('Special Troops, Allies & Mercenaries', 'Camel Riders', [M('Camel Rider', '6 3 3 3 3 1 3 1 5', 15, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Camels'], options=[('Throwing spear', 1), ('Shield', 1), ('Light armour', 2)])],
    'Hand weapon and bow. May have throwing spear (+1 pt), shields (+1 pt), light armour (+2 pts). Cause fear in enemy cavalry. 0-1.', mx=1, page='31'))
NH.append(U('Special Troops, Allies & Mercenaries', 'Wagon Laager', [
    M('Wagon', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Defender', '4 3 3 3 3 1 3 1 7', 0, mn=5, mx=5, key='crew', weapons=['Hand Weapon', 'Javelin'], options=[('Bow', 2)])],
    'Each wagon has a crew of five defenders armed with hand weapons and javelins. Any number of defenders may have bows (+2 pts). All wagons must be set up as a single group with no more than 2" between each wagon, within 6" of the Nomadic Horde player\'s table edge. Wagons count as a defended obstacle and provide hard cover. Defenders are skirmishers forming a single unit that must remain with the wagons unless they break or flee. 0-1 (one laager, any number of wagons: take several).', page='31'))
NH.append(U('Special Troops, Allies & Mercenaries', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. One artillery piece per 1,000 points in the army.', page='31'))
NH.append(U('Special Troops, Allies & Mercenaries', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit. One artillery piece per 1,000 points in the army.', page='31'))
NH_LIM = {'Cavalry': ('min', 50), 'Special Troops, Allies & Mercenaries': ('max', 25)}
NH_NOTES = ('NOMADIC HORDES ARMY LIST (Armies of Antiquity, pp.30-31): Scythians, Huns, Mongols and other steppe horse archers.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Cavalry at least half the points; Special Troops, Allies and Mercenaries up to a quarter, with one artillery piece per 1,000 points.\n'
  'Special Deployment: Nomadic horse archers may make a free march move after both sides have deployed (not a charge, and no shooting afterwards). Expert Horsemen: no -1 to hit for shooting after moving (not after a charge or march). Parthian Shot: a normal move immediately after shooting in the shooting phase (not a charge reaction; may not march). Feigned Flight: if Nomadic cavalry flee or fire & flee as a charge reaction they rally at the end of the move and may reform facing any direction; the charger still counts as charging. Hidden Ambush Force: one unit may be set up in hiding anywhere out of sight of the opponent\'s deployment zone, and is deployed at the start of the Nomadic player\'s first turn.\n'
  'Allies (not built here: make a separate small roster): from one of the Barbarian, Indian or Chinese lists.')
LISTS.append(('NH', 'Nomadic Hordes (Armies of Antiquity)', 'Nomadic_Hordes_Armies_of_Antiquity.cat', NH, NH_LIM, NH_NOTES, None))
FIGS.append(('NH', 'Noble Cavalry', 'Nomad Horse Archers', 3))   # figures of A <= figures of B / per
PTSLIM.append(('NH', 'Bolt Thrower', 1000, ['Stone Thrower']))
PTSLIM.append(('NH', 'Stone Thrower', 1000, ['Bolt Thrower']))

# ------------------------------------------------------------------ BYZANTINE (book pp.28-29)
BZ = []
BZCH = [('Light armour', 3), ('Heavy armour (replaces light armour)', 4), ('Warhorse', 4), ('Barding (-1 M)', 4)]
BZ.append(U('Characters', 'Army General', [M('General', '4 5 5 4 4 3 6 3 9', 200, weapons=['Hand Weapon'], rules=['Army General', 'Strategicon'], options=BZCH)],
    'Armed with a hand weapon. May have light armour (+3 pts), heavy armour (+4 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). (Printed Movement is 8, the mounted value; entered as 4 with the warhorse as an option.) 0-1.', mx=1, page='29'))
BZ.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon'], rules=['Army Standard'], options=BZCH)],
    'Armed with a hand weapon. May have light armour (+3 pts), heavy armour (+4 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). (Printed Movement is 8, the mounted value; entered as 4 with the warhorse as an option.) 0-1.', mx=1, page='29'))
BZ.append(U('Cavalry', 'Cataphracts', [M('Cataphract Cavalryman', '8 4 4 3 3 1 3 1 8', 26, mn=5, weapons=['Hand Weapon', 'Kontos', 'Light Armour'], rules=['Byzantine Cataphracts'], options=[('Buckler', 1), ('Javelins', 2), ('Darts', 2), ('Barding (-1 M)', 4), ('Heavy armour (replaces light armour)', 2), ('Shield (replaces buckler)', 1), ('Lance instead of kontos', 1)])],
    'Sword, kontos and light armour. May have buckler (+1 pt). Any model may have javelins (+2 pts), darts (+2 pts), barding (+4 pts). May replace light armour with heavy armour (+2 pts) and buckler with shield (+1 pt). May replace kontos with lance (+1 pt) or thrusting spear (free). Count rank bonus of +1 when charging. May combine with Cataphract Archers.', page='29'))
BZ.append(U('Cavalry', 'Cataphract Archers', [M('Cataphract Archer', '8 4 4 3 3 1 3 1 8', 24, mn=5, weapons=['Bow'], options=[('Buckler', 1), ('Javelins', 2), ('Darts', 2), ('Barding (-1 M)', 4), ('Light armour', 3)])],
    'Bow. May have buckler (+1 pt). Any model may have javelins (+2 pts), darts (+2 pts), barding (+4 pts) and light armour (+3 pts). Archers may not be taken on their own; they must be combined with Cataphracts (see Combined Formations; the combination is not enforced).', page='29'))
BZ.append(U('Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 4 4 3 3 1 3 1 8', 23, mn=5, weapons=['Throwing Spear', 'Javelin', 'Buckler'], options=[('Bow instead of thrusting spear and javelins', 0), ('Shield (replaces buckler)', 2), ('Large shield (replaces buckler)', 3), ('Kontos instead of throwing spear', 1)])],
    'Thrusting spears, javelins and buckler, or bow and buckler. May replace buckler with shield (+2 pts) or large shield (+3 pts). May replace thrusting spear with kontos (+1 pt). Light Cavalry.', page='29'))
BZ.append(U('Infantry', 'Skutatoi', [M('Spearman', '4 4 4 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Shield Wall (Late Roman)'], options=[('Light armour', 3), ('Javelins', 2), ('Darts', 1), ('Large shield (replaces shield)', 1)])],
    'Sword, thrusting spear, shield. May have light armour (+3 pts), javelins (+2 pts) and darts (+1 pt). May replace shield with large shield (+1 pt). May form shield wall instead of moving; all enemy attacks from the front are -1 to hit.', page='29'))
BZ.append(U('Infantry', 'Archers', [M('Archer', '4 3 4 3 3 1 3 1 8', 10, mn=5, weapons=['Bow'], options=[('Buckler', 1)])],
    'Bow. May have buckler (+1 pt). Light Infantry. May be combined with Skutatoi.', page='29'))
BZ.append(U('Infantry', 'Psiloi', [M('Psiloi', '4 3 4 3 3 1 3 1 6', 7, mn=5, weapons=['Javelin', 'Buckler'], options=[('Sling instead of javelins (free)', 0), ('Bow instead of javelins/sling', 1), ('Crossbow instead of javelins/sling', 2), ('Staff sling instead of javelins/sling', 2), ('Shield (replaces buckler)', 1)])],
    'Javelins or sling, and buckler. May replace javelins/sling with bow (+1 pt), crossbow (+2 pts) or staff sling (+2 pts, counts as crossbow). May replace buckler with shield (+1 pt). Skirmishers.', page='29'))
BZ.append(U('Allies & Mercenaries', 'Varangian Guard', [M('Varangian', '4 4 3 3 4 1 4 1 9', 20, mn=5, weapons=['Two-handed Weapon', 'Light Armour'], rules=['Stubborn'], options=[('Rhomphaia (counts as halberd) instead of axe (free)', 0), ('Shield', 2), ('Javelins', 1)])],
    'Double-handed axe and light armour. May replace axe with rhomphaia (counts as halberd) at no additional cost. May have shield (+2 pts) and javelins (+1 pt). Stubborn. 0-1.', mx=1, page='29'))
BZ.append(U('Allies & Mercenaries', 'Bolt Thrower', [
    M('Bolt Thrower', '- - - - 6 2 - - -', 50, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. No more than one artillery piece per Skutatoi unit in the army (not enforced). One artillery piece per 500 points.', page='29'))
BZ.append(U('Allies & Mercenaries', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit. No more than one artillery piece per Skutatoi unit in the army (not enforced). One artillery piece per 500 points.', page='29'))
BZ_LIM = {'Cavalry': ('min', 25), 'Infantry': ('max', 75), 'Allies & Mercenaries': ('max', 25)}
BZ_NOTES = ('BYZANTINE ARMY LIST (Armies of Antiquity, pp.28-29), 7th-11th centuries AD.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Cavalry at least a quarter of the points; Infantry up to three quarters; Allies & Mercenaries up to a quarter, with one artillery piece per 500 points.\n'
  'Combined Formations: skutatoi may be combined with archers into one regiment (archers in the rear ranks, losing light infantry status), and cataphracts may include bow-armed models in the same unit (the Cataphract Archers entry; they must be combined with Cataphracts). Casualties are taken from the front rank first. Not enforced; field the pieces as separate units and combine them on the table.\n'
  'Strategicon (choose one at the start of battle if the army has a General): Flank March (play the Flank Attack scenario as the flankers), Hidden Ambush Force (one unit set up in hiding, out of sight of the opponent\'s deployment zone, deployed at the start of your first turn) or Scouts (your opponent sets up first).\n'
  'Allies (not built here: make a separate small roster): troops from the Cataphract and/or Nomadic Hordes lists.')
LISTS.append(('BZ', 'Byzantine (Armies of Antiquity)', 'Byzantine_Armies_of_Antiquity.cat', BZ, BZ_LIM, BZ_NOTES, None))
PTSLIM.append(('BZ', 'Bolt Thrower', 500, ['Stone Thrower']))
PTSLIM.append(('BZ', 'Stone Thrower', 500, ['Bolt Thrower']))

# ------------------------------------------------------------------ ARABS AND SARACENS (book pp.32-33)
AR = []
ARCH = [('Light armour', 3), ('Shield', 2), ('Large shield', 3), ('Warhorse', 4), ('Barding (-1 M)', 4)]
AR.append(U('Characters', 'Army General', [M('General', '4 5 5 4 3 3 6 2 9', 140, weapons=['Hand Weapon'], rules=['Army General', 'Bedouin and Turkish Cavalry'], options=ARCH)],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). May be designated Bedouin or Turkish cavalry (free). 0-1.', mx=1, page='33'))
AR.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon'], rules=['Army Standard', 'Bedouin and Turkish Cavalry'], options=ARCH[:2] + ARCH[3:])],
    'Armed with a sword. May have light armour (+3 pts), shield (+2 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). May be designated Bedouin or Turkish cavalry (free). 0-1.', mx=1, page='33'))
AR.append(U('Cavalry', 'Arab Heavy Cavalry', [M('Arab Cavalryman', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Light Armour', 'Shield'], rules=['Bedouin and Turkish Cavalry'])],
    'Thrusting spear, sword, light armour and shield. May be designated Bedouin cavalry (at no additional cost).', page='33'))
AR.append(U('Cavalry', 'Iranian Heavy Cavalry', [M('Iranian Cavalryman', '6 4 4 3 3 1 4 1 7', 17, mn=5, weapons=['Bow', 'Hand Weapon', 'Light Armour'], options=[('Buckler', 1)])],
    'Bow, hand weapon and light armour. May have a buckler (+1 pt).', page='33'))
AR.append(U('Cavalry', 'Askaris, Ghulams or Mamluks', [M('Mamluk Cavalryman', '8 4 4 3 3 1 4 1 7', 28, mn=5, weapons=['Bow', 'Hand Weapon', 'Light Armour', 'Shield'], rules=['Bedouin and Turkish Cavalry'], options=[('Throwing spear', 2), ('Barding (-1 M)', 4)])],
    'Bow, hand weapon, light armour and shield. May have thrusting spear (+2 pts), horse barding (+4 pts). Turkish Cavalry.', page='33'))
AR.append(U('Cavalry', 'Arab Light Cavalry', [M('Arab Light Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Shield'], rules=['Bedouin and Turkish Cavalry'], options=[('Light armour', 2)])],
    'Thrusting spear, sword and shield. May have light armour (+2 pts). Light Cavalry and Bedouin Cavalry.', page='33'))
AR.append(U('Cavalry', 'Turkish Light Cavalry', [M('Turkish Light Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Bedouin and Turkish Cavalry'], options=[('Light armour', 2), ('Shield', 1), ('Throwing spear', 1)])],
    'Bow and hand weapon. May have light armour (+2 pts), shield (+1 pt), thrusting spear (+1 pt). Light Cavalry and Turkish Cavalry.', page='33'))
AR.append(U('Infantry', 'Arab Spearmen', [M('Arab Spearman', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Shield'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Throwing spear instead of thrusting spear (free)', 0)])],
    'Thrusting spear, sword and shield. May have light armour (+2 pts), large shield (+1 pt). May have throwing spear (free) instead of thrusting spear. Combined Formation; may include archers of the same origin.', page='33'))
AR.append(U('Infantry', 'Sudanese Spearmen', [M('Sudanese Spearman', '4 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Shield'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Throwing spear instead of thrusting spear (free)', 0)])],
    'Thrusting spear, sword and shield. May have light armour (+2 pts), large shield (+1 pt). May have throwing spear (free) instead of thrusting spear. Combined Formation; may include archers of the same origin.', page='33'))
AR.append(U('Infantry', 'Arab Archers', [M('Arab Archer', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Bow', 'Hand Weapon'], options=[('Light armour', 2), ('Buckler', 1)])],
    'Short bow and sword. May have light armour (+2 pts), buckler (+1 pt). Light Infantry. Alternatively Combined Formation: may be included in a unit of spearmen of the same origin.', page='33'))
AR.append(U('Infantry', 'Sudanese Archers', [M('Sudanese Archer', '4 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Bow', 'Hand Weapon'], options=[('Light armour', 2), ('Buckler', 1)])],
    'Short bow and sword. May have light armour (+2 pts), buckler (+1 pt). Light Infantry. Alternatively Combined Formation: may be included in a unit of spearmen of the same origin.', page='33'))
AR.append(U('Infantry', 'Religious Volunteers', [M('Volunteer', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'], options=[('Light armour', 2), ('Throwing spear', 1), ('Stubborn', 3)])],
    'Sword and shield. May have light armour (+2 pts), throwing spears (+1 pt). May be stubborn (+3 pts). Warband.', page='33'))
AR.append(U('Infantry', 'Auxiliary Infantry', [M('Auxiliary', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Shield'], options=[('Javelins instead of throwing spear (free)', 0)])],
    'Throwing spear, hand weapon and shield. May have javelins (free) instead of throwing spear. Light Infantry.', page='33'))
AR.append(U('Special Units', 'Ghaznavid Elephants', [
    M('Elephant', '6 4 0 7 6 6 3 4 4', 173, mn=1, mx=1, key='el'),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Throwing Spear', 'Bow', 'Hand Weapon'])],
    'Unarmed mahout and two crew armed with a thrusting spear, short bow and hand weapons. Elephant: may stampede; causes fear in infantry and terror in cavalry. One elephant per 1,000 points in the army.', page='33'))
AR.append(U('Special Units', 'Naffatun', [M('Naffatun', '5 3 3 3 3 1 3 1 7', 20, mn=1, mx=2)],
    'Incendiary projectiles and hand weapon. Light Infantry. Naffatun must be incorporated into units of light infantry (archers or auxiliary); a maximum of two may be included in each light infantry unit and must be placed in the front rank (not enforced; take them as a separate unit of one or two and combine on the table). Naffatun cause terror, but not until they have launched their projectiles for the first time in a battle. Projectiles: range as javelins (max 8"), Strength 8.', page='33'))
AR_LIM = {'Cavalry': ('max', 75), 'Infantry': ('min', 25), 'Special Units': ('max', 25)}
AR_NOTES = ('ARABS AND SARACENS ARMY LIST (Armies of Antiquity, pp.32-33), AD 630 - 1300.\n'
  'Characters: the army may have a General and an Army Battle Standard. Cavalry up to three quarters of the points; Infantry at least a quarter; Special Units up to a quarter, with one elephant per 1,000 points.\n'
  'Bedouin and Turkish Cavalry: cavalry in the list may turn without penalty during their move and change formation once during movement by any number of ranks at no penalty (including while marching). All bow-armed Turkish cavalry (Askaris, Ghulams, Mamluks and Turkish light cavalry) may make a normal move immediately after shooting in the shooting phase (Parthian Shot; not a charge reaction; may not march).\n'
  'Combined Formations: where specified, archers may be combined with other infantry in one regiment, in the rear ranks, losing light infantry status; casualties are taken from the other infantry first.')
LISTS.append(('AR', 'Arabs and Saracens (Armies of Antiquity)', 'Arabs_and_Saracens_Armies_of_Antiquity.cat', AR, AR_LIM, AR_NOTES, None))
PTSLIM.append(('AR', 'Ghaznavid Elephants', 1000, []))

# ------------------------------------------------------------------ SAXON (book pp.34-35)
SX = []
SX.append(U('Characters', 'Army General', [M('General', '4 6 4 4 4 3 6 3 9', 170, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General'], options=[('Throwing spear or axe', 2), ('Additional hand weapon instead of shield', 2), ('Double-handed axe instead of shield', 2)])],
    'Hand weapon, light armour and shield. May have a throwing spear/axe (+2 pts). May replace shield with additional hand weapon (+2 pts) or double-handed axe (+2 pts). 0-1.', mx=1, page='35'))
SX.append(U('Characters', 'Standard Bearer', [M('Standard Bearer', '4 5 4 4 4 2 5 2 8', 95, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army Standard'])],
    'Hand weapon, light armour and shield. 0-1.', mx=1, page='35'))
SX.append(U('Infantry', 'Huscarls', [M('Huscarl', '4 4 3 3 4 1 4 1 9', 20, mn=5, weapons=['Two-handed Weapon', 'Light Armour', 'Shield'], rules=['Stubborn', 'Huscarls (Armies of Antiquity)', 'Shield Wall (Saxon)'], options=[('Spear instead of double-handed axe (free)', 0), ('Javelins', 1)])],
    'Double-handed axe or spear, light armour and shield. May have javelins (+1 pt). Stubborn. May combine with Fyrd (see Huscarls rule). May form a shield wall. 0-1 unit.', mx=1, page='35'))
SX.append(U('Infantry', 'Select Fyrd', [M('Select Fyrd', '4 4 3 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Shield Wall (Saxon)', 'Fyrd Warband Psychology'], options=[('Light armour', 3)])],
    'Hand weapon, thrusting spear and shield. May have light armour (+3 pts). May form a shield wall. Subject to Warband psychology unless within 12" of the army\'s General. The army must have at least as many units of Fyrd as it has of Select Fyrd.', page='35'))
SX.append(U('Infantry', 'Fyrd Spearmen', [M('Fyrd', '4 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Shield Wall (Saxon)', 'Fyrd Warband Psychology'])],
    'Hand weapon, thrusting spear and shield. May form a shield wall. Subject to Warband psychology unless within 12" of the army\'s General.', page='35'))
SX.append(U('Special Troops & Mercenaries', 'Fyrd Skirmishers', [M('Fyrd Skirmisher', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Javelin'], options=[('Sling instead of javelins (free)', 0), ('Bow instead of javelins', 1)])],
    'Javelins or sling. Up to one unit in every two may have bows (+1 pt; not enforced). Skirmishers.', page='35'))
SX_LIM = {'Infantry': ('min', 50), 'Special Troops & Mercenaries': ('max', 25)}
SX_NOTES = ('SAXON ARMY LIST (Armies of Antiquity, pp.34-35), the Anglo-Saxon fyrd and huscarls, 5th century to 1066.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Infantry at least half the points; Special Troops & Mercenaries up to a quarter.\n'
  'Huscarls: the army may include a single unit of Huscarls, either alone or split up and added to units of Fyrd. Huscarls must be placed in the front rank of the unit they are added to, never behind it. While at least half (rounding up) of the front rank are Huscarls the unit is not subject to Warband psychology, has Leadership 9 and is stubborn. Once the front rank has under 50% Huscarls the unit is subject to Warband psychology with Leadership 6 (Select Fyrd) or 5 (Fyrd). Half of all missile casualties on a combined Huscarl/Fyrd unit fall on Huscarl models. In hand-to-hand combat, enemy models in base contact with a Huscarl must fight against him.\n'
  'Huscarl Hatred: if the army has a General and he is slain, Huscarls become subject to hatred for the rest of the battle, and so does any unit where Huscarls make up at least half the front rank.\n'
  'Shield Wall: units of Huscarls and Fyrd spearmen may form a shield wall instead of moving; all enemy attacks from the front (shooting and hand-to-hand) suffer -1 to hit while the unit has not moved or lost a round of close combat.\n'
  'Viking Mercenaries (not built here: make a separate small roster): the army may include Viking Huscarls from the Viking army list.')
LISTS.append(('SX', 'Saxon (Armies of Antiquity)', 'Saxon_Armies_of_Antiquity.cat', SX, SX_LIM, SX_NOTES, None))
RATIOS.append(('SX', 'Select Fyrd', ['Fyrd Spearmen'], 1))

# ------------------------------------------------------------------ VIKING (book pp.36-37)
VK = []
VKCH = [('Throwing spear or axe', 2), ('Additional hand weapon instead of shield', 2), ('Double-handed axe instead of shield', 2)]
VK.append(U('Characters', 'Army General', [M('General', '4 6 4 5 4 3 6 3 10', 200, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General'], options=VKCH)],
    'Hand weapon, light armour and shield. May have throwing spear/axe (+2 pts). May replace shield with additional hand weapon (+2 pts) or double-handed axe (+2 pts). 0-1.', mx=1, page='37'))
VK.append(U('Characters', 'Standard Bearer', [M('Standard Bearer', '4 5 4 4 4 2 5 2 9', 100, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army Standard'], options=VKCH)],
    'Hand weapon, light armour and shield. May have throwing spear (+2 pts). May replace shield with additional hand weapon (+2 pts) or double-handed axe (+2 pts). 0-1.', mx=1, page='37'))
VK.append(U('Infantry', 'Huscarls', [M('Huscarl', '4 4 3 3 4 1 4 1 8', 14, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Viking Huscarls'], options=VKCH)],
    'Hand weapon, light armour and shield. May have throwing spear/axe (+2 pts). May replace shield with additional hand weapon (+2 pts) or double-handed axe (+2 pts). Light Infantry. Cause fear in enemy troops with Leadership 7 or less. Different models may be armed with different weapons in the same unit (not enforced).', page='37'))
VK.append(U('Infantry', 'Bondir', [M('Bondi', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. May have light armour (+2 pts).', page='37'))
VK.append(U('Archers & Unusual Troops', 'Archers', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Sling instead of bow (free)', 0), ('Light armour', 2)])],
    'Hand weapon and bow. May replace bow with sling. May have light armour (+2 pts). Light Infantry.', page='37'))
VK.append(U('Archers & Unusual Troops', 'Thralls', [M('Thrall', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Javelin'], options=[('Thrusting spear instead of javelins (free)', 0), ('Shield', 1)])],
    'Javelins or thrusting spear. May have shield (+1 pt). Light Infantry.', page='37'))
VK.append(U('Archers & Unusual Troops', 'Beserkers', [M('Beserker', '4 4 3 4 3 1 4 1 8', 18, mn=1, mx=3, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Beserkers'], options=VKCH)],
    'Hand weapon, light armour and shield. May have throwing spear/axe (+2 pts). May replace shield with additional hand weapon (+2 pts) or double-handed axe (+2 pts). Beserkers. 0-3 per unit of Huscarls: a unit of Huscarls can contain up to three Beserkers (not enforced; add them to a Huscarl unit on the table).', page='37'))
VK.append(U('Archers & Unusual Troops', 'Ulfhednar', [M('Ulfhednar', '5 4 3 4 4 1 4 1 8', 18, mn=5, weapons=['Hand Weapon'], rules=['Frenzy'], options=[('Throwing spear or axe', 2), ('Additional hand weapon', 2)])],
    'Hand weapon. May have throwing spear/axe (+2 pts), additional hand weapon (+2 pts). Frenzied. Skirmishers. 0-1.', mx=1, page='37'))
VK_LIM = {'Infantry': ('min', 50), 'Archers & Unusual Troops': ('max', 25)}
VK_NOTES = ('VIKING ARMY LIST (Armies of Antiquity, pp.36-37), 9th-10th century raiders.\n'
  'Designer\'s note: a large Anglo-Danish field army is better represented by the Saxon list; early Saxon raiders are better represented by this list (but not Beserkers and Ulfhednar).\n'
  'Characters: the army may have a General and an Army Standard Bearer. Infantry at least half the points; Archers & Unusual Troops up to a quarter.\n'
  'Beserkers: a unit of Viking Huscarls can contain up to three Beserkers, represented by ferocious models in the front rank; they may be removed as casualties at the player\'s choice. If an enemy unit is within 12" of the unit at the start of a Viking turn, roll 2D6 for each Beserker: if the roll is equal to or greater than the distance to the nearest enemy, he charges the closest enemy immediately (automatically if the unit is within 2" of an enemy or in close combat). He causes D6 automatic Strength 5 hits and is then removed from play.')
LISTS.append(('VK', 'Viking (Armies of Antiquity)', 'Viking_Armies_of_Antiquity.cat', VK, VK_LIM, VK_NOTES, None))

# ------------------------------------------------------------------ THE NORMANS (book pp.38-39)
NM = []
NMCH = [('Heavy armour (replaces light armour)', 2), ('Lance', 3), ('Warhorse', 3)]
NM.append(U('Characters', 'Army General', [M('General', '4 6 6 4 4 3 6 4 9', 190, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General', 'Ferocious Charge'], options=NMCH)],
    'Armed with a sword, light armour and shield. May have heavy armour (+2 pts), lance (+3 pts), warhorse (+3 pts). The army must have a General. 0-1.', mx=1, page='39'))
NM.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 5 5 4 4 2 5 3 8', 100, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army Standard', 'Ferocious Charge'], options=NMCH)],
    'Armed with a sword, light armour and shield. May have heavy armour (+2 pts), lance (+3 pts), warhorse (+3 pts). 0-1.', mx=1, page='39'))
NM.append(U('Cavalry', 'Norman Knights', [M('Norman Knight Cavalryman', '8 4 3 3 3 1 4 1 8', 32, mn=5, weapons=['Hand Weapon', 'Lance', 'Light Armour', 'Shield'], rules=['Ferocious Charge', 'Knights Rank Bonus'], options=[('Heavy armour (replaces light armour)', 2), ('Fights on foot (M4, no warhorse)', -15)])],
    'Sword, lance, light armour and shield, riding warhorses. Any unit may have heavy armour (+2 pts). May fight on foot at a reduced cost of -15 points. Ferocious Charge. May count a rank bonus of up to +1 even though cavalry.', page='39'))
NM.append(U('Cavalry', 'Carolingian or Breton Knights', [M('Carolingian Knight Cavalryman', '8 4 3 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], rules=['Ferocious Charge', 'Knights Rank Bonus'], options=[('Thrusting spear instead of throwing spear (free)', 0)])],
    'Sword, thrusting or throwing spear, light armour and shield, riding warhorses. Ferocious Charge. May count a rank bonus of up to +1 even though cavalry.', page='39'))
NM.append(U('Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Throwing or thrusting spear instead of javelins (free)', 0)])],
    'Sword, javelins and shield. May replace javelins with throwing or thrusting spear (free). Light Cavalry.', page='39'))
NM.append(U('Infantry', 'Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. Any unit may have light armour (+2 pts).', page='39'))
NM.append(U('Infantry', 'Archers', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'])],
    'Hand weapon and bow. Light Infantry.', page='39'))
NM.append(U('Special Troops, Allies & Mercenaries', 'Mercenary Crossbowmen', [M('Crossbowman', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Crossbow'], options=[('Light armour', 2)])],
    'Sword and crossbow. May have light armour (+2 pts). Light Infantry.', page='39'))
NM.append(U('Special Troops, Allies & Mercenaries', 'Axemen', [M('Axeman', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Two-handed Weapon', 'Light Armour'])],
    'Double-handed sword or axe and light armour.', page='39'))
NM.append(U('Special Troops, Allies & Mercenaries', 'Skirmishers', [M('Skirmisher', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], options=[('Sling or staff sling instead of javelin (free)', 0)])],
    'Hand weapon and javelin or sling/staff sling. Skirmishers.', page='39'))
NM.append(U('Special Troops, Allies & Mercenaries', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone throwers may only be used during a siege (included for completeness). Range 48", Strength 7, no save, D3 wounds per hit. One artillery piece per 500 points.', page='39'))
NM_LIM = {'Cavalry': ('min', 25), 'Infantry': ('max', 50), 'Special Troops, Allies & Mercenaries': ('max', 25)}
NM_NOTES = ('NORMAN ARMY LIST (Armies of Antiquity, pp.38-39), from the rise of armoured cavalry under Charlemagne to the Third Crusade.\n'
  'Characters: the army must have a General (not enforced) and may have an Army Standard Bearer. Cavalry at least a quarter of the points; Infantry up to half; Special Troops, Allies & Mercenaries up to a quarter, with one artillery piece per 500 points.\n'
  'Ferocious Charge: if a unit noted as having a ferocious charge charges and wins the round of combat, its opponent automatically breaks with no Leadership test. Enemy units that normally ignore Break tests roll a D6: on 1-3 they are broken anyway, on 4-6 they hold.')
LISTS.append(('NM', 'Normans (Armies of Antiquity)', 'Normans_Armies_of_Antiquity.cat', NM, NM_LIM, NM_NOTES, None))
PTSLIM.append(('NM', 'Stone Thrower', 500, []))

# ------------------------------------------------------------------ CRUSADERS (book pp.40-41)
CR = []
CR.append(U('Characters', 'Army General', [M('General', '4 6 6 4 4 3 6 4 9', 195, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General', 'Ferocious Charge'], options=[('Heavy armour (replaces light armour)', 1), ('Double-handed weapon', 3), ('Lance', 3), ('Warhorse', 4), ('Barding (-1 M)', 4)])],
    'Shield, sword and light armour. May have heavy armour (+1 pt), double-handed weapon (+3 pts), lance (+3 pts). May ride a warhorse (+4 pts), which may have barding (+4 pts). 0-1.', mx=1, page='41'))
CR.append(U('Characters', 'Army Battle Standard', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 100, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army Standard', 'Ferocious Charge'], options=[('Heavy armour (replaces light armour)', 1), ('Warhorse', 4), ('Barding (-1 M)', 4)])],
    'Sword, shield and light armour. May have heavy armour (+1 pt). May ride a warhorse (+4 pts), which may have barding (+4 pts). 0-1.', mx=1, page='41'))
CRK = [('Heavy armour (replaces light armour)', 2), ('Horse barding (-1 M)', 4)]
CR.append(U('Cavalry', 'Secular Knights & Sergeants', [M('Secular Knight Cavalryman', '8 4 3 4 3 1 4 1 8', 35, mn=5, weapons=['Hand Weapon', 'Lance', 'Shield', 'Light Armour'], rules=['Ferocious Charge'], options=CRK)],
    'Sword, lance, shield, light armour; rides a warhorse. May have heavy armour (+2 pts). The warhorse may have horse barding (+4 pts). Ferocious Charge.', page='41'))
CR.append(U('Cavalry', 'Military Order Knights & Sergeants', [M('Military Order Cavalryman', '8 4 3 4 3 1 4 1 8', 40, mn=5, weapons=['Hand Weapon', 'Lance', 'Shield', 'Light Armour'], rules=['Ferocious Charge', 'Drilled', 'Stubborn'], options=CRK)],
    'Sword, lance, shield, light armour; rides a warhorse. May have heavy armour (+2 pts). The warhorse may have horse barding (+4 pts). Military Order brethren are drilled and stubborn. Ferocious Charge. See Military Orders: if any Military Order troops are fielded, two units of Military Order knights must be used.', page='41'))
CR.append(U('Cavalry', 'Turcopoles', [M('Turcopole', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Bow', 'Hand Weapon'], options=[('Light armour', 2), ('Shield', 1), ('Thrusting spear', 1)])],
    'Bow and hand weapon. May have light armour (+2 pts), shield (+1 pt), thrusting spear (+1 pt). Light Cavalry. Despite the name, Turcopoles are not Turkish cavalry.', page='41'))
DK = [('Heavy armour (replaces light armour)', 1), ('Thrusting spear', 2), ('Double-handed weapon', 3)]
CR.append(U('Infantry', 'Secular Dismounted Knights', [M('Dismounted Knight', '4 4 3 4 3 1 4 1 7', 15, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour'], options=DK)],
    'Sword, shield and light armour. May have heavy armour (+1 pt); may have thrusting spear (+2 pts) or double-handed weapon (+3 pts). Combined Formation; may include crossbowmen.', page='41'))
CR.append(U('Infantry', 'Military Order Dismounted Knights', [M('Military Order Dismounted Knight', '4 4 3 4 3 1 4 1 7', 20, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour'], rules=['Drilled', 'Stubborn'], options=DK)],
    'Sword, shield and light armour. May have heavy armour (+1 pt); may have thrusting spear (+2 pts) or double-handed weapon (+3 pts). Combined Formation; may include crossbowmen. Military Order dismounted knights are drilled and stubborn.', page='41'))
CR.append(U('Infantry', 'Secular Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Thrusting Spear', 'Hand Weapon', 'Shield'], options=[('Light armour', 2)])],
    'Thrusting spear, hand weapon and shield. May have light armour (+2 pts). Combined Formation; may include crossbowmen.', page='41'))
CR.append(U('Infantry', 'Military Order Spearmen', [M('Military Order Spearman', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Thrusting Spear', 'Hand Weapon', 'Shield'], rules=['Drilled'], options=[('Light armour', 2)])],
    'Thrusting spear, hand weapon and shield. May have light armour (+2 pts). Combined Formation; may include crossbowmen. Military Order foot sergeants are drilled, and may only be included in armies containing Military Order knights.', page='41'))
CR.append(U('Infantry', 'Secular Crossbowmen', [M('Crossbowman', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Crossbow', 'Hand Weapon'], options=[('Light armour', 2)])],
    'Crossbow and hand weapon. May have light armour (+2 pts). Light Infantry. Alternatively Combined Formation: may be included in a unit of dismounted knights or spearmen of the same origin.', page='41'))
CR.append(U('Infantry', 'Military Order Crossbowmen', [M('Military Order Crossbowman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Crossbow', 'Hand Weapon'], rules=['Drilled'], options=[('Light armour', 2)])],
    'Crossbow and hand weapon. May have light armour (+2 pts). Light Infantry. Alternatively Combined Formation: may be included in a unit of dismounted knights or spearmen of the same origin. Military Order crossbowmen are drilled, and may only be included in armies containing Military Order knights.', page='41'))
CR.append(U('Infantry', 'European Archers', [M('European Archer', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Bow', 'Hand Weapon'], options=[('Light armour', 2)])],
    'Short bow and hand weapon. May have light armour (+2 pts).', page='41'))
CR.append(U('Infantry', 'Syrian Archers', [M('Syrian Archer', '4 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Bow', 'Hand Weapon'], options=[('Light armour', 2)])],
    'Short bow and hand weapon. May have light armour (+2 pts).', page='41'))
CR.append(U('Infantry', 'Pilgrims', [M('Pilgrim', '5 3 3 3 3 1 3 1 7', 5, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Warband'], options=[('Shield', 1)])],
    'Mixed weapons (equivalent to javelins and a hand weapon). May have shield (+1 pt). Warband. Light Infantry.', page='41'))
CR.append(U('Special Troops & Allies', 'Stone Thrower', [
    M('Stone Thrower', '- - - - 7 3 - - -', 75, mn=1, mx=1, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
    M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Crew of two to five men armed with swords. May have light armour (+2 pts per crewman). Stone throwers may only be used during a siege (included for completeness). Range 48", Strength 7, no save, D3 wounds per hit. One artillery piece per 500 points.', page='41'))
CR_LIM = {'Cavalry': ('max', 75), 'Infantry': ('min', 25), 'Special Troops & Allies': ('max', 25)}
CR_NOTES = ('CRUSADER ARMY LIST (Armies of Antiquity, pp.40-41): the major Crusading movements or the field armies of the Crusader states.\n'
  'Characters: the army may have a General and an Army Standard Bearer. Cavalry up to three quarters of the points; Infantry at least a quarter; Special Troops & Allies up to a quarter, with one artillery piece per 500 points.\n'
  'Military Orders: if any Military Order troops are fielded, two units of Military Order mounted knights (Brethren) must be used (Military Order foot may only be taken with them; not enforced). On the battlefield, if one Military Order knight unit charges an enemy, the other automatically charges its nearest enemy (or, if none is within reach, moves at least 4" towards the nearest enemy).\n'
  'Combined Formations: crossbowmen may be combined with other infantry (dismounted knights or spearmen of the same origin) in a single regiment, initially making up the front ranks. On entering close combat the crossbowmen either stay in front (standing and shooting at a charging enemy; spear-armed figures in the second rank may fight) or retire to the rear (no shooting, but up to two full ranks of spearmen or one rank of other infantry fight); bringing them forward again costs a turn reforming.\n'
  'Allies (not built here: make a separate small roster): troops from the Byzantine and Arab & Saracen lists.')
LISTS.append(('CR', 'Crusaders (Armies of Antiquity)', 'Crusaders_Armies_of_Antiquity.cat', CR, CR_LIM, CR_NOTES, None))
PTSLIM.append(('CR', 'Stone Thrower', 500, []))

# ------------------------------------------------------------------ ANCIENT CHINESE (book pp.42-43)
CH = []
CH.append(U('Characters', 'General', [M('General', '4 5 5 4 3 3 6 2 9', 140, weapons=['Hand Weapon'], rules=['Army General'], options=[('Shield', 2), ('Light armour', 3), ('Horse (M8)', 0)])],
    'Armed with a hand weapon. May have shield (+2 pts), light armour (+3 pts), horse (free, increases Movement to 8"). May ride in a four-horse heavy chariot bought at additional cost from the list below (not enforced). The army must have a General. 0-1.', mx=1, page='43'))
CH.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon'], rules=['Army Standard'], options=[('Shield', 2), ('Light armour', 3), ('Horse (M8)', 0)])],
    'Armed with a hand weapon. May have shield (+2 pts), light armour (+3 pts), horse (free, increases Movement to 8"). May ride in a four-horse heavy chariot bought at additional cost from the list below (not enforced). 0-1.', mx=1, page='43'))
CH.append(U('Chariotry & Cavalry', 'Heavy Chariots', [M('Heavy Chariot', '6 4 4 4 4 2 4 4 8', 66, weapons=['Hand Weapon', 'Crossbow', 'Halberd', 'Shield', 'Light Armour'])],
    'Two crewmen armed with hand weapon, crossbow, halberd or thrusting spear, shield and light armour, riding in a four-horse heavy chariot with driver.', page='43'))
CH.append(U('Chariotry & Cavalry', 'Heavy Cavalry', [M('Heavy Cavalryman', '7 4 4 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Heavy Armour'], rules=['Knights Rank Bonus'], options=[('Bow', 3), ('Buckler', 1)])],
    'Hand weapon, thrusting spear, heavy armour and barding. May have bow (+3 pts), buckler (+1 pt). May count rank bonus of up to +1 even though cavalry. Designer\'s note: historically only an army that does not include any chariots, except those of the General or Army Standard Bearer, may have cataphracts.', page='43'))
CH.append(U('Chariotry & Cavalry', 'Lancers', [M('Lancer Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour'])],
    'Hand weapons, thrusting spear and light armour. Light Cavalry.', page='43'))
CH.append(U('Chariotry & Cavalry', 'Horse Archers', [M('Horse Archer Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Bow'])],
    'Bows. Light Cavalry.', page='43'))
CH.append(U('Infantry', 'Halberdiers', [M('Halberdier', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Halberd'], options=[('Light armour', 2)])],
    'Halberd. May have light armour (+2 pts).', page='43'))
CH.append(U('Infantry', 'Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear and large shield. May have light armour (+2 pts).', page='43'))
CH.append(U('Infantry', 'Swordsmen', [M('Swordsman', '4 4 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Buckler'], options=[('Light armour', 2)])],
    'Hand weapon and buckler. May have light armour (+2 pts). Light Infantry.', page='43'))
CH.append(U('Infantry', 'Missile Throwers', [M('Missile Thrower', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Light armour', 2), ('Crossbow instead of bow', 1)])],
    'Hand weapon and bow. May have light armour (+2 pts). May replace bow with crossbow (+1 pt).', page='43'))
CH.append(U('Allies & Mercenaries', 'Tribal Skirmishers', [M('Tribal Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Bow'], options=[('Javelin and shield instead of bow', 0)])],
    'Hand weapon and either bow or javelin & shield. Skirmishers.', page='43'))
for nm, st, pts, desc in (('Bolt Thrower', '- - - - 6 2 - - -', 50, 'Bolt thrower: Range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit.'),
                          ('Stone Thrower', '- - - - 7 3 - - -', 75, 'Stone thrower: Range 48", Strength 7, no save, D3 wounds per hit.'),
                          ('Rocket Artillery', '- - - - 6 2 - - -', 50, 'Rockets: Range 12D6", Strength 5, no save, 1 wound per hit; Panic test (on 3D6 for cavalry, chariots and elephants). See Rocket Artillery.')):
    CH.append(U('War Machines', nm, [
        M(nm, st, pts, mn=1, mx=1, key='machine'),
        M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)]),
        M('Additional Crewman', '4 3 3 3 3 1 3 1 7', 0, mn=0, mx=3, key='xcrew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
        'Crew of two to five men armed with swords. May have light armour (+2 pts). ' + desc + ' Up to one war machine per Halberdier or Spearman unit.', page='43'))
CH_LIM = {'Chariotry & Cavalry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)}
CH_NOTES = ('ANCIENT CHINESE ARMY LIST (Armies of Antiquity, pp.42-43), Chin and Han dynasties (500 BC - AD 300), with options for the Tang (AD 500-900).\n'
  'Characters: the army must have a General (not enforced) and may have an Army Standard Bearer. Chariotry & Cavalry up to a quarter of the points; Infantry at least a quarter; Allies & Mercenaries up to a quarter; War Machines up to one per Halberdier or Spearman unit.\n'
  'Rocket Artillery: rockets are war machines and follow the same general rules as stone throwers and bolt throwers for crew. Fired in the shooting phase: pick a direction and a fuse length 1-12 (the number of D6 thrown for the distance in inches). Roll the Scatter dice: on a Hit the rocket flies the rolled distance in the chosen direction; on a Scatter it flies off from its launcher in the direction of the arrow. Work out casualties with the circular template as for a stone thrower. Strength 5, negating armour saves. Any unit taking casualties from a rocket must take a Panic test or flee; cavalry, chariots and elephants test on 3D6 rather than 2D6.\n'
  'Allies (not built here: make a separate small roster): from the Nomadic Hordes list.')
LISTS.append(('CH', 'Ancient Chinese (Armies of Antiquity)', 'Ancient_Chinese_Armies_of_Antiquity.cat', CH, CH_LIM, CH_NOTES, None))
for m in ('Bolt Thrower', 'Stone Thrower', 'Rocket Artillery'):
    RATIOS.append(('CH', m, ['Halberdiers', 'Spearmen'], 1))

# ------------------------------------------------------------------ SAMURAI (book pp.44-45)
SM = []
SMW = [('Samurai armour (5+ save; counts as light armour for movement)', 4), ('Longbow', 3), ('Naginata', 2), ('Spear', 2), ('Additional hand weapon', 2)]
SM.append(U('Characters', 'General', [M('General', '4 6 6 4 4 3 6 4 10', 200, weapons=['Hand Weapon'], rules=['Army General', 'Warriors of Legend', 'Honourable', 'Katana', 'Stubborn'], options=SMW + [('Horse (M8)', 0)])],
    'Armed with a katana. May have Samurai armour (+4 pts), longbow (+3 pts), naginata (+2 pts), spear (+2 pts), additional hand weapon (+2 pts), horse (free, increases Movement to 8"). Army General, Warrior of Legend, Honourable and stubborn. The army must have a General (not enforced). 0-1.', mx=1, page='45'))
SM.append(U('Characters', 'Samurai Heroes', [M('Samurai Hero', '4 5 5 4 4 2 5 3 10', 100, weapons=['Hand Weapon'], rules=['Independent Character', 'Warriors of Legend', 'Honourable', 'Katana', 'Stubborn'], options=SMW + [('Horse (M8)', 0)])],
    'Armed with a katana. May have Samurai armour (+4 pts), longbow (+3 pts), naginata (+2 pts), spear (+2 pts), additional hand weapon (+2 pts), horse (free, increases Movement to 8"). Independent Character. Warrior of Legend, Honourable and stubborn. 0-7. Designer\'s Note: if you don\'t know why the number of heroes is limited to seven then shame (and I do mean shame) on you!', mx=7, page='45'))
SM.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 3 3 1 4 2 9', 60, weapons=['Hand Weapon'], rules=['Army Standard', 'Honourable', 'Katana', 'Stubborn'], options=[('Samurai armour (5+ save; counts as light armour for movement)', 4), ('Spear', 2), ('Additional hand weapon', 2), ('Horse (M8)', 0)])],
    'Armed with a katana. May have Samurai armour (+4 pts), spear (+2 pts), additional hand weapon (+2 pts), horse (free, increases Movement to 8"). Army Standard Bearer, Honourable and stubborn. 0-1.', mx=1, page='45'))
SM.append(U('Samurai', 'Samurai Cavalry', [M('Samurai Cavalryman', '8 4 4 3 3 1 4 2 9', 28, mn=5, weapons=['Hand Weapon'], rules=['Honourable', 'Katana', 'Stubborn'], options=SMW)],
    'Armed with a katana. May have Samurai armour (+4 pts), longbow (+3 pts), naginata (+2 pts), spear (+2 pts), additional hand weapon (+2 pts). Light Cavalry, Honourable and stubborn. Any Samurai or Ashigaru unit may carry Sashimonos for +15 pts per unit (a unit wearing them may re-roll a failed Break test; not built, add by hand).', page='45'))
SM.append(U('Samurai', 'Samurai Infantry', [M('Samurai Infantryman', '4 4 4 3 3 1 4 2 9', 16, mn=5, weapons=['Hand Weapon'], rules=['Honourable', 'Katana', 'Stubborn'], options=[('Samurai armour (5+ save; counts as light armour for movement)', 4), ('Longbow', 3), ('Spear', 2), ('Additional hand weapon', 2)])],
    'Armed with a katana. May have Samurai armour (+4 pts), longbow (+3 pts), spear (+2 pts), additional hand weapon (+2 pts). Honourable and stubborn. Any Samurai or Ashigaru unit may carry Sashimonos for +15 pts per unit (not built, add by hand).', page='45'))
ASH = [('Spear', 1), ('Naginata', 2), ('Bow', 2), ('Light armour', 2)]
SM.append(U('Infantry', 'Chugen', [M('Chugen', '4 4 3 3 3 1 4 1 8', 8, mn=5, weapons=['Hand Weapon'], options=ASH)],
    'Hand weapons. May have spear (+1 pt), naginata (+2 pts), bow (+2 pts), light armour (+2 pts). Light Infantry. 0-1.', mx=1, page='45'))
SM.append(U('Infantry', 'Ashigaru', [M('Ashigaru', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon'], options=ASH)],
    'Hand weapons. May have spear (+1 pt), naginata (+2 pts), bow (+2 pts), light armour (+2 pts). Light Infantry.', page='45'))
SM.append(U('Infantry', 'Wakato', [M('Wakato', '4 3 3 3 3 1 3 1 7', 5, mn=5, weapons=['Hand Weapon'], options=ASH)],
    'Hand weapons. May have spear (+1 pt), naginata (+2 pts), bow (+2 pts), light armour (+2 pts). Light Infantry.', page='45'))
SM.append(U('Infantry', 'Warrior Monks', [M('Warrior Monk', '5 5 5 4 3 1 7 2 10', 25, mn=5, weapons=['Hand Weapon', 'Hand Weapon'], rules=['Warrior Monks Dodge'], options=[('Spear or naginata instead of exotic weapons (free)', 0)])],
    'Exotic weapons (count as additional hand weapons). May replace exotic weapons with spear or naginata (no additional cost). Skirmishers. Warrior monks receive a 5+ special "dodge" save that is not modified by the strength of their opponent\'s attack. 0-1.', mx=1, page='45'))
SM.append(U('Infantry', 'Ninja', [M('Ninja', '5 4 4 3 3 1 4 1 7', 10, mn=1, weapons=['Hand Weapon'], rules=['Ninja Scouts'], options=[('Additional hand weapon', 1), ('Naginata', 2), ('Throwing stars (count as javelins)', 1), ('Light armour', 2)])],
    'Hand weapon. May have additional hand weapon (+1 pt), naginata (+2 pts), throwing stars (count as javelins, +1 pt), light armour (+2 pts). Skirmishers. Ninja scouts always set up last; they may deploy anywhere on the table outside the enemy\'s deployment zone and out of sight of the enemy. 0-1.', mx=1, page='45'))
SM.append(U('Infantry', 'Peasants', [M('Peasant', '4 2 2 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Peasants (Samurai)'])],
    'Farm implements and rocks (count as hand weapons and javelins with a range of 4"). Light Infantry. May only declare a charge if led by a Samurai Hero.', page='45'))
SM_LIM = {'Characters': ('max', 25), 'Samurai': ('max', 50), 'Infantry': ('max', 75)}
SM_NOTES = ('SAMURAI ARMY LIST (Armies of Antiquity, pp.44-45), Japan c. AD 400-1250.\n'
  'Designer\'s Note: the Samurai list is whimsical; serious players may want to tone down or leave out the Samurai heroes, warrior monks and peasants.\n'
  'Characters: the army must have a General (not enforced) and may have up to a quarter of its points in Hero characters including the General. Samurai up to half the points; Infantry up to three quarters.\n'
  'Warriors of Legend: Generals and Heroes may re-roll one failed to-hit and one failed to-wound roll in each combat phase, and may re-roll a failed armour save if the wound is their last one remaining.\n'
  'Honourable: Samurai characters in a position to charge an enemy character must do so, and must accept a challenge issued by an enemy character (if several are eligible, any one may be chosen). Infantry units may not declare a charge until after a Samurai unit has declared a charge or fought a round of combat as a defender (they may declare in the same turn, after the Samurai).\n'
  'Katana: a character or Samurai with a katana counts as having a shield as well (it can parry), and the katana adds +1 Strength on foot (mounted Samurai only use one hand, no bonus). With an additional hand weapon he loses the +1 Strength bonus but may still parry. Samurai Armour: 5+ armour save, counts as light armour for movement. Naginata: treated as a halberd on foot and a thrusting spear if mounted. Sashimono: any Samurai or Ashigaru unit may have them for +15 pts per unit; may re-roll a failed Break test. Bows: Samurai count as having a longbow, infantry have ordinary bows.')
LISTS.append(('SM', 'Samurai (Armies of Antiquity)', 'Samurai_Armies_of_Antiquity.cat', SM, SM_LIM, SM_NOTES, None))

EXCL.append(('AL', 'Royal Guard Phalanx', 'Hypaspists'))
EXCL.append(('AL', 'Indian Elephants', 'African Elephants'))
EXCL.append(('CH', 'Heavy Cavalry', 'Heavy Chariots'))
for u in ('Military Order Dismounted Knights', 'Military Order Spearmen', 'Military Order Crossbowmen'):
    REQ.append(('CR', u, 'Military Order Knights & Sergeants'))
