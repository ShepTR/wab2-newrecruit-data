# Chariot Wars (Warhammer Historical, 2nd ed. era supplement) army lists. Book page = pdf page - 2.
# Model stats order: M WS BS S T W I A Ld
from rb_data import M, U

# ------------------------------------------------------------------ SUMERIAN & AKKADIAN (pp.6-11)
SU = []
SU_GEN = [('Thrusting spear', 2), ('Javelins', 2), ('Double-handed weapon', 3)]
SU.append(U('Characters', 'Sumerian Lugal (General)', [M('Sumerian Lugal', '4 5 5 4 3 3 6 2 9', 143, weapons=['Hand Weapon', 'Light Armour'], rules=['Army General'], options=SU_GEN + [('Ride in an Onager Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. Thrusting spear +2, javelins +2, double-handed weapon +3. May ride in a chariot bought at additional cost from this list. Army General. 0-1 General (Lugal or King).', mx=1, page='8'))
SU.append(U('Characters', 'Akkadian King (General)', [M('Akkadian King', '4 5 5 4 3 3 6 2 9', 143, weapons=['Hand Weapon', 'Light Armour'], rules=['Army General'], options=SU_GEN + [('Composite bow', 3), ('Ride in an Onager Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. Thrusting spear +2, javelins +2, double-handed weapon +3 or composite bow +3. May ride in a chariot bought at additional cost from this list. Army General. 0-1 General (Lugal or King).', mx=1, page='8'))
SU.append(U('Characters', 'Sumerian Ensi (Senior Officer)', [M('Sumerian Ensi', '4 4 4 4 3 2 5 2 8', 63, weapons=['Hand Weapon', 'Light Armour'], options=SU_GEN + [('Composite bow', 3), ('Ride in an Onager Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. Thrusting spear +2, javelins +2, double-handed weapon +3 or composite bow +3. May ride in a chariot bought at additional cost from this list.', page='8'))
SU.append(U('Characters', 'Akkadian Shaknu (Senior Officer)', [M('Akkadian Shaknu', '4 4 4 4 3 2 5 2 8', 63, weapons=['Hand Weapon', 'Light Armour'], options=SU_GEN + [('Composite bow', 3), ('Ride in an Onager Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. Thrusting spear +2, javelins +2, double-handed weapon +3 or composite bow +3. May ride in a chariot bought at additional cost from this list.', page='8'))
SU.append(U('Characters', 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 4 4 3 2 5 2 8', 78, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'])],
    'Hand weapon and light armour. Army Standard. Always fights on foot and always accompanies a unit of Royal Guard or Spearmen. 0-1.', mx=1, page='8'))
SU.append(U('Chariotry', 'Onager Chariots', [M('4-Ass Heavy Chariot', '6 4 4 3 3 1 4 1 8', 30, weapons=['Hand Weapon', 'Javelins', 'Light Armour'], rules=['Onager Chariots'])],
    'One crewman armed with javelins and light armour riding in a four solid-wheeled heavy chariot pulled by four onagers (wild asses) with a driver. Special rule: Sumerian chariots (see Onager Chariots).', page='9'))
SU.append(U('Infantry', 'Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], options=[('Light armour (Ur-style)', 2), ('Large shield (Lagash-style)', 2)])],
    'Hand weapon and thrusting spear. Ur-style spearmen may have light armour +2; Lagash-style spearmen may have large shields +2. Akkadian spearmen can have equipment of either type. If the unit has large shields every model is treated as shielded.', page='9'))
SU.append(U('Infantry', 'Royal Guard', [M('Royal Guard', '4 4 3 3 3 1 4 1 8', 13, mn=5, weapons=['Hand Weapon', 'Double-handed Weapon', 'Light Armour'], options=[('Throw sticks (count as javelins)', 1)])],
    'Double-handed weapon and light armour. May have throw sticks +1 (count as javelins). 0-1 unit.', mx=1, page='10'))
SU.append(U('Infantry', 'Archers', [M('Archer', '4 2 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'], options=[('Light armour', 2)])],
    'Hand weapon and composite bow. May have light armour +2. Light Infantry.', page='10'))
SU.append(U('Infantry', 'Nim Skirmishers', [M('Nim Skirmisher', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Skirmishers', 'Chariot Runners'])],
    'Hand weapon and javelins. Skirmishers, Chariot Runners.', page='10'))
SU.append(U('Infantry', 'Slingers', [M('Slinger', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'])],
    'Hand weapon and sling. Skirmishers.', page='10'))
SU.append(U('Allies & Mercenaries', 'Amorites', [M('Amorite', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='10'))
SU.append(U('Allies & Mercenaries', 'Gutians', [M('Gutian', '5 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Double-handed Weapon', 'Javelins'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Double-handed weapons and throw sticks (count as javelins). Light Infantry. Subject to Warband psychology rules 1 & 2.', page='10'))
SU.append(U('Allies & Mercenaries', 'Amorite or Gutian Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Skirmishers'])],
    'Hand weapons and short bow. Skirmishers.', page='11'))
SU.append(U('Allies & Mercenaries', 'Makkanites', [M('Makkanite', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Warband (psychology rules 1 & 2)'])],
    'Sword and thrusting spear. Subject to Warband psychology rules 1 & 2.', page='11'))
SU.append(U('Allies & Mercenaries', 'Elamites', [M('Elamite', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'])],
    'Hand weapon and composite bow. Light Infantry.', page='11'))
SU_LIMITS = {'Characters': ('max', 25), 'Chariotry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)}
SU_NOTES = ('SUMERIAN & AKKADIAN ARMY LIST (Chariot Wars, pp.6-11), 2500 BC to 1800 BC.\n'
  'Characters up to 25% of the army; the army must include at least one character to command it. The commander is the character with the highest Leadership, so a small army of 1,000 points can be commanded by a Senior Officer (Ensi or Shaknu) rather than a General (Lugal or King). Chariotry up to 25%. Infantry at least 25%. Allies & Mercenaries up to 25%.\n'
  'Tactics: screen the army with skirmishing missile troops; advance massed spearmen with big shields; use onager chariots at the right moment on open ground, screened by javelinmen.')

# ------------------------------------------------------------------ NEW KINGDOM EGYPTIAN (pp.12-18)
EG = []
EG_GEN = [('Composite bow', 3), ('Javelins', 2), ('Shield', 2), ('Ride in a Light Chariot (cost of chariot extra)', 0)]
EG.append(U('Characters', 'Pharaoh/Prince (General)', [M('Pharaoh/Prince', '4 5 5 4 3 3 6 2 10', 153, weapons=['Hand Weapon', 'Light Armour'], rules=['Army General'], options=EG_GEN)],
    'Hand weapon and light armour. Composite bow +3, javelins +2, shield +2. Rides in a chariot bought at additional cost from this list. Army General. 0-1 General.', mx=1, page='14'))
EG.append(U('Characters', 'Army General/Viceroy (General)', [M('Army General/Viceroy', '4 5 5 4 3 3 6 2 9', 143, weapons=['Hand Weapon', 'Light Armour'], rules=['Army General'], options=EG_GEN)],
    'Hand weapon and light armour. Composite bow +3, javelins +2, shield +2. Rides in a chariot bought at additional cost from this list. Army General. 0-1 General.', mx=1, page='14'))
EG.append(U('Characters', 'Brigade Commanders', [M('Brigade Commander', '4 4 4 4 3 2 5 2 8', 63, weapons=['Hand Weapon', 'Light Armour'], options=EG_GEN)],
    'Hand weapon and light armour. Composite bow +3, javelins +2, shield +2. Rides in a chariot bought at additional cost from this list.', page='14'))
EG.append(U('Characters', 'Army Standard Bearer', [M('Army Standard', '4 4 4 4 3 1 4 2 8', 78, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Shield', 2), ('Ride in a Light Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. Shield +2. Rides in a chariot bought at additional cost from this list. Army Standard. 0-1.', mx=1, page='14'))
EG.append(U('Chariotry & Cavalry', 'Chariots', [M('Light Chariot', '8 4 4 3 4 1 4 2 8', 40, weapons=['Hand Weapon', 'Composite Bow', 'Javelins', 'Light Armour', 'Shield'], rules=['Egyptian Charioteers'])],
    'One crewman armed with composite bow, javelins, light armour and shield riding in a two-horse light chariot with a driver. Egyptian charioteers do not suffer -1 to hit for shooting on the move and may shoot as they charge (after enemy charge reactions); counts as short range. Enemy units that take 25% casualties must pass a Panic test or flee.', page='15'))
EG.append(U('Chariotry & Cavalry', 'Chariot Runners', [M('Chariot Runner', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=['Light Infantry', 'Chariot Runners'])],
    'Hand weapon, javelins and shield. Light Infantry, Chariot Runners. Up to one unit of Chariot Runners for each unit of Chariots in the army. In an earlier Egyptian army of a period before chariots you may use this troop type to represent Egyptian javelinmen.', page='15'))
EG.append(U('Chariotry & Cavalry', 'Cavalry', [M('Cavalryman', '8 2 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Cavalry'])],
    'Hand weapon and composite bow. Light Cavalry. 0-1 unit.', mx=1, page='15'))
EG.append(U('Infantry', 'Hand-to-hand Fighters', [M('Hand-to-hand Fighter', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Double-handed weapon (replaces throwing spear)', 1), ('Light armour (one unit only)', 2)])],
    'Khepesh (sickle sword), axe, mace or other hand weapon, throwing spear and shield. May have a double-handed weapon such as a mace-axe instead of throwing spear (+1 pt). One unit may have light armour (+2 pts).', page='16'))
EG.append(U('Infantry', 'Archers', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Composite Bow'], options=[('Light armour', 2)])],
    'Hand weapon and composite bow. May have light armour +2.', page='16'))
EG.append(U('Infantry', 'Marines', [M('Marine', '4 4 4 3 3 1 4 1 8', 11, mn=5, weapons=['Hand Weapon'])],
    'A unit may be entirely armed with bows, entirely armed with javelins and shields or include both in any proportions. Each model in the unit may fight as armed, or you may declare the entire unit to be archers or hand-to-hand fighters depending on the greater proportion represented in the unit.', page='16'))
EG.append(U('Allies & Mercenaries', 'Sherden Guards', [M('Sherden Guard', '5 4 3 3 3 1 3 1 8', 10, mn=5, weapons=['Hand Weapon', 'Buckler'], rules=['Stubborn'], options=[('Light armour', 3), ('Javelins', 2)])],
    'Sword and buckler. May have light armour +3 and javelins +2. Stubborn. 0-1 unit.', mx=1, page='16'))
EG.append(U('Allies & Mercenaries', 'Nubians', [M('Nubian', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Skirmishers'])],
    'Hand weapon and short bow. Skirmishers.', page='16'))
EG.append(U('Allies & Mercenaries', 'Libyans', [M('Libyan', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='16'))
EG.append(U('Allies & Mercenaries', 'Sea Peoples', [M('Sea Peoples Warrior', '5 4 3 3 3 1 3 1 5', 8, mn=5, weapons=['Sword', 'Javelins', 'Shield'], rules=['Warband (psychology rules 1 & 2)'], options=[('Light armour', 3)])],
    'Sword, javelins and shield. May have light armour +3. Subject to Warband psychology rules 1 & 2.', page='17'))
EG.append(U('Allies & Mercenaries', 'Syrians', [M('Syrian', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Light Infantry'], options=[('Short bows', 1), ('Composite bows', 2), ('Mixed weapons', 1)])],
    'Hand weapon and javelins. May have short bows +1 or composite bows +2. May have mixed weapons +1. Light Infantry.', page='17'))
EG.append(U('Allies & Mercenaries', 'Kushites', [M('Kushite', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='17'))
EG.append(U('Allies & Mercenaries', 'Slingers', [M('Slinger', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'], options=[('Shields', 1)])],
    'Hand weapon and sling. May have shields +1. Skirmishers.', page='17'))
EG.append(U('Allies & Mercenaries', "Ne'arin Chariotry", [M("Ne'arin Light Chariot", '8 4 4 3 4 1 4 2 8', 40, weapons=['Hand Weapon', 'Composite Bow', 'Javelins', 'Light Armour', 'Shield'], rules=['Egyptian Charioteers'], options=[('Thrusting spear', 3)])],
    'One crewman armed with composite bow and javelins, light armour and shield riding in a two-horse light chariot with a driver. May have thrusting spear +3. Egyptian charioteers rule as Chariots. 0-1 unit.', mx=1, page='18'))
EG_LIMITS = {'Characters': ('max', 25), 'Chariotry & Cavalry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)}
EG_NOTES = ('NEW KINGDOM EGYPTIAN ARMY LIST (Chariot Wars, pp.12-18), 1600 BC to 800 BC.\n'
  'Characters up to 25%; at least one character to command. Chariotry & Cavalry up to 25%. Infantry at least 25%. Allies & Mercenaries up to 25%. A small army of 1,000 points can be commanded by a Brigade Commander (Hery Pedjet) rather than a General (Pharaoh, Prince, Viceroy or Imyr-Mesha).\n'
  'Chariot Runners: up to one unit per unit of Chariots (an earlier-period army without chariots may use them as Egyptian javelinmen).')

# ------------------------------------------------------------------ HAMMURABIC BABYLONIA (pp.19-24)
HB = []
HB_GEN = [('Ride in a Chariot (cost of chariot extra)', 0)]
HB.append(U('Characters', 'King (Shar) (General)', [M('King (Shar)', '4 5 5 4 3 3 6 2 10', 156, weapons=['Hand Weapon', 'Composite Bow', 'Light Armour'], rules=['Army General'], options=HB_GEN)],
    'Hand weapon, composite bow and light armour. May ride in a chariot bought at additional cost from this army list. Army General. 0-1 General.', mx=1, page='21'))
HB.append(U('Characters', 'General (Alik-Pani) (General)', [M('General (Alik-Pani)', '4 5 5 4 3 3 6 2 9', 146, weapons=['Hand Weapon', 'Composite Bow', 'Light Armour'], rules=['Army General'], options=HB_GEN)],
    'Hand weapon, composite bow and light armour. May ride in a chariot bought at additional cost from this army list. Army General. 0-1 General.', mx=1, page='21'))
HB.append(U('Characters', 'Senior Officer', [M('Senior Officer', '4 4 4 3 3 2 5 2 8', 66, weapons=['Hand Weapon', 'Composite Bow', 'Light Armour'], options=HB_GEN)],
    'Hand weapon, composite bow and light armour. May ride in a chariot bought at additional cost from this army list.', page='21'))
HB.append(U('Characters', 'Amorite Chief', [M('Amorite Chief', '4 4 4 4 3 2 5 2 9', 95, weapons=['Hand Weapon'], rules=['Amorite Chief'], options=[('Composite bow', 3), ('Javelins', 2), ('Light armour', 3), ('Buckler', 1)])],
    'Hand weapon. May have composite bow +3 or javelins +2, light armour +3, buckler +1. May only lead Amorites. Any Amorite unit within 12" of the Chief may use his Leadership when it takes a Leadership test. 0-1.', mx=1, page='21'))
HB.append(U('Characters', 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 4 4 3 2 5 2 8', 78, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=HB_GEN)],
    'Hand weapon and light armour. May ride in a chariot bought at additional cost from this army list. Army Standard. 0-1.', mx=1, page='21'))
HB.append(U('Chariotry', 'Chariots', [M('Chariot', '8 4 4 3 4 1 4 2 8', 38, weapons=['Hand Weapon', 'Composite Bow', 'Light Armour'])],
    'One crewman armed with composite bow and light armour riding in a two-horse light chariot with a driver.', page='22'))
HB.append(U('Chariotry', 'Chariot Runners', [M('Chariot Runner', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry', 'Chariot Runners'])],
    'Hand weapon and composite bow. Light Infantry, Chariot Runners. The army may include up to one unit of Chariot Runners for each unit of Chariotry in the army.', page='22'))
HB.append(U('Chariotry', 'Mounted Scouts', [M('Cavalryman', '8 2 3 3 3 1 3 1 5', 15, mn=3, weapons=['Hand Weapon', 'Composite Bow'], rules=['Skirmishers'])],
    'Hand weapon and composite bow. Skirmishers. Minimum unit size three models; the army may not include more mounted scouts than it has characters. 0-1 unit.', mx=1, page='22'))
HB.append(U('Infantry', 'Royal Guards', [M('Royal Guard', '4 4 3 3 3 1 4 1 8', 14, mn=5, weapons=['Double-handed Weapon', 'Light Armour', 'Throw Sticks'])],
    'Double-handed weapon, light armour and throw sticks (count as javelins). 0-1 unit.', mx=1, page='22'))
HB.append(U('Infantry', 'Shock Troops', [M('Shock Trooper', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. May have light armour +2.', page='22'))
HB.append(U('Infantry', 'Light Troops', [M('Light Troop', '5 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Javelins', 'Shield'], rules=['Light Infantry'], options=[('Thrusting spear and throw sticks (replace javelins and shield)', 0)])],
    'Hand weapon, javelins and shield. May be armed with thrusting spear and throw sticks instead of javelins and shield. Light Infantry.', page='23'))
HB.append(U('Infantry', 'Archers', [M('Archer', '4 2 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'])],
    'Hand weapon and composite bow. Light Infantry.', page='23'))
HB.append(U('Infantry', "Ba'irum", [M("Ba'irum", '5 4 4 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'], options=[('Double-handed axes', 3), ('Javelins or throw sticks instead of composite bow', -1)])],
    'Hand weapon and composite bow. May have double-handed axes +3. May have javelins or throw sticks instead of composite bows (-1 pt). Light Infantry.', page='23'))
HB.append(U('Allies & Mercenaries', 'Amorites', [M('Amorite', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='23'))
HB.append(U('Allies & Mercenaries', 'Gutians or Elamites', [M('Gutian or Elamite', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Elamites are armed with a hand weapon and composite bow. Gutians are armed with double-handed weapons and throw sticks (count as javelins). Light Infantry. Subject to Warband psychology rules 1 & 2.', page='23'))
HB.append(U('Allies & Mercenaries', 'Hattians', [M('Hattian', '4 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Warband (psychology rules 1 & 2)'], options=[('Double-handed axes instead of thrusting spears', 1), ('Large shields', 1)])],
    'Hand weapon and thrusting spear. May have double-handed axes instead of thrusting spears +1 pt. May have large shields +1 pt. Subject to Warband psychology rules 1 & 2. 0-1 unit.', mx=1, page='23'))
HB.append(U('Allies & Mercenaries', 'Amorite Skirmishers', [M('Amorite Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'], options=[('Short bow instead of sling', 0), ('Javelins instead of sling', 0), ('Bucklers (javelin-armed skirmishers only)', 1)])],
    'Hand weapon and slings. May have short bow or javelins instead of sling. Javelin-armed skirmishers may have bucklers +1. Skirmishers.', page='24'))
HB.append(U('Allies & Mercenaries', 'Kassites', [M('Kassite Chariot', '8 4 4 3 4 1 4 2 8', 33, weapons=['Hand Weapon', 'Composite Bow'])],
    'One crewman armed with hand weapon and composite bow riding in a two-horse light chariot with driver.', page='24'))
HB_LIMITS = {'Characters': ('max', 25), 'Chariotry': ('max', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50)}
HB_NOTES = ('HAMMURABIC BABYLONIAN ARMY LIST (Chariot Wars, pp.19-24).\n'
  'Characters up to 25% of the army; at least one character to command. A small army of 1,000 points can be commanded by a Senior Officer (or Amorite chief) rather than a General (King, Vassal King or Alik Pani). Chariotry up to 25%. Infantry at least 25%. Allies & Mercenaries up to HALF the points value of the army.\n'
  'Chariot Runners: up to one unit per unit of Chariotry. Mounted Scouts: the army may not include more mounted scouts than it has characters.')

# ------------------------------------------------------------------ HITTITE EMPIRE (pp.25-32)
HT = []
HT_GEN = [('Shield', 2), ('Composite bow', 3), ('Javelins', 2), ('Ride in a Chariot (cost of chariot extra)', 0)]
HT.append(U('Characters', 'Great King (General)', [M('Great King', '4 5 5 4 4 3 6 3 10', 170, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour'], rules=['Army General'], options=HT_GEN)],
    'Hand weapon, thrusting spear and light armour. May have shield +2, composite bow +3 and javelins +2. Rides in a chariot bought at an additional cost from this list. Army General. 0-1 General.', mx=1, page='29'))
HT.append(U('Characters', 'Prince or Ally King (General)', [M('Prince or Ally King', '4 5 5 4 4 3 6 3 9', 160, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour'], rules=['Army General'], options=HT_GEN)],
    'Hand weapon, thrusting spear and light armour. May have shield +2, composite bow +3 and javelins +2. Rides in a chariot bought at an additional cost from this list. Army General. 0-1 General.', mx=1, page='29'))
HT.append(U('Characters', 'Vassal King', [M('Vassal King', '4 5 5 4 4 3 6 3 8', 140, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour'], rules=['Vassal King'], options=[('Shield', 2), ('Composite bow', 3), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Hand weapon, thrusting spear and light armour. May have shield +2 and a composite bow +3. Rides in a chariot bought at an additional cost from this list. Any units within 12" of the Vassal King, who are of the same nationality as him, may use his Leadership when it takes a Leadership test.', page='29'))
HT.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 73, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=[('Shield', 2), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Hand weapon and light armour. May have shield +2. Rides in a chariot bought at an additional cost from this list. Army Standard. 0-1.', mx=1, page='29'))
HT.append(U('Chariotry', 'Hittite Chariotry (3-crew)', [M('3-Crew Chariot', '7 4 4 4 4 1 4 3 8', 52, mn=3, weapons=['Hand Weapon', 'Thrusting Spear', 'Javelins', 'Light Armour', 'Shield'])],
    'Two crewmen and a driver (three crew) armed with hand weapon, thrusting spear, javelins, light armour and shield riding in a two-horse light chariot. 7", 52 pts.', page='30'))
HT.append(U('Chariotry', 'Hittite Chariotry (2-crew)', [M('2-Crew Chariot', '8 4 4 3 4 1 4 2 8', 38, mn=3, weapons=['Hand Weapon', 'Thrusting Spear', 'Javelins', 'Light Armour', 'Shield'])],
    'One crewman and a driver (two crew) armed with hand weapon, thrusting spear, javelins, light armour and shield riding in a two-horse light chariot. 8", 38 pts. Two-crew chariots may transport Chariot Runner models.', page='30'))
HT.append(U('Chariotry', 'Maryannu Chariotry', [M('2-Crew Chariotry', '8 4 4 3 4 1 4 2 7', 35, weapons=['Hand Weapon', 'Composite Bow', 'Light Armour', 'Shield'], options=[('Javelins', 3), ('Thrusting spear', 3)], key='Maryannu Chariot')],
    'One crewman armed with hand weapon, composite bow, light armour and shield riding in a two-horse light chariot with a driver. Crewman may have javelins +3 or thrusting spear +3.', page='30'))
HT.append(U('Chariotry', 'Hittite Chariot Runners', [M('Hittite Chariot Runner', '5 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Light Infantry', 'Chariot Runners'], options=[('Shields', 1)])],
    'Hand weapons and javelins. May have shields +1. Light Infantry, Chariot Runner. You may include one unit of Chariot Runners for each unit of two-crew chariots in the army. Hittite chariot runners rode in chariots at Kadesh.', page='30'))
HT.append(U('Chariotry', 'Hurrian, Syrian etc. Chariot Runners', [M('Hurrian, Syrian etc. Runner', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Light Infantry', 'Chariot Runners'], options=[('Shields', 1)])],
    'Hand weapons and javelins. May have shields +1. Light Infantry, Chariot Runner. You may include one unit of Chariot Runners for each unit of two-crew chariots in the army.', page='30'))
HT.append(U('Chariotry', 'Scout Cavalry', [M('Scout Cavalryman', '8 3 3 3 3 1 3 1 6', 16, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Cavalry'])],
    'Hand weapon and composite bow. Light Cavalry. 0-1 unit of Cavalry (Scout Cavalry or Hittite Successor Cavalry).', mx=1, page='30'))
HT.append(U('Chariotry', 'Hittite Successor Cavalry', [M('Hittite Successor Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Cavalry'], options=[('Thrusting spear and shield instead of composite bow', 0)])],
    'Hand weapon and composite bow, or thrusting spear and shield instead of bow (no extra cost). Light Cavalry. May fight in the gaps between chariots in the same way as Chariot Runners. 0-1 unit of Cavalry (Scout Cavalry or Hittite Successor Cavalry).', mx=1, page='30'))
HT.append(U('Infantry', 'Spearmen', [M('Spearman', '4 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], options=[('Shields', 1)])],
    'Hand weapon and thrusting spear. May have shields +1.', page='31'))
HT.append(U('Infantry', 'Hittite Guards', [M('Hittite Guard', '4 4 3 3 3 1 4 1 7', 7, mn=5, weapons=['Sword'], options=[('Thrusting spear and shield', 5), ('Double-handed weapon', 3)])],
    'Sword or other hand weapons. May have thrusting spear and shield (+5 pts) or double-handed weapon (+3 pts). 0-1 unit.', mx=1, page='31'))
HT.append(U('Infantry', 'Archers', [M('Archer', '4 2 3 3 3 1 2 1 6', 6, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'])],
    'Hand weapon and composite bow. Light Infantry.', page='31'))
HT.append(U('Infantry', 'Phoenicians', [M('Phoenician', '4 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Javelins', 'Composite Bow'], options=[('Light armour', 2)])],
    'Hand weapon, javelins and composite bow. May have light armour +2.', page='31'))
HT.append(U('Allies & Mercenaries', 'Lukka', [M('Lukka', '4 4 3 3 3 1 3 1 6', 9, mn=5, weapons=['Sword', 'Javelins', 'Shield'], rules=['Warband (psychology rules 1 & 2)'], options=[('Light armour', 3)])],
    'Sword, javelins and shield. May have light armour +3. Subject to Warband psychology rules 1 & 2.', page='31'))
HT.append(U('Allies & Mercenaries', 'Habiru Mercenaries', [M('Habiru', '5 4 4 3 3 1 3 1 6', 9, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='32'))
HT.append(U('Allies & Mercenaries', 'Aramaeans, Sutu or Shosu Scouts/Skirmishers', [M('Scout/Skirmisher', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Skirmishers'], options=[('Short bows instead of javelins', 0), ('Bucklers', 1)])],
    'Hand weapon and javelins. May have short bows instead of javelins (no additional points cost). May have bucklers +1. Skirmishers.', page='32'))
HT.append(U('Allies & Mercenaries', 'Aramaeans, Sutu or Shosu Slingers', [M('Slinger', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'])],
    'Hand weapon and sling only. Skirmishers.', page='32'))
HT.append(U('Allies & Mercenaries', 'Syrian & Canaanite Hupshu', [M('Syrian', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Light Infantry'], options=[('Composite bows', 2), ('Mixed weapons', 1)])],
    'Hand weapon and javelins. May have composite bows +2. May have mixed weapons +1. Light Infantry.', page='32'))
HT_LIMITS = {'Characters': ('max', 25), 'Chariotry': ('min', 25), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50)}
HT_NOTES = ('HITTITE EMPIRE ARMY LIST (Chariot Wars, pp.25-32), 1600 BC to 800 BC. Also used for Hurrian (Mitanni), Syrian, Canaanite, Phoenician and Hyksos armies, Arzawa, and (with modification) the Neo-Hittite successor states.\n'
  'Characters up to 25%; at least one character to command. A small army of 1,000 points can be commanded by a Senior Officer (or Vassal King) rather than a General (Great King, Prince or Ally King). Chariotry at least 25%. Infantry at least 25%. Allies & Mercenaries up to HALF the points value of the army.\n'
  'Chariot Runners: one unit per unit of two-crew chariots. The cavalry unit is 0-1 (Scout Cavalry or Hittite Successor Cavalry).')

# ------------------------------------------------------------------ TROJAN WAR: MYCENAEAN, MINOAN & TROJAN (pp.41-46)
TW = []
TW_CH = [('Change equipment to sword, javelins, light armour and shield (replaces heavy armour and spear)', 0), ('Ride in a Chariot (cost of chariot extra)', 0)]
TW.append(U('Characters', 'King (Wanax) (General)', [M('King (Wanax)', '4 6 6 4 4 3 6 4 9', 191, weapons=['Sword', 'Thrusting Spear', 'Heavy Armour'], rules=['Army General', 'Legendary Warriors'], options=TW_CH)],
    'Sword, thrusting spear and heavy armour. May change equipment to sword, javelins, light armour and shield. May ride in a chariot bought at an additional cost from this army list. Army General. Legendary Warrior: the General is the foremost hero in the army and benefits from the Legendary Warriors rule. 0-1 General (King or Lawageta).', mx=1, page='44'))
TW.append(U('Characters', 'Lawageta (General)', [M('Lawageta', '4 6 6 4 4 3 6 4 9', 191, weapons=['Sword', 'Thrusting Spear', 'Heavy Armour'], rules=['Army General', 'Legendary Warriors'], options=TW_CH)],
    'Sword, thrusting spear and heavy armour. May change equipment to sword, javelins, light armour and shield. May ride in a chariot bought at an additional cost from this army list. Army General. Legendary Warrior. 0-1 General (King or Lawageta).', mx=1, page='44'))
TW.append(U('Characters', 'Heroes', [M('Hero', '4 5 5 4 4 1 5 2 8', 50, weapons=['Sword', 'Thrusting Spear', 'Heavy Armour'], rules=['Legendary Warriors'], options=TW_CH)],
    'Sword, thrusting spear and heavy armour. May change equipment to sword, javelins, light armour and shield. Rides in a chariot bought at an additional cost from this army list. Legendary Warriors: may re-roll one failed to hit and one failed to wound roll each combat phase; may re-roll a failed armour save if the wound suffered is their last one remaining.', page='44'))
TW.append(U('Chariotry', 'Eqeta Chariot Warriors', [M('Eqeta', '8 4 4 3 4 1 4 2 8', 39, weapons=['Sword', 'Thrusting Spear', 'Heavy Armour'], options=[('Change equipment to sword, javelins, light armour and shield', 0)])],
    'One crewman armed with sword, thrusting spear and heavy armour riding in a two-horse light chariot with driver. May change chariot warrior\'s equipment to sword, javelins, light armour and shield.', page='44'))
TW.append(U('Infantry', 'Spearmen', [M('Spearman', '5 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Sword', 'Thrusting Spear', 'Large Shield'], rules=['Warband (psychology rules 1 & 2)'], options=[('Change to sword, javelins, light armour and shield', 1)])],
    'Sword, thrusting spear and large shield. May change equipment to sword, javelins, light armour and shield (+1 pt). Subject to Warband psychology rules 1 & 2. A unit of spearmen armed with thrusting spears may include a proportion of archers (one archer for every three spearmen, 25%). Any number of units of spearmen.', page='45'))
TW.append(U('Infantry', 'Javelinmen', [M('Javelinman', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Dagger', 'Javelins'], rules=['Light Infantry'], options=[('Bucklers', 1)])],
    'Dagger and javelins. May have bucklers +1. Light Infantry. May operate as a unit of Chariot Runners.', page='45'))
TW.append(U('Infantry', 'Archers', [M('Archer', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'])],
    'Hand weapon and composite bow. Light Infantry. Archers may be mixed into a unit of spearmen armed with thrusting spears in a ratio of one archer for every three spearmen (25%) and count as part of the spearmen unit; placed randomly among the spearmen but shoot from the front of the unit; cannot be picked out as targets and all count as shielded against missiles and in hand-to-hand combat. If included within a unit of spearmen, the archers become subject to Warband psychology rules 1 & 2.', page='45'))
TW.append(U('Infantry', 'Slingers', [M('Slinger', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'])],
    'Hand weapon and sling. Skirmishers.', page='45'))
TW.append(U('Allies & Mercenaries', 'Lukka', [M('Lukka Pirate', '5 4 3 3 3 1 3 1 6', 9, mn=5, weapons=['Sword', 'Javelins', 'Shield'], rules=['Warband (psychology rules 1 & 2)'], options=[('Light armour', 3)])],
    'Sword, javelins and shield. May have light armour +3. Subject to Warband psychology rules 1 & 2.', page='46'))
TW.append(U('Allies & Mercenaries', 'Libyans', [M('Libyan', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Mixed Weapons'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Mixed weapons. Light Infantry. Subject to Warband psychology rules 1 & 2.', page='46'))
TW_LIMITS = {'Characters': ('max', 25), 'Chariotry': ('max', 50), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50)}
TW_NOTES = ('TROJAN WAR ARMY LIST (Chariot Wars, pp.41-46): Mycenaean, Minoan & Trojan armies, 1600 BC to 800 BC.\n'
  'Characters up to 25%; at least one character to command. A small army of 1,000 points can be commanded by a Senior Officer (Hero) rather than a General (King or Lawageta). Chariotry up to HALF the points value. Infantry at least 25%. Allies & Mercenaries up to HALF.')

# ------------------------------------------------------------------ ISRAELITES (pp.47-52)
IS = []
IS.append(U('Characters', 'King (General)', [M('King', '4 5 5 4 3 3 6 2 9', 145, weapons=['Sword', 'Light Armour', 'Shield'], rules=['Army General'], options=[('Composite bow', 3), ('Spear', 2), ('Javelins', 2), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword, light armour and shield. May have composite bow +3, spear +2, javelins +2. May ride in a chariot bought at an additional cost from this army list. Army General. 0-1 General (King or General).', mx=1, page='49'))
IS.append(U('Characters', 'General (General)', [M('General', '5 5 5 4 4 2 5 3 8', 110, weapons=['Sword', 'Light Armour', 'Shield'], rules=['Army General'], options=[('Composite bow', 3), ('Spear', 2), ('Javelins', 2), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword, light armour and shield. May have composite bow +3, spear +2, javelins +2. May ride in a chariot bought at an additional cost from this army list. Army General. 0-1 General (King or General).', mx=1, page='49'))
IS.append(U('Characters', 'Senior Officer', [M('Senior Officer', '5 4 4 4 3 2 5 2 8', 63, weapons=['Sword', 'Light Armour'], options=[('Shield or buckler', 1), ('Sling', 2), ('Composite bow', 3), ('Spear', 2), ('Javelins', 2), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword and light armour. May have shield or buckler +1, sling +2, composite bow +3, spear +2, javelins +2. May ride in a chariot bought at additional cost from this army list.', page='49'))
IS.append(U('Characters', 'Army Standard Bearer', [M('Standard Bearer', '4 4 4 4 3 2 5 2 8', 75, weapons=['Sword', 'Light Armour'], rules=['Army Standard'], options=[('Shield or buckler', 1), ('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword and light armour. May have shield or buckler +1. May ride in a chariot bought at an additional cost from this army list. Army Standard. 0-1 Army Standard Bearer or Sacred Ark.', mx=1, page='49'))
IS.append(U('Characters', 'Sacred Ark', [M('Ark & four priests', '4 4 0 3 3 4 4 1 10', 150, weapons=['Sword', 'Light Armour'], rules=['Army Standard', 'Sacred Ark', 'Stubborn'])],
    'The Ark of the Covenant is a portable shrine accompanied by four priests armed with swords and light armour. Army Standard. May only be chosen instead of an army standard bearer, and only if the army does not include any chariots. The Ark and the Priests form a single unit and may not join other units; placed on a single base and move and manoeuvre as a heavy chariot; may not charge. Any unit within 6" of the Ark may automatically rally. Any unit within sight of the Ark may re-roll any Break or Rally tests. If the Ark flees or is captured or destroyed, all units within sight must take an immediate Panic test. The Priests are treated as being stubborn. 0-1 (instead of Army Standard Bearer).', mx=1, page='49'))
IS.append(U('Chariotry & Cavalry', 'Chariots', [M('Chariotry', '8 4 4 3 4 1 4 2 8', 46, weapons=['Sword', 'Composite Bow', 'Javelin', 'Light Armour'], rules=['Stubborn'], options=[('Thrusting spear', 3)])],
    'Crewman armed with sword, composite bow, javelin and light armour riding in a two-horse light chariot with a driver armed with a hand weapon and shield. May have thrusting spear +3. Stubborn. Chariots do not suffer -1 to hit for shooting on the move.', page='50'))
IS.append(U('Chariotry & Cavalry', 'Chariot Runners', [M('Chariot Runner', '5 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Javelins', 'Buckler'], rules=['Chariot Runners'])],
    'Hand weapon, javelins and buckler. Light Infantry, Chariot Runner.', page='50'))
IS.append(U('Chariotry & Cavalry', 'Horsemen', [M('Horseman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Light Cavalry'])],
    'Hand weapon, thrusting spear and shield. Light Cavalry. May fight in the gaps between chariots in the same way as chariot runners.', page='50'))
IS.append(U('Infantry', 'Gibborim', [M('Gibborim', '4 4 4 3 3 1 4 1 8', 16, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Stubborn'], options=[('Thrusting spears', 2), ('Javelins', 2)])],
    'Hand weapon, light armour and shield. May have thrusting spears +2; javelins +2. Stubborn. 0-1 unit.', mx=1, page='50'))
IS.append(U('Infantry', 'Judean Spearmen', [M('Judean Spearman', '5 4 3 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Stubborn', 'Warband (psychology rules 1 & 2)'])],
    'Hand weapon, thrusting spear and shield. Stubborn. Subject to Warband psychology rules 1 & 2.', page='50'))
IS.append(U('Infantry', 'Gadites', [M('Gadite', '5 4 4 3 3 1 3 1 6', 10, mn=5, weapons=['Sword', 'Javelins', 'Shield'], rules=['Light Infantry', 'Warband (psychology rules 1 & 2)'])],
    'Israelite Tribal Militia. Sword, javelins and shield. Light Infantry and subject to Warband psychology rules 1 & 2.', page='50'))
IS.append(U('Infantry', 'Zebulunites', [M('Zebulunite', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Sword', 'Thrusting Spear', 'Shield', 'Composite Bow'], rules=['Light Infantry'])],
    'Israelite Tribal Militia. Mixed spearmen and archers: half of the unit is armed with sword, thrusting spear and shield and the other half is armed with composite bow. Archers may shoot over the front rank of spearmen. Light Infantry.', page='50'))
IS.append(U('Infantry', 'Danites', [M('Danite', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Sword', 'Light Armour', 'Buckler'], rules=['Warband (psychology rules 1 & 2)'])],
    'Israelite Tribal Militia. Sword, light armour and buckler. Subject to Warband psychology rules 1 & 2.', page='50'))
IS.append(U('Infantry', 'Issachar', [M('Issachar', '5 2 3 3 3 1 4 1 6', 5, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Skirmishers'], options=[('Composite bows instead of javelins', 0)])],
    'Israelite Tribal Militia. Hand weapons and either javelins or composite bows. Skirmishers.', page='50'))
IS.append(U('Infantry', 'Benjaminites', [M('Benjaminite', '5 3 4 3 3 1 3 1 6', 8, mn=5, weapons=['Hand Weapon', 'Composite Bow'], rules=['Light Infantry'], options=[('Sling instead of bow', 0), ('Bucklers', 1)])],
    'Hand weapon and composite bow. May have sling instead of a bow. May have bucklers +1. Archers and slingers may be mixed into the same unit. Light Infantry.', page='51'))
IS.append(U('Allies & Mercenaries', 'Midianite Arabs', [M('Arab Camel Rider', '8 2 3 3 3 2 3 2 5', 16, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Light Cavalry', 'Camels'])],
    'Two riders armed with hand weapons and short bows riding a camel. Light Cavalry. Camels cause fear in cavalry and chariots.', page='51'))
IS.append(U('Allies & Mercenaries', 'Philistines', [M('Philistine', '5 3 3 3 3 1 3 1 6', 11, mn=5, weapons=['Sword', 'Javelins', 'Light Armour', 'Shield'], rules=['Stubborn'])],
    'Sword, javelins, light armour and shield. Stubborn.', page='51'))
IS.append(U('Allies & Mercenaries', 'Edomites, Moabites & Ammonites', [M('Edomite etc', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelins'], rules=['Skirmishers'])],
    'Hand weapon and javelins. Skirmishers.', page='52'))
IS.append(U('Allies & Mercenaries', 'Phoenicians', [M('Phoenician', '4 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Composite Bow', 'Javelins'], options=[('Light armour', 2)])],
    'Hand weapon, composite bow and javelins. May have light armour +2.', page='52'))
IS_LIMITS = {'Characters': ('max', 25), 'Chariotry & Cavalry': ('max', 50), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50)}
IS_NOTES = ('ISRAELITE ARMY LIST (Chariot Wars, pp.47-52).\n'
  'Characters up to 25%; at least one character to command. A small army of 1,000 points can be commanded by a Senior Officer rather than a General (or King). Chariotry & Cavalry up to HALF the points value. Infantry at least 25%. Allies & Mercenaries up to HALF.\n'
  'Early armies (Joshua, Saul, David) were almost entirely infantry; later armies (Solomon onwards) have a strong chariot force. The Sacred Ark may only be chosen if the army has no chariots.')

# ------------------------------------------------------------------ ASSYRIAN EMPIRE (pp.53-61), also Babylonian
AS = []
AS_BAB_NOT = ' (Assyrian armies only)'
AS.append(U('Characters', 'King (General)', [M('King', '4 5 5 4 3 3 6 3 10', 186, weapons=['Sword', 'Composite Bow', 'Light Armour'], rules=['Army General'], options=[('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword, composite bow and light armour. May ride in a chariot bought at an additional cost from this army list. Army General. 0-1 General (King or Turtanu).', mx=1, page='57'))
AS.append(U('Characters', 'Turtanu (General)', [M('Turtanu', '4 5 5 4 3 3 6 3 9', 176, weapons=['Sword', 'Composite Bow', 'Light Armour'], rules=['Army General'], options=[('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword, composite bow and light armour. May ride in a chariot bought at an additional cost from this army list. Army General. 0-1 General (King or Turtanu).', mx=1, page='57'))
AS.append(U('Characters', 'Shaknu', [M('Shaknu', '4 4 4 4 3 2 5 2 8', 66, weapons=['Sword', 'Composite Bow', 'Light Armour'], options=[('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword, composite bow and light armour. May ride in a chariot bought at an additional cost from this army list.', page='57'))
AS.append(U('Characters', 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 4 4 3 1 4 2 8', 63, weapons=['Sword', 'Light Armour'], rules=['Army Standard'], options=[('Ride in a Chariot (cost of chariot extra)', 0)])],
    'Sword and light armour. May ride in a chariot bought at an additional cost from this army list. Army Standard. 0-1. In a Babylonian army one may be included for free (pay for his chariot as normal).', mx=1, page='57'))
AS.append(U('Chariotry & Cavalry', 'Four-horse Heavy Chariots', [M('Chariot', '8 4 4 3 4 2 4 2 8', 97, weapons=['Thrusting Spear', 'Shield', 'Light Armour', 'Composite Bow'], rules=['Chariot Archers (Assyrian)'], options=[('Extra crewman (+1 Attack)', 5), ('Darts (siltahi, count as javelins) for the archer', 2)])],
    'Two crew armed with thrusting spear, shield and light armour riding in a four-horse heavy chariot with a driver. One crewman has a bow. May have an extra crewman adding +1 to Attacks (+5 pts per chariot). Archer may have darts (siltahi, count as javelins) kept in quivers at front of chariot (+2 pts). Chariot archers do not suffer the -1 to hit for shooting on the move. Automatic hits inflicted by a charging heavy chariot are added to the hits scored by the crew and happen at the same time.', page='57'))
AS.append(U('Chariotry & Cavalry', 'Assyrian Cavalry', [M('Assyrian Cavalryman', '8 4 4 3 3 1 4 1 8', 25, mn=5, weapons=['Sword', 'Light Armour', 'Composite Bow'], rules=['Mounted Archers (second rank)'], options=[('Royal Guard cavalry (barded horses, thrusting spear and composite bow; one unit)', 6)])],
    'Half the unit are armed with a sword and light armour and composite bow, the other half are armed with thrusting spear. One unit of Assyrian cavalry may be upgraded to Royal Guard cavalry with cavalrymen in the unit armed with both thrusting spear and composite bow and riding barded horses (+6 pts). Mounted archers in the second rank of the unit may shoot over the first rank. Assyrian armies only.', page='57'))
AS.append(U('Chariotry & Cavalry', 'Babylonian Cavalry', [M('Babylonian Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Sword', 'Light Armour', 'Composite Bow'], rules=['Mounted Archers (second rank)'])],
    'Half the unit are armed with a sword and light armour and composite bow, the other half are armed with thrusting spear. Mounted archers in the second rank of the unit may shoot over the first rank. Babylonian armies.', page='57'))
AS.append(U('Infantry', 'Qurubuti Royal Guard', [M('Qurubuti', '4 4 3 3 3 1 3 1 8', 18, mn=5, weapons=['Sword', 'Light Armour', 'Throwing Spear', 'Large Shield'], rules=['Stubborn'])],
    'All Qurubuti are armed with sword, light armour, throwing spear and large shield. Stubborn. 0-1 unit. Assyrian armies only.', mx=1, page='58'))
AS.append(U('Infantry', 'Assyrian Infantry (Kisir Sharruti)', [M('Assyrian Infantryman', '4 3 3 3 3 1 3 1 7', 12, mn=5, weapons=['Sword', 'Light Armour', 'Composite Bow', 'Thrusting Spear', 'Shield'], rules=['Stubborn', 'Mixed archers/spearmen'], options=[('Large shields for spearmen', 1)])],
    'Half the unit are armed with sword, light armour and composite bow; the other half with sword, light armour, thrusting spear and shield. Spearmen may have large shields +1. A single rank of archers may shoot over a single rank of spearmen of the same unit. Stubborn. Assyrian armies only.', page='58'))
AS.append(U('Infantry', 'Babylonian Infantry (Kisir Sharruti)', [M('Babylonian Infantryman', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Sword', 'Light Armour', 'Composite Bow', 'Thrusting Spear', 'Shield'], rules=['Mixed archers/spearmen'], options=[('Large shields for spearmen', 1)])],
    'Half the unit are armed with sword, light armour and composite bow; the other half with sword, light armour, thrusting spear and shield. Spearmen may have large shields +1. A single rank of archers may shoot over a single rank of spearmen of the same unit. Babylonian armies.', page='58'))
AS.append(U('Infantry', 'Sab Sharri Auxiliaries', [M('Auxiliary', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Sword', 'Thrusting Spear', 'Shield', 'Composite Bow'], rules=['Light Infantry', 'Mixed archers/spearmen'], options=[('Goatskins to cross water (+1 per model; one unit)', 1)])],
    'Half the unit are armed with sword, thrusting spear and shield. The other half are armed with swords and composite bows. Light Infantry. A single rank of archers may shoot over a single rank of spearmen. Crossing Water: one unit of Auxiliaries in the army may be equipped with inflated goatskins (+1 pt each) to cross water obstacles at half their Movement rate; you must have at least five models converted to represent swimming troops.', page='58'))
AS.append(U('Infantry', 'Heavy Slingers', [M('Armoured Archer/Slinger', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Sword', 'Light Armour'], rules=['Heavy Slingers'], options=[('Composite bows (archers)', 2), ('Slings (slingers)', 1)])],
    'Sword and light armour. Archers have composite bows (+2 pts). Slingers have slings (+1 pt). A unit of heavy slingers contains both archers and slingers in equal proportions. Models in a unit can have different weapon combinations. Armoured slingers in the second rank may shoot at full effect as long as the unit does not move. Slingers may shoot even if not in skirmish formation. Enemy units may not use shields against sling shot hits. 0-1 unit. Assyrian armies only.', mx=1, page='58'))
AS.append(U('Infantry', 'Mounted Infantry (Kallipani)', [M('Mounted Infantry', '4 3 3 3 3 1 3 1 5', 8, mn=5, weapons=['Sword', 'Composite Bow', 'Light Armour'], rules=['Mule Carts'])],
    'Armed with a sword, composite bow and light armour. The entire unit is mounted on two-wheeled carts (Mule Cart, M6, free), each drawn by two mules and carrying up to five soldiers. The unit must be equipped with the required number of cart models. The infantry automatically dismount from the carts to fight or shoot, even if charged. The carts are non-combatant and always placed directly behind any dismounted infantry; they do not count as chariots. When mounted on carts the unit may march move but may not charge. Dismounted infantry must remount to be able to flee. 0-1 unit.', mx=1, page='59'))
AS.append(U('Allies & Mercenaries', 'Urartians', [M('Urartian', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Sword', 'Thrusting Spear', 'Shield'], rules=['Warband (psychology rules 1 & 2)'])],
    'Sword, thrusting spear and shield. Warband Leadership. Subject to Warband psychology rules 1 & 2. Assyrian armies only.', page='59'))
AS.append(U('Allies & Mercenaries', 'Aramaeans', [M('Aramaean', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Sword', 'Javelin', 'Shield'], rules=['Light Infantry'], options=[('Sword and composite bow instead', 0)])],
    'Sword, javelin and shield. May instead be armed with sword and composite bow. Light Infantry.', page='60'))
AS.append(U('Allies & Mercenaries', 'Chaldeans', [M('Chaldean', '4 2 3 3 3 1 2 1 5', 5, mn=5, weapons=['Hand Weapon', 'Composite Bow'], options=[('Thrusting spears as well as bows (Babylonian army)', 1), ('Thrusting spear and large shield instead of bow (Babylonian army)', 1)])],
    'Hand weapon and composite bow. Chaldeans in a Babylonian army may have thrusting spears as well as bows (+1 pt) or may have thrusting spears and replace their bows with large shields (+1 pt). Half the unit may be equipped with spear and bow and the other half with thrusting spear and large shield, or the whole unit may all be equipped in the same way. In mixed units a single rank of archers may shoot over a single rank of spearmen.', page='60'))
AS.append(U('Allies & Mercenaries', 'Cimmerians or Scythians', [M('Cimmerian etc', '8 3 3 3 3 1 3 1 5', 16, mn=5, weapons=['Sword', 'Composite Bow'], rules=['Light Cavalry'])],
    'Sword and composite bow. Light Cavalry. 0-1 unit.', mx=1, page='60'))
AS.append(U('Allies & Mercenaries', 'Arab Camel Riders', [M('Arab Camelry', '8 2 3 3 3 2 3 2 5', 16, mn=5, weapons=['Short Bow'], rules=['Light Cavalry', 'Camels'])],
    'Each camel has two riders both armed with short bows. Light Cavalry. Camels cause fear in cavalry and chariots. 0-1 units.', mx=1, page='60'))
AS.append(U('Allies & Mercenaries', 'Elamite Chariots', [M('Elamite Chariot', '8 3 3 3 3 1 3 1 7', 25, weapons=['Sword'], rules=['Elamite Chariots'])],
    'Four-horse heavy chariots, crewed by a driver armed with a sword. Elamite chariots may transport up to three infantry models per chariot. Only Babylonian armies may include Elamite Chariots or Cavalry.', page='60'))
AS.append(U('Allies & Mercenaries', 'Elamite Cavalry', [M('Elamite Cavalryman', '8 3 3 3 3 1 3 1 6', 17, mn=5, weapons=['Sword', 'Thrusting Spear', 'Composite Bow'], rules=['Light Cavalry'])],
    'Swords, thrusting spears and composite bows. Light Cavalry. Only Babylonian armies may include Elamite Chariots or Cavalry.', page='60'))
AS.append(U('Allies & Mercenaries', 'Elamite Infantry', [M('Elamite Infantryman', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Sword', 'Composite Bow'], rules=['Light Infantry'])],
    'Swords and composite bows. Light Infantry. Only Babylonian armies may include Elamites.', page='60'))
AS.append(U('Allies & Mercenaries', 'Medes', [M('Mede', '5 3 3 3 3 1 3 1 5', 7, mn=5, weapons=['Sword', 'Thrusting Spear', 'Composite Bow'], rules=['Warband (psychology rules 1 & 2)'], options=[('Shields', 1)])],
    'Sword, thrusting spear and composite bow. May have shields +1. Subject to Warband psychology rules 1 & 2. May be used in Babylonian armies only. 0-1 unit.', mx=1, page='60'))
AS.append(U('Allies & Mercenaries', 'Chaldean or Aramaean Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Skirmishers'], options=[('Short bows instead of slings', 0), ('Javelins and bucklers instead of slings', 1)])],
    'Hand weapon and sling. May have short bows or javelins and bucklers instead of slings. Skirmishers.', page='61'))
AS.append(U('Allies & Mercenaries', 'Greek or Lydian Hoplites', [M('Greek/Lydian Hoplite', '4 4 4 3 3 1 4 1 8', 19, mn=5, weapons=['Sword', 'Thrusting Spear', 'Shield', 'Heavy Armour'], rules=['Stubborn', 'Phalanx (Chariot Wars)'])],
    'Sword, thrusting spear, shield and heavy armour. Stubborn. May only be used in Babylonian armies. 0-1 unit. Phalanx: in a unit of at least sixteen models with a rank bonus of at least +1: cavalry may not charge the front of the phalanx; phalanx models may charge and still fight in two ranks; all enemy attacks (shooting and hand-to-hand) at the front of the phalanx suffer -1 to hit. The only formation change allowed is an about face; may wheel, but cannot march or charge if they do so; may drift 1" to the right when they march or charge. As soon as it is reduced to less than sixteen models or loses its rank bonus these rules no longer apply.', mx=1, page='61'))
AS_ASSYRIAN_ONLY = ('Four-horse Heavy Chariots', 'Assyrian Cavalry', 'Qurubuti Royal Guard', 'Assyrian Infantry (Kisir Sharruti)', 'Heavy Slingers', 'Urartians')
AS_BABYLON_ONLY = ('Babylonian Cavalry', 'Babylonian Infantry (Kisir Sharruti)', 'Elamite Chariots', 'Elamite Cavalry', 'Elamite Infantry', 'Medes', 'Greek or Lydian Hoplites')
AS_VARIANTS = [
 ('Assyrian Empire - Assyrian', {'Characters': ('max', 25), 'Chariotry & Cavalry': ('max', 50), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 25)},
  'Assyrian army: Allies & Mercenaries up to a quarter of the points. Assyrian special rules (Terror, Highly Professional) apply. No Elamites, Medes or Hoplites.'),
 ('Assyrian Empire - Babylonian', {'Characters': ('max', 25), 'Chariotry & Cavalry': ('max', 50), 'Infantry': ('min', 25), 'Allies & Mercenaries': ('max', 50)},
  'Babylonian army: Allies & Mercenaries up to half the points. Assyrian special rules do not apply. May include an army standard bearer for free (pay for his chariot as normal). May not include Assyrian Cavalry, Assyrian Kisir Sharruti Infantry, Heavy Slingers or Urartians. Only Babylonian armies may include Chaldeans armed with spears and shields, Elamite Chariots or Cavalry, Medes or Hoplites.'),
]
AS_LIMITS = AS_VARIANTS[0][1]
AS_NOTES = ('ASSYRIAN EMPIRE ARMY LIST (Chariot Wars, pp.53-61), 745 BC to 610 BC. The list can also represent a Babylonian army of the same period.\n'
  'Characters up to 25%; at least one character to command. A small army of 1,000 points can be commanded by a Senior Officer (Shaknu) rather than a General (King or Turtanu). Chariotry & Cavalry up to HALF the points value. Infantry at least 25%. Allies & Mercenaries: Assyrian army up to a quarter; Babylonian army up to half. Only a Babylonian army can include Elamites or Hoplites.')
AS_RULES = {
 'Terror (Assyrian)': ('Chariot Wars p.56', 'The Assyrians cause fear in all units in an enemy army that have a Leadership value of 7 or less, after any modifications have been applied. This rule no longer applies once an Assyrian chariot, cavalry or infantry unit has been broken in combat. Does not apply to Babylonian armies, or any army that includes Elamites or Hoplites.'),
 'Highly Professional (Assyrian)': ('Chariot Wars p.56', 'The Assyrians may always choose who moves first or second in a battle if this would normally be decided randomly. In battles where who moves first is not determined by a dice roll, the Assyrians follow the normal rules. Does not apply to Babylonian armies.'),
}
