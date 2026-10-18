# Shieldwall (Warhammer Historical, 2002, Stephen Patten) army lists: Northmen, English, Caledonians, Welsh, Hibernians, Western Franks.
# Book page numbers are printed page numbers. Percentages are by points. Model stats order: M WS BS S T W I A Ld
import copy
from rb_data import M, U
LISTS = []      # (key, display name, catalogue file, units, variants [(variant name, limits, text)], notes)
VAR = {}        # key -> {short variant name: full variant name}
AVAIL = []      # (key, unit, [short variant names])      unit only available in those compositions
UNAV = []       # (key, unit, [short variant names])      unit NOT available in those compositions
OPTAV = []      # (key, unit, option label, [short variant names])   option only available in those compositions
OPTRULE = []    # (key, unit, option label, rule name)    the option carries a rule link (rule appears when chosen)
COSTV = []      # (key, unit, {short variant: points per model})
STATV = []      # (key, unit, stat, {short variant: value})
OPTSTAT = []    # (key, unit, option label, stat, value)  stat changes when the option is chosen
RATIOS = []     # (key, unit, [limiting units], per)
HIRDMEN_LE_BONDIR = []   # (key, unit, limiting unit, [short variants])
SECOND = {}     # (key, unit) -> [secondary category names]
OPT_ONCE = []   # (key, [(unit, option label)])   option may be taken once in the whole army
PAIRS = []      # (key, [units], tag)   0-1 across several units
COND_CHARS = [] # (key, unit)  characters limit drops to 25% if the army includes this unit
REQ = []        # (key, unit, required unit)

# ------------------------------------------------------------------ Dogs of War (book pp.77-79)
def DOW(name):
    d = {}
    d['Gall-Gaedhil'] = U('Uncommon Warriors', 'Gall-Gaedhil (Dogs of War)', [M('Son of Death', '5 3 3 3 3 1 3 1 6', 10, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband', 'Frenzy', 'Different Weapons'],
        options=[('Exchange buckler for shield', 1), ('Exchange javelins for double-handed weapon (axe)', 2)])],
        'Hand weapons, javelins and buckler. May have shield (+1 pt). May exchange javelins for double-handed axes (+2 pts). Light Infantry. Warband. Frenzied. Different Weapons. 0-1 unit. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules; they may have a leader, standard and musician as normal.', mx=1, page='77')
    d['Amsaigh'] = U('Uncommon Warriors', 'Amsaigh (Dogs of War)', [M('Irish Outlaw', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband', 'Different Weapons'],
        options=[('Exchange javelins for double-handed weapon (axe)', 2)])],
        'Hand weapons, javelins and buckler. May exchange javelins for double-handed axes (+2 pts). Light Infantry. Warband. Different Weapons. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='77')
    d['Bradwr'] = U('Uncommon Warriors', 'Bradwr (Dogs of War)', [M('Welsh Renegade', '5 4 4 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband'],
        options=[('Light armour', 2), ('Throwing spear', 2), ('Thrusting spear', 2), ('Exchange javelins and shield for bow', 0), ('Ride a horse', 8)])],
        'Hand weapons, javelins and shield. May have light armour (+2 pts) and throwing spear (+2 pts) or thrusting spears (+2 pts). May exchange javelins and shield for bow (free). May be mounted on a horse (+8 pts). Light Infantry. Warband. If the unit is broken it never rallies. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='77')
    d['Gasraidh'] = U('Uncommon Warriors', 'Gasraidh (Dogs of War)', [M('Scots Exile', '5 4 3 3 3 1 4 1 6', 12, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Buckler'], rules=['Warband', 'Hatred'],
        options=[('Exchange buckler for shield', 1), ('Javelins', 2), ('Throwing spear', 2), ('Thrusting spear', 2), ('Ride a horse', 8)])],
        'Hand weapons, light armour and buckler. May exchange buckler for shield (+1 pt), have javelins (+2 pts), throwing spears (+2 pts) or thrusting spears (+2 pts). May be mounted (+8 pts). Warband. Hatred. If the unit is within charge range of a character or unit containing a character then it must charge (the exiles hold him responsible for their predicament). 0-1 unit. (The printed profile row has one value fewer than the table header; Toughness 3 assumed.) Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', mx=1, page='77')
    d['Gestir'] = U('Uncommon Warriors', 'Gestir (Dogs of War)', [M('Guest warrior', '4 4 3 4 4 1 4 1 8', 14, mn=5, weapons=['Hand Weapon'], rules=['Fury of the Norsemen', 'Warband Psychology (rule 2)', 'Different Weapons'],
        options=[('Shield', 2), ('Additional hand weapon', 3), ('Throwing spear', 2), ('Double-handed weapon (axe)', 3), ('Javelins', 1)])],
        'Hand weapons. May have shield (+2 pts) or additional hand weapon (+3 pts). May have throwing spear (+2 pts), double-handed axe (+3 pts) and javelins (+1 pt). Light Infantry. Fury of the Norsemen. Subject to Warband psychology rule 2. Different Weapons. 0-1 unit. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', mx=1, page='78')
    d['Vikings'] = U('Uncommon Warriors', 'Vikings (Dogs of War)', [M('Pirate', '4 4 3 3 4 1 4 1 8', 10, mn=5, weapons=['Hand Weapon'], rules=['Fury of the Norsemen', 'Warband Psychology (rule 2)', 'Different Weapons'],
        options=[('Light armour', 3), ('Shield', 2), ('Additional hand weapon', 3), ('Throwing spear', 2), ('Double-handed weapon (axe)', 2), ('Javelins', 1)])],
        'Hand weapons. May have light armour (+3 pts). May have shield (+2 pts) or additional hand weapon (+3 pts). May have throwing spear (+2 pts), double-handed axe (+2 pts) and javelins (+1 pt). Light Infantry. Fury of the Norsemen. Different Weapons. Subject to Warband psychology rule 2. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='78')
    d['Jomsvikings'] = U('Uncommon Warriors', 'Jomsvikings or Viking Adventurers (Dogs of War)', [M('Jomsviking/Adventurer', '4 4 4 3 4 1 4 1 9', 16, mn=5, weapons=['Hand Weapon', 'Light Armour'], rules=['Stubborn', 'Fury of the Norsemen', 'Different Weapons', 'Jomsviking Bribe'],
        options=[('Shield', 2), ('Additional hand weapon', 2), ('Throwing spear', 2), ('Double-handed weapon (axe)', 2), ('Javelins', 2), ('Exchange light armour for heavy armour', 1)])],
        'Hand weapons and light armour. May have shield (+2 pts) or additional hand weapon (+2 pts), throwing spear (+2 pts), double-handed axe (+2 pts) and javelins (+2 pts). May exchange light armour for heavy armour (+1 pt). Light Infantry. Stubborn. Fury of the Norsemen. Different Weapons. Each turn roll a dice: on a 1 the Jomsvikings or Adventurers have accepted a bribe from the enemy and may not move that turn. 0-1 unit. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', mx=1, page='78')
    d['Stipendarii (dismounted)'] = U('Uncommon Warriors', 'Stipendarii (dismounted) (Dogs of War)', [M('Dismounted Stipendarius', '4 4 3 3 3 1 4 1 8', 13, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Throwing Spear'], rules=['Unreliable Mercenaries'],
        options=[('Exchange throwing spear for thrusting spear', 0), ('Exchange light armour for heavy armour', 1), ('Javelins', 1)])],
        'Hand weapon, light armour, shield and either throwing spear or thrusting spear. May upgrade armour to heavy armour (+1 pt), have javelins (+1 pt). Roll a dice the first time each unit wishes to move, charge or shoot: on a 1 it stays stationary and may not shoot (it may defend itself); on a 2-6 it may act as the player wishes. (The printed dismounted profile row has one value fewer than the header; Toughness 3 assumed.) Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='78')
    d['Stipendarii (mounted)'] = U('Uncommon Warriors', 'Stipendarii (mounted) (Dogs of War)', [M('Mounted Stipendarius Cavalryman', '8 4 3 3 3 1 4 1 8', 27, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Throwing Spear'], rules=['Unreliable Mercenaries'],
        options=[('Exchange throwing spear for thrusting spear', 0), ('Exchange light armour for heavy armour', 1), ('Javelins', 1)])],
        'Mounted milites (warhorses). Hand weapon, light armour, shield and either throwing spear or thrusting spear. May upgrade armour to heavy armour (+1 pt), have javelins (+1 pt). May receive up to a +1 rank bonus when mounted. Roll a dice the first time each unit wishes to move, charge or shoot: on a 1 it stays stationary and may not shoot (it may defend itself); on a 2-6 it may act as the player wishes. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='78')
    d['Serjeants'] = U('Uncommon Warriors', 'Serjeants (Dogs of War)', [M('Merc footman', '4 3 3 3 3 1 4 1 7', 5, mn=5, weapons=['Hand Weapon'], rules=['Unreliable Mercenaries'],
        options=[('Shield', 1), ('Light armour', 2), ('Javelins', 1), ('Throwing spear', 1), ('Double-handed weapon (axe or sword)', 2), ('Bow', 2), ('Crossbow', 5), ('Designate as light infantry (free)', 0)])],
        'Hand weapons. May have shield (+1 pt), light armour (+2 pts), javelin (+1 pt), throwing spear (+1 pt), double-handed axes/swords (+2 pts), bows (+2 pts) or crossbow (+5 pts). Any unit of Serjeants may be designated as light infantry at no additional cost. Roll a dice the first time each unit wishes to move, charge or shoot: on a 1 it stays stationary and may not shoot (it may defend itself); on a 2-6 it may act as the player wishes. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='78-79')
    d['Cottereaux'] = U('Uncommon Warriors', 'Cottereaux (Dogs of War)', [M('Merc skirmisher', '4 3 4 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Buckler', 'Javelin'], rules=['Mercenary Rally'])],
        'Hand weapons, buckler and javelins. Skirmishers. Any unit that chooses to flee or fire & flee as a charge reaction rallies automatically at the end of its move and may reform facing in any direction; a charging enemy that encounters them does not destroy them and they may instead fight in the close combat phase (their opponents still count as charging). Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='79')
    d['Devroet'] = U('Uncommon Warriors', 'Devroet (Dogs of War)', [M('Breton Exile Cavalryman', '8 4 4 3 3 1 4 1 7', 28, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Throwing Spear'], rules=['Mercenary Rally'],
        options=[('Exchange light armour for heavy armour', 1), ('Javelins', 2)])],
        'Hand weapon, light armour, shield and throwing spear, mounted on a warhorse. May upgrade armour to heavy armour (+1 pt), javelins (+2 pts). May receive up to a +1 rank bonus when mounted. Any unit that chooses to flee or fire & flee as a charge reaction rallies automatically at the end of its move and may reform facing in any direction; a charging enemy that encounters them does not destroy them. Despite their warhorses and armour the Devroet count as Light Cavalry. (The printed profile gives M4; M8 entered because the unit is mounted on warhorses.) Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='79')
    d['Freebooters'] = U('Uncommon Warriors', 'Freebooters (Dogs of War)', [M('English Freebooter', '4 4 4 4 3 1 4 1 6', 19, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], rules=['Shieldwall', 'Warband', 'Stubborn'], options=[('Javelins', 1)])],
        'Hand weapons, throwing spears, light armour and shield. May have javelins (+1 pt). Shieldwall. Warband. Stubborn. Dogs of War cannot be accompanied by characters and cannot benefit from the Army General and Standard Bearer rules.', page='79')
    return copy.deepcopy(d[name])

def pct(c, o, u): return {'Characters': {'max': c}, 'Common Warriors': o, 'Uncommon Warriors': {'max': u}}

# ------------------------------------------------------------------ NORTHMEN (book pp.6-16)
NO = []
NCH = lambda: [('Throwing spear', 2), ('Javelins', 2), ('Exchange shield for additional hand weapons', 3), ('Exchange shield for double-handed weapon (axe)', 3), ('Ride a horse', 8)]
NO.append(U('Characters', 'Konnungr', [M('Konnungr', '4 6 4 5 4 3 6 3 10', 200, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General'], options=NCH())],
    'Hand weapon, light armour and shield. May have throwing spear (+2 pts), javelins (+2 pts). May exchange shield for additional hand weapons (+3 pts) or double-handed axe (+3 pts). May be mounted on a horse (+8 pts). Army General. 0-1 Army General (Konnungr or Jarl).', mx=1, page='12'))
NO.append(U('Characters', 'Jarl', [M('Jarl', '4 5 4 4 4 3 6 3 9', 160, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Army General'], options=NCH())],
    'Hand weapon, light armour and shield. May have throwing spear (+2 pts), javelins (+2 pts). May exchange shield for additional hand weapons (+3 pts) or double-handed axe (+3 pts). May be mounted on a horse (+8 pts). Army General. 0-1 Army General (Konnungr or Jarl).', mx=1, page='12'))
NO.append(U('Characters', 'Hersir', [M('Hersir', '4 5 4 4 4 2 5 2 9', 85, weapons=['Hand Weapon', 'Light Armour', 'Shield'], options=NCH() + [('Army Standard Bearer', 15)])],
    'Hand weapon, light armour and shield. May have throwing spear (+2 pts), javelins (+2 pts). May exchange shield for additional hand weapons (+3 pts) or double-handed axe (+3 pts). May be mounted on a horse (+8 pts). One Hersir may be made Army Standard Bearer (+15 pts).', page='12'))
NO.append(U('Characters', 'Berserkers', [M('Berserker', '4 4 3 4 4 1 4 1 8', 18, mn=1, mx=3, weapons=['Hand Weapon', 'Shield'], rules=['Berserkers (Shieldwall)'],
    options=[('Throwing spear', 2), ('Exchange shield for additional hand weapon', 3), ('Exchange shield for double-handed weapon (axe)', 3)])],
    'Hand weapon and shield. May have throwing spear (+2 pts). May replace shield with additional hand weapon (+3 pts) or double-handed axe (+3 pts). Berserkers: a unit of Hirdmen can contain up to three Berserkers, placed with the unit at the start of the battle (not hidden; represented by a ferocious model in the front rank). Take at most one Berserker group per unit of Hirdmen.', page='13'))
NO.append(U('Characters', 'Ulfhednar', [M('Ulfhednar', '5 4 3 4 4 1 4 1 8', 18, mn=5, weapons=['Hand Weapon'], rules=['Frenzy', 'Different Weapons'],
    options=[('Additional hand weapon', 3), ('Double-handed weapon (axe)', 3)])],
    'Hand weapon. May have additional hand weapons (+3 pts) or double-handed axe (+3 pts). Frenzied. Skirmishers. Different Weapons. All the Ulfhednar must be grouped as a unit of at least five models.', page='13'))
NO.append(U('Characters', 'Godi', [M('Godi', '4 4 4 3 4 2 5 2 8', 80, weapons=['Hand Weapon'], rules=['Godi'], options=[('Ride a horse', 8)])],
    'Sword. May be mounted on a horse (+8 pts). The Godi and any unit he is with is immune to psychology and Break tests; as soon as the Godi is killed the unit tests as normal. 0-1.', mx=1, page='13'))
NO.append(U('Common Warriors', 'Hirdmen', [M('Hirdman', '4 4 3 3 4 1 4 1 8', 14, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Different Weapons', 'Fury of the Norsemen'],
    options=[('Throwing spear', 2), ('Double-handed weapon (axe)', 2), ('Javelins', 1), ('Exchange throwing spear for thrusting spear', 0), ('Stubborn', 3), ('Frenzied', 4)])],
    'Hand weapon, light armour and shield. May have throwing spear (+2 pts) or double-handed axe (+2 pts). All may have javelins (+1 pt). Different Weapons. Fury of the Norsemen. Light Infantry (all Hirdmen count as light infantry in the Norwegian, Hiberno-Norse, Orkneyinga and Isles lists). Orkneyinga: may exchange throwing spear for thrusting spear (free) and be upgraded to Stubborn (+3 pts per model). Kingdom of the Isles: may be frenzied (+4 pts per model).', page='14'))
NO.append(U('Common Warriors', 'Bondir', [M('Bondir', '4 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Exchange spear and shield for bow', 0), ('Exchange throwing spear for thrusting spear', 0)])],
    'Hand weapons, throwing spear, sword and shield. May exchange spear and shield for bow at no additional cost. Bow-armed Bondir count as light infantry; a player may not have more bow-armed Bondir than he has Bondir armed with other weapons (not enforced). Hiberno-Norse and Orkneyinga: may exchange throwing spear for thrusting spear (free).', page='14'))
NO.append(U('Uncommon Warriors', 'Thralls', [M('Subject warrior', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Javelin'], options=[('Buckler', 1), ('Exchange javelins and buckler for sling', 0), ('Exchange javelins for thrusting spear', 0)])],
    'Javelins. May have buckler (+1 pt). Light Infantry. Hiberno-Norse: may exchange javelins and bucklers for slings at no additional cost. Orkneyinga: may exchange javelins for thrusting spears at no additional cost.', page='14'))
for n in ('Vikings', 'Jomsvikings', 'Gestir', 'Freebooters', 'Serjeants', 'Amsaigh', 'Gasraidh', 'Gall-Gaedhil'): NO.append(DOW(n))
VAR['NO'] = {k: f'Shieldwall: Northmen - {k}' for k in ('Norwegians', 'Danes', 'Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles')}
NO_V = [
 (VAR['NO']['Norwegians'], pct(33, {'min': 50}, 33), 'Norwegians (p.10). Characters up to 33%; Hirdmen and/or Bondir at least 50%; Thralls and Dogs of War (Vikings, Jomsvikings, Gestir, Freebooters, Serjeants) up to 33%. All Hirdmen count as light infantry.'),
 (VAR['NO']['Danes'], pct(33, {'min': 50}, 33), 'Denmark (p.9; the list could equally be used for a Swedish army). Characters up to 33%; Hirdmen and Bondir at least 50%; Thralls and Dogs of War (Vikings, Jomsvikings, Gestir, Freebooters only) up to 33%. Bondir cost 7 pts each and have Leadership 7. Units of Hirdmen and Bondir may exchange throwing spear for thrusting spear (free).'),
 (VAR['NO']['Hiberno-Norse'], pct(33, {'min': 50}, 33), 'Hiberno-Norse (p.10). Characters up to 33%; the army may not include a Konnungr or Ulfhednar. Hirdmen and/or Bondir at least 50%; Thralls and Dogs of War (Vikings, Jomsvikings, Gestir, Amsaigh) up to 33%. All Hirdmen and Bondir count as light infantry; Bondir may exchange throwing spear for thrusting spear (free); Thralls may exchange javelins and bucklers for slings at no cost.'),
 (VAR['NO']['Orkneyinga'], pct(33, {'min': 50}, 33), 'Orkneyinga (pp.10-11). Characters up to 33%; no Konnungr or Ulfhednar. Hirdmen and/or Bondir at least 50%, and the army must not have more units of Hirdmen than Bondir; Thralls and Dogs of War (Vikings, Jomsvikings, Gestir, Gasraidh) up to 33%. Hirdmen count as light infantry and may be Stubborn (+3 pts per model); Thralls may exchange javelins for thrusting spears (free); Hirdmen and Bondir may exchange throwing spear for thrusting spear (free).'),
 (VAR['NO']['Kingdom of the Isles'], pct(33, {'min': 50}, 33), 'Kingdom of the Isles (p.11). Characters up to 33%; no Konnungr or Ulfhednar. Hirdmen and/or Bondir at least 50%, and the army must not have more units of Hirdmen than Bondir; Thralls and Dogs of War (Vikings, Jomsvikings, Gestir, Gall-Gaedhil) up to 33%. Hirdmen count as light infantry and may be frenzied (+4 pts per model).'),
]
NO_NOTES = ('NORTHMEN ARMY LISTS (Shieldwall, pp.6-16): Norwegians, Danes, Hiberno-Norse, Orkneyinga and Kingdom of the Isles. Percentages are by points. Special rules pp.4-5 and 12.\n'
  'Combined weapons within a Hirdmen unit (Different Weapons), the limit of bow-armed Bondir, and up to three Berserkers per unit of Hirdmen are tracked by the players, except that Berserker groups are limited to one per unit of Hirdmen.')
LISTS.append(('NO', 'Northmen (Shieldwall)', 'Northmen_Shieldwall.cat', NO, NO_V, NO_NOTES))
UNAV += [('NO', 'Konnungr', ['Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles']), ('NO', 'Ulfhednar', ['Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles'])]
AVAIL += [('NO', 'Vikings (Dogs of War)', ['Norwegians', 'Danes', 'Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles']), ('NO', 'Jomsvikings or Viking Adventurers (Dogs of War)', ['Norwegians', 'Danes', 'Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles']),
          ('NO', 'Gestir (Dogs of War)', ['Norwegians', 'Danes', 'Hiberno-Norse', 'Orkneyinga', 'Kingdom of the Isles']), ('NO', 'Freebooters (Dogs of War)', ['Norwegians', 'Danes']), ('NO', 'Serjeants (Dogs of War)', ['Norwegians']),
          ('NO', 'Amsaigh (Dogs of War)', ['Hiberno-Norse']), ('NO', 'Gasraidh (Dogs of War)', ['Orkneyinga']), ('NO', 'Gall-Gaedhil (Dogs of War)', ['Kingdom of the Isles'])]
OPTAV += [('NO', 'Hirdmen', 'Stubborn', ['Orkneyinga']), ('NO', 'Hirdmen', 'Frenzied', ['Kingdom of the Isles']), ('NO', 'Hirdmen', 'Exchange throwing spear for thrusting spear', ['Danes', 'Orkneyinga']),
          ('NO', 'Bondir', 'Exchange throwing spear for thrusting spear', ['Danes', 'Hiberno-Norse', 'Orkneyinga']),
          ('NO', 'Thralls', 'Exchange javelins and buckler for sling', ['Hiberno-Norse']), ('NO', 'Thralls', 'Exchange javelins for thrusting spear', ['Orkneyinga'])]
OPTRULE += [('NO', 'Hirdmen', 'Stubborn', 'Stubborn'), ('NO', 'Hirdmen', 'Frenzied', 'Frenzy')]
COSTV += [('NO', 'Bondir', {'Danes': 7})]
STATV += [('NO', 'Bondir', 'Ld', {'Danes': 7})]
RATIOS += [('NO', 'Berserkers', ['Hirdmen'], 1)]
HIRDMEN_LE_BONDIR += [('NO', 'Hirdmen', 'Bondir', ['Orkneyinga', 'Kingdom of the Isles'])]
OPT_ONCE += [('NO', [('Hersir', 'Army Standard Bearer')])]
PAIRS += [('NO', ['Konnungr', 'Jarl'], 'one-general')]

# ------------------------------------------------------------------ ENGLISH (book pp.17-25)
EN = []
ENCH = lambda: [('Javelins', 2), ('Ride a horse', 8)]
EN.append(U('Characters', 'Cyning', [M('Cyning', '4 6 4 4 4 3 6 3 9', 170, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Army General (English)'],
    options=[('Exchange thrusting spear and shield for double-handed weapon (axe)', 1)] + ENCH())],
    'Hand weapon, thrusting spear, light armour and shield. May exchange thrusting spear and shield for double-handed axe (+1 pt). May have javelins (+2 pts). May be mounted on a horse (+8 pts). Army General. Any friendly English unit within 12" of the Army General ignores Warband Psychology rule 2. 0-1 Army General (Cyning or Eorl). Not available to Anglia.', mx=1, page='22'))
EN.append(U('Characters', 'Eorl', [M('Eorl', '4 5 4 4 4 2 6 3 9', 150, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Army General (English)'],
    options=[('Exchange thrusting spear and shield for double-handed weapon (axe)', 1)] + ENCH())],
    'Hand weapon, thrusting spear, light armour and shield. May exchange thrusting spear and shield for double-handed axe (+1 pt). May have javelins (+2 pts). May be mounted on a horse (+8 pts). Army General. Any friendly English unit within 12" of the Army General ignores Warband Psychology rule 2. 0-1 Army General (Cyning or Eorl).', mx=1, page='22'))
EN.append(U('Characters', 'Ealdorman', [M('Ealdorman', '4 4 4 4 4 2 5 2 8', 60, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'],
    options=[('Double-handed weapon (axe)', 3), ('Javelins', 2), ('Ride a horse', 8), ('Army Standard Bearer', 15)])],
    'Hand weapon, thrusting spear, light armour and shield. May have double-handed axes (+3 pts). May have javelins (+2 pts). May be mounted on a horse (+8 pts). One Ealdorman may be made Army Standard Bearer (+15 pts).', page='23'))
EN.append(U('Characters', 'Abbod', [M('Abbod', '4 3 3 3 3 2 5 2 8', 60, weapons=['Hand Weapon'], rules=['Abbod'], options=[('Light armour', 3), ('Shield', 2), ('Ride a horse', 8)])],
    'Sword. May be armed with light armour (+3 pts), shield (+2 pts). May be mounted on a horse (+8 pts). A unit that the Abbod accompanies re-rolls any misses in the first round of any combat. 0-1.', mx=1, page='23'))
EN.append(U('Common Warriors', 'Huscarls', [M('Huscarl', '4 4 3 3 4 1 4 1 9', 20, mn=5, weapons=['Light Armour', 'Shield', 'Double-handed Weapon'], rules=['Shieldwall', 'Stubborn', 'Combined Units (English)'],
    options=[('Exchange double-handed weapon for thrusting spear', 0), ('Exchange thrusting spear for throwing spear', 0), ('Javelins', 1)])],
    'Light armour and shield. Double-handed axe or thrusting spear. May have javelins (+1 pt). Shieldwall. Stubborn. Combined Units. 0-1 unit. Northumbria: may exchange thrusting spears for throwing spears at no additional cost.', mx=1, page='23'))
EN.append(U('Common Warriors', 'Thegns', [M('Thegn', '4 4 3 3 3 1 4 1 6', 11, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Shieldwall', 'Warband', 'Combined Units (English)'],
    options=[('Javelins', 1), ('Ride a horse', 8), ('Exchange thrusting spear for throwing spear', 0), ('Designate as light infantry (free)', 0), ('Veterans', 0)])],
    'Hand weapons, thrusting spears, light armour and shield. All may be equipped with javelins (+1 pt). May be mounted on horses (+8 pts). Shieldwall. Warband. Combined Units. Wessex: Veterans (once per battle may re-roll all hit dice; the army may not have more units of mounted Thegns than dismounted Thegns). Mercia: any unit may be designated as light infantry (cannot combine with Ceorls). Northumbria and Kent: may exchange thrusting spears for throwing spears at no additional cost.', page='23'))
EN.append(U('Common Warriors', 'Ceorls', [M('Ceorl', '4 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Shieldwall', 'Warband', 'Combined Units (English)'], options=[('Exchange thrusting spear for throwing spear', 0)])],
    'Hand weapons, thrusting spears and shield. Shieldwall. Warband. Combined Units (the army may combine Ceorls with the Huscarls and Thegns). Kent: may exchange thrusting spears for throwing spears at no additional cost. Not available to Northumbria or Anglia.', page='23'))
EN.append(U('Uncommon Warriors', 'Geburs', [M('Gebur', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=[],
    options=[('Exchange javelins for sling', 0), ('Exchange javelins for bow', 1), ('Exchange javelins for shield and thrusting spear', 1)])],
    'Hand weapons and javelin. May exchange javelin for sling (free). May exchange javelin for bow (+1 pt). May exchange javelin for shield and thrusting spear (+1 pt). Geburs armed with javelin, sling or bow count as Skirmishers. Shield-armed Geburs have Shieldwall. No more than half the Gebur models may be bow-armed (not enforced). Anglia and Northumbria may combine spear and shield-armed Gebur with Thegns and Huscarls in the same way as Ceorls.', page='23'))
for n in ('Vikings', 'Freebooters', 'Stipendarii (dismounted)', 'Stipendarii (mounted)', 'Bradwr', 'Gasraidh', 'Gestir', 'Serjeants'): EN.append(DOW(n))
VAR['EN'] = {k: f'Shieldwall: English - {k}' for k in ('Wessex', 'Mercia', 'Northumbria', 'Anglia', 'Kent & the Home Counties')}
NOTE_HUS = ' The characters limit is 25% if the army includes Huscarls.'
EN_V = [
 (VAR['EN']['Wessex'], pct(33, {'min': 50}, 25), 'Wessex (p.20). Characters up to 33% (25% if the army includes Huscarls); the army may be led by a Cyning or an Eorl. Huscarls, Thegns or Ceorls at least 50%; Geburs and Dogs of War (Vikings, Freebooters, Stipendarii) up to 25%; no more than half of the Gebur models may be bow-armed. Veterans: Thegns may, once per battle, re-roll all their hit dice for close combat or shooting (the whole roll must be re-rolled and abided by). The army may not have more units of mounted Thegns than of dismounted Thegns.'),
 (VAR['EN']['Mercia'], pct(33, {'min': 50}, 33), 'Mercia (pp.20-21). Characters up to 33% (25% if the army includes Huscarls); led by a Cyning or an Eorl. Huscarls, Thegns or Ceorls at least 50%; Geburs and Dogs of War (Vikings, Freebooters, Bradwr) up to 33%. Any unit of Thegns may be designated as light infantry; such a unit cannot combine with Ceorls.'),
 (VAR['EN']['Northumbria'], pct(33, {'max': 50}, 33), 'Northumbria (p.21). Characters up to 33% (25% if the army includes Huscarls); led by a Cyning or an Eorl. Huscarls or Thegns up to 50% (Ceorls are not available); Geburs and Dogs of War (Gasraidh, Vikings, Gestir, Freebooters) up to 33%; no more than half of the Gebur models may be bow-armed. Thegns and Huscarls may exchange thrusting spears for throwing spears at no additional cost. Spear and shield-armed Gebur may combine with Thegns and Huscarls.'),
 (VAR['EN']['Anglia'], pct(33, {'max': 50}, 33), 'Anglia (p.21). Characters up to 33% (25% if the army includes Huscarls); the army may not be led by a Cyning. Huscarls or Thegns up to 50% (Ceorls are not available); Geburs and Dogs of War (Vikings, Gestir, Freebooters) up to 33%; no more than half of the Gebur models may be bow-armed. If the King is killed, all Ealdormen become subject to Hatred; any unit that includes Ealdormen also becomes subject to hatred of the enemy. Spear and shield-armed Gebur may combine with Thegns and Huscarls.'),
 (VAR['EN']['Kent & the Home Counties'], pct(33, {'min': 50}, 33), 'Kent & the Home Counties (p.21). Characters up to 33% (25% if the army includes Huscarls); led by a Cyning or an Eorl. Huscarls, Thegns or Ceorls at least 50%; Geburs and Dogs of War (Vikings, Freebooters, Serjeants) up to 33%; no more than half of the Gebur models may be bow-armed. Any Thegns or Ceorls may exchange thrusting spears for throwing spears at no additional cost.'),
]
EN_NOTES = ('ENGLISH ARMY LISTS (Shieldwall, pp.17-25): Wessex, Mercia, Northumbria, Anglia and Kent & the Home Counties. Percentages are by points. Special rules pp.20-23.\n'
  'Huscarls: the army may split its single unit of Huscarls and combine them with units of Ceorls (no more than 25% Huscarls or 50% Thegns in the combined unit; Thegns and Huscarls may not be mixed) - see the Combined Units rule; combined units are formed on the table, not in the roster.')
LISTS.append(('EN', 'English (Shieldwall)', 'English_Shieldwall.cat', EN, EN_V, EN_NOTES))
UNAV += [('EN', 'Cyning', ['Anglia']), ('EN', 'Ceorls', ['Northumbria', 'Anglia'])]
AVAIL += [('EN', 'Vikings (Dogs of War)', ['Wessex', 'Mercia', 'Northumbria', 'Anglia', 'Kent & the Home Counties']), ('EN', 'Freebooters (Dogs of War)', ['Wessex', 'Mercia', 'Northumbria', 'Anglia', 'Kent & the Home Counties']),
          ('EN', 'Stipendarii (dismounted) (Dogs of War)', ['Wessex']), ('EN', 'Stipendarii (mounted) (Dogs of War)', ['Wessex']), ('EN', 'Bradwr (Dogs of War)', ['Mercia']), ('EN', 'Gasraidh (Dogs of War)', ['Northumbria']),
          ('EN', 'Gestir (Dogs of War)', ['Northumbria', 'Anglia']), ('EN', 'Serjeants (Dogs of War)', ['Kent & the Home Counties'])]
OPTAV += [('EN', 'Huscarls', 'Exchange thrusting spear for throwing spear', ['Northumbria']), ('EN', 'Thegns', 'Exchange thrusting spear for throwing spear', ['Northumbria', 'Kent & the Home Counties']),
          ('EN', 'Thegns', 'Designate as light infantry (free)', ['Mercia']), ('EN', 'Thegns', 'Veterans', ['Wessex']), ('EN', 'Ceorls', 'Exchange thrusting spear for throwing spear', ['Kent & the Home Counties'])]
OPTRULE += [('EN', 'Thegns', 'Designate as light infantry (free)', 'Light Troops'), ('EN', 'Thegns', 'Veterans', 'Veterans (Wessex)')]
OPT_ONCE += [('EN', [('Ealdorman', 'Army Standard Bearer')])]
PAIRS += [('EN', ['Cyning', 'Eorl'], 'one-general')]
COND_CHARS += [('EN', 'Huscarls')]

# ------------------------------------------------------------------ CALEDONIANS (book pp.26-32)
CA = []
CA.append(U('Characters', 'Righ', [M('King', '5 6 4 4 4 3 6 3 7', 140, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Army General', 'Warband'],
    options=[('Javelins', 2), ('Double-handed weapon (axe)', 2), ('Ride a horse', 8)])],
    'Hand weapon, thrusting spear, light armour and shield. May have javelins (+2 pts) and may have double-handed axe (+2 pts). May be mounted on a horse (+8 pts). Army General. Warband. 0-1. Not available to the Picts or Strathclyde.', mx=1, page='29'))
CA.append(U('Characters', 'Mormaer', [M('Mormaer', '5 5 4 4 4 2 5 3 6', 75, weapons=['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Warband'],
    options=[('Javelins', 2), ('Double-handed weapon (axe)', 2), ('Army Standard Bearer (replaces shield)', 15), ('Army General (Strathclyde)', 25)])],
    'Hand weapon, thrusting spear, light armour and shield. May have javelins (+2 pts) and may have double-handed axe (+2 pts). Warband. One Mormaer may exchange shield for Army Standard Bearer (+15 pts). Strathclyde: one Mormaer may become Army General for +25 pts.', page='29'))
CA.append(U('Characters', 'Sagart', [M('Priest', '5 4 4 4 4 2 5 2 6', 80, weapons=['Hand Weapon'], rules=['Warband', 'Hatred'], options=[('Light armour', 3), ('Shield', 2)])],
    'Sword. May be armed with light armour (+3 pts), shield (+2 pts). Warband. Hatred. Any unit the Priest is with gains Hatred. 0-1.', mx=1, page='30'))
CA.append(U('Toisech', 'Toisech/Thanes', [M('Noble Warrior', '5 4 3 4 3 1 4 1 6', 13, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], rules=['Warband', 'Werod'],
    options=[('Javelins', 1), ('Ride a horse', 8), ('Stubborn', 3), ('Exchange throwing spear for thrusting spear', 0), ('Shieldwall', 1), ('Exchange throwing spear for pike', 1), ('Light infantry (light cavalry if mounted) (free)', 0)])],
    'Hand weapons, throwing spear, light armour and shield. May have javelins (+1 pt). May be mounted on a horse (+8 pts). Warband. Werod. 0-1 unit. If included in the army the Righ must accompany this unit at all times (not enforced). Dal Riata: the unit may be Stubborn (+3 pts per model). Scotland: may exchange throwing spear for thrusting spear (free) and pay +1 pt per model to use Shieldwall. Picts: count as light infantry and may be equipped with pike (+1 pt). Strathclyde: count as light infantry if not mounted, light cavalry if mounted.', mx=1, page='30'))
CA.append(U('Soer-chele', 'Soer-chele', [M('Wealthy freeman', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Buckler'], rules=['Warband'],
    options=[('Exchange thrusting spear for pike', 1), ('Light infantry (free)', 0)])],
    'Thrusting spears and bucklers. Warband. Alba, Picts and Strathclyde. Picts: count as light infantry and may be equipped with pike (+1 pt). Strathclyde: count as light infantry.', page='30'))
CA.append(U('Soer-chele', 'Soer-chele (Dal Riata)', [M('Wealthy freeman', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Buckler'], rules=['Warband'],
    options=[('Light infantry (free)', 0)])],
    'Throwing spears and bucklers (Dal Riata). Cost 6 pts and have Leadership 6. Warband. Any unit may be designated as light infantry for free.', page='28'))
CA.append(U('Soer-chele', 'Soer-chele (Scotland)', [M('Wealthy freeman', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Warband', 'Shieldwall'])],
    'Thrusting spears and shield (Scotland). Cost 6 pts. Warband. May use Shieldwall.', page='28'))
CA.append(U('Doer-chele', 'Doer-chele', [M('Poor freeman', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband'],
    options=[('Exchange javelins and buckler for bow', 1), ('Exchange javelins and buckler for hunting crossbow', 0)])],
    'Hand weapons, javelins and buckler. Skirmishers. Warband. Every other unit of Doer-chele may have bows (+1 pt) (Alba, Scotland, Picts); Picts may alternatively have hunting crossbows (free): these count as crossbows for all purposes except they have a range of 24" and are Strength 3. Not enforced: which units are bow-armed.', page='30'))
CA.append(U('Eachraidh', 'Eachraidh', [M('Horse warrior Cavalryman', '8 3 3 3 3 1 3 1 5', 17, mn=5, weapons=['Hand Weapon', 'Shield', 'Javelin'], rules=['Warband'], options=[('Exchange javelins for throwing spear', 0)])],
    'Hand weapons, shield and javelin. Light Cavalry. Warband. Strathclyde: units may exchange javelins for throwing spears (free).', page='31'))
for n in ('Vikings', 'Amsaigh', 'Gasraidh', 'Gall-Gaedhil', 'Freebooters', 'Stipendarii (dismounted)', 'Stipendarii (mounted)'): CA.append(DOW(n))
VAR['CA'] = {k: f'Shieldwall: Caledonians - {k}' for k in ('Dal Riata', 'Alba', 'The Picts (the Cruithne)', 'Scotland', 'Strathclyde')}
P_C1 = 'Common Warriors: Toisech, Soer-chele and Doer-chele'; P_C2 = 'Common Warriors: Toisech and Soer-chele'; P_C3 = 'Common Warriors: Toisech, Eachraidh, Soer-chele and Doer-chele'
P_U1 = 'Uncommon Warriors: Eachraidh and Dogs of War'; P_U2 = 'Uncommon Warriors: Doer-chele, Eachraidh and Dogs of War'
CA_V = [
 (VAR['CA']['Dal Riata'], {'Characters': {'max': 33}, P_C1: {'min': 50}, P_U1: {'max': 25}}, 'Dal Riata (p.28). Characters up to 33%; Toisech, Soer-chele and Doer-chele at least 50%; Eachraidh and Dogs of War (Vikings, Amsaigh, Gasraidh) up to 25%. The unit of Toisech may be Stubborn (+3 pts). All Soer-chele cost 6 pts, have Leadership 6 and use throwing spears, not thrusting spears; any unit of Soer-chele may be designated as light infantry for free.'),
 (VAR['CA']['Alba'], {'Characters': {'max': 33}, P_C1: {'min': 50}, P_U1: {'max': 25}}, 'Alba (p.28). Characters up to 33%; Toisech, Soer-chele and Doer-chele at least 50%; Eachraidh and Dogs of War (Vikings, Amsaigh, Gall-Gaedhil, Gasraidh) up to 25%. Every other unit of Doer-chele may have bows (+1 pt).'),
 (VAR['CA']['The Picts (the Cruithne)'], {'Characters': {'max': 33}, P_C1: {'min': 50}, P_U1: {'max': 25}}, 'The Picts (p.28). Characters up to 33%; the army may not include the Righ. Toisech, Soer-chele and Doer-chele at least 50%; Eachraidh and Dogs of War (Vikings, Gasraidh) up to 25%. All Toisech and Soer-chele count as light infantry and may be equipped with pike (+1 pt). Every other unit of Doer-chele may have bows (+1 pt) or hunting crossbows (free).'),
 (VAR['CA']['Scotland'], {'Characters': {'max': 33}, P_C2: {'min': 50}, P_U2: {'max': 33}}, 'Scotland (p.28). Characters up to 33%; Toisech and Soer-chele at least 50%; Doer-chele, Eachraidh and Dogs of War (Vikings, Gall-Gaedhil, Freebooters, Stipendarii) up to 33%. The Toisech may exchange throwing spear for thrusting spear (free) and may pay an additional +1 pt per model to use Shieldwall. The Soer-chele cost 6 pts, are equipped with shields and may use Shieldwall. Every other unit of Doer-chele may have bows (+1 pt).'),
 (VAR['CA']['Strathclyde'], {'Characters': {'max': 33}, P_C3: {'min': 50}, 'Dogs of War': {'max': 25}}, 'Strathclyde (p.28). Characters up to 33%; the army may not include the Righ; one Mormaer may become Army General for +25 pts. Toisech, Eachraidh, Soer-chele and Doer-chele at least 50%; Dogs of War (Vikings only) up to 25%. Toisech count as light infantry if not mounted, light cavalry if mounted. Units of Eachraidh may exchange javelins for throwing spears (free). All units of Soer-chele count as light infantry.'),
]
CA_NOTES = ('CALEDONIAN ARMY LISTS (Shieldwall, pp.26-32): Dal Riata, Alba, the Picts, Scotland and Strathclyde. Percentages are by points. Special rules pp.4-5 and 29 (Raiders: the Caledonian commander may always choose whether he moves first or second).\n'
  'The Common/Uncommon pools differ between the compositions, so the units also belong to pool categories named after them (Common Warriors: ... / Uncommon Warriors: ...).')
LISTS.append(('CA', 'Caledonians (Shieldwall)', 'Caledonians_Shieldwall.cat', CA, CA_V, CA_NOTES))
ALLCA = ['Dal Riata', 'Alba', 'The Picts (the Cruithne)', 'Scotland', 'Strathclyde']
UNAV += [('CA', 'Righ', ['The Picts (the Cruithne)', 'Strathclyde'])]
AVAIL += [('CA', 'Soer-chele', ['Alba', 'The Picts (the Cruithne)', 'Strathclyde']), ('CA', 'Soer-chele (Dal Riata)', ['Dal Riata']), ('CA', 'Soer-chele (Scotland)', ['Scotland']),
          ('CA', 'Vikings (Dogs of War)', ALLCA), ('CA', 'Amsaigh (Dogs of War)', ['Dal Riata', 'Alba']), ('CA', 'Gasraidh (Dogs of War)', ['Dal Riata', 'Alba', 'The Picts (the Cruithne)']),
          ('CA', 'Gall-Gaedhil (Dogs of War)', ['Alba', 'Scotland']), ('CA', 'Freebooters (Dogs of War)', ['Scotland']),
          ('CA', 'Stipendarii (dismounted) (Dogs of War)', ['Scotland']), ('CA', 'Stipendarii (mounted) (Dogs of War)', ['Scotland'])]
OPTAV += [('CA', 'Mormaer', 'Army General (Strathclyde)', ['Strathclyde']),
          ('CA', 'Toisech/Thanes', 'Stubborn', ['Dal Riata']), ('CA', 'Toisech/Thanes', 'Exchange throwing spear for thrusting spear', ['Scotland']), ('CA', 'Toisech/Thanes', 'Shieldwall', ['Scotland']),
          ('CA', 'Toisech/Thanes', 'Exchange throwing spear for pike', ['The Picts (the Cruithne)']), ('CA', 'Toisech/Thanes', 'Light infantry (light cavalry if mounted) (free)', ['The Picts (the Cruithne)', 'Strathclyde']),
          ('CA', 'Soer-chele', 'Exchange thrusting spear for pike', ['The Picts (the Cruithne)']), ('CA', 'Soer-chele', 'Light infantry (free)', ['The Picts (the Cruithne)', 'Strathclyde']),
          ('CA', 'Doer-chele', 'Exchange javelins and buckler for bow', ['Alba', 'The Picts (the Cruithne)', 'Scotland']), ('CA', 'Doer-chele', 'Exchange javelins and buckler for hunting crossbow', ['The Picts (the Cruithne)']),
          ('CA', 'Eachraidh', 'Exchange javelins for throwing spear', ['Strathclyde'])]
OPTRULE += [('CA', 'Toisech/Thanes', 'Stubborn', 'Stubborn'), ('CA', 'Toisech/Thanes', 'Shieldwall', 'Shieldwall'), ('CA', 'Toisech/Thanes', 'Light infantry (light cavalry if mounted) (free)', 'Light Troops'),
            ('CA', 'Soer-chele', 'Light infantry (free)', 'Light Troops'), ('CA', 'Soer-chele (Dal Riata)', 'Light infantry (free)', 'Light Troops')]
STATV += []
OPT_ONCE += [('CA', [('Mormaer', 'Army Standard Bearer (replaces shield)')]), ('CA', [('Mormaer', 'Army General (Strathclyde)')])]
SECOND.update({('CA', 'Toisech/Thanes'): [P_C1, P_C2, P_C3], ('CA', 'Soer-chele'): [P_C1, P_C2, P_C3], ('CA', 'Soer-chele (Dal Riata)'): [P_C1, P_C2, P_C3], ('CA', 'Soer-chele (Scotland)'): [P_C1, P_C2, P_C3],
               ('CA', 'Doer-chele'): [P_C1, P_C3, P_U2], ('CA', 'Eachraidh'): [P_C3, P_U1, P_U2]})
for n in ('Vikings', 'Amsaigh', 'Gasraidh', 'Gall-Gaedhil', 'Freebooters', 'Stipendarii (dismounted)', 'Stipendarii (mounted)'):
    pass
for u in CA:
    if u['cat'] == 'Uncommon Warriors':          # Dogs of War
        u['cat'] = 'Dogs of War'; SECOND[('CA', u['name'])] = [P_U1, P_U2]

# ------------------------------------------------------------------ WELSH (book pp.49-56)
WE = []
WKING = lambda: [('Exchange throwing spear for thrusting spear', 0), ('Ride a horse', 8)]
WE.append(U('Characters', 'Teyrn', [M('High King', '5 5 4 4 4 3 5 3 8', 140, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Light Armour', 'Shield'], rules=['Army General', 'Warband'], options=WKING())],
    'Hand weapon, throwing spear, javelin, light armour and shield. May exchange throwing spear for thrusting spear (free). May be mounted on a horse (+8 pts). Warband. Army General. 0-1. Not available to Powys or Dumnonia.', mx=1, page='52'))
WE.append(U('Characters', 'Uchelwyr', [M('Minor King', '5 5 4 4 4 2 5 3 7', 85, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Light Armour', 'Shield'], rules=['Warband'], options=WKING() + [('Army Battle Standard (replaces shield)', 15)])],
    'Hand weapon, throwing spear, javelin, light armour and shield. May exchange throwing spear for thrusting spear (free). May be mounted on a horse (+8 pts). Warband. One figure, other than one designated Army General, may exchange its shield for the Army Battle Standard (+15 pts). A Welsh army with no Teyrn may be led by an Uchelwyr.', page='52'))
WE.append(U('Characters', 'Offeiriad', [M('Priest', '5 4 4 3 4 2 5 2 7', 65, weapons=['Hand Weapon'], rules=['Warband', 'Offeiriad'], options=[('Light armour', 3), ('Shield', 2)])],
    'Sword. May be armed with light armour (+3 pts) and shield (+2 pts). May only accompany Teulu, Priodaur and Bonnedig. Warband. You may re-roll rally attempts of any unit the Priest is accompanying. 0-1.', mx=1, page='53'))
WE.append(U('Teulu', 'Teulu', [M('Bodyguard', '5 4 4 4 3 1 4 1 7', 12, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Werod'],
    options=[('Light armour', 3), ('Throwing spear', 2), ('Ride a horse', 8), ('Exchange throwing spear for thrusting spear', 0), ('Bow', 3)])],
    'Hand weapons, javelin and shield. May have light armour (+3 pts), throwing spear (+2 pts). All in a Teulu may be mounted on horses (+8 pts). Warband. Werod. Light Infantry. 0-1 unit. Gwynedd: the Teulu may exchange throwing spear for thrusting spears (free). Southern Kingdoms: the Teulu may have bows (+3 pts).', mx=1, page='53'))
WE.append(U('Common Warriors', 'Priodaur', [M('Freeman', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'],
    options=[('Javelins', 1), ('Throwing spear', 1), ('Exchange throwing spear for thrusting spear', 0), ('Exchange spear and shield for bow', 0)])],
    'Hand weapons and shield. May have javelins (+1 pt) and/or throwing spears (+1 pt). Warband. Light Infantry. Gwynedd: may exchange throwing spear for thrusting spears (free). Powys: every other unit of Priodaur may exchange shield and spear for bow (free). Southern Kingdoms: Priodaur may exchange their spear and shields for bows (free); at least half of the units of Priodaur must be bow-armed (not enforced).', page='53'))
WE.append(U('Common Warriors', 'Bonnedig', [M('Poor freeman', '5 2 3 3 3 1 3 1 6', 5, mn=5, weapons=['Javelin', 'Buckler'], options=[('Throwing spear', 1), ('Exchange javelins and buckler for bow', 0)])],
    'Javelins and buckler. May have throwing spear (+1 pt). Every other unit may exchange javelins and buckler for bows (free). Skirmishers.', page='54'))
WE.append(U('Uncommon Warriors', 'Taeog', [M('Slave', '5 2 2 2 3 1 2 1 4', 3, mn=5, weapons=['Improvised Weapon'], options=[('Sling', 1), ('Javelins', 1)])],
    'Improvised weapons. May have slings (+1 pt) or javelins (+1 pt). Skirmishers.', page='54'))
for n in ('Vikings', 'Freebooters', 'Amsaigh', 'Devroet'): WE.append(DOW(n))
VAR['WE'] = {k: f'Shieldwall: Welsh - {k}' for k in ('Gwynedd', 'Powys', 'Southern Kingdoms', 'Dumnonia')}
WE_V = [
 (VAR['WE']['Gwynedd'], pct(33, {'min': 50}, 25), 'Gwynedd (p.51). Characters up to 33%; Priodaur and Bonnedig at least 50%; Taeog and Dogs of War (Vikings, Freebooters) up to 25%. Teulu and Priodaur may exchange throwing spear for thrusting spears (free).'),
 (VAR['WE']['Powys'], pct(33, {'min': 50}, 25), 'Powys (pp.51-52). Characters up to 33%; the army may not include any Teyrn. Priodaur and Bonnedig at least 50%; Taeog and Dogs of War (Vikings, Freebooters) up to 25%. Every other unit of Priodaur may exchange shield and spear for bow (free).'),
 (VAR['WE']['Southern Kingdoms'], pct(33, {'min': 50}, 25), 'The Southern Kingdoms (p.52). Characters up to 33%; Priodaur and Bonnedig at least 50%; Taeog and Dogs of War (Vikings, Amsaigh) up to 25%. Priodaur may exchange their spear and shields for bows (free); the Teulu may have bows (+3 pts); at least half of the units of Priodaur must be bow-armed.'),
 (VAR['WE']['Dumnonia'], pct(33, {'min': 50}, 25), 'Dumnonia (p.52). Characters up to 33%; the army may not include the Teyrn. Priodaur and Bonnedig at least 50%; Taeog and Dogs of War (Vikings, Devroet) up to 25%. One unit armed with javelins may have poisoned javelins at an additional cost of +2 pts per model (counts as S4, armour saves not modified).'),
]
WE_NOTES = ('WELSH ARMY LISTS (Shieldwall, pp.49-56): Gwynedd, Powys, the Southern Kingdoms and Dumnonia. Percentages are by points. Special rules p.52 (Choice of Terrain: if players agree to randomly choose the terrain, the Welsh player may always select one additional item of terrain which he may place anywhere other than the opponent\'s deployment zone).\n'
  'The Teulu and the Priodaur/Bonnedig/Taeog pools are as printed: the Teulu is not part of the Common or Uncommon percentages.')
LISTS.append(('WE', 'Welsh (Shieldwall)', 'Welsh_Shieldwall.cat', WE, WE_V, WE_NOTES))
UNAV += [('WE', 'Teyrn', ['Powys', 'Dumnonia'])]
AVAIL += [('WE', 'Vikings (Dogs of War)', ['Gwynedd', 'Powys', 'Southern Kingdoms', 'Dumnonia']), ('WE', 'Freebooters (Dogs of War)', ['Gwynedd', 'Powys']), ('WE', 'Amsaigh (Dogs of War)', ['Southern Kingdoms']), ('WE', 'Devroet (Dogs of War)', ['Dumnonia'])]
OPTAV += [('WE', 'Teulu', 'Exchange throwing spear for thrusting spear', ['Gwynedd']), ('WE', 'Teulu', 'Bow', ['Southern Kingdoms']),
          ('WE', 'Priodaur', 'Exchange throwing spear for thrusting spear', ['Gwynedd']), ('WE', 'Priodaur', 'Exchange spear and shield for bow', ['Powys', 'Southern Kingdoms'])]
OPT_ONCE += [('WE', [('Uchelwyr', 'Army Battle Standard (replaces shield)')])]
PAIRS += []

# ------------------------------------------------------------------ HIBERNIANS (book pp.56-64)
HI = []
HI.append(U('Characters', 'Ri Ruirech', [M('Over-king', '5 6 4 4 4 3 6 3 7', 140, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Army General', 'Warband'], options=[('Ride a horse', 8)])],
    'Hand weapon, javelin, light armour and shield. May be mounted on a horse (+8 pts). Warband. Army General. 0-1.', mx=1, page='61'))
HI.append(U('Characters', 'Ri Tuathe', [M('Tribal King', '5 5 4 4 4 2 5 3 6', 95, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Warband'], options=[('Ride a horse', 8), ('Army General (no Ri Ruirech)', 0)])],
    'Hand weapon, javelin, light armour and shield. May be mounted on a horse (+8 pts). Warband. If no Ri Ruirech is present then one Ri Tuathe may be designated Army General.', page='61'))
HI.append(U('Characters', 'Curadh', [M('Champion', '5 4 4 4 4 2 4 2 6', 60, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband'],
    options=[('Light armour', 3), ('Exchange shield for double-handed weapon (axe)', 2), ('Exchange shield for additional hand weapons', 2), ('Ride a horse', 8), ('Army Standard Bearer', 15)])],
    'Hand weapon, javelin and shield. May have light armour (+3 pts). May exchange shield for double-handed axe (+2 pts) or additional hand weapons (+2 pts). May be mounted on a horse (+8 pts). Warband. One Champion may be made Army Standard Bearer (+15 pts).', page='62'))
HI.append(U('Characters', 'Sacardd', [M('Priest', '5 4 4 4 4 2 5 2 7', 80, weapons=['Hand Weapon'], rules=['Warband', 'Hatred'], options=[('Light armour', 3), ('Shield', 2)])],
    'Sword. May be armed with light armour (+3 pts) and shield (+2 pts). Warband. The Priest and any unit he is with is subject to Hatred of the enemy as described in the Warhammer Ancient Battles psychology rules. 0-1.', mx=1, page='62'))
HI.append(U('Fianna', 'Fianna', [M('Noble warrior', '5 4 3 4 3 1 4 1 5', 8, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Werod'],
    options=[('Exchange shield for double-handed weapon (axe)', 1), ('Ride a horse', 8), ('Light armour', 3), ('Exchange javelins for thrusting spear', 3), ('Throwing spear', 2), ('Stubborn', 3)])],
    'Hand weapons, javelins and shield. May exchange their shields for double-handed axes (+1 pt). May be mounted (+8 pts per model), if so they count as light cavalry. Warband. Werod. 0-1 unit. Munster: may have light armour (+3 pts) and exchange javelins for thrusting spears (+3 pts); if armed with thrusting spear they may use Shieldwall. Leinster: light armour (+3 pts), throwing spears (+2 pts). Connacht: count as light infantry. Ulster: light armour (+3 pts) and may be Stubborn (+3 pts).', mx=1, page='62'))
HI.append(U('Common Warriors', 'Bonnachts', [M('Tribal warrior', '5 3 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband'])],
    'Hand weapons, javelins and buckler. Warband. Connacht: count as light infantry.', page='62'))
HI.append(U('Common Warriors', 'Kerns', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Javelin'], rules=['Warband'], options=[('Exchange javelins for sling', 1)])],
    'Javelins. May exchange javelins for sling (+1 pt). Skirmishers. Warband.', page='62'))
HI.append(U('Uncommon Warriors', 'Madadh', [M('Packmaster', '5 4 4 3 3 1 4 1 6', 8, mn=1, mx=1, weapons=['Hand Weapon'], rules=['Warband'], options=[('Javelins', 2), ('Light armour', 3)]),
                                            M('Warhound', '6 4 0 3 3 1 3 1 3', 5, mn=1, mx=6, weapons=[], rules=['Warband'])],
    'The Packmaster has hand weapons; Warhounds have teeth. The Packmaster may have javelins (+2 pts) and/or light armour (+3 pts). Skirmishers. Warband. Any hit inflicted by missile weapons should be randomly divided between the Packmaster and hounds. Each unit may contain a maximum of one Packmaster and up to six hounds.', page='63'))
for n in ('Vikings', 'Amsaigh', 'Gall-Gaedhil', 'Gestir', 'Gasraidh'): HI.append(DOW(n))
VAR['HI'] = {k: f'Shieldwall: Hibernians - {k}' for k in ('Munster', 'Leinster', 'Connacht', 'Ulster')}
HI_V = [
 (VAR['HI']['Munster'], pct(33, {'min': 50}, 33), 'Munster (p.60). Characters up to 33%; Bonnachts and Kerns at least 50%; Madadh and Dogs of War (Vikings, Amsaigh, Gall-Gaedhil) up to 33%. The Fianna may have light armour (+3 pts). They may exchange javelins for thrusting spears (+3 pts); if armed with thrusting spear they may use Shieldwall.'),
 (VAR['HI']['Leinster'], pct(33, {'max': 50}, 33), 'Leinster (p.60). Characters up to 33%; Bonnachts and Kerns up to 50%; Madadh and Dogs of War (Vikings, Gestir, Amsaigh) up to 33%. The Fianna may have light armour (+3 pts). They may have throwing spears (+2 pts).'),
 (VAR['HI']['Connacht'], pct(33, {'min': 50}, 33), 'Connacht (p.60). Characters up to 33%; Bonnachts and Kerns at least 50%; Madadh and Dogs of War (Vikings, Amsaigh) up to 33%. The Fianna and Bonnachts count as light infantry.'),
 (VAR['HI']['Ulster'], pct(33, {'max': 50}, 33), 'Ulster (p.60). Characters up to 33%; Bonnachts and Kerns up to 50%; Madadh and Dogs of War (Vikings, Amsaigh, Gasraidh, Gall-Gaedhil) up to 33%. The Fianna may have light armour (+3 pts) and be Stubborn (+3 pts).'),
]
HI_NOTES = ('HIBERNIAN ARMY LISTS (Shieldwall, pp.56-64): Munster, Leinster, Connacht and Ulster. Percentages are by points. Special rules p.61 (Ambush: before units are placed, a Hibernian commander may keep one unit off the battlefield, written down as hidden; it is deployed when an enemy unit comes within 8" or earlier if he wishes, and is immune to psychology tests while hidden).\n'
  'The Fianna are not part of the Common or Uncommon percentages (printed lists name only Bonnachts, Kerns, Madadh and Dogs of War).')
LISTS.append(('HI', 'Hibernians (Shieldwall)', 'Hibernians_Shieldwall.cat', HI, HI_V, HI_NOTES))
AVAIL += [('HI', 'Vikings (Dogs of War)', ['Munster', 'Leinster', 'Connacht', 'Ulster']), ('HI', 'Amsaigh (Dogs of War)', ['Munster', 'Leinster', 'Connacht', 'Ulster']),
          ('HI', 'Gall-Gaedhil (Dogs of War)', ['Munster', 'Ulster']), ('HI', 'Gestir (Dogs of War)', ['Leinster']), ('HI', 'Gasraidh (Dogs of War)', ['Ulster'])]
OPTAV += [('HI', 'Fianna', 'Light armour', ['Munster', 'Leinster', 'Ulster']), ('HI', 'Fianna', 'Exchange javelins for thrusting spear', ['Munster']), ('HI', 'Fianna', 'Throwing spear', ['Leinster']), ('HI', 'Fianna', 'Stubborn', ['Ulster'])]
OPTRULE += [('HI', 'Fianna', 'Stubborn', 'Stubborn')]
OPT_ONCE += [('HI', [('Curadh', 'Army Standard Bearer')])]
PAIRS += []
OPTRULE += [('HI', 'Ri Tuathe', 'Army General (no Ri Ruirech)', 'Army General (Chariot Wars)')]
OPT_ONCE += [('HI', [('Ri Tuathe', 'Army General (no Ri Ruirech)')])]

# ------------------------------------------------------------------ WESTERN FRANKS (book pp.66-76)
FR = []
FCH = lambda: [('Exchange light armour for heavy armour', 1), ('Javelins', 2), ('Exchange throwing spear for thrusting spear', 0), ('Ride a warhorse', 16), ('Lance (Normandy; mounted)', 4)]
FR.append(U('Characters', 'Rex/Dux', [M('King/Duke', '4 6 4 4 4 3 6 4 9', 190, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], rules=['Army General'], options=FCH())],
    'Hand weapon, throwing spear, light armour and shield. May upgrade armour to heavy armour (+1 pt), have javelins (+2 pts), exchange throwing spear for thrusting spear (free), be mounted on a warhorse (+16 pts). Normandy: a mounted Rex or Comes may have a lance (+4 pts). Army General. 0-1.', mx=1, page='72'))
FR.append(U('Characters', 'Comes', [M('Count', '4 5 4 4 4 2 6 3 8', 100, weapons=['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Shield'], options=FCH() + [('Army Battle Standard (replaces shield)', 15)])],
    'Hand weapon, throwing spear, light armour and shield. May upgrade armour to heavy armour (+1 pt), have javelins (+2 pts), exchange throwing spear for thrusting spear (free), be mounted on a warhorse (+16 pts). Normandy: a mounted Rex or Comes may have a lance (+4 pts). One Comes may exchange its shield for the Army Battle Standard (+15 pts).', page='72'))
FR.append(U('Characters', 'Bishop', [M('Bishop', '4 5 4 4 4 2 6 3 9', 130, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Bishop'], options=[('Exchange light armour for heavy armour', 1), ('Ride a warhorse', 16)])],
    'Hand weapon, light armour and shield. May upgrade armour to heavy armour (+1 pt). May be mounted on a warhorse (+16 pts). Any unit the Bishop is with may re-roll failed Panic tests. 0-1.', mx=1, page='72'))
MILOPT = [('Exchange light armour for heavy armour', 1), ('Javelins', 1), ('Exchange throwing spear for thrusting spear', 0), ('Bow', 1), ('Exchange throwing spear for lance', 4), ('Shieldwall', 0)]
FR.append(U('Milites', 'Dismounted Milites', [M('Dismounted knight', '4 4 3 3 3 1 4 1 8', 14, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Throwing Spear'], options=[o for o in MILOPT if 'lance' not in o[0]])],
    'Hand weapon, light armour, shield and either throwing spear or thrusting spear. May upgrade armour to heavy armour (+1 pt), have javelins (+1 pt). Carolingian French: may have bows (+1 pt); up to half of a unit, including mounted troops, may exchange shield and spear for bow (free), deployed in the rear ranks. Flanders: dismounted Milites cost 15 pts each and have Shieldwall.', page='73'))
FR.append(U('Milites', 'Mounted Milites', [M('Mounted knight Cavalryman', '8 4 3 3 3 1 4 1 8', 28, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Throwing Spear'], rules=['Knights Rank Bonus'], options=[o for o in MILOPT if o[0] != 'Shieldwall'])],
    'Hand weapon, light armour, shield and either throwing spear or thrusting spear. Mounted Milites have warhorses. May upgrade armour to heavy armour (+1 pt), have javelins (+1 pt). Mounted Milites may receive up to a +1 rank bonus. Carolingian French: may have bows (+1 pt); up to half of a unit may exchange shield and spear for bow (free). Normandy: cost 30 pts each, may exchange thrusting spear for lance (+4 pts), Ferocious Charge. Bretons: cost 30 pts each and have BS 4; fleeing/firing and fleeing as a charge reaction rallies automatically (see rule); all mounted troops count as light cavalry. Capetian French: cost 29 pts each, Ferocious Charge.', page='73'))
FR.append(U('Pueri', 'Pueri', [M('Pueri Light Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Exchange javelins for throwing spear', 2), ('Exchange javelins for thrusting spear', 2), ('Exchange javelin and shield for bow', 0)])],
    'Sword, javelins and shield. May exchange javelins for throwing spear or thrusting spear (+2 pts). Light Cavalry. Carolingian French: every other unit of Pueri may exchange javelin and shield for bow.', page='73'))
FR.append(U('Liberi', 'Liberi', [M('Freeman', '4 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Javelins', 1), ('Exchange thrusting spear and shield for bow', 0), ('Light infantry (free)', 0),
    ('Men of the Marches (Leadership 7)', 1), ('Light armour', 2), ('Shieldwall', 0), ('Exchange thrusting spear for throwing spear', 0)])],
    'Hand weapons, thrusting spears and shield. May be additionally equipped with javelins (+1 pt). Every other unit may exchange thrusting spear and shield for bows (free). Any unit of Liberi may be designated as light infantry (free). Carolingian French: units may be upgraded to Men of the Marches (+1 pt; Leadership 7). Flanders: cost 7 pts each, have Shieldwall and may be given light armour (+2 pts). Bretons: all Liberi count as light infantry and may exchange thrusting spears for throwing spears (free).', page='73'))
FR.append(U('Coloni', 'Coloni', [M('Unfree & poor', '4 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], options=[('Exchange javelins for sling', 0), ('Exchange javelins for bow', 1)])],
    'Hand weapons and javelins. May exchange javelins (and buckler) for sling (free), or bow (+1 pt). Skirmishers.', page='73'))
for n in ('Vikings', 'Gestir', 'Stipendarii (dismounted)', 'Stipendarii (mounted)', 'Serjeants', 'Devroet', 'Freebooters', 'Cottereaux'): FR.append(DOW(n))
VAR['FR'] = {k: f'Shieldwall: Western Franks - {k}' for k in ('Carolingian French', 'County of Flanders', 'Duchy of Normandy', 'The Bretons', 'Capetian French')}
FC_ML = 'Common Warriors: Milites and Liberi'; FC_MP = 'Common Warriors: Milites and Pueri'
FU1 = 'Uncommon Warriors: Pueri, Liberi, Coloni and Dogs of War'; FU2 = 'Uncommon Warriors: Pueri, Coloni and Dogs of War'; FU3 = 'Uncommon Warriors: Liberi, Coloni and Dogs of War'; FU4 = 'Uncommon Warriors: Coloni and Dogs of War'
FR_V = [
 (VAR['FR']['Carolingian French'], {'Characters': {'max': 25}, 'Milites': {'min': 50}, FU1: {'max': 33}}, 'Carolingian French (p.70). Characters up to 25%; Milites at least 50%; Pueri, Liberi, Coloni and Dogs of War (Vikings, Gestir, Stipendarii, Serjeants, Devroet) up to 33%. Milites may have bows (+1 pt); up to half of a unit of Milites, including mounted troops, may exchange shield and spear for bow (free), deployed in the rear ranks. Units of Liberi may be upgraded to Men of the Marches (+1 pt; Leadership 7). Every other unit of Pueri may exchange javelin and shield for bow.'),
 (VAR['FR']['County of Flanders'], {'Characters': {'max': 25}, FC_ML: {'min': 50}, FU2: {'max': 25}}, 'The County of Flanders (pp.70-71). Characters up to 25%; Milites and Liberi at least 50%; Pueri, Coloni and Dogs of War (Vikings, Freebooters, Stipendarii, Serjeants) up to 25%. Dismounted Milites cost 15 pts each and have Shieldwall. Liberi cost 7 pts each and have Shieldwall; Liberi may be given light armour (+2 pts).'),
 (VAR['FR']['Duchy of Normandy'], {'Characters': {'max': 25}, FC_MP: {'min': 50}, FU3: {'max': 33}}, 'The Duchy of Normandy (p.71). Characters up to 25%; a mounted Rex or Comes may have a lance (+4 pts). Milites and Pueri at least 50%; Liberi, Coloni and Dogs of War (Vikings, Stipendarii, Serjeants, Devroet) up to 33%. Mounted Milites cost 30 pts each and may exchange thrusting spear for lance (+4 pts); mounted Milites have Ferocious Charge.'),
 (VAR['FR']['The Bretons'], {'Characters': {'max': 25}, FC_MP: {'min': 50}, FU4: {'max': 25}}, 'The Bretons (p.71). Characters up to 25%; Milites and Pueri at least 50%; Coloni and Dogs of War (Vikings, Stipendarii, Serjeants) up to 25%. Mounted Milites cost 30 pts and have a BS of 4. Any character or unit of mounted Milites that chooses to flee or fire & flee as a charge reaction rallies automatically at the end of its move and may reform facing in any direction; if the charging enemy encounters them they are not destroyed and may instead fight in the close combat phase (their opponents still count as charging). All mounted troops count as Light Cavalry. All Liberi may exchange their thrusting spears for throwing spears and count as Light Infantry.'),
 (VAR['FR']['Capetian French'], {'Characters': {'max': 33}, 'Milites': {'min': 50}, FU2: {'max': 25}}, 'Capetian French (& Late Carolingian French) (p.71). Characters up to 33%; Milites at least 50%; Pueri, Coloni and Dogs of War (Stipendarii, Serjeants, Cottereaux) up to 25%. Mounted Milites cost 29 pts each and have Ferocious Charge. At the beginning of each turn roll a dice for each character: on a 1 the character and any unit he is with must try to charge the closest enemy; if no enemy is within range they must move as far as possible directly towards the nearest enemy.'),
]
FR_NOTES = ('WESTERN FRANKS ARMY LISTS (Shieldwall, pp.66-76): Carolingian French, the County of Flanders, the Duchy of Normandy, the Bretons and Capetian French. Percentages are by points. Special rules p.72 (Ferocious Charge).\n'
  'The Common/Uncommon pools differ between the compositions, so the units also belong to pool categories named after them. In the Carolingian French and Capetian lists the Common Warriors are the Milites alone.')
LISTS.append(('FR', 'Western Franks (Shieldwall)', 'Western_Franks_Shieldwall.cat', FR, FR_V, FR_NOTES))
ALLFR = ['Carolingian French', 'County of Flanders', 'Duchy of Normandy', 'The Bretons', 'Capetian French']
for u in FR:
    if u['cat'] == 'Uncommon Warriors' and u['name'].endswith('(Dogs of War)'): u['cat'] = 'Dogs of War'
AVAIL += [('FR', 'Vikings (Dogs of War)', ['Carolingian French', 'County of Flanders', 'Duchy of Normandy', 'The Bretons']), ('FR', 'Gestir (Dogs of War)', ['Carolingian French']),
          ('FR', 'Stipendarii (dismounted) (Dogs of War)', ALLFR), ('FR', 'Stipendarii (mounted) (Dogs of War)', ALLFR), ('FR', 'Serjeants (Dogs of War)', ALLFR),
          ('FR', 'Devroet (Dogs of War)', ['Carolingian French', 'Duchy of Normandy']), ('FR', 'Freebooters (Dogs of War)', ['County of Flanders']), ('FR', 'Cottereaux (Dogs of War)', ['Capetian French'])]
COSTV += [('FR', 'Dismounted Milites', {'County of Flanders': 15}), ('FR', 'Mounted Milites', {'Duchy of Normandy': 30, 'The Bretons': 30, 'Capetian French': 29}), ('FR', 'Liberi', {'County of Flanders': 7})]
STATV += [('FR', 'Mounted Milites', 'BS', {'The Bretons': 4})]
OPTSTAT += [('FR', 'Liberi', 'Men of the Marches (Leadership 7)', 'Ld', 7)]
OPTAV += [('FR', 'Dismounted Milites', 'Bow', ['Carolingian French']), ('FR', 'Mounted Milites', 'Bow', ['Carolingian French']), ('FR', 'Mounted Milites', 'Exchange throwing spear for lance', ['Duchy of Normandy']),
          ('FR', 'Dismounted Milites', 'Shieldwall', ['County of Flanders']), ('FR', 'Rex/Dux', 'Lance (Normandy; mounted)', ['Duchy of Normandy']), ('FR', 'Comes', 'Lance (Normandy; mounted)', ['Duchy of Normandy']),
          ('FR', 'Pueri', 'Exchange javelin and shield for bow', ['Carolingian French']),
          ('FR', 'Liberi', 'Men of the Marches (Leadership 7)', ['Carolingian French']), ('FR', 'Liberi', 'Light armour', ['County of Flanders']), ('FR', 'Liberi', 'Shieldwall', ['County of Flanders']),
          ('FR', 'Liberi', 'Exchange thrusting spear for throwing spear', ['The Bretons'])]
OPTRULE += [('FR', 'Dismounted Milites', 'Shieldwall', 'Shieldwall'), ('FR', 'Liberi', 'Shieldwall', 'Shieldwall'), ('FR', 'Liberi', 'Light infantry (free)', 'Light Troops')]
OPT_ONCE += [('FR', [('Comes', 'Army Battle Standard (replaces shield)')])]
PAIRS += []
SECOND.update({('FR', 'Dismounted Milites'): [FC_ML, FC_MP], ('FR', 'Mounted Milites'): [FC_ML, FC_MP], ('FR', 'Pueri'): [FC_MP, FU1, FU2], ('FR', 'Liberi'): [FC_ML, FU1, FU3], ('FR', 'Coloni'): [FU1, FU2, FU3, FU4]})
for u in FR:
    if u['cat'] == 'Dogs of War': SECOND[('FR', u['name'])] = [FU1, FU2, FU3, FU4]
