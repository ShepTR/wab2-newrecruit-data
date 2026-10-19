# El Cid: Warfare in the Spanish Reconquista 900-1250 AD (Warhammer Historical, 2007, James Morris) army lists:
# Christian Spain, Al-Andalus and The African Invaders (Almoravids & Almohads), with Aliados y Mercenarios units inside each catalogue.
# Book page numbers are printed page numbers. Percentages are by points. Model stats order: M WS BS S T W I A Ld
import copy
from rb_data import M, U
LISTS = []      # (key, display name, catalogue file, units, variants [(variant name, limits, text)], notes)
VAR = {}        # key -> {short variant name: full variant name}
AVAIL = []      # (key, unit, [short variant names])      unit only available in those compositions
UNAV = []       # (key, unit, [short variant names])      unit NOT available in those compositions
OPTAV = []      # (key, unit, option label, [short variant names])   option only available in those compositions
OPTRULE = []    # (key, unit, option label, rule name)
OPTSTAT = []    # (key, unit, option label, stat, value)
RATIOS = []     # (key, unit, [limiting units], per)
OPT_ONCE = []   # (key, [(unit, option label)])
PAIRS = []      # (key, [units], tag)
SECOND = {}     # (key, unit) -> [secondary pool category names]
UNIT_MAX_IN = []  # (key, unit, max, [short variants])   0-N only in those compositions
GEN = {}        # key -> ([units that are Army General by themselves], [(unit, option label)])   at most one Army General in the army
GEN_LABEL = 'Army General (if no other Army General)'
COND_CHARS = []; COSTV = []; STATV = []; HIRDMEN_LE_BONDIR = []
EXCL = [('AF', 'Imam', 'Christian Captain', 'Army General (if no other Army General)')]   # (key, unit, other unit, other unit's option): the unit and the option exclude each other

PRI_CH, PRI_CAV, PRI_INF, PRI_SK, PRI_MERC = 'Characters', 'Cavalry', 'Infantry', 'Skirmishers', 'Aliados y Mercenarios'
MERC_TAIL = ' Aliados y Mercenarios: may have a leader, standard bearer and musician as normal; roll a dice the first time each unit moves, charges or shoots (on a 1 it stays stationary); may not benefit from the Army General or Army Standard Bearer abilities (they may be led by any appropriate character). One Aliados y Mercenarios unit may be personally led by the Army General and is then exempt from these rules.'

# ------------------------------------------------------------------ Aliados y Mercenarios (book pp.54-55)
def MERC(name):
    d = {}
    d['Mercenary Spearmen'] = U(PRI_MERC, 'Mercenary Spearmen', [M('Spearmen', '4 4 3 3 3 1 4 1 7', 11, mn=5, weapons=['Thrusting Spear', 'Shield', 'Javelin'], rules=['Combined Formation (El Cid)', 'Aliados y Mercenarios'],
        options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Stubborn', 3)])],
        'Thrusting spear, shield, javelins. May have light armour (+2 pts) and/or large shields (+1 pt). A single unit of Mercenary Spearmen in an army may be Stubborn (+3 pts per model). Combined Formation: may have up to 50% Mercenary Archers in the rear ranks of the unit; Mercenary Archers cannot be combined with Stubborn Mercenary Spearmen.' + MERC_TAIL, page='54')
    d['Mercenary Archers'] = U(PRI_MERC, 'Mercenary Archers', [M('Archers', '4 3 3 3 3 1 4 1 7', 7, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Combined Formation (El Cid)', 'Aliados y Mercenarios'],
        options=[('Light armour', 2), ('Shield', 1)])],
        'Composite bow, sword. May have light armour (+2 pts) and/or shields (+1 pt). Light Infantry. May form a Combined Unit with Mercenary Spearmen.' + MERC_TAIL, page='54')
    d['Basque Javelinmen'] = U(PRI_MERC, 'Basque Javelinmen', [M('Javelinmen', '5 3 4 3 3 1 3 1 6', 9, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Feigned Flight', 'Aliados y Mercenarios'],
        options=[('Shield', 1), ('Throwing spear', 2), ('Light armour (Reconquista)', 2)])],
        'Javelins, hand weapons. May have shield (+1 pt) and/or throwing spears (+2 pts). Skirmishers. Feigned Flight.' + MERC_TAIL, page='54')
    d['Mercenary Jinetes'] = U(PRI_MERC, 'Mercenary Jinetes', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Feigned Flight', 'Aliados y Mercenarios'],
        options=[('Throwing spear', 2), ('Shield', 1), ('Exchange javelins for bow', 3), ('Light armour (Jinetes)', 2)])],
        'Javelins and hand weapon. May have throwing spears (+2 pts); may have shield (+1 pt). May exchange javelins for bow (+3 pts); bow-armed Mercenary Jinetes are Expert Horsemen. Light Cavalry. Feigned Flight.' + MERC_TAIL, page='55')
    d['Mercenary Caballeros'] = U(PRI_MERC, 'Mercenary Caballeros', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 8', 23, mn=5, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Feigned Flight', 'Aliados y Mercenarios'],
        options=[('Throwing spear', 2)])],
        'Hand weapons, light armour, javelins, shield. May have throwing spears (+2 pts). Light Cavalry. Feigned Flight.' + MERC_TAIL, page='55')
    d['Mercenary Crossbowmen'] = U(PRI_MERC, 'Mercenary Crossbowmen', [M('Merc. Crossbowmen', '4 3 3 3 3 1 4 1 7', 12, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], rules=['Aliados y Mercenarios'],
        options=[('Shield', 1)])],
        'Crossbow, sword, light armour. May have shield (+1 pt). Light Infantry. You may not have more units of Mercenary Crossbowmen than units of Mercenary Knights in an army.' + MERC_TAIL, page='55')
    d['Mercenary Knights'] = U(PRI_MERC, 'Mercenary Knights', [M('Merc. Knights Cavalryman', '8 4 3 3 3 1 4 1 8', 27, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Ferocious Charge', 'Knights Rank Bonus', 'Aliados y Mercenarios'],
        options=[('Ride a warhorse', 4), ('Exchange light armour for heavy armour', 1), ('Exchange thrusting spear for throwing spear', 0), ('Exchange thrusting spear for lance', 4), ('Barding (-1 M)', 2)])],
        'Horse, thrusting or throwing spear, light armour, sword, shield. May ride a warhorse (+4 pts). May exchange light armour for heavy armour (+1 pt). Ferocious Charge. May count a Rank Bonus of up to +1 in combat. Later Taifas and Almohads: may exchange spear for lance (+4 pts per model) and have horse barding (+2 pts per model).' + MERC_TAIL, page='55')
    d['Ghuzz Horse Archers'] = U(PRI_MERC, 'Ghuzz Horse Archers', [M('Ghuzz Cavalryman', '8 3 4 3 3 1 3 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Feigned Flight', 'Parthian Shot', 'Expert Horsemen', 'Aliados y Mercenarios'],
        options=[('Shield', 1), ('Light armour', 2), ('Throwing spear', 2)])],
        'Hand weapon, horse and composite bow. May have shields (+1 pt) or light armour (+2 pts). May have throwing spears (+2 pts). Light Cavalry. Feigned Flight. Parthian Shot (a normal move immediately after shooting, only in the Shooting phase; not a charge reaction; may not march). Expert Horsemen. 0-1 unit.' + MERC_TAIL, mx=1, page='55')
    return copy.deepcopy(d[name])

PRIM_OF = {}
def pools(key, comps, mem):
    """mem: {unit name: {composition: 'C' or 'U'}} -> SECOND pool categories"""
    for unit, cm in mem.items():
        SECOND[(key, unit)] = [f'{"Common" if t == "C" else "Uncommon"} Troops: {c}' for c, t in cm.items()]

def variants(key, comps, lims):
    VAR[key] = {c: f'El Cid: {lims[c][0]} - {c}' for c in comps}
    out = []
    for c in comps:
        _, chars, com, unc, txt = lims[c]
        out.append((VAR[key][c], {'Characters': {'max': chars}, f'Common Troops: {c}': com, f'Uncommon Troops: {c}': {'max': unc}}, txt))
    return out

ARMOUR_H = 'Exchange light armour for heavy armour'
HEAVY_R = 'Heavy armour (replaces light armour)'

# ------------------------------------------------------------------ CHRISTIAN SPAIN (book pp.7-16)
CS = []
CCH = [('Ride a horse', 8), ('Ride a warhorse', 16), ('Javelins', 2), ('Throwing spear', 2), ('Thrusting spear', 2), (ARMOUR_H, 1), ('Lance', 4), ('Barding (-1 M)', 2)]
CS.append(U(PRI_CH, 'Rey', [M('King', '4 6 5 4 4 3 6 3 9', 170, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General'], options=CCH)],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear heavy armour (+1 pt). Army General. 0-1. Not available in Asturias & the Early Christian Kingdoms. Reconquista: may have a lance (+4 pts; no javelins, throwing or thrusting spear as well) and horse barding (+2 pts).', mx=1, page='12'))
CS.append(U(PRI_CH, 'Infante', [M('Prince', '4 5 4 4 4 2 5 2 8', 75, weapons=['Hand Weapon', 'Light Armour', 'Shield'], options=CCH + [(GEN_LABEL, 25)])],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear heavy armour (+1 pt). If no other Army General is taken, a single Infante may be made Army General for +25 pts (in Asturias & the Early Christian Kingdoms the Army General may only be an Infante). Asturias: characters may not wear heavy armour or ride warhorses. Reconquista: may have a lance (+4 pts) and horse barding (+2 pts).', page='12'))
CS.append(U(PRI_CH, 'Armiger', [M('Army Stan. Bearer', '4 5 4 4 4 2 5 2 8', 90, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army Standard'], options=[('Ride a horse', 8), ('Ride a warhorse', 16), (ARMOUR_H, 1), ('Barding (-1 M)', 2)])],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May wear heavy armour (+1 pt). Army Standard Bearer. 0-1. Asturias: no heavy armour or warhorse. Reconquista: horse barding (+2 pts); the Armiger may not take a lance.', mx=1, page='12'))
CS.append(U(PRI_CH, 'Cantador', [M('Cantador', '4 4 4 3 3 2 4 1 8', 50, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Cantador (El Cid)'], options=CCH)],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear heavy armour (+1 pt). The Cantador may lead a single formed unit (not skirmishers); after deployment, before the first move, roll a D6 for his song. 0-1. Asturias: no heavy armour or warhorse. Reconquista: may have a lance (+4 pts) and horse barding (+2 pts).', mx=1, page='12'))
CS.append(U(PRI_CH, 'Bishop', [M('Priest', '4 4 4 4 3 2 4 2 8', 80, weapons=['Hand Weapon'], rules=['Bishop (El Cid)'],
    options=[('Ride a horse', 8), ('Ride a warhorse', 16), ('Javelins', 2), ('Throwing spear', 2), ('Thrusting spear', 2), ('Light armour', 3), (HEAVY_R, 4), ('Shield', 2), ('Lance', 4), ('Barding (-1 M)', 2), ('Crusading Bishop', 40)])],
    'Sword or mace. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear light armour (+3 pts) or heavy armour (+4 pts; light and heavy armour are exclusive) and may carry a shield (+2 pts). Any unit led by the Bishop may re-roll failed Panic tests. 0-1. Asturias: no heavy armour or warhorse. Reconquista: may be upgraded to a Crusading Bishop (+40 pts; Ld 9, Hatred of the enemy, Bloodthirsty with the unit he leads, cannot re-roll failed Panic tests), may have a lance (+4 pts) and horse barding (+2 pts).', mx=1, page='12'))
CS.append(U(PRI_CAV, 'Jinetes', [M('Light Horseman Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Feigned Flight'],
    options=[('Throwing spear', 2), ('Shield', 1), ('Light armour (Reconquista)', 2)])],
    'Javelins, hand weapon. May have throwing spears (+2 pts). May have a shield (+1 pt). Light Troops (Light Cavalry). Feigned Flight. Reconquista: may have light armour (+2 pts per model).', page='13'))
CS.append(U(PRI_CAV, 'Caballeros', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 8', 24, mn=5, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Feigned Flight'], options=[('Throwing spear', 2)])],
    'Hand weapons, javelins, light armour, shield. May have throwing spears (+2 pts). Light Troops (Light Cavalry). Feigned Flight.', page='13'))
CS.append(U(PRI_CAV, 'Caballeros Hidalgos', [M('Noble Knights Cavalryman', '8 4 3 3 3 1 4 1 8', 26, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Ferocious Charge', 'Knights Rank Bonus'],
    options=[('Ride a warhorse', 4), (ARMOUR_H, 1), ('Exchange thrusting spear for throwing spear', 0), ('Exchange thrusting spear for lance', 4), ('Barding (-1 M)', 2)])],
    'Horse, thrusting or throwing spear, light armour, sword, shield. May ride a warhorse (+4 pts). May exchange light armour for heavy armour (+1 pt). Ferocious Charge. May count a Rank Bonus of up to +1 in combat. Not available in Asturias. Reconquista: may exchange thrusting spears for lances (+4 pts per model) and have horse barding (+2 pts per model).', page='13'))
CS.append(U(PRI_CAV, 'Caballeros Villanos', [M('Commoner Knights Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Knights Rank Bonus'],
    options=[('Light armour', 2), ('Exchange thrusting spear for throwing spear', 0), ('Ride a warhorse (Reconquista)', 4), ('Exchange thrusting spear for lance (Reconquista)', 2)])],
    'Horse, thrusting or throwing spear, sword, shield. May wear light armour (+2 pts). May count a Rank Bonus of up to +1 in combat. Not available in Asturias. Reconquista: may ride warhorses (+4 pts per model) and exchange thrusting spears for lances (+2 pts per model).', page='13'))
CS.append(U(PRI_CAV, 'Caballeros de las Ordenes Militares', [M('Military Order Knights Cavalryman', '8 4 3 3 3 1 4 1 9', 27, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Ferocious Charge', 'Knights Rank Bonus', 'Bloodthirsty'],
    options=[('Ride a warhorse', 4), (ARMOUR_H, 1), ('Exchange thrusting spear for lance', 4), ('Barding (-1 M)', 2)])],
    'Horse, thrusting spear, light armour, sword, shield. May have warhorse (+4 pts). May exchange light armour for heavy armour (+1 pt). May exchange thrusting spear for lance (+4 pts). May have horse barding (+2 pts). Ferocious Charge. May count a Rank Bonus of up to +1 in combat. Bloodthirsty. Reconquista only.', page='13'))
CS.append(U(PRI_INF, 'Guard Spearmen', [M('Guard', '4 4 4 3 3 1 4 1 8', 14, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Javelin'], options=[('Light armour', 2), ('Stubborn', 3)])],
    'Sword, thrusting spear, shield, javelins. May have light armour (+2 pts). May be Stubborn (+3 pts). 0-1 unit. Not available in Asturias.', mx=1, page='13'))
CS.append(U(PRI_INF, 'Peones', [M('Spearmen', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Thrusting Spear', 'Shield', 'Javelin'], rules=['Combined Formation (El Cid)'],
    options=[('Exchange thrusting spear for throwing spear', 1), ('Designate as light infantry (free)', 0), ('Light armour (Reconquista)', 2)])],
    'Thrusting spear, shield, javelins. May exchange thrusting spear for throwing spear (+1 pt). Any Peones unit may be declared Light Infantry prior to deployment for no extra cost. Combined Formation: may have up to 50% Arqueros in the rear ranks of the unit. Reconquista: may have light armour (+2 pts per model).', page='13'))
CS.append(U(PRI_INF, 'Arqueros', [M('Archers', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Combined Formation (El Cid)'], options=[('Shield', 1), ('Light armour (Reconquista)', 2)])],
    'Composite bow, sword. May have shield (+1 pt). Light Troops (Light Infantry). Combined Formation: may be combined with a Peones unit. Reconquista: may have light armour (+2 pts per model).', page='14'))
CS.append(U(PRI_SK, 'Skirmishers', [M('Skirmishers', '4 2 3 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'],
    options=[('Throwing spear', 2), ('Buckler', 1), ('Exchange javelins for shortbow', 0), ('Exchange javelins for sling', 0)])],
    'Hand weapons, javelins. May have throwing spears (+2 pts). May have buckler (+1 pt). May exchange javelins for shortbow or sling for no extra cost. Skirmishers.', page='14'))
CS.append(U(PRI_INF, 'Ballesteros', [M('Professional Crossbowmen', '4 3 3 3 3 1 4 1 7', 12, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], options=[('Shield', 1)])],
    'Crossbow, sword, light armour. May have shields (+1 pt). Light Infantry. The number of units of Ballesteros in an army cannot exceed the total number of units of Caballeros Hidalgos and Military Order Knights. Not available in Asturias.', page='14'))
CS.append(U(PRI_INF, 'Militia Crossbowmen', [M('Militia Crossbowmen', '4 3 2 3 3 1 3 1 7', 9, mn=5, weapons=['Crossbow', 'Hand Weapon'], options=[('Shield', 1), ('Light armour', 2)])],
    'Crossbow, sword. May have shields (+1 pt) and/or light armour (+2 pts). Light Infantry. The number of units of Militia Crossbowmen may not exceed the total number of units of Peones. The Age of El Cid: only a single unit (0-1). Not available in Asturias.', page='14'))
for n in ('Mercenary Spearmen', 'Mercenary Archers', 'Mercenary Jinetes', 'Basque Javelinmen'): CS.append(MERC(n))

CS_LIM = {
 'Asturias': ('Christian Spain', 25, {'min': 33}, 33, 'Asturias & the Early Christian Kingdoms, c.900-1040 AD (pp.9-10; Asturias, Leon, Galicia, Navarre, Aragon, Castile). Characters up to 25%: Infante, Armiger, Cantador, Bishop (no Rey); the Army General may only be an Infante. Characters cannot wear heavy armour or ride warhorses. Common Troops at least 33%: Jinetes, Caballeros, Peones, Arqueros, Skirmishers, Basque Javelinmen. Uncommon Troops up to 33%: Mercenary Spearmen, Archers and Jinetes. Andalusian Allies (up to 25%: Andalusian Jinetes, Noble Cavalry, Spearmen, Archers, Skirmishers, from the Al-Andalus list; they become Aliados y Mercenarios) are not built.'),
 'El Cid': ('Christian Spain', 25, {'min': 50}, 33, 'The Age of El Cid, c.1040-1100 AD (p.10). Characters up to 25% (Rey, Infante, Armiger, Cantador, Bishop; the Army General may be a Rey or an Infante). Common Troops at least 50%: Jinetes, Caballeros, Caballeros Hidalgos, Caballeros Villanos, Skirmishers. Uncommon Troops up to 33%: Guard Spearmen, Peones, Arqueros, Ballesteros, Militia Crossbowmen (0-1 unit only), Mercenary Spearmen, Archers and Jinetes, Basque Javelinmen. Andalusian Allies (up to 33%: Andalusian Jinetes, Noble Cavalry, Spearmen, Archers, Skirmishers) are not built.'),
 'Reconquista': ('Christian Spain', 25, {'min': 50}, 33, 'The Reconquista, c.1100-1250 AD (pp.10-11). Characters up to 25% (Rey, Infante, Armiger, Cantador, Bishop; the Army General may be a Rey or an Infante). Common Troops at least 50%: Jinetes, Caballeros, Caballeros Hidalgos, Caballeros Villanos, Caballeros de las Ordenes Militares, Guard Spearmen, Peones, Arqueros, Skirmishers, Militia Crossbowmen. Uncommon Troops up to 33%: Ballesteros, Basque Javelinmen, Mercenary Spearmen, Archers and Jinetes. Special rules: the Bishop may be upgraded to a Crusading Bishop (+40 pts); mounted characters and Caballeros Hidalgos may have horse barding (+2 pts); Caballeros Villanos can ride warhorses (+4 pts per model); Jinetes, Peones, Arqueros and Basque Javelinmen may have light armour (+2 pts per model); Hidalgos may exchange spears for lances (+4 pts), Villanos (+2 pts); any character except the Armiger may take a lance (+4 pts). Andalusian Allies (up to 33%: Andalusian Jinetes, Noble Cavalry, Knights, Spearmen, Archers, Skirmishers, Crossbowmen, Mounted Crossbowmen) are not built.'),
}
CS_V = variants('CS', ['Asturias', 'El Cid', 'Reconquista'], CS_LIM)
CS_NOTES = ('CHRISTIAN SPAIN ARMY LIST (El Cid, pp.7-16): Asturias & the Early Christian Kingdoms (c.900-1040), the Age of El Cid (c.1040-1100) and the Reconquista (c.1100-1250). Percentages are by points. Special rules p.9 (Bloodthirsty).\n'
  'Each troop type belongs to a Common or Uncommon pool that depends on the composition chosen; the units therefore also belong to pool categories named after the composition. Andalusian Allies are documented only (no pick list). Not enforced: mixed weapons within a unit, the Andalusian Allies percentages, and "may have up to 50% Arqueros" in combined units.')
LISTS.append(('CS', 'Christian Spain (El Cid)', 'Christian_Spain_El_Cid.cat', CS, CS_V, CS_NOTES))
ALL_CS = ['Asturias', 'El Cid', 'Reconquista']
UNAV += [('CS', 'Rey', ['Asturias']), ('CS', 'Caballeros Hidalgos', ['Asturias']), ('CS', 'Caballeros Villanos', ['Asturias']), ('CS', 'Guard Spearmen', ['Asturias']), ('CS', 'Ballesteros', ['Asturias']), ('CS', 'Militia Crossbowmen', ['Asturias'])]
AVAIL += [('CS', 'Caballeros de las Ordenes Militares', ['Reconquista'])]
pools('CS', ALL_CS, {
 'Jinetes': {c: 'C' for c in ALL_CS}, 'Caballeros': {c: 'C' for c in ALL_CS}, 'Skirmishers': {c: 'C' for c in ALL_CS},
 'Caballeros Hidalgos': {'El Cid': 'C', 'Reconquista': 'C'}, 'Caballeros Villanos': {'El Cid': 'C', 'Reconquista': 'C'}, 'Caballeros de las Ordenes Militares': {'Reconquista': 'C'},
 'Guard Spearmen': {'El Cid': 'U', 'Reconquista': 'C'}, 'Peones': {'Asturias': 'C', 'El Cid': 'U', 'Reconquista': 'C'}, 'Arqueros': {'Asturias': 'C', 'El Cid': 'U', 'Reconquista': 'C'},
 'Ballesteros': {'El Cid': 'U', 'Reconquista': 'U'}, 'Militia Crossbowmen': {'El Cid': 'U', 'Reconquista': 'C'},
 'Mercenary Spearmen': {c: 'U' for c in ALL_CS}, 'Mercenary Archers': {c: 'U' for c in ALL_CS}, 'Mercenary Jinetes': {c: 'U' for c in ALL_CS},
 'Basque Javelinmen': {'Asturias': 'C', 'El Cid': 'U', 'Reconquista': 'U'}})
CH_CS = ['Rey', 'Infante', 'Armiger', 'Cantador', 'Bishop']
for u in CH_CS:
    lab = ARMOUR_H if u != 'Bishop' else HEAVY_R
    OPTAV += [('CS', u, lab, ['El Cid', 'Reconquista']), ('CS', u, 'Ride a warhorse', ['El Cid', 'Reconquista']), ('CS', u, 'Barding (-1 M)', ['Reconquista'])]
    if u != 'Armiger': OPTAV += [('CS', u, 'Lance', ['Reconquista'])]
OPTAV += [('CS', 'Bishop', 'Crusading Bishop', ['Reconquista'])]
OPTSTAT += [('CS', 'Bishop', 'Crusading Bishop', 'Ld', 9)]
OPTRULE += [('CS', 'Bishop', 'Crusading Bishop', 'Crusading Bishop'), ('CS', 'Infante', GEN_LABEL, 'Army General (Chariot Wars)'), ('CS', 'Peones', 'Designate as light infantry (free)', 'Light Troops')]
OPTAV += [('CS', 'Caballeros Hidalgos', 'Exchange thrusting spear for lance', ['Reconquista']), ('CS', 'Caballeros Hidalgos', 'Barding (-1 M)', ['Reconquista']),
          ('CS', 'Caballeros Villanos', 'Ride a warhorse (Reconquista)', ['Reconquista']), ('CS', 'Caballeros Villanos', 'Exchange thrusting spear for lance (Reconquista)', ['Reconquista']),
          ('CS', 'Jinetes', 'Light armour (Reconquista)', ['Reconquista']), ('CS', 'Peones', 'Light armour (Reconquista)', ['Reconquista']), ('CS', 'Arqueros', 'Light armour (Reconquista)', ['Reconquista']),
          ('CS', 'Basque Javelinmen', 'Light armour (Reconquista)', ['Reconquista'])]
RATIOS += [('CS', 'Ballesteros', ['Caballeros Hidalgos', 'Caballeros de las Ordenes Militares'], 1), ('CS', 'Militia Crossbowmen', ['Peones'], 1)]
UNIT_MAX_IN += [('CS', 'Militia Crossbowmen', 1, ['El Cid'])]
OPT_ONCE += [('CS', [('Infante', GEN_LABEL), ('Mercenary Spearmen', 'Stubborn')])]
GEN['CS'] = (['Rey'], [('Infante', GEN_LABEL)])

# ------------------------------------------------------------------ AL-ANDALUS (book pp.35-42)
AA = []
ACH = lambda extra=(): [('Ride a horse', 8)] + list(extra)
def acharopts(light=3, shield=2, jav=2, thr=2, large=False, warhorse=True, heavy=True, lance=True):
    o = [('Light armour', light), ('Shield', shield), ('Javelins', jav), ('Throwing spear', thr), ('Ride a horse', 8)]
    if large: o.insert(2, ('Large shield (on foot only)', 3))
    if warhorse: o.append(('Ride a warhorse', 16))
    if heavy: o.append((HEAVY_R, 0))
    if lance: o.append(('Lance', 6))
    return o
AA.append(U(PRI_CH, 'Caliph', [M('Caliph', '4 5 4 4 4 3 6 3 9', 160, weapons=['Hand Weapon'], rules=['Army General'], options=acharopts(warhorse=False, heavy=False, lance=False))],
    'Sword. May have light armour (+3 pts), shield (+2 pts), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). Army General. 0-1. The Caliphate of Cordoba only.', mx=1, page='39'))
AA.append(U(PRI_CH, 'Amir', [M('Andalusian Prince', '4 4 4 4 3 2 5 2 8', 65, weapons=['Hand Weapon'], options=acharopts() + [(GEN_LABEL, 25)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). If no other Army General is chosen, one Amir may be made Army General for +25 pts. Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may wear heavy armour and may have a lance (+6 pts).', page='39'))
AA.append(U(PRI_CH, 'Berber Shaykh', [M('Berber Chief', '4 4 4 4 4 2 5 3 8', 75, weapons=['Hand Weapon'], options=acharopts(large=True) + [(GEN_LABEL, 25)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts, only if on foot), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). If no other Army General is chosen, one Berber Shaykh may be made Army General for +25 pts. You may not have both a Berber Shaykh and Christian Captain in the same army. 0-1. Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may wear heavy armour and may have a lance (+6 pts).', mx=1, page='40'))
AA.append(U(PRI_CH, 'Christian Captain', [M('Christian Captain', '4 5 4 4 4 2 5 2 8', 75, weapons=['Hand Weapon', 'Light Armour', 'Shield'],
    options=[('Ride a horse', 8), ('Javelins', 2), ('Throwing spear', 2), ('Thrusting spear', 2), (ARMOUR_H, 1), ('Ride a warhorse', 16), ('Exchange spear for lance (+4)', 4), ('Barding (-1 M)', 2), (GEN_LABEL, 25)])],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear heavy armour (+1 pt). If no other Army General is taken, the army may be led by a Christian Captain (+25 pts; not in the Caliphate of Cordoba). You may not have both a Christian Captain and Berber Shaykh in the same army. 0-1. Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may exchange thrusting or throwing spear for lance (+4 pts) and have horse barding (+2 pts); characters may have a lance (+6 pts).', mx=1, page='40'))
AA.append(U(PRI_CH, 'Alferez', [M('Army Stan. Bearer', '4 4 4 4 3 2 5 2 8', 80, weapons=['Hand Weapon'], rules=['Army Standard'], options=[('Light armour', 3), ('Shield', 2), ('Ride a horse', 8), ('Ride a warhorse', 16), (HEAVY_R, 0)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts). May be mounted on a horse (+8 pts). Army Standard Bearer. 0-1. Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may wear heavy armour (no lance).', mx=1, page='40'))
AA.append(U(PRI_CH, 'Cantador', [M('Cantador', '4 4 4 3 3 2 4 1 8', 50, weapons=['Hand Weapon'], rules=['Cantador (El Cid)'], options=acharopts())],
    'Sword. May have light armour (+3 pts), shield (+2 pts), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). The Cantador may lead a single formed unit (not skirmishers); after deployment, before the first move, roll a D6 for his song. 0-1. Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may wear heavy armour and may have a lance (+6 pts).', mx=1, page='40'))
AA.append(U(PRI_CH, 'Qadi', [M('Islamic Judge', '4 3 3 3 3 2 4 1 8', 40, weapons=['Hand Weapon'], rules=['Qadi'],
    options=[('Light armour', 3), ('Shield', 2), ('Javelins', 1), ('Throwing spear', 2), ('Ride a horse', 8), ('Ride a warhorse', 16), (HEAVY_R, 0), (GEN_LABEL + ' (Qadi-General)', 50)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), javelins (+1 pt), throwing spear (+2 pts). May be mounted on a horse (+8 pts). The Qadi can lead a single formed unit (not skirmishers) which may re-roll failed Rally attempts while the Qadi is alive and leading. 0-1. Later Taifas: if no other Army General is chosen, the Qadi may be made Army General for +50 pts (units he leads may also re-roll failed Panic tests; the Qadi-General loses the Rally re-roll). Taifa Kings and Later Taifas: may ride a warhorse (+16 pts). Later Taifas: may wear heavy armour (no lance).', mx=1, page='40'))
AA.append(U(PRI_CAV, 'Andalusian Jinetes', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 6', 17, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Feigned Flight', 'Andalusian Horsemen'],
    options=[('Throwing spear', 2), ('Shield', 1), ('Exchange javelins for bow', 2), ('Light armour (Later Taifas)', 2)])],
    'Javelins and hand weapon. May have throwing spears (+2 pts). May have shields (+1 pt). Up to half the units of Andalusian Jinetes may exchange javelins for bow (+2 pts), in which case throwing spears may not be taken as well; bow-armed Jinetes are Expert Horsemen. Light Troops (Light Cavalry). Feigned Flight. Andalusian Horsemen. Later Taifas: may have light armour (+2 pts per model).', page='41'))
AA.append(U(PRI_CAV, 'Andalusian Noble Cavalry', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 7', 23, mn=5, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Feigned Flight', 'Andalusian Horsemen'], options=[('Throwing spear', 2)])],
    'Hand weapons, light armour, javelins, shield. May have throwing spears (+2 pts). Light Troops (Light Cavalry). Feigned Flight. Andalusian Horsemen.', page='41'))
AA.append(U(PRI_CAV, 'Andalusian Knights', [M('Andalusian Knights Cavalryman', '8 4 4 3 3 1 4 1 7', 23, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Knights Rank Bonus'],
    options=[('Ride a warhorse', 4), (ARMOUR_H, 1), ('Exchange thrusting spear for throwing spear', 0), ('Exchange thrusting spear for lance', 4)])],
    'Horse, thrusting or throwing spear, light armour, sword, shield. May ride a warhorse (+4 pts). May exchange light armour for heavy armour (+1 pt). May exchange throwing or thrusting spear for lance (+4 pts). May count a Rank Bonus of up to +1 in combat. Later Taifas only.', page='41'))
AA.append(U(PRI_INF, 'Andalusian Spearmen', [M('And. Spearmen', '4 2 3 3 3 1 2 1 6', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Combined Formation (El Cid)'], options=[('Light armour', 2), ('Javelins', 1)])],
    'Hand weapon, thrusting spear, shield. May have light armour (+2 pts), javelins (+1 pt). Combined Formation: may be combined with an Andalusian Archers unit (the archers lose Light Troops).', page='41'))
AA.append(U(PRI_CAV, 'Andalusian Mounted Crossbowmen', [M('Mtd Crossbowmen Cavalryman', '8 3 3 3 3 1 3 1 6', 19, mn=5, weapons=['Hand Weapon', 'Light Crossbow'], rules=['Feigned Flight', 'Andalusian Horsemen', 'Mounted Crossbow (El Cid)'], options=[('Shield', 1), ('Light armour', 2)])],
    'Hand weapons, horse and latch (light crossbow). May have shields (+1 pt) and/or light armour (+2 pts). Light Cavalry. Feigned Flight. Andalusian Horsemen. The light crossbow has a range of 24", Strength 3 and a -1 save modifier; units that move in the Movement phase cannot fire that turn. 0-1 unit. Later Taifas only.', mx=1, page='42'))
AA.append(U(PRI_INF, 'Andalusian Archers', [M('Archers', '4 2 3 3 3 1 2 1 6', 5, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Combined Formation (El Cid)'], options=[('Shield', 1), ('Light armour', 1)])],
    'Bow, hand weapon. May have shields or light armour (+1 pt). Light Troops (Light Infantry). Combined Formation: may be combined with an Andalusian Spearmen unit (they lose the Light Troops ability).', page='42'))
AA.append(U(PRI_SK, 'Andalusian Skirmishers', [M('Skirmishers', '4 2 3 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], options=[('Throwing spear', 2), ('Buckler', 1), ('Exchange javelins for sling', 0)])],
    'Hand weapons, javelins. May have throwing spears (+2 pts). May have buckler (+1 pt). May exchange javelins for shortbow or sling at no extra cost. Skirmishers.', page='42'))
AA.append(U(PRI_INF, 'Andalusian Crossbowmen', [M('And. Crossbowmen', '4 2 2 3 3 1 2 1 6', 8, mn=5, weapons=['Crossbow', 'Hand Weapon'], options=[('Shield', 1), ('Light armour', 2)])],
    'Crossbow, sword. May have shield (+1 pt) and/or light armour (+2 pts). Light Infantry. Taifa Kings: only a single unit (0-1). Not available in the Caliphate of Cordoba.', page='42'))
for n in ('Mercenary Spearmen', 'Mercenary Archers', 'Mercenary Jinetes', 'Mercenary Caballeros', 'Mercenary Crossbowmen', 'Mercenary Knights'): AA.append(MERC(n))
AA_LIM = {
 'Caliphate': ('Al-Andalus', 25, {'min': 50}, 33, 'The Caliphate of Cordoba, c.912-1008 AD (p.37). Characters up to 25% (Caliph, Amir, Berber Shaykh, Christian Captain, Alferez, Cantador, Qadi; the Army General may be a Caliph, Amir or Berber Shaykh, but not a Christian Captain). Common Troops at least 50%: Andalusian Jinetes, Noble Cavalry, Spearmen, Archers, Skirmishers, Mercenary Spearmen and Archers. Uncommon Troops up to 33%: Mercenary Jinetes and Mercenary Caballeros. At least half the number of cavalry models selected must be Andalusian Jinetes.'),
 'Taifa Kings': ('Al-Andalus', 25, {'min': 33}, 50, 'The Taifa Kings, c.1008-1110 AD (p.38). Characters up to 25% (Amir, Berber Shaykh, Christian Captain, Alferez, Cantador, Qadi; the Army General may be an Amir, Berber Shaykh or Christian Captain). Characters may ride warhorses (+16 pts). Common Troops at least 33%: Andalusian Jinetes, Noble Cavalry, Spearmen, Archers, Skirmishers. Uncommon Troops up to 50%: Andalusian Crossbowmen (0-1 unit only), Mercenary Spearmen, Archers, Jinetes, Crossbowmen and Knights. At least half the number of cavalry models selected must be Andalusian Jinetes.'),
 'Later Taifas': ('Al-Andalus', 25, {'min': 33}, 50, 'Survivors and Renegades - the Later Taifas and Nasrid Granada, c.1110-1250 AD (pp.38-39). Characters up to 25% (Amir, Berber Shaykh, Christian Captain, Alferez, Cantador, Qadi; the Army General may be an Amir, Berber Shaykh, Christian Captain or a Qadi). Characters may ride warhorses (+16 pts) and wear heavy armour (+3 pts); any character except the Alferez or Qadi may have a lance (+6 pts). Andalusian Jinetes and Mercenary Jinetes may take light armour (+2 pts per model). Christian Captains and Mercenary Knights may exchange spears for lances (+4 pts per model) and have horse barding (+2 pts). If no other Army General is chosen the Qadi may be made Army General (+50 pts). Common Troops at least 33%: Andalusian Jinetes, Noble Cavalry, Knights, Spearmen, Archers, Skirmishers, Crossbowmen, Mounted Crossbowmen. Uncommon Troops up to 50%: Mercenary Spearmen, Archers, Jinetes, Crossbowmen and Knights. At least half the number of cavalry models selected must be Andalusian Jinetes.'),
}
AA_V = variants('AA', ['Caliphate', 'Taifa Kings', 'Later Taifas'], AA_LIM)
AA_NOTES = ('AL-ANDALUS ARMY LIST (El Cid, pp.35-42): the Caliphate of Cordoba (c.912-1008), the Taifa Kings (c.1008-1110) and the Later Taifas and Nasrid Granada (c.1110-1250). Percentages are by points. Special rules p.37 (Andalusian Horsemen).\n'
  'Not enforced: "at least half the number of cavalry models selected must be Andalusian Jinetes" (a cross-unit figure percentage), and up to half the units of Andalusian Jinetes may have bows. The printed Later Taifas rule gives heavy armour for characters at +3 pts, the same as light armour; heavy armour is therefore entered at no extra charge over light armour.')
LISTS.append(('AA', 'Al-Andalus (El Cid)', 'Al_Andalus_El_Cid.cat', AA, AA_V, AA_NOTES))
ALL_AA = ['Caliphate', 'Taifa Kings', 'Later Taifas']
UNAV += [('AA', 'Caliph', ['Taifa Kings', 'Later Taifas']), ('AA', 'Andalusian Knights', ['Caliphate', 'Taifa Kings']), ('AA', 'Andalusian Mounted Crossbowmen', ['Caliphate', 'Taifa Kings']),
         ('AA', 'Andalusian Crossbowmen', ['Caliphate']), ('AA', 'Mercenary Caballeros', ['Taifa Kings', 'Later Taifas']), ('AA', 'Mercenary Crossbowmen', ['Caliphate']), ('AA', 'Mercenary Knights', ['Caliphate'])]
pools('AA', ALL_AA, {
 'Andalusian Jinetes': {c: 'C' for c in ALL_AA}, 'Andalusian Noble Cavalry': {c: 'C' for c in ALL_AA}, 'Andalusian Knights': {'Later Taifas': 'C'}, 'Andalusian Spearmen': {c: 'C' for c in ALL_AA},
 'Andalusian Archers': {c: 'C' for c in ALL_AA}, 'Andalusian Skirmishers': {c: 'C' for c in ALL_AA}, 'Andalusian Crossbowmen': {'Taifa Kings': 'U', 'Later Taifas': 'C'},
 'Andalusian Mounted Crossbowmen': {'Later Taifas': 'C'},
 'Mercenary Spearmen': {'Caliphate': 'C', 'Taifa Kings': 'U', 'Later Taifas': 'U'}, 'Mercenary Archers': {'Caliphate': 'C', 'Taifa Kings': 'U', 'Later Taifas': 'U'},
 'Mercenary Jinetes': {c: 'U' for c in ALL_AA}, 'Mercenary Caballeros': {'Caliphate': 'U'}, 'Mercenary Crossbowmen': {'Taifa Kings': 'U', 'Later Taifas': 'U'}, 'Mercenary Knights': {'Taifa Kings': 'U', 'Later Taifas': 'U'}})
for u in ('Amir', 'Berber Shaykh', 'Christian Captain', 'Cantador'):
    OPTAV += [('AA', u, 'Ride a warhorse', ['Taifa Kings', 'Later Taifas'])]
for u in ('Amir', 'Berber Shaykh', 'Cantador'): OPTAV += [('AA', u, 'Lance', ['Later Taifas'])]
for u in ('Amir', 'Berber Shaykh', 'Cantador'): OPTAV += [('AA', u, HEAVY_R, ['Later Taifas'])]
OPTAV += [('AA', 'Alferez', 'Ride a warhorse', ['Taifa Kings', 'Later Taifas']), ('AA', 'Alferez', HEAVY_R, ['Later Taifas']),
          ('AA', 'Qadi', 'Ride a warhorse', ['Taifa Kings', 'Later Taifas']), ('AA', 'Qadi', HEAVY_R, ['Later Taifas']), ('AA', 'Qadi', GEN_LABEL + ' (Qadi-General)', ['Later Taifas']),
          ('AA', 'Christian Captain', GEN_LABEL, ['Taifa Kings', 'Later Taifas']),
          ('AA', 'Christian Captain', 'Exchange spear for lance (+4)', ['Later Taifas']), ('AA', 'Christian Captain', 'Barding (-1 M)', ['Later Taifas']),
          ('AA', 'Andalusian Jinetes', 'Light armour (Later Taifas)', ['Later Taifas']), ('AA', 'Mercenary Jinetes', 'Light armour (Jinetes)', ['Later Taifas']),
          ('AA', 'Mercenary Knights', 'Exchange thrusting spear for lance', ['Later Taifas']), ('AA', 'Mercenary Knights', 'Barding (-1 M)', ['Later Taifas'])]
OPTRULE += [('AA', u, GEN_LABEL, 'Army General (Chariot Wars)') for u in ('Amir', 'Berber Shaykh', 'Christian Captain')] + [('AA', 'Qadi', GEN_LABEL + ' (Qadi-General)', 'Army General (Chariot Wars)')]
OPTRULE += [('AA', 'Andalusian Jinetes', 'Exchange javelins for bow', 'Expert Horsemen'), ('AA', 'Mercenary Jinetes', 'Exchange javelins for bow', 'Expert Horsemen')]
RATIOS += [('AA', 'Mercenary Crossbowmen', ['Mercenary Knights'], 1)]
UNIT_MAX_IN += [('AA', 'Andalusian Crossbowmen', 1, ['Taifa Kings'])]
PAIRS += [('AA', ['Berber Shaykh', 'Christian Captain'], 'shaykh-or-captain')]
OPT_ONCE += [('AA', [('Amir', GEN_LABEL), ('Berber Shaykh', GEN_LABEL), ('Christian Captain', GEN_LABEL), ('Qadi', GEN_LABEL + ' (Qadi-General)'), ('Mercenary Spearmen', 'Stubborn')])]
GEN['AA'] = (['Caliph'], [('Amir', GEN_LABEL), ('Berber Shaykh', GEN_LABEL), ('Christian Captain', GEN_LABEL), ('Qadi', GEN_LABEL + ' (Qadi-General)')])

# ------------------------------------------------------------------ THE AFRICAN INVADERS (book pp.43-51)
AF = []
AFO = lambda: [('Light armour', 3), ('Shield', 2), ('Large shield (on foot only)', 3), ('Javelins', 2), ('Throwing spear', 2), ('Ride a horse', 8), ('Drilled', 2), ('Stubborn', 3)]
AF.append(U(PRI_CH, 'Emir', [M('Emir', '4 5 4 4 4 3 6 3 9', 160, weapons=['Hand Weapon'], rules=['Army General'], options=AFO() + [('Venerable Emir', 0)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts, only if on foot), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). May be Drilled (+2 pts). May be Stubborn (+3 pts). Army General. 0-1 Emir. The Emir may be a Venerable Emir (free; WS4 BS3 S3 T3 I5 A2 Ld10): an old and wizened but charismatic leader.', mx=1, page='50'))
AF.append(U(PRI_CH, 'Sayyid', [M('Lord', '4 4 4 4 4 2 5 3 8', 75, weapons=['Hand Weapon'], options=AFO() + [(GEN_LABEL, 25)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts, only if on foot), javelins (+2 pts), throwing spear (+2 pts). May be mounted on a horse (+8 pts). May be Drilled (+2 pts). May be Stubborn (+3 pts). If no other Army General is chosen, one Sayyid may be made Army General (+25 pts).', page='50'))
AF.append(U(PRI_CH, 'Christian Captain', [M('Christian Captain', '4 5 4 4 4 2 4 2 8', 75, weapons=['Hand Weapon', 'Light Armour', 'Shield'],
    options=[('Ride a horse', 8), ('Ride a warhorse', 16), ('Javelins', 2), ('Throwing spear', 2), ('Thrusting spear', 2), (ARMOUR_H, 1), ('Exchange spear for lance (+4)', 4), ('Barding (-1 M)', 2), (GEN_LABEL, 25)])],
    'Sword, light armour, shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have javelins (+2 pts), throwing spear or thrusting spear (+2 pts). May wear heavy armour (+1 pt). If no other Army General is chosen, a Christian Captain may be made Army General (+25 pts); if he does, the army may not include an Imam. 0-1. Almohads: may exchange thrusting or throwing spear for lance (+4 pts) and have horse barding (+2 pts).', mx=1, page='50'))
AF.append(U(PRI_CH, 'Army Standard Bearer', [M('Army Standard', '4 4 4 4 4 2 5 2 8', 80, weapons=['Hand Weapon'], rules=['Army Standard'],
    options=[('Light armour', 3), ('Shield', 2), ('Large shield (on foot only)', 3), ('Ride a horse', 8), ('Drilled', 2), ('Stubborn', 3)])],
    'Sword. May have light armour (+3 pts), shield (+2 pts), large shield (+3 pts, only if on foot). May be mounted on a horse (+8 pts). May be Drilled (+2 pts). May be Stubborn (+3 pts). Army Standard Bearer. 0-1.', mx=1, page='50'))
AF.append(U(PRI_CH, 'Imam', [M('Religious Leader', '4 4 3 3 4 2 4 2 8', 70, weapons=['Hand Weapon'], rules=['Imam'], options=[('Light armour', 3), ('Drilled', 2), ('Stubborn', 3)])],
    'Sword. May have light armour (+3 pts). May be Drilled (+2 pts). May be Stubborn (+3 pts). The Imam may lead a unit of either Black Guard or Berber Spearmen (with or without Berber Archers); he cannot lead any other unit. The Imam is subject to Hatred of the enemy, as is any unit he leads. 0-1. The army may not include an Imam if a Christian Captain is the Army General.', mx=1, page='50'))
DRUM = ('Second Musician (African Drummers)', 5)
AF.append(U(PRI_INF, 'Black Guard', [M('Black Guard', '4 4 4 3 3 1 4 1 8', 17, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Large Shield', 'Javelin'], rules=['Stubborn'], options=[('Light armour', 2), ('Drilled', 1), DRUM])],
    'Sword, thrusting spear, large shield, javelins. May have light armour (+2 pts). May be Drilled (+1 pt). Stubborn. 0-1 unit. May take a second Musician (African Drummers).', mx=1, page='51'))
AF.append(U(PRI_INF, 'Berber Spearmen', [M('Berber Spearmen', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Thrusting Spear', 'Shield', 'Javelin'], rules=['Combined Formation (El Cid)'], options=[('Large shield (replaces shield)', 1), ('Stubborn', 3), DRUM])],
    'Thrusting spear, shield, javelins. May have large shield (+1 pt per model). Combined Formation: may have up to 50% Berber Archers in the rear ranks of the unit. Any Berber Spearmen unit may be made Stubborn (+3 pts per model; Almohads: up to half the units). May take a second Musician (African Drummers).', page='51'))
AF.append(U(PRI_INF, 'Berber Archers', [M('Berber Archers', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Combined Formation (El Cid)'], options=[('Stubborn (only in a Combined Unit with Stubborn Berber Spearmen)', 3), DRUM])],
    'Composite bow, sword. Light Infantry. May form a Combined Formation with Berber Spearmen. Berber Archers must also be made Stubborn (+3 pts per model) if they are in a Combined Unit with Stubborn Berber Spearmen (they cannot be Stubborn on their own). May take a second Musician (African Drummers).', page='51'))
AF.append(U(PRI_SK, 'Tribal Skirmishers', [M('Skirmisher', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], options=[('Throwing spear', 2), ('Exchange javelins for shortbow', 0), ('Shield', 1)])],
    'Hand weapons, javelins. May have throwing spears (+2 pts), or may exchange javelins for shortbow for no extra cost. May have shield (+1 pt). Skirmishers.', page='51'))
AF.append(U(PRI_CAV, 'Berber Cavalry', [M('Berber Cavalry Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Feigned Flight'], options=[('Throwing spear', 2), ('Shield', 1), DRUM])],
    'Javelins and hand weapon. May have throwing spears (+2 pts); may have shield (+1 pt). Feigned Flight. Light Cavalry. May take a second Musician (African Drummers).', page='51'))
AF.append(U(PRI_CAV, 'Camel Riders', [M('Camelry Cavalryman', '6 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Javelin', 'Hand Weapon'], rules=['Camel Riders (El Cid)'], options=[('Throwing spear', 2), ('Shield', 1), DRUM])],
    'Javelins and hand weapon. May have throwing spear (+2 pts). May have shield (+1 pt). Light Troops (Light Cavalry). Camels cause fear in all cavalry (and chariots). 0-1 unit. May take a second Musician (African Drummers).', mx=1, page='51'))
AF.append(U(PRI_CAV, 'Hasham Guard Cavalry', [M('Guard Cavalry Cavalryman', '8 4 4 3 3 1 4 1 8', 20, mn=5, weapons=['Javelin', 'Hand Weapon', 'Shield'], options=[('Light armour', 2), ('Throwing spear', 2), ('Drilled', 2), DRUM])],
    'Javelins, sword, shield. May have light armour (+2 pts); may have throwing spears (+2 pts). May be Drilled (+2 pts). 0-1 unit. May take a second Musician (African Drummers).', mx=1, page='51'))
for n in ('Mercenary Caballeros', 'Mercenary Crossbowmen', 'Mercenary Jinetes', 'Mercenary Spearmen', 'Mercenary Archers', 'Mercenary Knights', 'Ghuzz Horse Archers'): AF.append(MERC(n))
AF_LIM = {
 'Almoravids': ('African Invaders', 25, {'min': 33}, 33, 'The Almoravids, c.1042-1149 AD (p.48). Characters up to 25% (Emir, which may be a Venerable Emir, Sayyid, Christian Captain, Army Standard Bearer, Imam; the Army General may be an Emir, Venerable Emir, Sayyid or Christian Captain). Common Troops at least 33%: Black Guard, Berber Spearmen, Berber Archers, Berber Cavalry, Tribal Skirmishers. Uncommon Troops up to 33%: Hasham Guard Cavalry, Camel Riders, Mercenary Caballeros, Crossbowmen and Knights, Ghuzz Horse Archers. Any Berber Spearmen unit may be made Stubborn (+3 pts per model). Andalusian Allies (up to 33%: Andalusian Jinetes, Noble Cavalry, Spearmen, Archers, Skirmishers) are not built.'),
 'Almohads': ('African Invaders', 25, {'max': 50}, 50, 'The Almohads, c.1128-1269 AD (p.49). Characters up to 25% (same as the Almoravids). Common Troops: Black Guard, Berber Spearmen, Berber Archers, Berber Cavalry, Tribal Skirmishers (printed "up to 50%", confirmed). Uncommon Troops up to 50%: Hasham Guard Cavalry, Camel Riders, Mercenary Caballeros, Crossbowmen, Jinetes, Spearmen, Archers and Knights, Ghuzz Horse Archers. Up to half the units of Berber Spearmen may be Stubborn (+3 pts per model); Christian Captains and Mercenary Knights may exchange spears for lances (+4 pts) and have horse barding (+2 pts). Andalusian Allies (up to 33%: Andalusian Jinetes, Noble Cavalry, Knights, Spearmen, Archers, Skirmishers, Crossbowmen, Mounted Crossbowmen) are not built.'),
}
AF_V = variants('AF', ['Almoravids', 'Almohads'], AF_LIM)
AF_NOTES = ('THE AFRICAN INVADERS ARMY LIST (El Cid, pp.43-51): the Almoravids (c.1042-1149) and the Almohads (c.1128-1269). Percentages are by points. Special rules p.46 (African Drummers: certain units may feature two Musician models for +5 pts per model; any unit so equipped automatically wins a drawn combat by one point; a Berber Archer or combined Berber Archers/Spearmen unit with two drummers may use Massed Archery even if it has moved up to its normal movement, with the -1 to hit still applying).\n'
  'Not enforced: "up to half the units of Berber Spearmen may be Stubborn" (Almohads).')
LISTS.append(('AF', 'African Invaders (El Cid)', 'African_Invaders_El_Cid.cat', AF, AF_V, AF_NOTES))
ALL_AF = ['Almoravids', 'Almohads']
UNAV += [('AF', 'Mercenary Jinetes', ['Almoravids']), ('AF', 'Mercenary Spearmen', ['Almoravids']), ('AF', 'Mercenary Archers', ['Almoravids'])]
pools('AF', ALL_AF, {
 'Black Guard': {c: 'C' for c in ALL_AF}, 'Berber Spearmen': {c: 'C' for c in ALL_AF}, 'Berber Archers': {c: 'C' for c in ALL_AF}, 'Berber Cavalry': {c: 'C' for c in ALL_AF}, 'Tribal Skirmishers': {c: 'C' for c in ALL_AF},
 'Hasham Guard Cavalry': {c: 'U' for c in ALL_AF}, 'Camel Riders': {c: 'U' for c in ALL_AF}, 'Mercenary Caballeros': {c: 'U' for c in ALL_AF}, 'Mercenary Crossbowmen': {c: 'U' for c in ALL_AF},
 'Mercenary Knights': {c: 'U' for c in ALL_AF}, 'Ghuzz Horse Archers': {c: 'U' for c in ALL_AF},
 'Mercenary Jinetes': {'Almohads': 'U'}, 'Mercenary Spearmen': {'Almohads': 'U'}, 'Mercenary Archers': {'Almohads': 'U'}})
OPTAV += [('AF', 'Christian Captain', 'Exchange spear for lance (+4)', ['Almohads']), ('AF', 'Christian Captain', 'Barding (-1 M)', ['Almohads']),
          ('AF', 'Mercenary Knights', 'Exchange thrusting spear for lance', ['Almohads']), ('AF', 'Mercenary Knights', 'Barding (-1 M)', ['Almohads'])]
OPTRULE += [('AF', 'Sayyid', GEN_LABEL, 'Army General (Chariot Wars)'), ('AF', 'Christian Captain', GEN_LABEL, 'Army General (Chariot Wars)'), ('AF', 'Mercenary Jinetes', 'Exchange javelins for bow', 'Expert Horsemen')]
for u in ('Black Guard', 'Berber Spearmen', 'Berber Archers', 'Berber Cavalry', 'Camel Riders', 'Hasham Guard Cavalry'): OPTRULE += [('AF', u, DRUM[0], 'African Drummers')]
OPTRULE += [('AF', u, 'Drilled', 'Drilled') for u in ('Emir', 'Sayyid', 'Army Standard Bearer', 'Imam', 'Black Guard', 'Hasham Guard Cavalry')]
OPTRULE += [('AF', u, 'Stubborn', 'Stubborn') for u in ('Emir', 'Sayyid', 'Army Standard Bearer', 'Imam', 'Berber Spearmen')] + [('AF', 'Berber Archers', 'Stubborn (only in a Combined Unit with Stubborn Berber Spearmen)', 'Stubborn')]
RATIOS += [('AF', 'Mercenary Crossbowmen', ['Mercenary Knights'], 1)]
OPT_ONCE += [('AF', [('Sayyid', GEN_LABEL), ('Christian Captain', GEN_LABEL), ('Mercenary Spearmen', 'Stubborn')])]
GEN['AF'] = (['Emir'], [('Sayyid', GEN_LABEL), ('Christian Captain', GEN_LABEL)])

# options that do not apply in a catalogue
def _drop(units, name, label):
    for u in units:
        if u['name'] == name:
            for m in u['models']: m['options'] = [o for o in m['options'] if o[0] != label]
_drop(CS, 'Mercenary Jinetes', 'Light armour (Jinetes)'); _drop(AF, 'Mercenary Jinetes', 'Light armour (Jinetes)')
for _u in AA + AF:
    if _u['name'] == 'Mercenary Knights': pass
_drop(AA, 'Basque Javelinmen', 'Light armour (Reconquista)')

OPTSTAT += [('AF', 'Emir', 'Venerable Emir', st, v) for st, v in (('WS', 4), ('BS', 3), ('S', 3), ('T', 3), ('I', 5), ('A', 2), ('Ld', 10))]
