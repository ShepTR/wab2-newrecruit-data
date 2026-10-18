# Fall of the West (Warhammer Historical, 2002) army lists: Roman, Barbarian and Warlord. Book pp.44-48, special rules p.58. pdf page = book + 2.
# Model stats order: M WS BS S T W I A Ld
from rb_data import M, U

GEN_OPT = [('Warhorse', 3), ('Light armour', 3), ('Shield', 1), ('Large shield', 3)]
BAR_OPT = [('Warhorse', 3), ('Throwing spear', 2), ('Shield', 2), ('Heavy armour (replaces light armour)', 1), ('Bow', 3), ('Kontos', 3), ('Barding (-1 M)', 4)]
OFF_OPT = [('Warhorse', 3), ('Light armour', 3)]

CH = []
CH.append(U('Characters', 'Roman Army General', [M('Roman Army General', '4 5 5 3 3 3 6 2 9', 135, weapons=['Hand Weapon'], rules=['Army General (Fall of the West)', 'Drilled', 'Stubborn'], options=GEN_OPT)],
    'Sword. May ride a warhorse (+3), light armour (+3), shield (+1) or large shield (+3). Army General: any unit within 12" may use his Leadership when it takes a Leadership test. Drilled. Stubborn. 0-1. A Roman or Warlord army may be led by a Roman senior commander (magister, patrician, warlord, a member of the Imperial family or the Emperor).', mx=1, page='44'))
CH.append(U('Characters', 'Barbarian Warlord', [M('Barbarian Warlord', '5 6 6 4 4 3 6 3 9', 145, weapons=['Hand Weapon', 'Light Armour'], rules=['Army General (Fall of the West)'], options=BAR_OPT)],
    'Sword and light armour. May ride a warhorse (+3), throwing spear (+2), shield (+2), heavy armour (+1, replaces light), bow (+3), kontos (+3), barding (+4, -1 Movement). Army General. May be accompanied by a unit of Comitatus. 0-1. A Barbarian or Warlord army may be led by a Barbarian senior chief (a powerful regales or warlord).', mx=1, page='45'))
CH.append(U('Characters', 'Comitatus', [M('Comitatus', '5 4 4 4 3 1 4 1 8', 13, mn=5, weapons=['Light Armour', 'Shield'], rules=['Mixed Weapons (Fall of the West)', 'Comitatus Oath'],
    options=[('Heavy throwing spear', 3), ('Heavy armour (replaces light armour)', 1), ('Bow', 3), ('Kontos', 3), ('Barding (-1 M)', 4), ('Horse (M8)', 10)])],
    'A barbarian chief\'s personal bodyguard. Light armour, shields and mixed weapons (swords, javelins, axes). May have heavy throwing spears (+3), heavy armour (+1, replaces light), bow (+3), kontos (+3), barding (+4, -1 Movement). Would normally be mounted (+10 pts, Movement 8). Must be led by the army general.', page='45'))
CH.append(U('Characters', 'Roman Army Standard Bearer', [M('Roman Army Standard Bearer', '4 4 4 4 3 1 4 2 8', 68, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard', 'Drilled', 'Stubborn'], options=[('Warhorse', 3), ('Shield', 1), ('Large shield', 3)])],
    'Sword and light armour. May ride a warhorse (+3), shield (+1) or large shield (+3). Any unit within 12" of the Standard Bearer may re-roll any failed Break test. Drilled. Stubborn. 0-1 (Roman or Warlord army).', mx=1, page='45'))
CH.append(U('Characters', 'Barbarian Army Warbanner', [M('Barbarian Warbanner Bearer', '5 4 4 4 3 1 4 2 8', 68, weapons=['Hand Weapon', 'Light Armour'], rules=['Army Standard'], options=BAR_OPT)],
    'Sword and light armour. May ride a warhorse (+3), throwing spear (+2), shield (+2), heavy armour (+1, replaces light), bow (+3), kontos (+3), barding (+4, -1 Movement). Any unit within 12" of the Standard Bearer may re-roll any failed Break tests. 0-1 (Barbarian or Warlord army).', mx=1, page='45'))
CH.append(U('Characters', 'Priest', [M('Priest', '5 3 3 3 3 2 4 2 6', 75, weapons=['Hand Weapon'], rules=['Priest (Fall of the West)'])],
    'Hand weapons. No options. Any unit that includes a pagan priest hates all its enemies; a Catholic priest hates enemies who are pagans or Arian Christians; an Arian priest hates enemies who are pagans or Catholic Christians. If an army includes a priest his opponent must declare a religious alignment. Pagan or Roman Catholic priests may be attached to a Roman army; pagan or Arian Christian priests to a Barbarian army. 0-1.', mx=1, page='45'))
CH.append(U('Characters', 'Senior Roman Officer', [M('Senior Roman Officer', '4 5 5 3 3 3 6 2 9', 110, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=OFF_OPT)],
    'Sword. May ride a warhorse (+3) and wear light armour (+3). Drilled. Stubborn. A senior officer (comes, dux, etc.) to assist the general and command units, brigades or small armies.', page='45'))
CH.append(U('Characters', 'Senior Barbarian Chief', [M('Senior Barbarian Chief', '5 6 6 4 4 3 5 3 8', 115, weapons=['Hand Weapon', 'Light Armour'], options=BAR_OPT)],
    'Sword and light armour. May ride a warhorse (+3), throwing spear (+2), shield (+2), heavy armour (+1, replaces light), bow (+3), kontos (+3), barding (+4, -1 Movement). A sub-regales commanding key units or a small army.', page='45'))
CH.append(U('Characters', 'Junior Roman Officer', [M('Praepositus', '4 4 4 3 3 2 5 2 8', 55, weapons=['Hand Weapon'], rules=['Drilled', 'Stubborn'], options=OFF_OPT)],
    'Sword. May ride a warhorse (+3) and wear light armour (+3). Drilled. Stubborn.', page='46'))
CH.append(U('Characters', 'Barbarian Chieftain (Optimates)', [M('Optimates', '5 4 4 4 3 2 4 2 8', 50, weapons=['Hand Weapon', 'Light Armour'], options=BAR_OPT)],
    'Sword and light armour. May ride a warhorse (+3), throwing spear (+2), shield (+2), heavy armour (+1, replaces light), bow (+3), kontos (+3), barding (+4, -1 Movement). Barbarian optimates could be attached to barbarian units as leaders.', page='46'))

RI_OPT = [('Light armour', 2), ('Javelins and darts', 2), ('Heavy throwing spear (replaces throwing spear)', 1), ('Drilled', 1)]
RI_NOTE = ('Large shield, sword and throwing spear. May have light armour (+2), javelins and darts (+2), heavy throwing spear instead of throwing spear (+1). May be drilled (+1 pt). Can form shield wall. Archers would normally be deployed at the rear of the unit. One soldier in four may replace the throwing spear and shield with a bow (+1 pt) but may not take other weapon options except light armour (not modelled: all models of a unit are equipped alike). Skirmishers replace their equipment with shield, hand weapon, javelins and darts and may take no other options.')
RI = []
RI.append(U('Roman Infantry', 'Pedes', [M('Pedes', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Large Shield'], rules=['Shield Wall (Fall of the West)'], options=RI_OPT)],
    'The "poor bloody infantry" of a Roman army. ' + RI_NOTE + ' One unit may skirmish.', page='46'))
RI.append(U('Roman Infantry', 'Palantina', [M('Palantine', '4 3 3 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Large Shield'], rules=['Shield Wall (Fall of the West)'], options=RI_OPT)],
    'Originally the Emperor\'s personal force. ' + RI_NOTE + ' Any unit may skirmish. Not found in Limitanei armies.', page='46'))
RI.append(U('Roman Infantry', 'Veterans', [M('Veteran', '4 4 4 3 3 1 4 1 8', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Large Shield'], rules=['Shield Wall (Fall of the West)'], options=RI_OPT)],
    'Years of successful battles; may have supplemented equipment with loot. ' + RI_NOTE + ' Any unit may skirmish.', page='46'))
RI.append(U('Roman Infantry', 'Roman Sagittarii', [M('Sagittarii', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Bow'], rules=[], options=[('Light armour', 2)])],
    'Bow and sword. May take light armour (+2). Light Infantry. Specialist archer units.', page='46'))
RI.append(U('Roman Infantry', 'Militia or Bacaudae', [M('Militia', '4 2 2 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon'], rules=[])],
    'Roman citizens in arms: hunting gear, farm tools and other sharp implements treated as hand weapons. Light Infantry. May not have standards or musicians in the unit; may have a Roman infantryman from one of the above types as a leader.', page='46'))

RC = []
RC.append(U('Roman Cavalry', 'Roman Shock Cavalry', [M('Roman Shock Cavalryman', '8 3 3 3 3 1 3 1 6', 21, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour', 'Throwing Spear'], rules=['Drilled'], options=[('Palantina (+1 Ld)', 1)])],
    'Includes Scutarii, Promoti and Stablesiani. Sword, shield, light armour and throwing spear. May be upgraded to palantina (+1 Ld, +1 pt). Drilled.', page='47'))
RC.append(U('Roman Cavalry', 'Scholae', [M('Scholae', '8 4 4 3 3 1 4 1 8', 26, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour', 'Throwing Spear'], rules=['Drilled'])],
    'Elite shock cavalry found in praesental armies. Sword, shield, light armour and throwing spear. Drilled.', page='47'))
RC.append(U('Roman Cavalry', 'Light Cavalry', [M('Light Cavalryman', '8 2 3 3 3 1 3 1 5', 14, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=[], options=[('Light armour', 2), ('Bow (replaces javelins and shield)', 1)])],
    'Includes Equites Sagittarii, Mauri and Dalmatae. Sword, javelins and shield. May have light armour (+2); may replace javelins and shield with bow (+1). Light Cavalry.', page='47'))
RC.append(U('Roman Cavalry', 'Heavy Shock Cavalry', [M('Heavy Shock Cavalryman', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Kontos'], rules=['Drilled', 'Heavy Shock Cavalry'], options=[('Shield', 1), ('Barding (-1 M)', 4), ('Bow (replaces kontos; one unit)', 1)])],
    'Includes Cataphractii and Clibanarii. Heavy armour, sword, kontos. May have shield (+1) and barding (+4, -1 Movement). One unit may replace kontos with bow (+1). Drilled. 0-2 units.', mx=2, page='47'))

BI = []
BI.append(U('Barbarian Infantry', 'Warrior', [M('Warrior', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Shield'], rules=['Mixed Weapons (Fall of the West)', 'Warband'], options=[('Heavy throwing spear (replaces mixed weapons)', 2)])],
    'Shields and mixed weapons (swords, javelins, axes). May replace mixed weapons with heavy throwing spear (eg angons or franciscas) +2. A warrior unit may be designated light infantry and may skirmish at no extra cost. Warband rules apply. If a character joins the unit or the army General is within 12" the unit may use either its own modified Ld or the character\'s/General\'s Ld; if the latter is used it is not modified by the unit\'s rank bonus.', page='48'))
BC = []
BC.append(U('Barbarian Cavalry', 'Barbarian Shock Cavalry', [M('Barbarian Shock Cavalryman', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Light Armour', 'Shield'], rules=['Mixed Weapons (Fall of the West)'])],
    'Most Barbarian cavalry in Western Europe. Light armour, shields and mixed weapons (swords, javelins, axes).', page='48'))
BC.append(U('Barbarian Cavalry', 'Barbarian Light Cavalry', [M('Barbarian Light Cavalryman', '8 2 3 3 3 1 3 1 5', 14, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=[], options=[('Bow (replaces javelins and shield)', 2)])],
    'Includes North African Moors. Sword, javelins and shield. May replace javelins and shield with bow (+2). Light Cavalry.', page='48'))
BC.append(U('Barbarian Cavalry', 'Steppe Cavalry', [M('Steppe Cavalryman', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Nomad Cavalry (Fall of the West)'], options=[('Shield', 1), ('Throwing spear', 1), ('Lassoes', 1)])],
    'Includes Huns and Alans. Sword and bow. May have shield (+1), throwing spear (+1) and lassoes (+1). Light Cavalry. Nomad cavalry. Normally restricted to Central and Eastern barbarian armies.', page='48'))
BC.append(U('Barbarian Cavalry', 'Noble Steppe Cavalry', [M('Noble Steppe Cavalryman', '8 4 4 3 3 1 4 1 7', 26, mn=5, weapons=['Heavy Armour', 'Hand Weapon', 'Kontos'], rules=[], options=[('Shield', 2), ('Barding (-1 M)', 4), ('Bow and throwing spear (replaces kontos)', 2)])],
    'Sarmatians, Alans and Huns. Heavy armour, sword, kontos. May have shield (+2) and barding (+4, -1 Movement). May replace kontos with bow and throwing spear (+2); Noble Steppe cavalry armed with bow and throwing spear are Nomad cavalry; those armed with a kontos fight in a dense formation (maximum rank bonus +2) and lose half their movement if they wheel more than 1". 0-2 units. Central and Eastern barbarian armies only.', mx=2, page='48'))
BC.append(U('Barbarian Cavalry', 'North African Camelry', [M('Camelry Rider', '6 2 3 3 3 1 3 1 5', 16, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Camelry Fear (Fall of the West)'])],
    'Sword, javelins and shield. Causes fear in enemy cavalry. Included for North African Moors.', page='48'))

SP = []
SP.append(U('Special Units', 'Currus Drepanus', [M('Currus Drepanus', '6 3 3 4 4 2 3 4 6', 80, weapons=['Hand Weapon', 'Kontos', 'Heavy Armour', 'Buckler'], rules=['Currus Drepanus'])],
    'Shock chariot with hinged scythes drawn by cataphract horses. Hand weapons, kontos, heavy armour, bucklers and barding (statistics already include bonuses for equipment). No options. D3+2 automatic hits when charging in addition to normal attacks. Destroyed if it breaks from close combat (it is not destroyed after charging). Move as a chariot. 0-2. Roman artillery is otherwise as in the rulebook (p.124).', mx=2, page='48'))

# Roman artillery "is otherwise as in the rulebook (p.124)" (Fall of the West p.48): Scorpio, Ballista and Tormenta from rulebook pp.179-181.
import copy as _copy
from rb_data import ROMAN as _RB
for _n in ('Light Bolt Thrower (Scorpio)', 'Bolt Thrower (Ballista)', 'Small Stone Thrower (Tormenta)'):
    _u = _copy.deepcopy(next(u for u in _RB if u['name'] == _n))
    _u['notes'] = _u['notes'] + ' Roman artillery as in the rulebook Roman list (Fall of the West p.48; rulebook pp.179-181). Special Units: at most a quarter of the army\'s points.'
    _u['page'] = '179-181 (rulebook)'
    SP.append(_u)

RULES = {
 'Army General (Fall of the West)': ('Fall of the West p.44-45', 'Any unit within 12" of the General may use his Leadership value when it takes a Leadership test.'),
 'Comitatus Oath': ('Fall of the West p.45', 'Must be led by the army general. Barbarian bodyguards took oaths of allegiance extremely seriously. If the General is killed roll a D6: on a 4+ they immediately attack the nearest enemy and are immune to Psychology and Break tests. If they eliminate their opponent they attack the next nearest enemy unit and so on.'),
 'Priest (Fall of the West)': ('Fall of the West p.45', 'Any unit that includes a pagan priest hates all its enemies. Any unit that includes a Catholic priest hates enemies who are pagans or Arian Christians. Any unit that includes an Arian priest hates enemies who are pagans or Catholic Christians. If an army includes a priest, his opponent must declare a religious alignment.'),
 'Shield Wall (Fall of the West)': ('Fall of the West p.58', 'In the Army lists some units of Roman infantry can form a shield wall. They may do this instead of moving. As long as the unit is in a shield wall all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer a -1 to hit modifier. The unit benefits from the shield wall as long as it does not move or lose a round of close combat.'),
 'Mixed Weapons (Fall of the West)': ('Fall of the West p.58', 'Whatever the models are actually carrying they count as being armed with javelins if they are in skirmish formation and throwing spears otherwise. This replaces the mixed weapons rule of the Barbarian Army list in the Warhammer Ancient Battles rulebook (which counted javelins in any formation); players using the rulebook Barbarian list may use this interpretation at +1 pt per model it applies to.'),
 'Nomad Cavalry (Fall of the West)': ('Fall of the West p.58', 'a) Nomad cavalry may make a free march move after both sides have deployed; they may not use it to charge and may not shoot after making it. b) They do not suffer the -1 to hit for shooting if they moved in the same turn, but this does not allow them to shoot if they charge or march. c) They make a normal move immediately after shooting (Shooting phase only, not a charge reaction, and the unit may not have marched). d) If they flee or fire and flee as a charge reaction they rally immediately at the end of their move and may reform facing any direction; the charging enemy still counts as charging and the Nomad cavalry may fight in the close combat phase if encountered.'),
 'Lassoes': ('Fall of the West p.58', 'Some steppe cavalry can use lassoes. A lasso attack is an additional special attack made by a successfully charging cavalryman before normal combat. Roll a D6: on a 6+ the lasso attack is successful and an enemy model in base contact with the attacker loses one attack for that round of combat. Lassoes cannot be used in subsequent rounds of combat or by a model that has been charged.'),
 'Barbarian Cunning': ('Fall of the West p.58', 'The Barbarian player may hide a unit in a piece of suitable rough terrain on his half of the battlefield, noting its position on paper. The concealed unit is revealed and placed at the Barbarian General\'s choice or when a Roman comes within 6" of the concealing terrain. Warbands must still check for undisciplined movement but, provided they have a character leading them, may re-roll the dice once.'),
 'Heavy Shock Cavalry': ('Fall of the West p.47', 'Heavy shock cavalry fought in a dense formation and count their rank bonus as light infantry do (maximum +2). They lose half their movement if they wheel more than 1" in a move.'),
 'Camelry Fear (Fall of the West)': ('Fall of the West p.48', 'North African camelry cause fear in enemy cavalry.'),
 'Currus Drepanus': ('Fall of the West p.48', 'D3+2 automatic hits when charging in addition to normal attacks. Destroyed if it breaks from close combat (it is not automatically destroyed after charging). Moves as a chariot.'),
}
ROMAN_UNITS = CH_ROMAN = None
