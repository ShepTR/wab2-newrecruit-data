# Hannibal & the Punic Wars - Spanish (pp.70-73), Numidian (pp.74-75), Ligurian (pp.76-79), Gallic (pp.80-81) lists. pdf = book + 2.
from rb_data import M, U

# ------------------------------------------------------------------ SPANISH
SP = []
SPC = [('Light armour', 3), ('Javelins', 2), ('Throwing spear', 2), ('Heavy throwing spear (on foot)', 3), ('Horse (free)', 0)]
SP.append(U('Characters', 'Army General', [M('Army General', '4 5 5 4 4 3 6 3 9', 145, weapons=['Hand Weapon', 'Shield'], rules=['Stubborn'], options=SPC)],
    'Sword and shield. Javelins or throwing spear +2; if on foot heavy throwing spear +3; light armour +3. May ride a horse (free). Army General, Stubborn. If no Army General is taken the commander must be a Heroic Leader.', mx=1, page='71'))
SP.append(U('Characters', 'Army Battle Standard', [M('Army Standard Bearer', '4 4 4 4 3 2 5 2 8', 80, weapons=['Hand Weapon', 'Shield'], rules=['Stubborn'], options=[('Light armour', 3), ('Horse (free)', 0)])],
    'Sword and shield. Light armour +3. May ride a horse (free). Army Standard Bearer, Stubborn.', mx=1, page='71'))
SP.append(U('Characters', 'Heroic Leaders', [M('Heroic Leader', '4 5 5 4 4 2 5 3 8', 85, weapons=['Hand Weapon', 'Shield'], rules=['Stubborn'], options=SPC + [('May be Army General', 25)])],
    'Sword and shield. Javelins or throwing spear +2; if on foot heavy throwing spear +3; light armour +3. May ride a horse (free). May be Army General (+25 pts). Stubborn.', page='71'))
SP.append(U('Cavalry', 'Heavy Cavalry', [M('Heavy Cavalryman', '8 4 4 3 3 1 3 1 7', 23, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'],
    options=[('Javelins', 1), ('Thrusting spear (replaces throwing spear)', 0), ('Light armour', 2), ('Stubborn (per figure)', 3)])],
    'Sword, throwing spear, shield. May be designated Stubborn (+3 pts per figure). 0-1 unit.', mx=1, page='71'))
SP.append(U('Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], options=[('Javelins', 1), ('Light armour (Lusitanians only)', 2)])],
    'Sword, throwing spear, buckler. Light Cavalry.', page='71'))
SP.append(U('Infantry', 'Scutarii', [M('Scutarius', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Feigned Flight', 'Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear; loses Feigned Flight)', 2), ('Javelins', 1), ('Stubborn (one unit, per figure)', 3)])],
    'Sword, throwing spear, shield. Feigned Flight (lost if armed with heavy throwing spears), Stealth. One unit may be Stubborn (+3 per figure).', page='71'))
SP.append(U('Infantry', 'Tribesmen', [M('Tribesman', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Warband', 'Stealth'], options=[('Javelins', 1)])],
    'Sword, throwing spear, shield. Warband, Stealth. Hastily raised, less-experienced tribesmen.', page='71'))
SP.append(U('Infantry', 'Caetrati', [M('Caetratus', '5 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Feigned Flight'], options=[('Bladders (optional rule, p.73)', 1)])],
    'Sword, javelins, buckler. Skirmishers, Feigned Flight. An Iberian army may not have more than one unit of Caetrati per two units of Scutarii (unless none are used) and no Caetrati unit may outnumber the smallest Scutarii unit. In Celtiberian armies no Caetrati unit may outnumber the smallest Celtiberian unit; in Lusitanian armies one Lusitanian unit per two Caetrati units.', page='72'))
SP.append(U('Infantry', 'Celtiberian Warriors', [M('Celtiberian', '5 3 3 3 3 1 3 1 5', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Warband', 'Feigned Flight', 'Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear; loses Feigned Flight)', 1), ('Javelins', 1)])],
    'Sword, throwing spear, shield. Warband, Feigned Flight, Stealth.', page='72'))
SP.append(U('Infantry', 'Lusitanians', [M('Lusitanian', '5 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Buckler'], rules=['Feigned Flight', 'Stealth'],
    options=[('Shield (replaces buckler)', 1), ('Heavy throwing spear (replaces throwing spear; loses Feigned Flight)', 1), ('Javelins', 1)])],
    'Sword, throwing spear, light armour, buckler. Feigned Flight (lost if armed with heavy throwing spears), Stealth.', page='72'))
SP.append(U('Special Units', 'Slingers', [M('Slinger', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Sling'], options=[('Buckler', 1)])],
    'Sword and sling. Skirmishers.', page='72'))
SP.append(U('Special Units', 'Balearic Slingers', [M('Balearic Slinger', '5 3 4 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Sling'], rules=['Warband'], options=[('Buckler', 1)])],
    'Sword and sling. Skirmishers, Warband. May not outnumber any other skirmishing infantry unit in the army. Every other unit may be Balearic Slingers.', page='72'))
SP.append(U('Special Units', 'Celtiberian Warriors (Special - Iberians)', [M('Celtiberian', '5 3 3 3 3 1 3 1 5', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Warband', 'Feigned Flight', 'Stealth'],
    options=[('Heavy throwing spear (replaces throwing spear; loses Feigned Flight)', 1), ('Javelins', 1)])],
    'As Celtiberian Warriors; counts as a Special Unit in Iberian armies only.', page='72'))
SP_VARIANTS = [
 ('Spanish - Iberians', {'Characters': ('max', 25), 'Infantry': ('min', 50), 'Cavalry': ('max', 25), 'Special Units': ('max', 25)},
  'Infantry: Scutarii, Tribesmen, Caetrati. Cavalry: 0-1 Heavy Cavalry, Light Cavalry. Special Units: Slingers, Balearic Slingers, Celtiberian Warriors.'),
 ('Spanish - Celtiberians', {'Characters': ('max', 25), 'Infantry': ('min', 50), 'Cavalry': ('max', 25), 'Special Units': ('max', 10)},
  'Infantry: Celtiberian Warriors, Tribesmen, Caetrati. Cavalry: 0-1 Heavy Cavalry, Light Cavalry. Special Units: Slingers.'),
 ('Spanish - Lusitanians', {'Characters': ('max', 25), 'Infantry': ('min', 50), 'Cavalry': ('max', 25), 'Special Units': ('max', 10)},
  'Infantry: Lusitanians and Caetrati (one unit of Lusitanians for every two units of Caetrati; no Caetrati unit may outnumber the smallest Lusitanian unit). Cavalry: 0-1 Heavy Cavalry, Light Cavalry (may have light armour +2). Special Units: Slingers.'),
]
SP_NOTES = ('SPANISH ARMY LIST (Hannibal & the Punic Wars, pp.70-73)\n'
  'Northern Spanish tribes may be represented using the Gallic list. Characters up to 25%; the army must have one character as the overall leader; besides a General it may have an Army Standard Bearer and additional Heroic Leaders. If no Army General is selected the commander must be a Heroic Leader.\n'
  'Terrain: the Spanish player may place his generated terrain on his opponent\'s side of the table. Ambush: before deployment the Spanish player may hide one unit anywhere out of sight of the enemy deployment zone and deploy it at the start of his first turn.\n'
  'Optional rules (p.73, with consent): Sertorius and other revolts (field up to a quarter of points from the Roman list; Roman characters up to the character allowance; no Praetorian Guard, Lanciarii, Auxiliaries, Marines, Camelry or Elephants); Amphibious Caetrati (bladders +1 pt per model let Caetrati cross rivers and lakes).')

# ------------------------------------------------------------------ NUMIDIAN
NU = []
NUC = [('Throwing spear', 2), ('Javelins', 2), ('Light armour', 3), ('Shield (replaces buckler)', 1)]
NU.append(U('Characters', 'Army General', [M('Army General', '8 5 5 4 4 3 6 3 9', 140, weapons=['Hand Weapon', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'], options=NUC)],
    'Sword and buckler. Rides a horse. Army General, Feigned Flight, Parthian Shot.', mx=1, page='74'))
NU.append(U('Characters', 'Army Battle Standard', [M('Army Standard Bearer', '8 4 4 4 3 2 5 2 8', 75, weapons=['Hand Weapon', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'], options=[('Light armour', 3), ('Shield (replaces buckler)', 1)])],
    'Sword and buckler. Rides a horse. Army Standard Bearer, Feigned Flight, Parthian Shot.', mx=1, page='74'))
NU.append(U('Characters', 'Tribal Leaders', [M('Tribal Leader', '8 5 5 4 4 2 5 3 8', 80, weapons=['Hand Weapon', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'], options=NUC + [('May be Army General', 25)])],
    'Sword and buckler. Rides a horse. May be Army General (+25 pts). Feigned Flight, Parthian Shot. 0-2.', mx=2, page='74'))
NU.append(U('Infantry', 'Trained Infantry', [M('Trained Infantryman', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'])],
    'Sword, javelins, shield. Light Infantry. The total of Trained Infantry figures may not outnumber the total number of Warriors.', page='75'))
NU.append(U('Infantry', 'Warriors', [M('Warrior', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Javelin', 'Buckler'], rules=['Warband', 'Stealth'], options=[('Shield (replaces buckler)', 0)])],
    'Javelins and buckler. Warband (rule 1 only), Stealth.', page='75'))
NU.append(U('Infantry', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Javelin', 'Buckler'], rules=['Feigned Flight'],
    options=[('Shield (replaces buckler)', 0), ('Bow (replaces javelins; every third unit)', 1), ('Sling (replaces javelins; every third unit)', 0)])],
    'Javelins and buckler. Skirmishers, Feigned Flight. No bow- or sling-equipped unit may outnumber the smallest javelin-equipped skirmisher unit.', page='75'))
NU.append(U('Cavalry', 'Numidian Cavalry', [M('Retainer', '8 3 4 3 3 1 4 1 7', 21, mn=5, weapons=['Dagger', 'Javelin', 'Buckler'], rules=['Feigned Flight', 'Parthian Shot'], options=[('Shield (replaces buckler)', 1)])],
    'Knife, javelins, buckler. Light Cavalry, Feigned Flight, Parthian Shot. Only characters may have armour.', page='75'))
NU.append(U('Cavalry', 'Levy Cavalry', [M('Levy', '8 2 3 3 3 1 3 1 5', 10, mn=5, weapons=['Javelin', 'Buckler'], rules=['Levies (Hannibal)'], options=[('Shield (replaces buckler)', 1)])],
    'Javelins and buckler. Light Cavalry, Levy.', page='75'))
NU.append(U('Special Units', 'Elephants', [
    M('African Elephant', '6 4 0 6 5 5 3 4 4', 114, mn=1, mx=1, key='el', options=[('Shields on tower (+1 save for crew)', 4)]),
    M('Mahout', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='mahout'),
    M('Crew', '4 2 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Javelin'], options=[('Bow (replaces javelins)', 1)]),
    M('Third Crewman', '4 2 3 3 3 1 3 1 7', 7, mn=0, mx=1, key='crew3', weapons=['Javelin'], options=[('Bow (replaces javelins)', 1)])],
    'Unarmed mahout and two crew with javelins in a fighting tower (+5 save). Crew may have bows (+1 each). Shields on the tower +4 (+1 save for crew). Third crewman +7 (+8 if bow-armed). Elephant: may stampede; causes fear in infantry and terror in cavalry. Crew WS 2 as printed.', page='75'))
NU.append(U('Special Units', 'Imitation Legionaries (optional)', [M('Imitation Legionary', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Hand Weapon', 'Heavy Throwing Spear', 'Light Armour', 'Shield'])],
    'Sword, pilum, light armour, shield. Optional (opponent\'s permission, out-of-period scenarios). Total Imitation Legionary figures may not outnumber the total number of Warriors; they count as infantry in the Army Composition.', page='75'))
NU_VARIANTS = [('Numidian', {'Characters': ('max', 25), 'Infantry': ('max', 50), 'Cavalry': ('min', 25), 'Special Units': ('max', 25)}, 'Standard Numidian composition.')]
NU_NOTES = ('NUMIDIAN ARMY LIST (Hannibal & the Punic Wars, pp.74-75)\n'
  'Characters up to 25%; at least one must be the overall leader; besides a General the army may have an Army Standard Bearer and additional leaders. If no Army General is selected the commander must be a Tribal Leader.\n'
  'Terrain: the Numidian player may place his generated terrain on his opponent\'s side of the table; on a roll of 9 (Walls/Hedges) he may place any other terrain instead.\n'
  'Field Fortifications: after terrain is determined the Numidian player may place 4D6" of linear obstacles or field fortifications on his side of the table at no cost.\n'
  'Ambush: before deployment the Numidian player may hide one unit anywhere out of sight of the enemy deployment zone and deploy it at the start of his first turn.')

# ------------------------------------------------------------------ LIGURIAN
LG = []
LGC = [('Light armour', 3), ('Shield', 2), ('Thrusting spear', 2), ('Throwing spear', 2), ('Javelins', 2), ('Pennato (Apuani only)', 2)]
LG.append(U('Characters', 'Prince', [M('Prince', '5 6 6 4 4 3 6 3 8', 150, weapons=['Hand Weapon'], rules=['Warband'], options=LGC)],
    'Sword or axe. Light armour +3, shield +2; thrusting spear, throwing spear or javelins +2; a Prince of the Apuani may have a pennato (+2). Army General, Warband.', mx=1, page='78'))
LG.append(U('Characters', 'Cycnus Standard Bearer', [M('Cycnus Standard Bearer', '5 4 4 4 3 1 5 2 7', 85, weapons=['Hand Weapon'], rules=['Warband'], options=LGC[:5])],
    'Sword or axe. Light armour +3, shield +2; thrusting spear, throwing spear or javelins +2. Army Standard Bearer, Warband. If he joins a unit it is Stubborn until he is killed or leaves.', mx=1, page='78'))
LG.append(U('Characters', 'Clan-Chieftains', [M('Clan-Chieftain', '5 5 5 4 4 2 5 3 7', 80, weapons=['Hand Weapon'], rules=['Warband'], options=LGC + [('May be Army General', 25)])],
    'Sword or axe. Light armour +3, shield +2; thrusting spear, throwing spear or javelins +2; a Chieftain of the Apuani may have a pennato (+2). May be Army General (+25 pts). Warband.', page='78'))
LG.append(U('Characters', 'Ligurian Bard', [M('Bard', '5 3 4 3 4 2 5 2 8', 80, weapons=['Hand Weapon'], rules=['Warband', 'Hatred'], options=[('Shield', 2), ('Sling', 2), ('Javelins', 2), ('Pennato (Apuani Bard only)', 2)])],
    'Hand weapon. Warband. Any unit to which the Bard is attached becomes subject to Hatred. 0-1.', mx=1, page='78'))
LG.append(U('Warriors', 'Warriors', [M('Warrior', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'],
    options=[('Wild beast skins', 1), ('Throwing spear (replaces mixed weapons)', 1)])],
    'Mixed weapons and shield. Warband, Light Infantry, Stealth.', page='78'))
LG.append(U('Warriors', 'Veterans', [M('Veteran', '5 4 3 3 3 1 3 1 6', 11, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], rules=['Warband'], options=[('Thrusting spear (replaces throwing spear)', 0)])],
    'Sword or axe, throwing spear, light armour, shield. Warband. 0-1.', mx=1, page='78'))
LG.append(U('Warriors', 'Apuani', [M('Apuani Warrior', '5 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband', 'Stealth'], options=[('Wild beast skins', 1), ('Javelins', 1)])],
    'Pennato (hand weapon, or +1 Strength as a halberd when used two-handed), shield. Warband, Light Infantry, Stealth. 0-1.', mx=1, page='79'))
LG.append(U('Warriors', 'Capillati', [M('Capillati Warrior', '5 3 3 3 3 1 3 1 6', 9, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Fear', 'Mixed Weapons (Hannibal)'], options=[('Wild beast skins', 1)])],
    'Mixed weapons and shield. Warband, Light Infantry, Stealth. Capillati cause fear. 0-1.', mx=1, page='79'))
LG.append(U('Skirmishers', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 6', 4, mn=5, weapons=['Dagger'], rules=['Feigned Flight'], options=[('Javelins', 1), ('Sling', 1), ('Composite bow', 2)])],
    'Knife. Skirmishers, Feigned Flight (Ligurian skirmishers only). They do not have Warband psychology.', page='79'))
LG_VARIANTS = [('Ligurian', {'Characters': ('max', 25), 'Warriors': ('min', 50), 'Skirmishers': ('max', 25)}, 'Standard Ligurian composition.')]
LG_NOTES = ('LIGURIAN ARMY LIST (Hannibal & the Punic Wars, pp.76-79)\n'
  'Characters up to 25%; at least one must be the overall leader. If the Prince is not the Army General the commander must be a Clan Chieftain. Warriors at least 50%; Skirmishers up to 25%.\n'
  'Special rules: Warband (all Warband Psychology rules); Feigned Flight for Ligurian skirmishers only (they rally immediately after a flee or fire-and-flee charge reaction and may reform facing any direction; the charging enemy still counts as charging); Cycnus Standard Bearer (swan symbol); Ligurian Bard; Pennato (hand weapon, or like a halberd with +1 Strength two-handed); Wild Beast Skin (+1 save bonus against missile fire, combinable with a shield).\n'
  'Optional variants (opponent\'s consent): an Apuani army ignores the 0-1 limit on Apuani and omits Capillati and Veterans; an Alpine Capillati army (1st century BC) ignores the 0-1 limit on Capillati and omits Apuani and Veterans.')

# ------------------------------------------------------------------ GALLIC
GL = []
GLC = [('Thrusting spear', 2), ('Throwing spear', 2), ('Javelins', 2), ('Light armour', 3), ('Shield', 2), ('Horse (free)', 0), ('Light chariot (Cavalry and Chariots, extra cost)', 0)]
GL.append(U('Characters', 'High Chieftain', [M('High Chieftain', '5 6 6 4 4 3 6 3 7', 140, weapons=['Hand Weapon'], rules=['Warband', 'Stealth'], options=GLC + [('Warhorse (replaces horse)', 4)])],
    'Sword. Thrusting or throwing spear +2, javelins +2, light armour +3, shield +2. Horse (free) or Warhorse (+4), or a Light Chariot at additional cost. Army General, Warband, Stealth.', mx=1, page='80'))
GL.append(U('Characters', 'Army Battle Standard', [M('Army Standard Bearer', '5 4 4 4 3 1 4 2 5', 50, weapons=['Hand Weapon'], rules=['Warband', 'Stealth'], options=GLC)],
    'Sword. Thrusting or throwing spear +2, javelins +2, light armour +3, shield +2. Horse (free) or Light Chariot at additional cost. Army Standard Bearer, Warband, Stealth.', mx=1, page='80'))
GL.append(U('Characters', 'Chieftains', [M('Chieftain', '5 5 5 4 4 2 5 3 6', 70, weapons=['Hand Weapon'], rules=['Warband', 'Stealth'], options=GLC + [('May be Army General', 25)])],
    'Sword. Thrusting or throwing spear +2, javelins +2, light armour +3, shield +2. Horse (free) or Light Chariot at additional cost. May be Army General (+25 pts). Warband, Stealth.', page='80'))
GL.append(U('Infantry', 'Warriors', [M('Warrior', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Stealth', 'Mixed Weapons (Hannibal)'],
    options=[('Light armour (up to a quarter of figures)', 2), ('Stubborn (one unit, per figure)', 3)])],
    'Shield and mixed weapons. Up to a quarter of the figures in each unit may have light armour (+2). Warband, Stealth. One unit in the army may be Stubborn (+3 per figure).', page='80'))
GL.append(U('Infantry', 'Fanatics', [M('Fanatic', '5 3 3 3 3 1 3 1 5', 10, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Frenzy', 'Warband', 'Stealth', 'Mixed Weapons (Hannibal)'])],
    'Shield and mixed weapons. Frenzy, Warband, Stealth. At least one unit of Chariots must be in the army to take any Fanatics; total Fanatic figures may not exceed total Warrior figures.', page='81'))
GL.append(U('Cavalry and Chariots', 'Cavalry', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 6', 21, mn=5, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Warband', 'Mixed Weapons (Hannibal)'])],
    'Light armour, shield, mixed weapons. Warband.', page='81'))
GL.append(U('Cavalry and Chariots', 'Chariots', [M('Noble Chariot', '8 4 4 3 4 1 4 2 6', 36, mn=3, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Chariots'])],
    'Pulled by two horses, crewed by a driver and a noble warrior (sword, javelins, light armour, shield). Light chariots as in the WAB rulebook. Not subject to Warband Psychology. Squadrons of at least three models. With opponent\'s permission use the Ancient Briton chariot rules from AoA p.47.', page='81'))
GL.append(U('Supporting Infantry', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Dagger'], rules=[], options=[('Buckler', 1), ('Javelins', 1), ('Sling', 2), ('Bow', 3)])],
    'Dagger or other improvised weapon. Skirmishers. A unit of Slingers or Bowmen may not outnumber any other skirmishing infantry unit in the army.', page='81'))
GL_VARIANTS = [('Gallic', {'Characters': ('max', 25), 'Infantry': ('min', 50), 'Cavalry and Chariots': ('max', 25), 'Supporting Infantry': ('max', 20)}, 'Standard Gallic composition.')]
GL_NOTES = ('GALLIC ARMY LIST (Hannibal & the Punic Wars, pp.80-81)\n'
  'Represents the Celtic tribes of northern Italy and the Mediterranean coast; may also represent northern Spanish tribes. Characters up to 25%; at least one must be the overall leader; if no High Chieftain is taken the commander must be a Chieftain. Infantry at least 50%; Cavalry and Chariots up to 25%; Supporting Infantry up to 20%.\n'
  'Allies: limited documentation; Hannibal\'s Boii and Insubres are better represented as Gallic allies for a Carthaginian army.')

# Shared rules for these lists
OTHER_RULES = {}
