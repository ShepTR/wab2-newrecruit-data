# Armies of Chivalry (Warhammer Historical, 2004): medieval army lists. Book page = printed page number (pdf page - 2).
# Stat order: M WS BS S T W I A Ld.  Mounted and dismounted troops are separate unit entries (both count as Cavalry).
import copy
from rb_data import M, U
LISTS = []; VAR = {}; AVAIL = []; UNAV = []; OPTAV = []; OPTRULE = []; OPTSTAT = []; RATIOS = []; OPT_ONCE = []; PAIRS = []
SECOND = {}; UNIT_MAX_IN = []; GEN = {}; COND_CHARS = []; COSTV = []; STATV = []; HIRDMEN_LE_BONDIR = []; EXCL = []
CH, CAV, INF, ARC, SKI = 'Characters', 'Cavalry', 'Infantry', 'Archers', 'Skirmishers'

def variants(key, comps):
    """comps: {short: (limits {cat: {'min'|'max': pct}}, text)}  -> list of (variant name, limits, text)"""
    VAR[key] = {}; out = []
    for c, (lim, txt) in comps.items():
        VAR[key][c] = f'Armies of Chivalry: {key_title(key)}' if len(comps) == 1 else f'Armies of Chivalry: {key_title(key)} - {c}'
        out.append((VAR[key][c], lim, txt))
    return out
TITLES = {}
def key_title(k): return TITLES[k]
def single(key, title, lim, txt):
    TITLES[key] = title
    return variants(key, {title: (lim, txt)})
def multi(key, title, comps):
    TITLES[key] = title
    return variants(key, comps)
def pc(**kw):
    out = {}
    for k, v in kw.items():
        cat = k.replace('_', ' ')
        out[cat] = {'min': v[0], 'max': v[1]} if isinstance(v, tuple) and v[0] and v[1] < 100 else ({'min': v[0]} if isinstance(v, tuple) and v[0] else {'max': v[1] if isinstance(v, tuple) else v})
    return out
def L(**kw): return pc(**kw)

HEAVY = 'Heavy armour (replaces light armour)'
def plates(full=True, dis_pp=2, dis_fp=4):
    o = [('Partial plate armour, if mounted (replaces heavy armour)', 0), (f'Partial plate armour, if dismounted (replaces heavy armour)', dis_pp)]
    if full: o += [('Full plate armour, if mounted (replaces heavy armour)', 0), ('Full plate armour, if dismounted (replaces heavy armour)', dis_fp)]
    return o
def lord_opts(full=True, horse=True, warhorse_only=False):
    o = plates(full)
    o += [('Lance', 4)]
    o += ([('Ride a warhorse', 0)] if warhorse_only else [('Ride a horse', 0), ('Ride a warhorse', 4)])
    o += [('Cloth barding (-1 M)', 4), ('Halberd', 3), ('Double-handed weapon', 3)]
    return o
LORD_NOTE_P = ('Hand weapon, heavy armour and shield. May wear partial plate (mounted free, dismounted +2 pts)%s. May have a lance (+4 pts) if mounted. %s The warhorse can have cloth barding (+4 pts). May have a halberd (+3 pts) or a double-handed weapon (+3 pts) if on foot (not tied to being dismounted).')
def general(pts, st, full=True, warhorse_only=False, extra='', stubborn=False, name='Army General'):
    return U(CH, name, [M(name, st, pts, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General'] + (['Stubborn (if dismounted)'] if stubborn else []), options=lord_opts(full, True, warhorse_only))],
        (LORD_NOTE_P % (' or full plate armour (mounted free, dismounted +4 pts)' if full else '', 'Must have a warhorse (free) if mounted.' if warhorse_only else 'May have a horse (free) or warhorse (+4 pts).')) + ' Army General. 0-1.' + extra, mx=1, page='AoC')
def noble(pts, st, full=True, warhorse_only=False, extra='', stubborn=False, mx=None):
    return U(CH, 'Nobles', [M('Noble', st, pts, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=(['Stubborn (if dismounted)'] if stubborn else []), options=lord_opts(full, True, warhorse_only) + [('Army Standard Bearer (hand weapon only)', 15)])],
        (LORD_NOTE_P % (' or full plate armour (mounted free, dismounted +4 pts)' if full else '', 'Must have a warhorse (free) if mounted.' if warhorse_only else 'May have a horse (free) or warhorse (+4 pts).')) + ' One Noble may be the Army Standard Bearer (+15 pts) and may only be armed with a hand weapon (not enforced).' + extra, mx=mx, page='AoC')
def artillery(page, master=False, units_note=''):
    return U(INF, 'Light Artillery', [M('Light Artillery', '- - - 6 5 3 - - -', 50, key='gun', rules=['Artillery (Chivalry)']),
        M('Crew', '4 2 3 3 3 1 2 1 6', 0, mn=3, mx=3, key='crew', weapons=['Hand Weapon', 'Light Armour'], options=[('Heavy armour (replaces light armour)', 2)]),
        M('Additional Crew', '4 2 3 3 3 1 2 1 6', 10, mn=0, mx=2, key='crew2', weapons=['Hand Weapon', 'Light Armour'])],
        'Each gun has a crew of three; two additional crew may be added (+10 pts each). Crewmen have hand weapon and light armour and may upgrade to heavy armour (+2 pts). Light artillery range 36", Strength 6. Artillery: up to one gun for every 1,000 army points (bought from the Infantry allocation).' + (' One model per gun may be upgraded to Master Gunner.' if master else '') + units_note, page=page)
def poor_archers(page): pass
ENG = []; SCOT = []; FRE = []
# ====================================================================== ENGLISH (book pp.14-15)
E = ENG
E.append(general(160, '4 5 4 4 3 3 5 3 9'))
E.append(noble(70, '4 4 3 4 3 2 5 2 8'))
E.append(U(CH, 'Bishop (Religious Leader)', [M('Religious Leader', '4 4 1 3 4 2 5 1 9', 70, weapons=['Hand Weapon'], rules=['Bishop (Chivalry)'], options=[('Light armour', 2), ('Shield', 2), ('Ride a horse', 0)])],
    'Hand weapon (mace or club). May have light armour (+2 pts) and shield (+2 pts). May ride a horse (free). Bishop: Knights, Men-at-Arms or a Combined Formation of Knights and Men-at-Arms led by a Bishop are Stubborn; Archers or Infantry led by a Bishop may re-roll failed Panic tests. 0-1.', mx=1, page='15'))
KN_P = ' Mounted Knights are subject to First Charge, +1 rank bonus when mounted. Combined Formation; Knights may be combined with Men-at-Arms.'
E.append(U(CAV, 'Knights (Mounted)', [M('Mounted Knight', '8 4 3 3 3 1 4 1 8', 32, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['First Charge (Chivalry)', 'Combined Formation (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Lance', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May wear partial plate armour (free). Mounted Knights may have a lance (+4 pts) and warhorse (free) that can have cloth barding (+4 pts).' + KN_P, page='15'))
E.append(U(CAV, 'Knights (Dismounted)', [M('Dismounted Knight', '4 4 3 3 3 1 4 1 8', 18, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Combined Formation (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 2), ('Halberd', 3), ('Double-handed weapon', 3), ('Thrusting spear (shortened lance)', 3)])],
    'Hand weapon, heavy armour and shield. May wear partial plate armour (+2 pts). Dismounted Knights may have a halberd (+3 pts), double-handed weapon (+3 pts) or a shortened lance that counts as a thrusting spear (+3 pts). Combined Formation; Knights may be combined with Men-at-Arms. The Herce applies.', page='15'))
E.append(U(CAV, 'Men-at-Arms (Mounted)', [M('Mounted Man-at-Arms', '8 4 3 3 3 1 3 1 7', 24, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Horse'], rules=['Combined Formation (Chivalry)'],
    options=[('Heavy armour (replaces light armour)', 0), ('Lance', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, light armour and shield. May wear heavy armour (free). Mounted Men-at-Arms may have a lance (+4 pts) and horse (free) that can have cloth barding (+4 pts). Combined Formation; Men-at-Arms may be combined with Knights.', page='15'))
E.append(U(CAV, 'Men-at-Arms (Dismounted)', [M('Dismounted Man-at-Arms', '4 4 3 3 3 1 3 1 7', 12, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Combined Formation (Chivalry)'],
    options=[('Heavy armour (replaces light armour)', 2), ('Halberd', 2), ('Double-handed weapon', 2), ('Thrusting spear (shortened lance)', 2)])],
    'Hand weapon, light armour and shield. May wear heavy armour (+2 pts). Dismounted Men-at-Arms may have a halberd (+2 pts), double-handed weapon (+2 pts) or a shortened lance that counts as a thrusting spear (+2 pts). Combined Formation; Men-at-Arms may be combined with Knights.', page='15'))
E.append(U(CAV, 'Hobilars', [M('Hobilar', '8 3 3 3 3 1 3 1 6', 17, mn=5, weapons=['Hand Weapon', 'Shield', 'Thrusting Spear', 'Horse'], rules=['Open Order'], options=[('Light armour', 2)])],
    'Hand weapon, shield, thrusting spear and horse. May have light armour (+2 pts). Open Order. 0-2 units.', mx=2, page='15'))
E.append(U(ARC, 'Veteran Longbowmen', [M('Veteran Longbowman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Long Bow', 'Hand Weapon'], rules=['Open Order', 'Stakes', 'Veteran'], options=[('Light armour', 2), ('Stakes (+20 pts per unit)', 0)])],
    'Longbow and hand weapon. Stakes (+20 pts per unit). May have light armour (+2 pts). Open Order, Stakes, Veteran.', page='15'))
E.append(U(ARC, 'Trained Archers', [M('Trained Archer', '4 2 3 3 3 1 3 1 7', 8, mn=5, weapons=['Long Bow', 'Hand Weapon'], rules=['Open Order'], options=[('Light armour', 2), ('Stakes (+20 pts per unit)', 0), ('Mounted Infantry (no stakes)', 0)])],
    'Longbow and hand weapon. Stakes (+20 pts per unit). May have light armour (+2 pts). Open Order, Stakes. 0-1 unit of Trained Archers may be designated Mounted Infantry, but cannot take stakes as an equipment option.', page='15'))
E.append(U(ARC, 'Poor Archers', [M('Poor Archer', '4 2 2 3 3 1 3 1 6', 6, mn=5, weapons=['Long Bow', 'Hand Weapon'], rules=['Open Order'], options=[('Light armour', 2), ('Stakes (+20 pts per unit)', 0)])],
    'Longbow and hand weapon. Stakes (+20 pts per unit). May have light armour (+2 pts). Open Order, Stakes. Not allowed in the Continental army; the Home army must have at least one unit of Poor Archers (not enforced).', page='15'))
E.append(U(INF, 'Spearmen / Billmen', [M('Spearman/Billman', '4 3 2 3 3 1 3 1 6', 7, mn=5, weapons=['Thrusting Spear', 'Hand Weapon', 'Shield'], options=[('Light armour', 2), (HEAVY, 1)])],
    'Thrusting spear or bill (counts as halberd; both entered as the thrusting spear), hand weapon and shield. May have light armour (+2 pts) or heavy armour (+3 pts).', page='15'))
E.append(U(INF, 'Peasants', [M('Peasant', '4 1 2 3 3 1 2 1 4', 3, mn=5, weapons=['Improvised Weapon'], rules=['Open Order', 'Warband Psychology (rule 1)', 'Peasants (Chivalry)'])],
    'Improvised weapons. Open Order. Warband Rule 1. Peasants fear all formed enemy cavalry and infantry except other peasants. Peasant units may not include a Standard or Musician. Not allowed in the Continental army.', page='15'))
E.append(U(INF, 'Mercenary Handgunners', [M('Handgunner', '4 2 2 3 3 1 3 1 6', 10, mn=5, weapons=['Handgun', 'Hand Weapon', 'Light Armour'], rules=['Skirmishers (Chivalry)', 'Allies and Mercenaries (Chivalry)'])],
    'Handgun, hand weapon and light armour. Skirmishers. Allies & Mercenaries. 0-1 unit. Not allowed in the Home army.', mx=1, page='15'))
E.append(artillery('15'))
ENG_V = multi('ENG', 'English Hundred Years War', {
 'Continental': (L(Characters=25, Cavalry=35, Archers=(25, 50), Infantry=35),
   'Continental Army (Crecy 1346, Agincourt 1415). Characters 0-25%, Cavalry 0-35%, Archers 25-50% (cannot have Poor Archers), Infantry 0-35% (cannot have Peasants). Artillery: up to 1 light artillery per 1,000 army points, bought from the Infantry allocation. Mercenaries: 0-20% from the Free Companies list (no characters or Artillery); all are subject to the Allies and Mercenaries rule (documented only).'),
 'Home': (L(Characters=25, Cavalry=30, Archers=(20, 40), Infantry=40),
   'Home Army (Shrewsbury 1403 and other battles in Britain). Characters 0-25%, Cavalry 0-30%, Archers 20-40% (must have 1+ unit of Poor Archers), Infantry 0-40% (cannot have Mercenary Handgunners). Artillery: up to 1 light artillery per 1,000 army points, bought from the Infantry allocation.')})
ENG_NOTES = 'HUNDRED YEARS WAR ENGLISH 1337-1453 (Armies of Chivalry, pp.14-15). Special rule The Herce: units of Archers within 4" of a unit or combined unit of Dismounted Knights or Dismounted Men-at-Arms may stand & fire at chargers without the -1 penalty.'
LISTS.append(('ENG', 'English Hundred Years War (Armies of Chivalry)', 'English_HYW_Chivalry.cat', ENG, ENG_V, ENG_NOTES))
UNAV += [('ENG', 'Poor Archers', ['Continental']), ('ENG', 'Peasants', ['Continental']), ('ENG', 'Mercenary Handgunners', ['Home'])]
OPT_ONCE += [('ENG', [('Nobles', 'Army Standard Bearer (hand weapon only)')])]
OPTRULE += [('ENG', 'Nobles', 'Army Standard Bearer (hand weapon only)', 'Army Standard'), ('ENG', 'Veteran Longbowmen', 'Stakes (+20 pts per unit)', 'Stakes')]
RATIOS += [('ENG', 'Light Artillery', [], 1000)] if False else []
FLAT = []   # (key, unit, option label, flat points once per unit)
FLAT += [('ENG', u, 'Stakes (+20 pts per unit)', 20) for u in ('Veteran Longbowmen', 'Trained Archers', 'Poor Archers')]
# ====================================================================== SCOTLAND & THE BORDERS (book pp.16-17)
S = SCOT
S.append(general(160, '4 5 4 4 3 3 5 3 9', full=False, stubborn=True, extra=' Stubborn if dismounted.'))
S.append(noble(70, '4 4 3 4 3 2 5 2 8', full=False, stubborn=True, extra=' Stubborn if dismounted.'))
S.append(U(CAV, 'Knights (Mounted)', [M('Mounted Knight', '8 4 3 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Impetuous', 'First Charge (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Lance', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May upgrade to partial plate armour (free if mounted). May have a lance (+4 pts) and must have a warhorse (free). Warhorse may have cloth barding (+4 pts). Mounted Knights are Impetuous and have First Charge. 0-1 unit.', mx=1, page='16'))
S.append(U(CAV, 'Knights (Dismounted)', [M('Dismounted Knight', '4 4 3 3 3 1 4 1 8', 16, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Stubborn', 'Different Weapons'],
    options=[('Partial plate armour (replaces heavy armour)', 2), ('Halberd', 3), ('Double-handed weapon', 3)])],
    'Hand weapon, heavy armour and shield. May upgrade to partial plate armour (+2 pts if dismounted). May have a halberd (+3 pts) or a double-handed weapon (+3 pts) if dismounted. Dismounted Knights are Stubborn and can have Different Weapons. 0-1 unit.', mx=1, page='16'))
S.append(U(CAV, 'Borders Cavalry', [M('Borders Cavalryman', '8 3 3 3 3 1 3 1 7', 17, mn=5, weapons=['Thrusting Spear', 'Hand Weapon', 'Shield', 'Horse'], rules=['Open Order'], options=[('Exchange thrusting spear for throwing spear', 0), ('Light armour', 2)])],
    'Thrusting spear or throwing spear, hand weapon and shield. May have light armour (+2 pts). Open Order.', page='16'))
S.append(U(INF, 'Spearmen', [M('Spearman', '4 3 2 3 3 1 3 1 6', 7, mn=5, weapons=['Thrusting Spear', 'Hand Weapon', 'Shield'], rules=['Medieval Phalanx'], options=[('Exchange thrusting spear for pike', 1), ('Light armour', 2)])],
    'Thrusting spear, hand weapon and shield. May exchange thrusting spear for a pike (+1 pt). 0-2 units may have light armour (+2 pts). Medieval Phalanx. All units of Spearmen in the army must be armed with the same weapon (either thrusting spear or pike).', page='16'))
S.append(U(INF, 'Highlanders', [M('Highlander', '5 3 2 3 3 1 3 1 5', 7, mn=5, weapons=['Hand Weapon', 'Buckler'], rules=['Warband', 'Different Weapons'], options=[('Exchange buckler for shield', 1), ('Double-handed weapon', 2), ('Additional hand weapon', 2)])],
    'Hand weapon and buckler. May upgrade buckler to shield (+1 pt). May have double-handed weapons (+2 pts) or additional hand weapon (+2 pts). Warband. Different Weapons.', page='16'))
S.append(U(INF, 'Camp Followers', [M('Camp Follower', '4 1 1 2 3 1 2 1 4', 3, mn=5, weapons=['Improvised Weapon'], rules=['Open Order', 'Warband Psychology (rule 1)', 'Peasants (Chivalry)'])],
    'Improvised weapons. Open Order, Warband Rule 1, fear all formed enemy cavalry and infantry. May not include a Standard or Musician. Casualties from artillery cause a Panic test.', page='16'))
S.append(U(ARC, 'Archers', [M('Archer', '4 2 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Open Order'])],
    'Hand weapon and short bow. May be Open Order or Skirmishers (entered as Open Order).', page='16'))
SCOT_V = single('SCOT', 'Scotland & the Borders', L(Characters=20, Cavalry=25, Infantry=100, Archers=10),
   'Characters 0-20%, Cavalry 0-25%, Infantry 0-100%, Archers 0-10%.')
LISTS.append(('SCOT', 'Scotland & the Borders (Armies of Chivalry)', 'Scotland_Borders_Chivalry.cat', SCOT, SCOT_V, 'SCOTLAND & THE BORDERS c.1250-1513 (Armies of Chivalry, pp.16-17). One Noble may be the Army Standard Bearer (+15 pts), hand weapon only.'))
OPT_ONCE += [('SCOT', [('Nobles', 'Army Standard Bearer (hand weapon only)')])]
OPTRULE += [('SCOT', 'Nobles', 'Army Standard Bearer (hand weapon only)', 'Army Standard')]
# ====================================================================== FRENCH HUNDRED YEARS WAR (book pp.32-33)
F = FRE
F.append(general(160, '4 6 4 4 3 3 6 2 9', warhorse_only=True))
F.append(noble(70, '4 5 3 4 3 2 5 2 8', warhorse_only=True))
F[-1]['models'][0]['options'].append(('Oriflamme (Army Standard, King-led army only)', 50))
FKN = ' Mounted Knights are subject to Impetuous, First Charge, Arrogant Pride, and may count a rank bonus of up to +1 in combat. Combined Formation; may be combined with Esquires.'
F.append(U(CAV, 'Knights (Mounted)', [M('Mounted Knight', '8 5 3 3 3 1 4 1 8', 31, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Impetuous', 'First Charge (Chivalry)', 'Arrogant Pride', 'Combined Formation (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Lance', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May have a lance (+4 pts) and must have a warhorse (free). May wear partial plate (free) or full plate armour (free if mounted). Warhorse may have cloth barding (+4 pts).' + FKN, page='32'))
F.append(U(CAV, 'Knights (Dismounted)', [M('Dismounted Knight', '4 4 3 3 3 1 4 1 8', 16, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Combined Formation (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 2), ('Full plate armour (replaces heavy armour)', 4), ('Halberd', 3), ('Double-handed weapon', 3)])],
    'Hand weapon, heavy armour and shield. May have a halberd (+3 pts) or a double-handed weapon (+3 pts). May wear partial plate (+2 pts) or full plate armour (+4 pts). Combined Formation; may be combined with Esquires.', page='32'))
F.append(U(CAV, 'Esquires (Mounted)', [M('Mounted Esquire', '8 4 3 3 3 1 3 1 8', 27, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Warhorse'], rules=['Impetuous', 'Arrogant Pride', 'Combined Formation (Chivalry)'],
    options=[('Heavy armour (replaces light armour)', 2), ('Thrusting spear', 2), ('Lance', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, light armour and shield. May upgrade to heavy armour (+2 pts). May have thrusting spear (+2 pts) or a lance (+4 pts) and must have a warhorse (free). Warhorse may have cloth barding (+4 pts). Combined Formation; may be combined with Knights. Mounted Esquires are subject to Impetuous and Arrogant Pride.', page='33'))
F.append(U(CAV, 'Esquires (Dismounted)', [M('Dismounted Esquire', '4 3 3 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Combined Formation (Chivalry)'], options=[('Heavy armour (replaces light armour)', 2)])],
    'Hand weapon, light armour and shield. May upgrade to heavy armour (+2 pts). Combined Formation; may be combined with Knights.', page='33'))
F.append(U(CAV, 'Sergeants', [M('Sergeant', '8 3 3 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Horse'], rules=['Open Order'], options=[('Light armour', 2), ('Shield', 2), ('Thrusting spear', 2), ('Bow', 2)])],
    'Hand weapon and horse. May have light armour (+2 pts), shield (+2 pts), thrusting spear (+2 pts) and bow (+2 pts). Open Order.', page='33'))
F.append(U(INF, 'Genoese Crossbowmen', [M('Genoese', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], rules=['Combined Formation (Chivalry)'], options=[('Heavy armour (replaces light armour)', 3), ('Pavise', 1)])],
    'Crossbow, hand weapon and light armour. May upgrade to heavy armour (+3 pts). May have a pavise (+1 pt) if not combined with Pavisiers. Combined Formation; may be included in a unit of Pavisiers in which the Pavisiers form the front rank and the Crossbowmen the subsequent ranks. 0-1 unit.', mx=1, page='33'))
F.append(U(INF, 'Crossbowmen', [M('Crossbowman', '4 2 2 3 3 1 3 1 6', 7, mn=5, weapons=['Crossbow', 'Hand Weapon'], rules=['Combined Formation (Chivalry)'], options=[('Light armour', 1), ('Pavise', 1)])],
    'Crossbow and hand weapon. May upgrade to light armour (+1 pt). May have a pavise (+1 pt) if not combined with Pavisiers. Combined Formation; may be included in a unit of Pavisiers in which the Pavisiers form the front rank and the Crossbowmen the subsequent ranks.', page='33'))
F.append(U(INF, 'Pavisiers', [M('Pavisier', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Thrusting Spear', 'Pavise', 'Light Armour'], rules=['Combined Formation (Chivalry)'])],
    'Thrusting spear, pavise and light armour. Combined Formation; Pavisiers (not Voulgiers) may be included in a unit of Crossbowmen in which the Pavisiers form the front rank and the Crossbowmen the subsequent ranks. Pavisiers and Voulgiers cannot be used in the same army (not enforced).', page='33'))
F.append(U(INF, 'Voulgiers', [M('Voulgier', '4 3 3 3 3 1 3 1 7', 12, mn=5, weapons=['Thrusting Spear', 'Heavy Armour', 'Shield'], options=[('Exchange thrusting spear for halberd', 1)])],
    'An upgrade of Pavisiers (+3 pts): heavy armour and shield replace the pavise and light armour. Thrusting spear, may exchange for halberd (+1 pt). Pavisiers and Voulgiers cannot be used in the same army (not enforced).', page='33'))
F.append(U(ARC, 'Archers', [M('Archer', '4 2 2 3 3 1 3 1 5', 4, mn=5, weapons=['Short Bow', 'Hand Weapon'], rules=['Open Order', 'Stakes'], options=[('Light armour', 2), ('Buckler', 1), ('Stakes (+20 pts per unit)', 0)])],
    'Short bow and hand weapon. May have light armour (+2 pts), buckler (+1 pt) and stakes (+20 pts per unit). Open Order, Stakes.', page='33'))
F.append(U(INF, 'Handgunners', [M('Handgunner', '4 3 2 3 3 1 3 1 6', 10, mn=5, weapons=['Hand Weapon', 'Handgun', 'Light Armour'], rules=['Skirmishers (Chivalry)'])],
    'Hand weapon, handgun and light armour. Skirmishers. 0-1 unit.', mx=1, page='33'))
F.append(U(INF, 'Brigans', [M('Brigan', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Open Order'], options=[('Light armour', 2), ('Buckler', 1)])],
    'Hand weapon and thrusting spear. May have light armour (+2 pts) and buckler (+1 pt). Open Order.', page='33'))
F.append(U(INF, 'Peasants', [M('Peasant', '4 1 2 3 3 1 2 1 4', 3, mn=5, weapons=['Improvised Weapon'], rules=['Peasants (Chivalry)'])],
    'Improvised weapons. Peasants fear all formed enemy cavalry and infantry except other peasants. Peasant units may not include a Standard or Musician.', page='33'))
F.append(artillery('33'))
FRE_V = single('FRE', 'French Hundred Years War', L(Characters=25, Cavalry=(25, 75), Infantry=(25, 75)),
   'Characters 0-25%, Cavalry 25-75%, Infantry 25-75%. Artillery: 0-1 guns per 1,000 army points, bought from the Infantry allocation. Allies: 0-25% from the Scotland and the Borders list (documented only).')
FRE_NOTES = ('HUNDRED YEARS WAR FRENCH 1337-1445 (Armies of Chivalry, pp.32-33). Keeper of the Oriflamme: if French armies are led by the King himself, the Oriflamme (Gold Flame) may be carried as the army battle standard (+50 pts). It may only be accompanied by a unit of Knights or a Combined Formation of Knights and Esquires; that unit is immune to panic. If the unit surrenders the Oriflamme to a victorious opponent it is worth 250 Victory points; its powers are lost when the Battle Standard Bearer is killed. '
    'Arrogant Pride: if a unit containing French Knights and/or Esquires charges an enemy unit, any unit containing mounted French Knights and/or Esquires within 12" of the charging unit must charge its nearest enemy (or, if none is in charge distance, move at least 4" towards the nearest enemy within its charge arc).')
LISTS.append(('FRE', 'French Hundred Years War (Armies of Chivalry)', 'French_HYW_Chivalry.cat', FRE, FRE_V, FRE_NOTES))
OPT_ONCE += [('FRE', [('Nobles', 'Army Standard Bearer (hand weapon only)')])]
OPTRULE += [('FRE', 'Nobles', 'Army Standard Bearer (hand weapon only)', 'Army Standard'), ('FRE', 'Nobles', 'Oriflamme (Army Standard, King-led army only)', 'Keeper of the Oriflamme')]
FLAT += [('FRE', 'Archers', 'Stakes (+20 pts per unit)', 20)]
OPTRULE += [('FRE', 'Archers', 'Stakes (+20 pts per unit)', 'Stakes')]
GEN_LABEL = 'Army General (if no other Army General)'
# ====================================================================== FREE COMPANIES (book pp.34)
FC = []
FOPT = lambda full=False: [('Partial plate armour (replaces heavy armour)', 2), ('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4), ('Halberd', 4), ('Double-handed weapon', 4)]
FC.append(U(CH, 'Commander', [M('Commander', '4 6 3 4 3 3 6 2 9', 160, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General', 'Stubborn (if dismounted)'], options=FOPT())],
    'Hand weapon, heavy armour and shield. May have a halberd (+4 pts) or double-handed weapon (+4 pts) if dismounted. May wear partial plate (+2 pts). May have a lance (+4 pts), and must have a horse (free) or warhorse (+4 pts) if mounted. Warhorse may have cloth barding (+4 pts). Army General. Stubborn if dismounted. 0-1.', mx=1, page='34'))
FC.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 4 3 2 5 2 8', 100, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army Standard', 'Stubborn (if dismounted)'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May wear partial plate armour (+2 pts). Must have a horse (free) or warhorse (+4 pts) if mounted. Warhorse may have cloth barding (+4 pts). Army Standard Bearer. Stubborn if dismounted. 0-1.', mx=1, page='34'))
FC.append(U(CH, 'Captain', [M('Captain', '4 5 3 4 3 2 5 2 8', 75, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Stubborn (if dismounted)'], options=FOPT() + [(GEN_LABEL, 25)])],
    'Hand weapon, heavy armour and shield. May have a halberd (+4 pts) or double-handed weapon (+4 pts) if dismounted. May wear partial plate armour (+2 pts). May have a lance (+4 pts), and must have a horse (free) or warhorse (+4 pts) if mounted. Warhorse may have cloth barding (+4 pts). If no other Army General is taken, a Captain may be made Army General for +25 pts. Stubborn if dismounted.', page='34'))
FC.append(U(CAV, 'Superior Men-at-Arms (Mounted)', [M('Mounted Superior Man-at-Arms', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May wear partial plate armour (+2 pts). Lance and warhorse. First Charge. May count a Rank Bonus of up to +1 in combat. (The unit may add cloth barding +4 pts, not printed for this entry.)', page='34'))
FC.append(U(CAV, 'Superior Men-at-Arms (Dismounted)', [M('Dismounted Superior Man-at-Arms', '4 4 3 3 3 1 4 1 8', 15, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Stubborn'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Thrusting spear (cut-down lance)', 1), ('Halberd', 2), ('Double-handed weapon', 2)])],
    'Hand weapon, heavy armour and shield. May wear partial plate armour (+2 pts). May have thrusting spear (a cut-down lance, +1 pt), a halberd (+2 pts), or a double-handed weapon (+2 pts). Stubborn.', page='34'))
FC.append(U(CAV, 'Lesser Men-at-Arms (Mounted)', [M('Mounted Lesser Man-at-Arms', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Lance', 'Horse'], options=[('Heavy armour (replaces light armour)', 1)])],
    'Hand weapon, light armour and shield. Lance and horse when mounted. May wear heavy armour (+1 pt). May count a Rank Bonus of up to +1 in combat.', page='34'))
FC.append(U(CAV, 'Lesser Men-at-Arms (Dismounted)', [M('Dismounted Lesser Man-at-Arms', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], options=[('Heavy armour (replaces light armour)', 1), ('Thrusting spear', 1), ('Halberd', 2), ('Double-handed weapon', 2)])],
    'Hand weapon, light armour and shield. May wear heavy armour (+1 pt). May have a thrusting spear (+1 pt), a halberd (+2 pts), or a double-handed weapon (+2 pts).', page='34'))
FC.append(U(CAV, 'Sergeants', [M('Sergeant', '8 3 3 3 3 1 3 1 6', 14, mn=5, weapons=['Hand Weapon', 'Horse'], rules=['Open Order'], options=[('Light armour', 3), ('Thrusting spear and shield', 3), ('Light crossbow', 3)])],
    'Hand weapon and horse. May wear light armour (+3 pts). May carry a thrusting spear and shield (+3 pts) or light crossbow (+3 pts). Open Order.', page='34'))
FC.append(U(INF, 'Longbowmen', [M('Longbowman', '4 3 3 3 3 1 4 1 7', 11, mn=5, weapons=['Long Bow', 'Light Armour', 'Hand Weapon'], rules=['Stakes', 'Open Order'], options=[('Buckler', 1), ('Maul (+1 S, strikes last)', 1), ('Stakes (+20 pts per unit)', 0)])],
    'Longbow, light armour and hand weapon. May carry a buckler (+1 pt). May have a maul (+1 pt, a clumsy double-handed mallet that swings last at +1 Strength). May have Stakes (+20 pts per unit). Stakes. May be Open Order (free).', page='34'))
FC.append(U(INF, 'Crossbowmen', [M('Crossbowman', '4 3 2 3 3 1 3 1 6', 7, mn=5, weapons=['Crossbow', 'Hand Weapon'], rules=['Open Order'], options=[('Light armour', 1), ('Pavise', 1), ('Upgrade to BS3 (one unit; +4 pts covers BS3 and Ld7)', 4), ('Upgrade to Ld7 (one unit; take with BS3)', 0)])],
    'Crossbow and hand weapon. May wear light armour (+1 pt), and may carry a pavise (+1 pt). One unit may upgrade to BS 3 and Ld 7 (+4 pts per model). May be Open Order (free).', page='34'))
FC.append(U(INF, 'Bidets', [M('Bidet', '5 3 3 3 3 1 4 1 6', 9, mn=5, weapons=['Throwing Spear', 'Javelin', 'Hand Weapon', 'Buckler'], rules=['Open Order', 'Feigned Flight'])],
    'Throwing spear, javelins, hand weapon and buckler. Open Order. Feigned Flight. One unit per 1,000 army points may give up throwing spears and become skirmishers (not enforced).', page='34'))
FC.append(U(INF, 'Brigans/Ribauds', [M('Brigan/Ribaud', '5 2 2 3 3 1 3 1 6', 4, mn=5, weapons=['Improvised Weapon'], rules=['Fear'], options=[('Light armour', 1), ('Hand weapon and buckler', 1), ('Thrusting spear', 1), ('Halberd', 2)])],
    'Improvised weapon (a dagger for slashing downed knights\' throats). May have light armour (+1 pt). May have hand weapon and buckler (+1 pt) or thrusting spear (+1 pt) or halberd (+2 pts). Fear formed cavalry units.', page='34'))
FC.append(artillery('34', units_note=' One gun allowed per 1,000 army points.'))
FC_V = single('FC', 'Free Companies', L(Characters=25, Cavalry=(25, 75), Infantry=50), 'Characters 0-25%, Cavalry 25-75%, Infantry 0-50%. Artillery: one gun allowed per 1,000 army points, bought from the Infantry allocation.')
LISTS.append(('FC', 'Free Companies (Armies of Chivalry)', 'Free_Companies_Chivalry.cat', FC, FC_V, 'FREE COMPANIES 1357-1444 (Armies of Chivalry, p.34). The same entries serve as Mercenaries (Allies and Mercenaries rule) for the English Continental and Condotta armies (documented only).'))
FLAT += [('FC', 'Longbowmen', 'Stakes (+20 pts per unit)', 20)]
OPTRULE += [('FC', 'Longbowmen', 'Stakes (+20 pts per unit)', 'Stakes'), ('FC', 'Captain', GEN_LABEL, 'Army General (Chariot Wars)')]
GEN['FC'] = (['Commander'], [('Captain', GEN_LABEL)])
OPT_ONCE += [('FC', [('Captain', GEN_LABEL)])]
OPTSTAT += [('FC', 'Crossbowmen', 'Upgrade to BS3 (one unit; +4 pts covers BS3 and Ld7)', 'BS', 3), ('FC', 'Crossbowmen', 'Upgrade to Ld7 (one unit; take with BS3)', 'Ld', 7)]
OPT_ONCE += [('FC', [('Crossbowmen', 'Upgrade to BS3 (one unit; +4 pts covers BS3 and Ld7)'), ('Crossbowmen', 'Upgrade to Ld7 (one unit; take with BS3)')])]
def multi_barrelled(page, note=''):
    return U(INF, 'Multi-barrelled Artillery', [M('Multi-barrelled Artillery', '- - - 4 5 2 - - -', 50, key='gun', rules=['Artillery (Chivalry)', 'Multi-barrelled Artillery (Chivalry)']),
        M('Crew', '4 2 3 3 3 1 2 1 6', 0, mn=3, mx=3, key='crew', weapons=['Hand Weapon', 'Light Armour'], options=[('Heavy armour (replaces light armour)', 2)]),
        M('Additional Crew', '4 2 3 3 3 1 2 1 6', 10, mn=0, mx=2, key='crew2', weapons=['Hand Weapon', 'Light Armour'])],
        'Each gun has a crew of three; two additional crew may be added (+10 pts each). Crewmen have hand weapon and light armour and may upgrade to heavy armour (+2 pts). Multi-barrelled artillery (ribauld/organ-gun): fires with a template at Strength 4, can stand & shoot when charged.' + note, page=page)
# ====================================================================== THE LOW COUNTRIES (book pp.38-39)
LC = []
LCO = lambda: [('Full plate armour, if mounted (replaces partial plate armour)', 0), ('Full plate armour, if dismounted (replaces partial plate armour)', 2), ('Ride a warhorse', 0), ('Lance', 0), ('Exchange double-handed weapon for pike', 2), ('Cloth barding (-1 M)', 4)]
LC.append(U(CH, 'Army General', [M('Army General', '4 4 3 3 3 3 5 3 9', 140, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Double-handed Weapon'], rules=['Army General'], options=LCO())],
    'Hand weapon, partial plate armour and shield. May be mounted with a lance and a warhorse. Armed with a double-handed weapon (free) or a pike (+2 pts) if on foot. May wear full plate armour (mounted free, dismounted +2 pts). The warhorse may have cloth barding (+4 pts). Army General. 0-1.', mx=1, page='38'))
LC.append(U(CH, 'Alderman', [M('Alderman', '4 3 3 3 3 2 4 2 8', 70, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Double-handed Weapon'], options=LCO() + [(GEN_LABEL, 25)])],
    'Hand weapon, partial plate armour and shield. May be mounted with a lance and a warhorse. Armed with a double-handed weapon or a pike (+2 pts) if on foot. May wear full plate armour (mounted free, dismounted +2 pts). The warhorse may have cloth barding (+4 pts). If no other Army General is taken, a single Alderman may be made Army General for +25 pts.', page='38'))
LC.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 3 3 3 3 2 4 2 8', 80, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army Standard'],
    options=[('Partial plate armour, if mounted (replaces heavy armour)', 0), ('Partial plate armour, if dismounted (replaces heavy armour)', 2), ('Full plate armour, if mounted (replaces heavy armour)', 0), ('Full plate armour, if dismounted (replaces heavy armour)', 4), ('Ride a warhorse', 0), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May wear partial plate (mounted free, dismounted +2 pts) or full plate armour (mounted free, dismounted +4 pts). Rides a warhorse (free) if mounted. The warhorse may have cloth barding (+4 pts). Army Battle Standard. 0-1.', mx=1, page='38'))
LC.append(U(CAV, 'Mercenary Knights (Mounted)', [M('Mounted Mercenary Knight', '8 4 3 3 3 1 4 1 8', 35, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Lance', 'Warhorse'], rules=['Impetuous', 'First Charge (Chivalry)', 'Combined Formation (Chivalry)'],
    options=[('Full plate armour (replaces partial plate armour)', 0), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, partial plate armour and shield. Armed with a lance and a warhorse. May wear full plate armour (free). The warhorse may have cloth barding (+4 pts). Impetuous, First Charge, Combined Formation (may include Sergeants). Mounted Mercenary Knights count a Rank Bonus of up to +1 if supported by Sergeants.', page='38'))
LC.append(U(CAV, 'Mercenary Knights (Dismounted)', [M('Dismounted Mercenary Knight', '4 4 3 3 3 1 4 1 8', 18, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Double-handed Weapon'], options=[('Full plate armour (replaces partial plate armour)', 2)])],
    'Hand weapon, partial plate armour and shield. Armed with a double-handed weapon. May wear full plate armour (+2 pts).', page='38'))
LC.append(U(CAV, 'Communal Knights (Mounted)', [M('Mounted Communal Knight', '8 3 3 3 3 1 3 1 7', 28, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Lance', 'Warhorse'], rules=['Impetuous', 'First Charge (Chivalry)'],
    options=[('Full plate armour (replaces partial plate armour)', 0), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, partial plate armour and shield. Armed with a lance and a warhorse. May wear full plate armour (free). The warhorse may have cloth barding (+4 pts). Impetuous and First Charge. Mounted Communal Knights count a Rank Bonus of up to +1 in combat.', page='38'))
LC.append(U(CAV, 'Communal Knights (Dismounted)', [M('Dismounted Communal Knight', '4 3 3 3 3 1 3 1 7', 14, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Double-handed Weapon'], options=[('Full plate armour (replaces partial plate armour)', 2), ('Exchange double-handed weapon for pike', 2)])],
    'Hand weapon, partial plate armour and shield. Armed with a double-handed weapon or a pike (+2 pts). May wear full plate armour (+2 pts).', page='38'))
LC.append(U(CAV, 'Sergeants', [M('Sergeant', '8 3 3 3 3 1 3 1 6', 17, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Horse'], rules=['Open Order', 'Combined Formation (Chivalry)'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear, shield and horse. May wear light armour (+2 pts). Open Order. Combined Formation; may be included in a unit of Mounted Mercenary Knights in which case they are no longer Open Order.', page='39'))
LC.append(U(INF, 'Communal Pikemen', [M('Communal Pikeman', '4 3 2 3 3 1 3 1 7', 10, mn=5, weapons=['Pike', 'Hand Weapon'], rules=['Medieval Phalanx', 'Stubborn'], options=[('Light armour', 1)])],
    'Pike and hand weapon. May have light armour (+1 pt). Medieval Phalanx. Stubborn. On the turn they charge, Pikemen receive up to a maximum of +2 rank bonus; up to +3 in subsequent rounds of combat or if charged.', page='39'))
LC.append(U(INF, 'Communal Plançonniers', [M('Plançonnier', '4 3 3 3 3 1 4 1 7', 10, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Plançon'])],
    'Plançon, hand weapon, light armour and shield. The plançon had a wooden or iron shaft broadening at the top where a socket and iron pike were fitted. Plançons confer a +1 Strength bonus on all hits.', page='39'))
LC.append(U(INF, 'Communal Crossbowmen', [M('Communal Crossbowman', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], rules=['Combined Formation (Chivalry)'])],
    'Crossbow, hand weapon and light armour. Combined Formation; may include Targedragers.', page='39'))
LC.append(U(INF, 'Communal Targedragers', [M('Targedrager', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Pavise'], rules=['Combined Formation (Chivalry)'])],
    'Hand weapon and a targe (pavise). Combined Formation; Targedragers may be included in a unit of Crossbowmen in which the Targedragers form the front ranks and the Crossbowmen the subsequent ranks.', page='39'))
LC.append(U(INF, 'Communal Archers', [M('Communal Archer', '5 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Short Bow', 'Hand Weapon'], rules=['Open Order'], options=[('Light armour', 1)])],
    'Shortbow and hand weapon. May have light armour (+1 pt). Open Order.', page='39'))
LC.append(U(INF, 'Whitehoods', [M('Whitehood', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon'], rules=['Open Order', 'Warband'], options=[('Shield', 1)])],
    'Mixed weapons. May have a shield (+1 pt). Open Order. Warband. 0-1 unit.', mx=1, page='39'))
LC.append(U(INF, 'Handgunners', [M('Handgunner', '5 3 3 3 3 1 3 1 6', 10, mn=5, weapons=['Handgun', 'Hand Weapon', 'Light Armour'], rules=['Skirmishers (Chivalry)'])],
    'Handgun, hand weapon and light armour. Skirmishers. 0-1 unit for every unit of Communal Pikemen; may not be larger than the smallest unit of Communal Pikemen (size not enforced).', page='39'))
LC.append(artillery('39', units_note=' Up to one gun for every 400 army points.'))
LC.append(multi_barrelled('39', ' Up to one gun for every 400 army points (light artillery and multi-barrelled together).'))
LC_V = single('LC', 'The Low Countries', L(Characters=25, Cavalry=25, Infantry=(50, 75)), 'Characters 0-25%, Cavalry 0-25%, Infantry 50-75% (special units are purchased from the Infantry allocation). Mercenaries: 0-1 unit of English Veteran Longbowmen or Trained Archers from the HYW English list (documented only).')
LISTS.append(('LC', 'The Low Countries (Armies of Chivalry)', 'Low_Countries_Chivalry.cat', LC, LC_V, 'THE LOW COUNTRIES early 14th to late 15th century (Armies of Chivalry, pp.38-39).'))
OPTRULE += [('LC', 'Alderman', GEN_LABEL, 'Army General (Chariot Wars)')]
GEN['LC'] = (['Army General'], [('Alderman', GEN_LABEL)])
OPT_ONCE += [('LC', [('Alderman', GEN_LABEL)])]
RATIOS += [('LC', 'Handgunners', ['Communal Pikemen'], 1)]
PTSLIM = []   # (key, unit, N, [other units sharing the allowance]): at most one per N army points
PTSLIM += [('ENG', 'Light Artillery', 1000, []), ('FRE', 'Light Artillery', 1000, []), ('FC', 'Light Artillery', 1000, []),
           ('LC', 'Light Artillery', 400, ['Multi-barrelled Artillery']), ('LC', 'Multi-barrelled Artillery', 400, ['Light Artillery'])]
def war_wagon(page, note=''):
    return U(INF, 'War Wagon', [M('War Wagon', '6 - - - 6 4 - - -', 120, key='wagon', rules=['War Wagon (Chivalry)']),
        M('Halberd Crewmen', '4 3 3 3 3 1 4 1 8', 0, mn=3, mx=3, key='melee', weapons=['Halberd', 'Light Armour']),
        M('Missile Crewmen', '4 3 3 3 3 1 4 1 8', 0, mn=3, mx=3, key='missile', weapons=['Crossbow', 'Light Armour'], options=[('Exchange crossbow for handgun', 0)])],
        'The cost of the war wagon includes six crewmen: three armed with halberds and three with crossbow or handgun, all with light armour. A team of 2-4 horses. War wagons may be single models (no Leader, Standard Bearer or Musician) or grouped in units of at least three models. One wagon per unit may include a tarasnices (palisade gun) for +20 pts (not built).' + note, page=page)
def wagon_tabor(page, note=''):
    return U(INF, 'Wagon Tabor', [M('Tabor Wagon', '- - - - 6 3 - - -', 15, key='wagon', rules=['Wagon Tabor (Chivalry)']),
        M('Defenders', '4 2 3 3 3 1 2 1 7', 6, mn=5, mx=10, key='def', weapons=['Hand Weapon', 'Bow', 'Light Armour'],
          options=[('Exchange bow for thrusting spear', 0), ('Exchange bow for throwing spear', 0), ('Exchange bow for halberd', 1), ('Exchange bow for crossbow', 6), ('Exchange bow for handgun', 6)])],
        'Each wagon has from 5-10 defenders armed with hand weapon, bow and light armour; the defenders of each wagon are a separate unit. May exchange bow for thrusting or throwing spear (free) or halberd (+1 pt), or for crossbow or handgun (+6 pts). Different Weapons. The Wagon Tabor is deployed as one unit and placed first; the wagons are up to 3" apart with the end wagons touching the owning player\'s table edge; it may not move after deployment. Each undefended wagon at the end of the game gives the opponent +15 Victory points.' + note, page=page)
def carrocio(page, avail_note):
    return U(CH, 'Carrocio', [M('Carrocio Wagon', '- - - - 6 3 - - -', 50, key='wagon', rules=['Army Standard', 'Wagon Tabor (Chivalry)']),
        M('Defenders', '4 2 3 3 3 1 2 1 7', 6, mn=5, mx=10, key='def', weapons=['Hand Weapon', 'Bow', 'Light Armour'], options=[('Exchange bow for thrusting spear', 0), ('Exchange bow for halberd', 1), ('Exchange bow for crossbow', 6)])],
        'The Carrocio (50 pts, plus the cost of the defenders; no handguns) is paid out of the Character points allowance and is an Army Standard Wagon - a regular Wagon (like Tabor wagons) as well as the Army Standard. It is placed last like other characters and is not restricted to the Tabor rule for placement, but cannot move once placed. ' + avail_note, mx=1, page=page)
# ====================================================================== THE HOLY ROMAN EMPIRE (book pp.40-41)
HR = []
MERC, MILI = 'Mercenaries', 'Infantry'
def hr_cmdr(kind, pts, st):
    return U(CH, f'{kind} Commander', [M(f'{kind} Commander', st, pts, weapons=['Hand Weapon', 'Shield', 'Heavy Armour'], options=[
        ('Ride a warhorse', 0), ('Partial plate armour, if mounted (replaces heavy armour)', 0), ('Partial plate armour, if on foot (replaces heavy armour)', 2), ('Lance', 4), ('Cloth barding (-1 M)', 4),
        ('Halberd', 3), ('Double-handed weapon', 4), ('Full plate armour, if mounted (replaces heavy armour)', 0), ('Full plate armour, if on foot (replaces heavy armour)', 4), ('Barding (plate, -1 M)', 6),
        ('Army General (+35 pts, +1 Wound)', 35), ('Army Standard Bearer (+15 pts)', 15)])],
    'Hand weapon, shield and heavy armour. May ride a warhorse (free). May have partial plate armour (free if mounted, +2 pts if on foot). Mounted Commanders may have a lance (+4 pts) and cloth barding (+4 pts) for their mounts. Commanders on foot may have halberd (+3 pts) or double-handed weapon (+4 pts). Later Army options: full plate armour (free if mounted, +4 pts if on foot) and plate barding (+6 pts). One Commander may be upgraded to Army General (+35 pts, +1 Wound); one other Commander may be upgraded to Army Standard Bearer (+15 pts), who may not upgrade equipment except for a warhorse and partial plate armour. ' + ('Imperial Commanders and Army Generals may only be chosen for Imperial armies.' if kind == 'Imperial' else ('Any unit led by a Clerical Commander is immune to panic as long as he is alive and with the unit.' if kind == 'Clerical' else '')), page='41')
HR.append(hr_cmdr('Imperial', 100, '4 5 3 4 3 2 6 2 9')); HR.append(hr_cmdr('Clerical', 110, '4 5 3 4 3 2 6 2 8')); HR.append(hr_cmdr('Feudal', 90, '4 6 3 4 3 2 6 2 8')); HR.append(hr_cmdr('City', 80, '4 5 3 4 3 2 6 2 8'))
HR.append(carrocio('41', 'Early Clerical and Early City armies where no Army Standard Bearer is chosen.'))
HR.append(U(CAV, 'Ritter (Mounted)', [M('Mounted Ritter', '8 4 3 3 3 1 3 1 7', 27, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Lance', 'Warhorse'], rules=['Combined Formation (Chivalry)', 'Impetuous', 'First Charge (Chivalry)'],
    options=[('Cloth barding (-1 M)', 4), ('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Barding (plate, -1 M)', 6), ('Stubborn (one unit, led by the Army General)', 3)])],
    'Hand weapon, heavy armour and shield, lance and warhorse. May take cloth barding (+4 pts) and partial plate armour (free, shield optional). Later Army: full plate armour (free if mounted) and plate barding (+6 pts). One unit of Ritter may be Stubborn (+3 pts) and must be led by the Army General. Combined Formation; Ritter may combine with Ministerialen, who are placed in the rear ranks. In Early Armies mounted Ritter have First Charge, are Impetuous and may count their Rank Bonus up to +1. In Later Armies mounted Ritter may count a Rank Bonus of up to +2. 0-2 Ritter units (mounted and dismounted together; entered as 0-2 each).', mx=2, page='41'))
HR.append(U(CAV, 'Ritter (Dismounted)', [M('Dismounted Ritter', '4 4 3 3 3 1 3 1 7', 12, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Thrusting Spear'], rules=['Combined Formation (Chivalry)'],
    options=[('Exchange thrusting spear for halberd', 2), ('Exchange thrusting spear for double-handed weapon', 2), ('Partial plate armour (replaces heavy armour)', 2), ('Full plate armour (replaces heavy armour)', 4), ('Stubborn (one unit, led by the Army General)', 3)])],
    'Hand weapon, heavy armour and shield, thrusting spear. May take halberd or double-handed weapon instead of spear (+2 pts), and partial plate armour (+2 pts) instead of heavy armour. Later Army: full plate armour (+4 pts). One unit of Ritter may be Stubborn (+3 pts) and must be led by the Army General. Combined Formation; may combine with Ministerialen. 0-2 units.', mx=2, page='41'))
HR.append(U(MERC, 'Allied or Mercenary Knights', [M('Mercenary Knight', '8 4 3 3 3 1 4 1 7', 33, mn=5, weapons=['Hand Weapon', 'Lance', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['First Charge (Chivalry)', 'Impetuous', 'Allies and Mercenaries (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, lance, heavy armour, shield and warhorse. May take partial plate armour instead of heavy armour (free). Warhorse may have cloth barding (+4 pts). Later Army: full plate armour (free). First Charge. Impetuous. May count Rank Bonus of up to +1. 0-2 units. Allies and Mercenaries rule applies.', mx=2, page='41'))
HR.append(U(CAV, 'Ministerialen (Mounted)', [M('Mounted Ministerialis', '8 3 3 3 3 1 3 1 7', 24, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Lance', 'Warhorse'], options=[('Cloth barding (-1 M)', 4), ('Heavy armour (replaces light armour)', 1)])],
    'Hand weapon, light armour and shield, lance and warhorse. May have cloth barding (+4 pts). May have heavy armour (+1 pt). Mounted Ministerialen count Rank Bonus of up to +1. Combined with Ritter (placed in the rear ranks).', page='41'))
HR.append(U(CAV, 'Ministerialen (Dismounted)', [M('Dismounted Ministerialis', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Thrusting Spear'], options=[('Heavy armour (replaces light armour)', 1), ('Exchange thrusting spear for halberd', 1), ('Exchange thrusting spear for double-handed weapon', 1)])],
    'Hand weapon, light armour and shield, thrusting spear. May have heavy armour (+1 pt). May take halberd or double-handed weapon instead of spear (+1 pt).', page='41'))
HR.append(U(MERC, 'Diener (Mercenary)', [M('Mercenary Diener', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Horse'], rules=['Open Order', 'Allies and Mercenaries (Chivalry)'], options=[('Exchange thrusting spear and shield for light crossbow', 0), ('Light armour', 2), ('Exchange crossbow for handgun', 2)])],
    'Hand weapon, and either thrusting spear and shield, or light crossbow. Rides a horse. May have light armour (+2 pts). Later Army: may exchange crossbow for handgun (+2 pts). Open Order. 0-2 Diener units (Mercenary and Militia together).', mx=2, page='41'))
HR.append(U(CAV, 'Diener (Militia)', [M('Militia Diener', '8 2 2 3 3 1 3 1 6', 14, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Horse'], rules=['Open Order'], options=[('Exchange thrusting spear and shield for light crossbow', 0), ('Light armour', 2), ('Exchange crossbow for handgun', 2)])],
    'Hand weapon, and either thrusting spear and shield, or light crossbow. Rides a horse. May have light armour (+2 pts). Later Army: may exchange crossbow for handgun (+2 pts). Open Order. 0-2 Diener units.', mx=2, page='41'))
HSP = lambda mil: [('Light armour', 1)] + ([] if mil else [('Heavy armour (replaces light armour)', 1)]) + [('Exchange thrusting spear for halberd', 1), ('Exchange thrusting spear and shield for pike', 1)]
HR.append(U(MERC, 'Mercenary Spearmen, Pikemen & Halberdiers', [M('Mercenary Infantryman', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Allies and Mercenaries (Chivalry)'],
    options=[('Light armour', 1), ('Heavy armour (replaces light armour)', 2), ('Exchange thrusting spear for halberd', 1), ('Exchange thrusting spear and shield for pike', 1), ('Partial plate armour (replaces heavy armour)', 3), ('Landsknecht (+1 pt per model)', 1), ('Verlorene Haufe (Skirmishers; +1 pt per model)', 1)])],
    'Hand weapon, thrusting spear and shield. May have light armour (+1 pt) or heavy armour (+2 pts). Later Army options: halberd instead of spear (+1 pt), or pike instead of spear & shield (+1 pt); partial plate armour (+3 pts). May be in Mixed Order units with Crossbowmen, Archers or Handgunners of the same type. Pikemen fight in a Medieval Phalanx and may not be in Mixed Order units. Later Imperial Armies: mercenaries that fight on foot count as Landsknecht (+1 pt per model up to 20 pts per unit); for every unit of Landsknecht Pikemen, a unit of eight Landsknecht Halberdier or Handgunner models may be upgraded to Verlorene Haufe (+1 pt per model).', page='41'))
HR.append(U(MILI, 'Militia Spearmen, Pikemen & Halberdiers', [M('Militia Infantryman', '4 2 2 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Open Order'],
    options=[('Light armour', 1), ('Heavy armour (replaces light armour)', 2), ('Exchange thrusting spear for halberd', 1), ('Exchange thrusting spear and shield for pike', 1), ('Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 1)])],
    'Hand weapon, thrusting spear and shield. May have light armour (+1 pt). Later Army options: all may have heavy armour (+2 pts), and either take halberd instead of spear (+1 pt), or pike instead of spear & shield (+1 pt). May be in Mixed Order units with Crossbowmen, Archers or Handgunners of the same type. Pikemen fight in a Medieval Phalanx and may not be in Mixed Order units. Militia troops may be Open Order. City armies: Militia may be upgraded to WS3 & BS3 (+1 pt per model).', page='41'))
HR.append(U(MERC, 'Mercenary Archers, Crossbowmen & Handgunners', [M('Mercenary Missile Trooper', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Open Order', 'Allies and Mercenaries (Chivalry)'],
    options=[('Exchange bow for crossbow', 2), ('Exchange bow for handgun', 2), ('Light armour', 1), ('Heavy armour (replaces light armour)', 2), ('Pavise', 2), ('Landsknecht (+1 pt per model)', 1), ('Verlorene Haufe (Skirmishers; +1 pt per model)', 1)])],
    'Hand weapon and bow. May take crossbow or handgun instead of bow (+2 pts). May have light armour (+1 pt). Later Army options: crossbowmen and handgunners may have heavy armour (+2 pts) and pavise (+2 pts). Open Order or Mixed Order with Spearmen or Halberdiers of the same type. For each Crossbowman model at least two Spearmen, Pikemen or Halberdier models must be taken. Early Armies: only 0-1 unit of Handgunners. Later Armies: only 0-1 Archer unit and 0-2 Handgunner units.', page='41'))
HR.append(U(MILI, 'Militia Archers, Crossbowmen & Handgunners', [M('Militia Missile Trooper', '4 2 2 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Open Order'],
    options=[('Exchange bow for crossbow', 2), ('Exchange bow for handgun', 2), ('Light armour', 1), ('Heavy armour (replaces light armour)', 2), ('Pavise', 2), ('Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 1)])],
    'Hand weapon and bow. May take crossbow or handgun instead of bow (+2 pts). May have light armour (+1 pt). Later Army options: crossbowmen and handgunners may have heavy armour (+2 pts) and pavise (+2 pts). Open Order or Mixed Order with Spearmen or Halberdiers of the same type. For each Crossbowman model at least two Spearmen, Pikemen or Halberdier models must be taken. City armies: Militia may be upgraded to WS3 & BS3 (+1 pt per model).', page='41'))
HR.append(U(MILI, 'Levies', [M('Levy', '4 2 2 3 3 1 2 1 5', 3, mn=5, weapons=['Improvised Weapon'], rules=['Open Order', 'Warband Psychology (rule 1)'])],
    'Improvised weapons. Open Order. Subject to Warband Psychology, Rule 1. Only Imperial and Feudal armies may take Levies.', page='41'))
HR.append(artillery('41', master=True, units_note=' Later armies only: one gun for every 1,000 army points; one crewman in the army may be upgraded to Master Gunner (+20 pts). Bought from the Infantry allocation.'))
HR.append(multi_barrelled('41', ' Later armies only: one gun for every 1,000 army points (light artillery and multi-barrelled together).'))
HR.append(war_wagon('41', ' Later Feudal or Clerical armies: 0-1 War Wagon.'))
HR[-1]['mx'] = 1
HR.append(wagon_tabor('41', ' Later City, League or Communal armies, if at least 33% of the available points have been spent on Militia troops: 1 Wagon per 500 army points, paid out of the Infantry points allowance.'))
ECHR = {'Characters': {'max': 25}}
HRC = {}
for per, (cav, inf, mer) in {'Early': ((15, 33), (25, 50), (25, 50)), 'Later': ((15, 33), (25, 33), (25, 75))}.items():
    for typ in ('Imperial', 'Feudal', 'Clerical', 'City'):
        HRC[f'{per} {typ}'] = (L(Characters=25, Cavalry=cav, Infantry=inf, Mercenaries=mer), f'{per} {typ} Army ({"1254-1438" if per == "Early" else "1438-1519"}).')
HRN = {
 'Early Imperial': 'If an Imperial Army General is chosen and the army includes less than three Militia units, either 0-2 units from the English HYW list, or 0-2 Communal troops from the Low Countries list, or 0-1 unit from the Teutonic Order list may be chosen as additional Mercenaries (documented only).',
 'Early Feudal': 'If a Feudal Army General is chosen, the army may include either 0-2 units of Hungarian Light Cavalry from the Kingdom of Hungary list, or 0-2 Communal troops from the Low Countries list (documented only).',
 'Early Clerical': 'If a Clerical Army General is chosen, the army may include either 0-2 units of Hungarian Light Cavalry from the Kingdom of Hungary list, or 0-2 Communal troops from the Low Countries list (documented only). If no Army Standard Bearer is chosen a Carrocio may be taken.',
 'Early City': 'If a City Army General is chosen, any Militia unit may be upgraded to WS3 & BS3 (+1 pt per model). 0-2 Mercenary units from this list may be chosen. If no Army Standard Bearer is chosen a Carrocio may be taken.',
 'Later Imperial': 'If an Imperial Army General is chosen, only 0-2 Militia units may be chosen. All Mercenaries from this list that fight on foot count as Landsknecht (+1 pt per model up to a maximum points cost of 20 pts per unit). Landsknecht do not roll to test their loyalty at the beginning of the battle like other Allies & Mercenaries, but still cannot use the benefits of the Army General or the Army Standard Bearer. Later Imperial armies may draw on 0-1 unit from the Teutonic Order list, and 0-2 units of Pikemen from the Low Countries or the Swiss lists (documented only).',
 'Later Feudal': 'Only 0-2 Militia or Levy units may be chosen. 0-1 War Wagon may be chosen.',
 'Later Clerical': 'Only 0-2 Militia or Levy units may be chosen. 0-1 War Wagon may be chosen.',
 'Later City': 'If a City Army General is chosen, every other Militia unit may be upgraded to WS3 & BS3 (+1 pt per model). 0-3 Mercenary units from this list may be chosen. Levies may not be chosen. If at least 33% of the available points have been spent on Militia troops, a Wagon Tabor may be chosen (1 Wagon per 500 army points), paid out of the Infantry points allowance.'}
HR_V = multi('HRE', 'Holy Roman Empire', {k: (v[0], v[1] + ' ' + HRN[k]) for k, v in HRC.items()})
HR_NOTES = ('THE HOLY ROMAN EMPIRE 1254-1519 (Armies of Chivalry, pp.40-41). Choose Early (1254-1438) or Later (1438-1519) and the type of the Army General (Imperial, Feudal, Clerical or City) in the Army composition list. Characters 0-25%, Cavalry 15-33%, Infantry 25-50% (Early) or 25-33% (Later), Mercenaries 25-50% (Early) or 25-75% (Later). In this catalogue the Mercenary versions of troops, the Allied or Mercenary Knights and the Mercenary Diener count against the Mercenaries allocation; Ritter, Ministerialen and Militia Diener count as Cavalry; Militia, Levies, artillery and wagons count as Infantry. '
    'Verlorene Haufe (Lost Bunch): for every unit of Landsknecht Pikemen, a unit of eight Landsknecht Halberdier or Handgunner models may be upgraded to Verlorene Haufe (+1 pt per model). They are Skirmishers and may re-roll their first failed Panic test; each unit must be attached to a parent unit of Landsknecht Pikemen at the start of the battle and stay within 6" of it or lose the re-roll. Only in Later Imperial armies. '
    'Allies & Mercenaries: unless stated otherwise all Allied & Mercenary troops in this list and troops drawn from other lists are subject to the Allies & Mercenaries rule. Mercenary units led by a Commander, the Army General or the Army Standard Bearer are not subject to it. Any unit led by a Clerical Commander is immune to panic as long as he is alive and with the unit.')
LISTS.append(('HRE', 'Holy Roman Empire (Armies of Chivalry)', 'Holy_Roman_Empire_Chivalry.cat', HR, HR_V, HR_NOTES))
EARLY = [k for k in HRC if k.startswith('Early')]; LATER = [k for k in HRC if k.startswith('Later')]
for typ in ('Imperial', 'Feudal', 'Clerical', 'City'):
    AVAIL += [('HRE', f'{typ} Commander', [f'Early {typ}', f'Later {typ}'])]
UNAV += [('HRE', 'Levies', ['Early Clerical', 'Later Clerical', 'Early City', 'Later City']), ('HRE', 'Carrocio', ['Early Imperial', 'Early Feudal'] + LATER),
         ('HRE', 'Light Artillery', EARLY), ('HRE', 'Multi-barrelled Artillery', EARLY), ('HRE', 'War Wagon', [k for k in HRC if k not in ('Later Feudal', 'Later Clerical')]), ('HRE', 'Wagon Tabor', [k for k in HRC if k != 'Later City'])]
for u, lab in [('Ritter (Mounted)', 'Barding (plate, -1 M)'), ('Ritter (Mounted)', 'Full plate armour (replaces heavy armour)'), ('Ritter (Dismounted)', 'Full plate armour (replaces heavy armour)'),
               ('Allied or Mercenary Knights', 'Full plate armour (replaces heavy armour)'), ('Diener (Mercenary)', 'Exchange crossbow for handgun'), ('Diener (Militia)', 'Exchange crossbow for handgun'),
               ('Mercenary Spearmen, Pikemen & Halberdiers', 'Exchange thrusting spear for halberd'), ('Mercenary Spearmen, Pikemen & Halberdiers', 'Exchange thrusting spear and shield for pike'), ('Mercenary Spearmen, Pikemen & Halberdiers', 'Partial plate armour (replaces heavy armour)'),
               ('Militia Spearmen, Pikemen & Halberdiers', 'Exchange thrusting spear for halberd'), ('Militia Spearmen, Pikemen & Halberdiers', 'Exchange thrusting spear and shield for pike'), ('Militia Spearmen, Pikemen & Halberdiers', 'Heavy armour (replaces light armour)'),
               ('Mercenary Archers, Crossbowmen & Handgunners', 'Heavy armour (replaces light armour)'), ('Mercenary Archers, Crossbowmen & Handgunners', 'Pavise'), ('Militia Archers, Crossbowmen & Handgunners', 'Heavy armour (replaces light armour)'), ('Militia Archers, Crossbowmen & Handgunners', 'Pavise')]:
    OPTAV += [('HRE', u, lab, LATER)]
for u in ('Imperial Commander', 'Clerical Commander', 'Feudal Commander', 'City Commander'):
    for lab in ('Full plate armour, if mounted (replaces heavy armour)', 'Full plate armour, if on foot (replaces heavy armour)', 'Barding (plate, -1 M)'): OPTAV += [('HRE', u, lab, LATER)]
OPTAV += [('HRE', 'Mercenary Spearmen, Pikemen & Halberdiers', 'Landsknecht (+1 pt per model)', ['Later Imperial']), ('HRE', 'Mercenary Spearmen, Pikemen & Halberdiers', 'Verlorene Haufe (Skirmishers; +1 pt per model)', ['Later Imperial']),
          ('HRE', 'Mercenary Archers, Crossbowmen & Handgunners', 'Landsknecht (+1 pt per model)', ['Later Imperial']), ('HRE', 'Mercenary Archers, Crossbowmen & Handgunners', 'Verlorene Haufe (Skirmishers; +1 pt per model)', ['Later Imperial']),
          ('HRE', 'Militia Spearmen, Pikemen & Halberdiers', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', ['Early City', 'Later City']), ('HRE', 'Militia Archers, Crossbowmen & Handgunners', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', ['Early City', 'Later City'])]
OPTSTAT += [('HRE', 'Militia Spearmen, Pikemen & Halberdiers', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 'WS', 3), ('HRE', 'Militia Archers, Crossbowmen & Handgunners', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 'WS', 3),
            ('HRE', 'Militia Spearmen, Pikemen & Halberdiers', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 'BS', 3), ('HRE', 'Militia Archers, Crossbowmen & Handgunners', 'Upgrade to WS3 & BS3 (City armies; +1 pt per model)', 'BS', 3)]
for u in ('Imperial Commander', 'Clerical Commander', 'Feudal Commander', 'City Commander'):
    OPTRULE += [('HRE', u, 'Army General (+35 pts, +1 Wound)', 'Army General (Chariot Wars)'), ('HRE', u, 'Army Standard Bearer (+15 pts)', 'Army Standard')]
    OPTSTAT += [('HRE', u, 'Army General (+35 pts, +1 Wound)', 'W', 3)]
OPT_ONCE += [('HRE', [(f'{t} Commander', 'Army General (+35 pts, +1 Wound)') for t in ('Imperial', 'Clerical', 'Feudal', 'City')]),
             ('HRE', [(f'{t} Commander', 'Army Standard Bearer (+15 pts)') for t in ('Imperial', 'Clerical', 'Feudal', 'City')]),
             ('HRE', [('Ritter (Mounted)', 'Stubborn (one unit, led by the Army General)'), ('Ritter (Dismounted)', 'Stubborn (one unit, led by the Army General)')])]
OPTRULE += [('HRE', 'Ritter (Mounted)', 'Stubborn (one unit, led by the Army General)', 'Stubborn'), ('HRE', 'Ritter (Dismounted)', 'Stubborn (one unit, led by the Army General)', 'Stubborn')]
PAIRS += [('HRE', ['Carrocio'], 'x')] if False else []
PTSLIM += [('HRE', 'Light Artillery', 1000, ['Multi-barrelled Artillery']), ('HRE', 'Multi-barrelled Artillery', 1000, ['Light Artillery']), ('HRE', 'Wagon Tabor', 500, [])]
# ====================================================================== THE TEUTONIC ORDER (book pp.42-43)
TE = []
TFP = lambda: [('Full plate armour, if mounted (replaces partial plate armour)', 0), ('Full plate armour, if dismounted (replaces partial plate armour)', 2), ('Ride a warhorse', 0), ('Lance', 0), ('Exchange halberd for double-handed weapon', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
TE.append(U(CH, 'Army General', [M('Army General', '4 6 3 3 3 3 6 2 9', 160, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Halberd'], rules=['Army General', 'Stubborn'], options=TFP() + [('Hochmeister (Ld 10)', 30)])],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). Has a halberd or a double-handed weapon if on foot. Has a lance and warhorse if mounted. The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). A Teutonic Army may be led by the Hochmeister with a Ld of 10 (+30 pts). Army General. Stubborn. 0-1.', mx=1, page='42'))
TE.append(U(CH, 'Magister', [M('Magister', '4 5 3 3 3 2 5 2 8', 100, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Halberd'], rules=['Stubborn'], options=TFP() + [(GEN_LABEL, 25)])],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). Has a halberd or a double-handed weapon if on foot. Has a lance and warhorse if mounted. The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Stubborn. If no other Army General is taken, a single Magister may be made Army General for +25 pts. 0-2.', mx=2, page='42'))
TE.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 3 3 2 5 2 8', 90, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield'], rules=['Army Standard', 'Stubborn'], options=[('Full plate armour, if mounted (replaces partial plate armour)', 0), ('Full plate armour, if dismounted (replaces partial plate armour)', 2), ('Ride a warhorse', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). May have a warhorse (free) which may have cloth barding (+4 pts), or plate barding (+6 pts). Army Battle Standard. Stubborn. 0-1.', mx=1, page='42'))
MN = {'Ritterbrüder and Ordensdiener': 'Bruder', 'Crusader Knights': 'Crusader Knight'}
def tkn(name, pts, st, mounted, cav_note):
    if mounted:
        return U(CAV, name + ' (Mounted)', [M('Mounted ' + MN.get(name, name.rstrip('s')), st, pts, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)'] + (['Stubborn'] if 'brüder' in name else ['Impetuous']),
            options=[('Full plate armour (replaces partial plate armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)] + ([('Veteran', 3)] if 'brüder' in name else []))],
            'Hand weapon, partial plate armour and shield, lance and warhorse. May wear full plate armour (free if mounted). The warhorse may have cloth barding (+4 pts), or plate barding (+6 pts). ' + cav_note, page='42')
    return U(CAV, name + ' (Dismounted)', [M('Dismounted ' + MN.get(name, name.rstrip('s')), st, pts, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Halberd'], rules=['Different Weapons'] + (['Stubborn'] if 'brüder' in name else []),
        options=[('Full plate armour (replaces partial plate armour)', 2), ('Exchange halberd for double-handed weapon', 0)] + ([('Veteran', 3)] if 'brüder' in name else []))],
        'Hand weapon, partial plate armour and shield. May wear full plate armour (+2 pts if dismounted). Has a halberd or a double-handed weapon. Different Weapons if dismounted. ' + cav_note, page='42')
RB_NOTE = 'Stubborn. First Charge. May be Veteran (+3 pts). Combined Formation; may include Turkopolen. When mounted, Brüder count a Rank Bonus of up to +1 in combat. Up to two units of Brüder (mounted and dismounted together; entered as 0-2 each) may be taken. One unit of Brüder may be upgraded to WS5 (+3 pts).'
TE.append(tkn('Ritterbrüder and Ordensdiener', 36, '8 4 3 3 3 1 4 1 8', True, RB_NOTE)); TE[-1]['mx'] = 2
TE.append(tkn('Ritterbrüder and Ordensdiener', 18, '4 4 3 3 3 1 4 1 8', False, RB_NOTE)); TE[-1]['mx'] = 2
for u in TE[-2:]:
    u['models'][0]['options'].append(('Upgrade to WS5 (one unit)', 3)); u['models'][0]['rules'].append('Combined Formation (Chivalry)')
TE.append(tkn('Crusader Knights', 25, '8 3 3 3 3 1 3 1 7', True, 'Impetuous and First Charge if mounted. Mounted Crusader Knights count a Rank Bonus of up to +1 in combat.'))
TE.append(tkn('Crusader Knights', 12, '4 3 3 3 3 1 3 1 7', False, 'Different Weapons if dismounted.'))
TE.append(U(CAV, 'Turkopolen', [M('Turkopole', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Bow', 'Light Armour', 'Shield', 'Throwing Spear', 'Horse'], rules=['Open Order', 'Combined Formation (Chivalry)'], options=[('Exchange throwing spear for thrusting spear', 0), ('Heavy armour (replaces light armour)', 2)])],
    'Hand weapon, bow, light armour, shield, and thrusting or throwing spear. May have heavy armour (+2 pts). Open Order. Combined formation; Turkopolen may be included in a unit of Brüder, they then lose their Open Order ability.', page='42'))
TE.append(U(CAV, 'Native Light Cavalry', [M('Native Cavalryman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Bow', 'Shield', 'Horse'], rules=['Feigned Flight'], options=[('Exchange bow for javelin', 0), ('Light armour', 2)])],
    'Hand weapon, bow or javelin, and shield. May have light armour (+2 pts). Bow armed Native Cavalry are Skirmishers. Javelin armed Native Cavalry are Open Order. All have Feigned Flight.', page='43'))
TE.append(U(CAV, 'Knechte', [M('Knecht', '8 3 3 3 3 1 3 1 6', 14, mn=5, weapons=['Hand Weapon', 'Light Crossbow', 'Horse'], rules=['Skirmishers (Chivalry)'], options=[('Light armour', 2)])],
    'Hand weapon and light crossbow. May have light armour (+2 pts). Skirmishers.', page='43'))
TE.append(U(INF, 'Ordensdiener Spearmen', [M('Ordensdiener Spearman', '4 3 3 3 3 1 3 1 8', 15, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield', 'Partial Plate Armour'], rules=['Stubborn'], options=[('Full plate armour (replaces partial plate armour and shield)', 0)])],
    'Hand weapon, thrusting spear, shield and partial plate armour. May wear full plate armour instead of partial plate armour and shield. Stubborn.', page='43'))
TE.append(U(INF, 'Ordensdiener Crossbowmen', [M('Ordensdiener Crossbowman', '4 3 3 3 3 1 3 1 8', 16, mn=5, weapons=['Hand Weapon', 'Crossbow', 'Pavise', 'Heavy Armour'], rules=['Stubborn'], options=[('Partial plate armour (replaces heavy armour)', 2)])],
    'Hand weapon, crossbow, pavise and heavy armour. May upgrade to partial plate armour (+2 pts). Stubborn.', page='43'))
TE.append(U(INF, 'Schiffskinder', [M('Schiffskind', '4 4 3 3 3 1 3 1 8', 15, mn=5, weapons=['Hand Weapon', 'Halberd', 'Buckler', 'Partial Plate Armour'], rules=['Stubborn'])],
    'Hand weapon, pole axe (treat as halberd), buckler and partial plate armour. Stubborn. 0-1 unit.', mx=1, page='43'))
TE.append(U(INF, 'Crusader Crossbowmen', [M('Crusader Crossbowman', '4 3 3 3 3 1 3 1 6', 10, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], options=[('Pavise', 2)])],
    'Crossbow, hand weapon and light armour. May have a pavise (+2 pts).', page='43'))
TE.append(U(INF, 'Colonist Spearmen', [M('Colonist Spearman', '4 2 2 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Light armour', 2)])],
    'Hand weapon, thrusting spear and shield. May have light armour (+2 pts).', page='43'))
TE.append(U(INF, 'Native Regular Infantry', [M('Native Infantryman', '4 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Open Order'])],
    'Hand weapon, thrusting spear and shield. Open Order.', page='43'))
TE.append(U(INF, 'Native Subject Infantry', [M('Native Levy', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Open Order', 'Warband'])],
    'Mixed weapons and shield. Open Order. Warband.', page='43'))
TE.append(U(INF, 'Handgunners', [M('Handgunner', '5 3 3 3 3 1 3 1 6', 10, mn=5, weapons=['Handgun', 'Hand Weapon', 'Light Armour'], rules=['Skirmishers (Chivalry)'])],
    'Handgun, hand weapon and light armour. Skirmishers. 0-1 unit.', mx=1, page='43'))
TE.append(artillery('43', units_note=' May have one gun per 1,000 army points.'))
TE_V = single('TEU', 'The Teutonic Order', L(Characters=25, Cavalry=(25, 50), Infantry=(25, 75)), 'Characters 0-25%, Cavalry 25-50%, Infantry 25-75%. Artillery is bought from the Infantry allocation.')
LISTS.append(('TEU', 'The Teutonic Order (Armies of Chivalry)', 'Teutonic_Order_Chivalry.cat', TE, TE_V, 'THE TEUTONIC ORDER 14th to late 15th century (Armies of Chivalry, pp.42-43).'))
PTSLIM += [('TEU', 'Light Artillery', 1000, [])]
OPTRULE += [('TEU', 'Magister', GEN_LABEL, 'Army General (Chariot Wars)'), ('TEU', 'Ritterbrüder and Ordensdiener (Mounted)', 'Veteran', 'Veteran'), ('TEU', 'Ritterbrüder and Ordensdiener (Dismounted)', 'Veteran', 'Veteran')]
GEN['TEU'] = (['Army General'], [('Magister', GEN_LABEL)])
OPT_ONCE += [('TEU', [('Magister', GEN_LABEL)]), ('TEU', [('Ritterbrüder and Ordensdiener (Mounted)', 'Upgrade to WS5 (one unit)'), ('Ritterbrüder and Ordensdiener (Dismounted)', 'Upgrade to WS5 (one unit)')])]
OPTSTAT += [('TEU', 'Army General', 'Hochmeister (Ld 10)', 'Ld', 10), ('TEU', 'Ritterbrüder and Ordensdiener (Mounted)', 'Upgrade to WS5 (one unit)', 'WS', 5), ('TEU', 'Ritterbrüder and Ordensdiener (Dismounted)', 'Upgrade to WS5 (one unit)', 'WS', 5)]
# ====================================================================== THE KINGDOM OF POLAND (book pp.44-45)
PL = []; SPC = 'Special Units'
PLC = lambda: [('Partial plate armour (replaces heavy armour)', 2), ('Full plate armour (replaces heavy armour)', 2), ('Lance', 4), ('Cloth barding (-1 M)', 4)]
def war_wagon_cat(page, note, cat=SPC):
    u = war_wagon(page, note); u['cat'] = cat; return u
def wagon_tabor_cat(page, note, cat=SPC):
    u = wagon_tabor(page, note); u['cat'] = cat; return u
def artillery_cat(page, cat=SPC, **kw):
    u = artillery(page, **kw); u['cat'] = cat; return u
PL.append(U(CH, 'King', [M('King', '8 6 3 4 3 3 6 2 9', 160, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Army General', 'Stubborn (if with Knights)'], options=PLC())],
    'Hand weapon, heavy armour, shield and warhorse. May upgrade to partial plate or full plate armour (+2 pts), lance (+4 pts) and cloth barding (+4 pts). Army General; must take either the King or the Marshal as Army General. Stubborn if with a unit of Knights.', mx=1, page='44'))
PL.append(U(CH, 'Marshal', [M('Marshal', '8 5 3 3 3 3 5 3 9', 140, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Army General', 'Stubborn (if with Knights)'], options=PLC())],
    'Hand weapon, heavy armour, shield and warhorse. May upgrade to partial plate or full plate armour (+2 pts), lance (+4 pts) and cloth barding (+4 pts). Army General; must take either the King or the Marshal as Army General. Stubborn if with a unit of Knights.', mx=1, page='44'))
PL.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '8 5 3 4 3 2 5 2 8', 90, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Army Standard', 'Stubborn (if with Knights)'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Full plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour, shield and warhorse. May upgrade to partial plate or full plate armour (+2 pts) and cloth barding (+4 pts). Army Battle Standard. Stubborn if with a unit of Knights. 0-1.', mx=1, page='44'))
PL.append(U(CH, 'Noble Commanders', [M('Noble Commander', '8 4 3 3 3 2 4 2 8', 65, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Noble Commander (Poland)'], options=PLC())],
    'Hand weapon, heavy armour, shield and warhorse. May upgrade to partial plate or full plate armour (+2 pts), lance (+4 pts), and cloth barding (+4 pts). Noble Commander: substituted for unit Leaders in units of Knights; roll a D6 for each before deployment on the Noble Commander Attributes chart (1 Young Hotspur: +1 Attack, Impetuous roll 1 or 2; 2 Venerable Leader: Ld 9; 3 Potential Usurper: Ld 7 for him and the unit, which cannot use the General\'s Ld; 4 Defiant/Reluctant Leader: unit subject to Allies & Mercenaries rule; 5 Charismatic Leader: Knights may re-roll misses once; 6 Notable Reputation: +1 WS and fear). All units of Knights in the army must be led by a Noble Commander, who cannot lead any other type of unit (one Noble Commander per Knights unit is enforced as a ratio).', page='44'))
PL.append(U(CAV, 'Knights', [M('Knight', '8 4 3 3 3 1 4 1 8', 36, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse', 'Lance'], rules=['Stubborn', 'Impetuous', 'First Charge (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 2), ('Full plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4), ('Elite (WS5; one unit)', 2)])],
    'Hand weapon, heavy armour, shield, warhorse and lance. May upgrade to partial plate or full plate armour (+2 pts) and cloth barding (+4 pts). Stubborn, Impetuous, and First Charge. 0-1 unit may upgrade to Elite (+2 pts) and increase to WS5. The Elite unit cannot outnumber any other unit of Knights and must be accompanied by the General and Army Standard Bearer if taken. The Elite unit may not have a Noble Commander or Unit Leader. 1+ unit.', page='45'))
PL.append(U(CAV, 'Followers/Retainers (Mounted)', [M('Mounted Retainer', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Thrusting Spear', 'Horse'], options=[('Exchange thrusting spear for lance', 4), ('Bow', 2), ('Light crossbow', 2), ('Heavy armour (replaces light armour)', 4)])],
    'Hand weapon, light armour, shield, thrusting spear and horse. May substitute lance (+4 pts) for thrusting spear; or add light crossbow (treat as bow, +2 pts) or bow (+2 pts). May have heavy armour (+4 pts). 1+ unit of Followers/Retainers.', page='45'))
PL.append(U(CAV, 'Followers/Retainers (Dismounted)', [M('Dismounted Retainer', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Thrusting Spear'], options=[('Bow', 2), ('Light crossbow', 2), ('Heavy armour (replaces light armour)', 4)])],
    'Hand weapon, light armour, shield and thrusting spear. May add light crossbow (treat as bow, +2 pts) or bow (+2 pts). May have heavy armour (+4 pts).', page='45'))
PL.append(U(CAV, 'Lithuanian Light Cavalry', [M('Lithuanian', '8 3 3 3 3 1 3 1 7', 23, mn=5, weapons=['Hand Weapon', 'Bow', 'Shield', 'Thrusting Spear', 'Horse'], rules=['Open Order', 'Feigned Flight'], options=[('Exchange thrusting spear for throwing spear', 0), ('Light armour', 2), ('Heavy armour (replaces light armour)', 2)])],
    'Hand weapon, bow, shield, and thrusting or throwing spear. May upgrade to light armour (+2 pts). May upgrade to heavy armour (+4 pts). Open Order, Feigned Flight. Lithuanians become Close Order if they upgrade to heavy armour.', page='45'))
PL.append(U(INF, 'Infantry', [M('Infantryman', '4 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], options=[('Light armour', 1), ('Exchange spear and shield for bow', 0), ('Exchange thrusting spear and shield for double-handed axe (0-1 unit; Open Order, +2 pts with light armour)', 2)])],
    'Hand weapon, thrusting spear and shield. May upgrade to light armour (+1 pt). Every second unit may exchange spear and shield for bow at no cost and become Open Order (not enforced). 0-1 unit may exchange thrusting spear and shield for double-handed axe and light armour (+2 pts); the unit of axemen are Open Order if taken.', page='45'))
PL.append(U(INF, 'Peasants', [M('Peasant', '4 1 2 3 3 1 2 1 5', 3, mn=5, weapons=['Javelin', 'Hand Weapon', 'Shield'], rules=['Peasants (Chivalry)'])],
    'Mixed weapons (count as javelins and hand weapons) and shield. Fear formed foot units they do not outnumber by at least two to one. Fear formed cavalry units. Casualties from artillery cause a Panic test. Peasant units may not include a Standard or Musician.', page='45'))
PL.append(U(INF, 'Militia', [M('Militia', '4 2 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Combined Formation (Chivalry)'], options=[('Pavise', 2), ('Exchange thrusting spear for crossbow', 4), ('Light armour', 1), ('Exchange thrusting spear for halberd', 1)])],
    'Hand weapon and thrusting spear. May have pavise (+2 pts) or exchange thrusting spear for crossbows (+4 pts). May have light armour (+1 pt). Any unit may exchange thrusting spears for halberds/bills (+1 pt) but may not take pavises or crossbows. Combined Formation; crossbow armed Militia must be in a Combined Formation with spear armed Militia who may make up no more than the first two ranks of the unit. Crossbowmen cannot outnumber other Militia. Militia units with pavises in the front rank gain a +2 armour save in hand-to-hand combat and are -1 to hit in hand-to-hand combat if they are stationary and do not charge (front only).', page='45'))
PL.append(U(INF, 'Handgunners', [M('Handgunner', '4 3 3 3 3 1 2 1 7', 11, mn=5, weapons=['Hand Weapon', 'Handgun', 'Light Armour'], rules=['Skirmishers (Chivalry)'], options=[('Heavy armour (replaces light armour)', 2), ('Partial plate armour (replaces light armour)', 3)])],
    'Hand weapon, handgun and light armour. May upgrade to heavy armour (+2 pts) or partial plate armour (+3 pts). Skirmishers. For every Handgunner model, at least two Militia models must be taken (not enforced).', page='45'))
PL.append(artillery_cat('45', units_note=' Up to one gun for every 1,000 army points.'))
PL.append(wagon_tabor_cat('45', ' Polish Wagon Tabors may be placed in groups of 2-4 wagons at a right angle to, and with one wagon contacting, the owning player\'s baseline; they cannot be deployed outside the deployment area. Up to one Wagon for every 500 army points.'))
PL.append(war_wagon_cat('45', ' Up to one war wagon for every 1,500 army points.'))
PL_V = single('POL', 'The Kingdom of Poland', L(Characters=25, Cavalry=(50, 100), Infantry=50, **{'Special_Units': 25}), 'Characters up to 25%, Cavalry at least 50%, Infantry up to 50%, Special Units up to 25%. Allies: up to 25% from the Kingdom of Hungary list (no Peasants, War Wagons or Artillery) or the Principality of Moldavia list (no Peasantry or Mercenaries) - documented only. Hungarians, Moldavians (Calarasi) and Tartars (Tartar Warriors) are allied light cavalry entries from the other lists, subject to the Allies & Mercenaries rule.')
LISTS.append(('POL', 'The Kingdom of Poland (Armies of Chivalry)', 'Poland_Chivalry.cat', PL, PL_V, 'THE KINGDOM OF POLAND mid 14th to early 16th century (Armies of Chivalry, pp.44-45).'))
PAIRS += [('POL', ['King', 'Marshal'], 'king-or-marshal')]
PTSLIM += [('POL', 'Light Artillery', 1000, []), ('POL', 'Wagon Tabor', 500, []), ('POL', 'War Wagon', 1500, [])]
RATIOS += [('POL', 'Knights', ['Noble Commanders'], 1)]
OPT_ONCE += [('POL', [('Knights', 'Elite (WS5; one unit)')])]
OPTSTAT += [('POL', 'Knights', 'Elite (WS5; one unit)', 'WS', 5)]
# ====================================================================== MOLDAVIA & WALLACHIA (book pp.46-47)
MW = []; ALM = 'Allies & Mercenaries'
MWC = lambda foot2=True: [('Ride a horse', 8), ('Ride a warhorse', 16), ('Thrusting spear', 2), ('Partial plate armour (replaces heavy armour)', 2)] + ([('Double-handed weapon', 2)] if foot2 else [])
MW.append(U(CH, 'Voievod', [M('Voievod', '4 5 5 4 4 3 5 2 9', 165, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General'], options=MWC())],
    'Hand weapon, heavy armour and a shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts) and may wear partial plate armour (+2 pts). If on foot, may have a two-handed weapon (+2 pts). May take either the Voievod or the Vornic as the Army General.', mx=1, page='46'))
MW.append(U(CH, 'Vornic', [M('Vornic', '4 5 5 4 3 2 5 2 8', 120, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General'], options=MWC())],
    'Hand weapon, heavy armour and a shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts) and may wear partial plate armour (+2 pts). If on foot, may have a two-handed weapon (+2 pts). May take either the Voievod or the Vornic as the Army General.', mx=1, page='46'))
MW.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 4 4 3 2 4 2 8', 80, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army Standard'], options=MWC(False))],
    'Hand weapon, heavy armour and a shield. May ride a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts) and partial plate armour (+2 pts). Army Battle Standard. 0-1.', mx=1, page='46'))
MW.append(U(CH, 'Dregator', [M('Dregator', '4 4 4 4 3 2 4 2 8', 65, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], options=MWC())],
    'Hand weapon, heavy armour and a shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts) and may wear partial plate armour (+2 pts). If on foot, may have a two-handed weapon (+2 pts).', page='46'))
MW.append(U(CH, 'Hatman', [M('Hatman', '4 5 3 4 3 2 5 2 8', 75, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield'], options=[('Ride a horse', 8), ('Ride a warhorse', 16), ('Full plate armour (replaces partial plate armour)', 2), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, partial plate armour and a shield. May be mounted on a horse (+8 pts) or a warhorse (+16 pts). May have full plate armour (+2 pts) and plate barding (+6 pts). The Hatman may only lead a unit of Western Men-at-Arms (an allied unit, documented only). 0-1.', mx=1, page='46'))
MW.append(U(CAV, 'Viteji', [M('Viteji', '8 4 4 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Bow', 'Shield', 'Horse'], rules=['Eastern Shock Cavalry'], options=[('Thrusting spear', 2), ('Heavy armour (replaces light armour)', 2), ('Partial plate armour (replaces light armour)', 4)])],
    'Hand weapon, light armour, bow, shield and a horse. May have a thrusting spear (+2 pts) and wear heavy armour (+2 pts) or partial plate armour (+4 pts). Eastern Shock Cavalry. 0-1 unit of Boyars: Viteji.', mx=1, page='46'))
MW.append(U(CAV, 'Boieri', [M('Boieri', '8 4 3 3 3 1 4 1 7', 26, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Bow', 'Shield', 'Horse'], rules=['Eastern Shock Cavalry'], options=[('Thrusting spear', 2), ('Curteni (Ld 8; every other unit)', 2), ('Heavy armour (replaces light armour; Curteni only)', 2)])],
    'Hand weapon, light armour, bow, shield and a horse. May have a thrusting spear (+2 pts). Every other unit of Boieri may be upgraded to Curteni with Ld 8 (+2 pts). Curteni may wear heavy armour (+2 pts). Eastern Shock Cavalry.', page='49'))
MW.append(U(CAV, 'Calarasi', [M('Calarasi', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Bow', 'Thrusting Spear', 'Horse'], options=[('Shield', 1), ('Javelins', 1), ('Expert Horsemen (Moldavian Calarasi)', 2)])],
    'Hand weapon, bow, thrusting spear and a horse. May have a shield (+1 pt) and javelins (+1 pt). May be Open Order or Skirmishers. Moldavian Calarasi are Expert Horsemen (+2 pts).', page='49'))
MW.append(U(INF, 'Lefegii', [M('Lefegii', '4 4 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], options=[('Heavy armour (replaces light armour)', 2), ('Thrusting spear', 2), ('Halberd', 2)])],
    'Hand weapon, light armour and shield. May have heavy armour (+2 pts) and thrusting spear or halberd (+2 pts).', page='49'))
MW.append(U(INF, 'Strajeri', [M('Strajeri', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield', 'Bow'], rules=['Mounted Infantry'], options=[('Heavy armour (replaces light armour)', 2), ('Exchange bow for thrusting spear', 0)])],
    'Hand weapon, light armour, shield and bow. May have heavy armour (+2 pts) and may replace the bow with thrusting spear (free). Mounted Infantry.', page='49'))
MW.append(U(INF, 'Pedestrasi', [M('Pedestrasi', '4 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Shield'], options=[('Light armour', 2), ('Thrusting spear', 2)])],
    'Hand weapon and shield. May have light armour (+2 pts) and thrusting spear (+2 pts).', page='49'))
MW.append(U(INF, 'Tarani', [M('Tarani', '4 2 2 3 3 1 2 1 5', 3, mn=5, weapons=['Improvised Weapon'], rules=['Peasants (Chivalry)'], options=[('Bow', 2)])],
    'Improvised weapons. May have a bow (+2 pts). Fear enemies they do not outnumber by at least two to one. They do not fear other peasants or skirmishers.', page='49'))
MW.append(U(INF, 'Razesi', [M('Razesi', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon'], rules=['Open Order', 'Hatred (Tartars and Akinjis)'], options=[('Shield', 1), ('Double-handed weapon', 2), ('Thrusting spear', 2)])],
    'Hand weapon. May have shield (+1 pt) and either two-handed weapon (+2 pts) or thrusting spear (+2 pts). Open Order, may count Rank Bonus up to +2 in the Open. Hate Tartars and Akinjis. Available in Moldavian armies only. 1+ unit.', page='49'))
MW.append(U(INF, 'Darabanti', [M('Darabanti', '5 2 3 3 3 1 3 1 6', 11, mn=5, weapons=['Double-handed Weapon'], rules=['Hidden Ambush Force', 'Skirmishers (Chivalry)'])],
    'Two-handed weapon. Hidden Ambush Force. Skirmishers. 0-2 units.', mx=2, page='49'))
MW.append(artillery_cat('49', cat=ALM, units_note=' Up to one gun for every 1,000 army points (0-1 Light Cannon per 1,000 points, counted in the Allies & Mercenaries allocation).'))
MW.append(wagon_tabor_cat('49', ' 0-1 Wagon Tabor, available in Moldavian armies only.', cat=ALM)); MW[-1]['mx'] = 1
MW_V = multi('MW', 'Moldavia & Wallachia', {
 'Moldavia': (L(Characters=25, Cavalry=(33, 100), Infantry=(25, 50), **{'Allies_&_Mercenaries': 33}), 'The Principality of Moldavia 1359-1517. Characters up to 25%, Cavalry at least 33%, Infantry 25-50%, Allies & Mercenaries up to 33% (includes 0-1 light cannon per 1,000 points). Artillery and Handgunners should be taken only in armies after 1462. Allies: Kingdom of Poland (0-1 Noble who acts as General for the Polish contingent, 0-1 Knights, Retainers, Lithuanian Light Cavalry, Infantry and Handgunners) and Kingdom of Hungary (0-1 Noble, 0-1 Knights, Hungarian/Cuman Cavalry, Szekels, Serbians, Armati, Clipeati, Crossbowmen and Handgunners); Crimean Tartars (Tartar Warriors from the Medieval Russia list) available in Moldavian armies only - all documented only.'),
 'Wallachia': (L(Characters=25, Cavalry=(25, 100), Infantry=(25, 50), **{'Allies_&_Mercenaries': 50}), 'The Principality of Wallachia 1330-1508. Characters up to 25%, Cavalry at least 25%, Infantry 25-50%, Allies & Mercenaries up to 50% (includes 0-1 light cannon per 1,000 points). Artillery and Handgunners should be taken only in armies after 1448. If Ottoman allies are chosen, the Wallachian army may not include Western Men-at-Arms and Szekels, nor take any Hungarian allies. Allies: Kingdom of Hungary (0-1 Noble who acts as General, 0-2 Knights, Hungarian/Cuman Cavalry, Szekels, Serbians, Armati, Clipeati, Crossbowmen and Handgunners), Ottoman Empire (0-1 Beylerbegh who acts as General, Sipahis, Akincis, 0-1 Janissaries (not Solaks), Volunteers and all Vassals options) and Serbian Vlastelas - documented only.')})
LISTS.append(('MW', 'Moldavia & Wallachia (Armies of Chivalry)', 'Moldavia_Wallachia_Chivalry.cat', MW, MW_V, 'ARMIES OF MOLDAVIA & WALLACHIA 1330-1517 (Armies of Chivalry, pp.46-47). Strategist: after choosing sides, the Wallachian or Moldavian general may place one additional terrain feature anywhere on the battlefield outside the enemy deployment zone. Hidden Ambush Force: at the start of deployment the player may set up units with this rule in hiding anywhere on the table that is out of sight and not in the opposing deployment zone, writing down their positions; they deploy at the start of the player\'s first turn. Allies & Mercenaries entries for Western Men-at-Arms (Superior Men-at-Arms, Free Companies), Crossbowmen (Mercenary Crossbowmen, Italian Condotta), Handgunners and Szekels (Hungary) and Serbian Vlastelas (Ottoman Turks) are documented only.'))
UNAV += [('MW', 'Razesi', ['Wallachia']), ('MW', 'Wagon Tabor', ['Wallachia'])]
OPTAV += [('MW', 'Calarasi', 'Expert Horsemen (Moldavian Calarasi)', ['Moldavia'])]
OPTRULE += [('MW', 'Calarasi', 'Expert Horsemen (Moldavian Calarasi)', 'Expert Horsemen')]
PAIRS += [('MW', ['Voievod', 'Vornic'], 'voievod-or-vornic')]
PTSLIM += [('MW', 'Light Artillery', 1000, [])]
OPT_ONCE += [('MW', [('Boieri', 'Curteni (Ld 8; every other unit)')])] if False else []
# ====================================================================== MEDIEVAL RUSSIAN STATES (book pp.48-49)
RU = []; VAS = 'Vassals, Allies & Mercenaries'
RUO = lambda foot=True: [('Ride a warhorse', 16), ('Thrusting spear', 2), ('Partial plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4)] + ([('Double-handed weapon', 2)] if foot else [])
RUH = ['Hand Weapon', 'Heavy Armour', 'Shield']
RU.append(U(CH, 'Kniaz', [M('Kniaz', '4 5 5 4 4 3 5 3 9', 170, weapons=RUH, rules=['Army General', 'Stubborn (if dismounted)'], options=RUO() + [('Veliki Kniaz (WS6, I6; Eastern armies only)', 15)])],
    'Hand weapon, heavy armour and shield. May ride a warhorse (+16 pts). May have a thrusting spear (+2 pts), partial plate armour (+2 pts) and cloth barding (+4 pts). If on foot, may have a two-handed weapon (+2 pts). May take either the Kniaz or the Voyvoda as the Army General. Stubborn if on foot. In Eastern Russian armies a Kniaz may be upgraded to Veliki Kniaz (+15 pts, WS6, I6); a Veliki Kniaz may only lead a unit of Senior Druzhniks.', mx=1, page='48'))
RU.append(U(CH, 'Voyvoda', [M('Voyvoda', '4 5 5 4 3 2 5 3 8', 140, weapons=RUH, rules=['Army General', 'Stubborn (if dismounted)'], options=RUO())],
    'Hand weapon, heavy armour and shield. May ride a warhorse (+16 pts). May have a thrusting spear (+2 pts), partial plate armour (+2 pts) and cloth barding (+4 pts). If on foot, may have a two-handed weapon (+2 pts). May take either the Kniaz or the Voyvoda as the Army General. Stubborn if on foot.', mx=1, page='48'))
RU.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 5 4 3 2 5 2 8', 90, weapons=RUH, rules=['Army Standard'], options=[('Ride a horse', 8), ('Ride a warhorse', 16), ('Thrusting spear', 2), ('Partial plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, heavy armour and shield. May ride a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts), partial plate armour (+2 pts) and cloth barding (+4 pts). Army Battle Standard. 0-1.', mx=1, page='48'))
for nm, st, pt in (('Boyar', '4 5 5 4 3 2 5 2 8', 75), ('Pomestnik', '4 4 4 4 3 2 4 2 8', 65)):
    RU.append(U(CH, nm, [M(nm, st, pt, weapons=RUH, options=[('Ride a horse', 8)] + RUO())],
    'Hand weapon, heavy armour and shield. May ride a horse (+8 pts) or a warhorse (+16 pts). May have a thrusting spear (+2 pts), partial plate armour (+2 pts) and cloth barding (+4 pts). If on foot, may have a two-handed weapon (+2 pts).', page='48'))
RU.append(U(CAV, 'Senior Druzhina', [M('Senior Druzhnik', '8 4 4 3 3 1 4 1 8', 32, mn=5, weapons=RUH + ['Thrusting Spear', 'Warhorse'], rules=['First Charge (Chivalry)', 'Eastern Shock Cavalry'], options=[('Bow', 3), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, thrusting spear, heavy armour, shield and warhorse. May have a bow (+3 pts) and cloth barding (+4 pts). First Charge. Eastern Shock Cavalry. At least one unit of Junior Druzhniks must be taken if the army includes a unit of Senior Druzhniks. 0-1 unit. (Eastern Russian States.)', mx=1, page='48'))
RU.append(U(CAV, 'Senior Druzhina (Western)', [M('Senior Druzhnik', '8 4 4 3 3 1 4 1 8', 36, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)', 'Eastern Shock Cavalry'], options=[('Cloth barding (-1 M)', 4)])],
    'Hand weapon, partial plate armour, lance, shield and warhorse. May have cloth barding (+4 pts); may not take a bow. First Charge. Eastern Shock Cavalry. At least one unit of Junior Druzhniks must be taken if the army includes a unit of Senior Druzhniks. In armies of the Western Russian States Senior Druzhniks cost 36 points. 0-1 unit.', mx=1, page='48'))
RU.append(U(CAV, 'Junior Druzhina', [M('Junior Druzhnik', '8 4 3 3 3 1 4 1 7', 29, mn=5, weapons=RUH + ['Thrusting Spear', 'Warhorse'], rules=['Superior Shock Cavalry'], options=[('Bow', 2), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, thrusting spear, heavy armour, shield and warhorse. May have a bow (+2 pts) and cloth barding (+4 pts). Superior Shock Cavalry.', page='49'))
RU.append(U(CAV, 'Junior Druzhina (Western)', [M('Junior Druzhnik', '8 4 3 3 3 1 4 1 7', 33, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Shield', 'Lance', 'Warhorse'], rules=['Superior Shock Cavalry'], options=[('Cloth barding (-1 M)', 4)])],
    'Hand weapon, partial plate armour, lance, shield and warhorse. May have cloth barding (+4 pts); may not take a bow. Superior Shock Cavalry. In armies of the Western Russian States Junior Druzhniks cost 33 points.', page='49'))
RU.append(U(INF, 'Dismounted Druzhina', [M('Dismounted Druzhnik', '4 4 3 3 3 1 4 1 8', 17, mn=5, weapons=RUH + ['Thrusting Spear'], rules=['Shieldwall', 'Stubborn (if led by Kniaz)'], options=[('Exchange thrusting spear for double-handed weapon', 0), ('Partial plate armour (replaces heavy armour)', 1)])],
    'Hand weapon, thrusting spear, heavy armour and shield. May replace thrusting spear with two-handed weapon (free) and may take partial plate armour (+1 pt). Shieldwall. Stubborn if led by a Kniaz. Dismounted Druzhniks may only be taken in the armies of the Western Russian States. 0-1 unit.', mx=1, page='49'))
RU.append(U(CAV, 'Horse Archers', [M('Horse Archer', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Bow', 'Shield', 'Horse'], options=[('Thrusting spear', 2), ('Light armour', 2), ('Expert Horsemen (Eastern armies only)', 2)])],
    'Hand weapon, bow, shield and a horse. May take a thrusting spear (+2 pts) and light armour (+2 pts). May be Open Order or Skirmishers. In armies of the Eastern Russian States, may be upgraded to Expert Horsemen (+2 pts).', page='49'))
RU.append(U(INF, 'Urban Footman', [M('Urban Footman', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour'], rules=['Combined Formation (Chivalry)'], options=[('Thrusting spear', 2), ('Two-handed weapon in place of shield', 1)])],
    'Hand weapon, shield and light armour. May take a thrusting spear (+2 pts) or replace shield with a two-handed weapon (+1 pt). Combined Formation - may have up to 50% Urban Militia Archers in the rear ranks of the unit.', page='49'))
RU.append(U(ARC, 'Urban Archers', [M('Urban Archer', '4 3 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Open Order', 'Combined Formation (Chivalry)'], options=[('Light armour', 2)])],
    'Hand weapon and a bow. May have light armour (+2 pts). Open Order. Combined Formation with Urban Militia Footmen, in which case they are no longer Open Order.', page='49'))
RU.append(U(ARC, 'Militia Crossbow', [M('Militia Crossbowman', '4 3 3 3 3 1 3 1 6', 9, mn=5, weapons=['Hand Weapon', 'Crossbow'], rules=['Open Order'], options=[('Light armour', 2), ('Pavise', 2)])],
    'Hand weapon and crossbow. May have light armour (+2 pts) and pavise (+2 pts). Open Order.', page='49'))
RU.append(U(INF, 'Smerdys', [M('Smerdys', '4 2 2 3 3 1 2 1 5', 3, mn=5, weapons=['Improvised Weapon'], rules=['Peasants (Chivalry)'], options=[('Bow (instead of shield)', 2), ('Shield', 1)])],
    'Improvised weapons. May have either a bow (+2 pts) or a shield (+1 pt). Rural Levies: Fear enemies they do not outnumber by at least two to one. They do not fear other levies or skirmishers.', page='49'))
RU.append(U(CAV, 'Tartar Nobles', [M('Tartar Noble', '8 4 3 3 3 1 4 1 7', 30, mn=5, weapons=['Hand Weapon', 'Bow', 'Light Armour', 'Thrusting Spear', 'Horse'], rules=['Open Order', 'Nomad Cavalry'], options=[('Shield', 2), ('Barding (half, -1 M)', 4)])],
    'Hand weapon, bow, light armour, thrusting spear and horse. May have a shield (+2 pts) and half-barding (+4 pts). Open Order and Nomad Cavalry. Tartar Nobles may only be taken in the armies of the Eastern Russian States. 0-1 unit.', mx=1, page='49'))
RU.append(U(CAV, 'Tartar Warriors', [M('Tartar Warrior', '8 3 3 3 3 1 4 1 6', 21, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Nomad Cavalry'], options=[('Thrusting spear', 2), ('Light armour', 2), ('Shield', 2)])],
    'Hand weapon and bow. May have a thrusting spear (+2 pts), light armour (+2 pts) and a shield (+2 pts). May be Open Order or Skirmishers. Nomad Cavalry. Tartar Warriors may only be taken in the armies of the Eastern Russian States. At least one unit of Tartar Warriors must be taken for every unit of Tartar Nobles in the army.', page='49'))
RU.append(U(ARC, 'Handgunners', [M('Handgunner', '4 3 3 3 3 1 2 1 7', 11, mn=5, weapons=['Hand Weapon', 'Handgun'], rules=['Open Order'], options=[('Light armour', 2)])],
    'Hand weapon and handgun. May have light armour (+2 pts). Open Order. Only one unit of Handgunners may be taken in armies of the Eastern Russian States. Only after 1425 (Eastern) / 1380 (Western).', page='49'))
RU.append(U(CAV, 'Western Knights', [M('Mounted Crusader Knight', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['Impetuous', 'First Charge (Chivalry)', 'Allies and Mercenaries (Chivalry)'], options=[('Lance', 4), ('Partial plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4)])],
    'See the entry for Mounted Crusader Knights in the Teutonic Order list (approximated here: hand weapon, heavy armour, shield, warhorse; lance +4, partial plate free, cloth barding +4). Allies & Mercenaries. Western Knights may only be taken in the armies of the Western Russian States. 0-1 unit.', mx=1, page='49'))
RU.append(artillery_cat('49', cat=VAS, units_note=' Up to one gun for every 1,000 army points in Western Russian States armies and up to one gun for every 1,500 army points in Eastern Russian States armies.'))
RU_V = multi('RU', 'Medieval Russian States', {
 'Eastern Russian States': (L(Characters=25, Cavalry=(33, 100), Infantry=(25, 50) if False else 50, **{'Vassals,_Allies_&_Mercenaries': 33}), 'Muscovy, Vladimir, Suzdal, Ryazan, Tver. Characters up to 25%, Cavalry at least 33%, Infantry up to 50%, Vassals, Allies & Mercenaries up to 33% (includes 0-1 light cannon for every 1,500 pts). Handgunners and Artillery should be taken only after 1425. If Allies from the Western Russian States are taken, no Tartar Nobles or Tartar Warriors may be taken. Allies (documented only): Western Russian States - 0-1 Boyar (acts as General for the Western contingent), Junior Druzhniks, Dismounted Druzhniks, Horse Archers and all Urban Militia units.'),
 'Western Russian States': (L(Characters=25, Cavalry=50, Infantry=(33, 100), **{'Vassals,_Allies_&_Mercenaries': 25}), 'Novgorod, Pskov, Galych. Characters up to 25%, Cavalry up to 50%, Infantry at least 33%, Vassals, Allies & Mercenaries up to 25% (includes 0-1 light cannon for every 1,000 pts). Handgunners and Artillery should be taken only after 1380. Allies (documented only): Eastern Russian States - 0-1 Boyar (acts as General for the Eastern contingent), Junior Druzhniks, Horse Archers, all Urban Militia units and Tartar Warriors.')})
LISTS.append(('RU', 'Medieval Russian States (Armies of Chivalry)', 'Russian_States_Chivalry.cat', RU, RU_V, 'ARMIES OF THE MEDIEVAL RUSSIAN STATES 1276-1501 (Armies of Chivalry, pp.48-49). Shieldwall: units that benefit from the Shieldwall special rule may form a Shieldwall instead of moving, causing all enemy attacks from the front to suffer -1 to hit (shooting and hand-to-hand), lasting until the unit moves or is defeated in hand-to-hand combat. Superior Shock Cavalry and Eastern Shock Cavalry as given in the army rules.'))
UNAV += [('RU', n, ['Western Russian States']) for n in ('Senior Druzhina', 'Junior Druzhina', 'Tartar Nobles', 'Tartar Warriors')]
UNAV += [('RU', n, ['Eastern Russian States']) for n in ('Senior Druzhina (Western)', 'Junior Druzhina (Western)', 'Dismounted Druzhina', 'Western Knights')]
OPTAV += [('RU', 'Kniaz', 'Veliki Kniaz (WS6, I6; Eastern armies only)', ['Eastern Russian States']), ('RU', 'Horse Archers', 'Expert Horsemen (Eastern armies only)', ['Eastern Russian States'])]
OPTRULE += [('RU', 'Horse Archers', 'Expert Horsemen (Eastern armies only)', 'Expert Horsemen')]
PAIRS += [('RU', ['Kniaz', 'Voyvoda'], 'kniaz-or-voyvoda')]
OPTSTAT += [('RU', 'Kniaz', 'Veliki Kniaz (WS6, I6; Eastern armies only)', 'WS', 6)]
PTSLIM += [('RU', 'Light Artillery', 1000, [])]
# ====================================================================== HUNGARY (book pp.50-51)
HU = []
HUF = [('Full plate armour, if mounted (replaces partial plate armour)', 0), ('Full plate armour, if dismounted (replaces partial plate armour)', 2)]
HUB = [('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
HUP = ['Hand Weapon', 'Partial Plate Armour', 'Shield']
HU.append(U(CH, 'King/General', [M('General', '4 6 3 4 3 3 6 2 9', 160, weapons=HUP, rules=['Army General', 'Stubborn (if with Royal Banderium)'], options=HUF + [('Lance', 4), ('Halberd', 4), ('Double-handed weapon', 4)] + HUB)],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). May have a lance (+4 pts) and must have a horse (free) or warhorse (+4 pts) if mounted. May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted. The warhorse may have cloth (+4 pts) or plate (+6 pts) barding. Army General. Stubborn if with the Royal Banderium. 0-1.', mx=1, page='50'))
HU.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 4 3 2 5 2 8', 100, weapons=HUP, rules=['Army Standard', 'Stubborn (if with Royal Banderium)'], options=HUF + HUB)],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). Must have a horse (free) or warhorse (+4 pts) if mounted. The warhorse may have cloth (+4 pts) or plate (+6 pts) barding. Army Standard Bearer. Stubborn if with the Royal Banderium. 0-1.', mx=1, page='50'))
HU.append(U(CH, 'Noble', [M('Noble', '4 5 3 4 3 2 5 2 8', 75, weapons=HUP, options=HUF + [('Lance', 4), ('Halberd', 4), ('Double-handed weapon', 4)] + HUB)],
    'Hand weapon, partial plate armour and shield. May wear full plate armour (free if mounted, +2 pts if dismounted). May have a lance (+4 pts) and must have a horse (free) or warhorse (+4 pts) if mounted. May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted. The warhorse may have cloth (+4 pts) or plate (+6 pts) barding.', page='50'))
HU.append(U(CH, 'Religious Personality', [M('Religious Personality', '4 3 3 3 3 2 4 2 6', 60, weapons=['Hand Weapon'], rules=['Warband', 'Frenzy (Religious Personality)'], options=[('Double-handed weapon', 4)])],
    'Hand weapon. May have a double-handed weapon (+4 pts). Warband. The Religious Personality must lead one unit of Crusading Peasants. The Religious Personality and his unit are subject to frenzy. Frenzy is lost either by the Religious Personality\'s death, or by the unit being broken in combat. Any other Crusading Peasant units within 12" of the Religious Personality may use his Leadership. 0-1.', mx=1, page='50'))
HU.append(U(CAV, 'Hungarian Knights (Mounted)', [M('Mounted Knight', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)'],
    options=plates(True, 2, 4) + [('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6), ('Royal Banderium (WS5, Stubborn; one unit)', 6)])],
    'Hand weapon, heavy armour, shield, lance and a warhorse. The warhorse may have cloth (+4 pts) or plate (+6 pts) barding. May wear partial plate (mounted free) or full plate armour (mounted free). First Charge. One unit may be upgraded to WS5 and Stubborn as Royal Banderium (+6 pts).', page='50'))
HU.append(U(CAV, 'Hungarian Knights (Dismounted)', [M('Dismounted Knight', '4 4 3 3 3 1 4 1 8', 12, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'],
    options=plates(True, 2, 4)[1::2] + [('Halberd', 2), ('Double-handed weapon', 2), ('Royal Banderium (WS5, Stubborn; one unit)', 6)])],
    'Hand weapon, heavy armour and shield. May wear partial plate (+2 pts) or full plate armour (+4 pts). May have a halberd (+2 pts) or a double-handed weapon (+2 pts). One unit may be upgraded to WS5 and Stubborn as Royal Banderium (+6 pts).', page='50'))
HU.append(U(CAV, 'German/Bohemian Mercenary Knights', [M('Mercenary Knight', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Heavy Armour', 'Shield', 'Horse'], rules=['Allies and Mercenaries (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, thrusting spear, heavy armour, shield and horse. May wear partial plate or full plate armour (free, shield optional). The horse may have cloth (+4 pts) or plate (+6 pts) barding. May count Rank Bonus of up to +2 in combat.', page='51'))
HU.append(U(CAV, 'Hungarian/Cuman Cavalry', [M('Hungarian/Cuman', '8 2 3 3 3 1 4 1 6', 20, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Nomad Cavalry'], options=[('Buckler', 2)])],
    'Horse, hand weapon and bow. May have a buckler (+2 pts). Skirmishers and Nomad Cavalry.', page='51'))
HU.append(U(CAV, 'Szekeler Cavalry', [M('Szekeler', '8 3 3 3 3 1 4 1 7', 24, mn=5, weapons=['Horse', 'Bow', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Open Order', 'Expert Horsemen', 'Feigned Flight', 'Parthian Shot'])],
    'Horse, bow, thrusting spear, light armour and shield. Open Order and Expert Horsemen with Feigned Flight and Parthian Shot.', page='51'))
HU.append(U(CAV, 'Serbian Cavalry', [M('Serbian', '8 3 3 3 3 1 4 1 7', 17, mn=5, weapons=['Horse', 'Lance', 'Shield'], rules=['Open Order'], options=[('Light armour', 3)])],
    'Horse, lance and shield. May have light armour (+3 pts). Open Order.', page='51'))
HU.append(U(CAV, 'Tartar Warriors', [M('Tartar Warrior', '8 3 3 3 3 1 4 1 6', 21, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Nomad Cavalry'], options=[('Thrusting spear', 2), ('Light armour', 2), ('Shield', 2)])],
    'See the Tartar Warriors entry in the Armies of the Medieval Russian States list: hand weapon and bow; thrusting spear (+2 pts), light armour (+2 pts) and shield (+2 pts); Open Order or Skirmishers; Nomad Cavalry.', page='51'))
HU.append(U(INF, 'Armati', [M('Armati', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Halberd', 'Heavy Armour'], rules=['Veteran', 'Mixed Armour'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Shield', 1)])],
    'Halberd and heavy armour. May wear partial plate armour (+2 pts) and carry a shield (+1 pt). Veteran. May be in Mixed Order with Crossbowmen or Handgunners.', page='51'))
HU.append(U(INF, 'Clipeati', [M('Clipeati', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Thrusting Spear', 'Light Armour', 'Large Shield'], rules=['Mixed Order (Chivalry)'])],
    'Thrusting spear, light armour and large shield. May be in Mixed Order with Crossbowmen or Handgunners.', page='51'))
HU.append(U(ARC, 'Crossbowmen/Handgunners', [M('Crossbowman/Handgunner', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], options=[('Exchange crossbow for handgun', 0), ('Pavise', 1)])],
    'Crossbow or handgun, hand weapon and light armour. May have a pavise (+1 pt).', page='51'))
HU.append(U(ARC, 'Archers', [M('Archer', '4 2 3 3 3 1 3 1 5', 6, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Skirmishers (Chivalry)'])],
    'Bow and hand weapon. Skirmishers.', page='51'))
HU.append(U(INF, 'Crusading Peasants', [M('Peasant', '4 1 1 3 3 1 3 1 5', 3, mn=5, weapons=['Improvised Weapon'], rules=['Warband'])],
    'Improvised weapons. Warband.', page='51'))
HU.append(artillery('51', units_note=' May have one gun per 750 army points (bought from the Infantry allocation).'))
HU.append(war_wagon('51', ' May have one War Wagon per 1,000 army points (bought from the Infantry allocation).'))
HU_V = single('HU', 'The Kingdom of Hungary', L(Characters=25, Cavalry=(25, 50), Infantry=(25, 50)), 'Characters 0-25%, Cavalry 25-50%, Infantry 25-50%. Artillery and War Wagons are bought from the Infantry allocation. Allies 0-25%: may have Moldavian/Wallachian, Polish, or Hundred Years War French allies (documented only); Moldavians/Wallachians are subject to the Allies & Mercenaries rule.')
LISTS.append(('HU', 'Kingdom of Hungary (Armies of Chivalry)', 'Hungary_Chivalry.cat', HU, HU_V, 'THE KINGDOM OF HUNGARY 1307-1526 (Armies of Chivalry, pp.50-51). Allies (Moldavian/Wallachian, Polish, Hundred Years War French) are documented only.'))
PTSLIM += [('HU', 'Light Artillery', 750, []), ('HU', 'War Wagon', 1000, [])]
OPTRULE += []
# ====================================================================== OTTOMAN TURKS (book pp.52-53)
OT = []; GH = 'Ghazi Ottomans'; CQ = 'Conquest Ottomans'
OTC = 'Ottoman Cavalry'; TKC = 'Turkoman & Akincis Cavalry'; VOL = 'Volunteers'; JAN = 'Janissaries'; VAS2 = 'Vassals'; ART = 'Artillery'
GHZ = ('Ghazi (+1 pt per model)', 1)
def _ot_chars():
    o = [('Shield', 2), ('Light armour', 3), (HEAVY.replace('light armour', 'light armour'), 4), ('Thrusting spear', 2), ('Bow', 3), ('Ride a horse', 8), ('Barding (half, -1 M)', 4), ('Cloth barding (-1 M)', 4)]
    return o
OTH = ['Hand Weapon']
OT.append(U(CH, 'Amir/Sultan', [M('Amir/Sultan', '4 4 5 4 3 3 5 2 9', 135, weapons=OTH, rules=['Army General'], options=_ot_chars())],
    'Hand weapon. May have shield (+2 pts), light armour (+3 pts), heavy armour (+4 pts), thrusting spear (+2 pts) and bow (+3 pts). May ride a horse (+8 pts) and take half-barding (+4 pts) or cloth barding (+4 pts). The Amir or Sultan is the Army General. 0-1.', mx=1, page='52'))
OT.append(U(CH, 'Beylerbegh', [M('Beylerbegh', '4 5 4 4 3 2 6 2 8', 75, weapons=OTH, options=_ot_chars() + [('Army Standard Bearer (no spear)', 15)])],
    'Hand weapon. May have shield (+2 pts), light armour (+3 pts), heavy armour (+4 pts), thrusting spear (+2 pts) and bow (+3 pts). May ride a horse (+8 pts) and take half-barding (+4 pts) or cloth barding (+4 pts). One Beylerbegh without spear may be upgraded to Army Standard Bearer (+15 pts).', page='52'))
OT.append(U(CH, 'Mehterhane', [M('Mehterhane', '4 3 3 3 3 2 4 1 8', 20, weapons=OTH, rules=['Mehterhane'], options=[('Ride a horse', 8)])],
    'A hand weapon, and some sort of hellish musical instrument. May ride a horse (+8 pts). The Mehterhane characters must be placed in the same unit as the Army General; the unit is immune to panic and for every Mehterhane model in the unit 1" is added to the Army General\'s Leadership radius, up to a maximum of +3". 0-3.', mx=3, page='52'))
OT.append(U(OTC, 'Kapikulu', [M('Kapikulu', '8 4 4 3 3 1 4 1 8', 26, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Thrusting Spear', 'Horse'], rules=['Open Order'],
    options=[('Light armour', 2), ('Heavy armour (replaces light armour)', 3), ('Drilled', 1), ('Barding (half, -1 M)', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, shield, bow and thrusting spear. May have light armour (+2 pts), heavy armour (+3 pts) and may be Drilled (+1 pt). May also have either half-barding (+4 pts) or cloth barding (+4 pts). Open Order. With heavy armour they are Eastern Shock Cavalry; otherwise subject to Eastern Shock Cavalry rule 1. May only be chosen if an Army General has been chosen as well. 0-1 unit.', mx=1, page='53'))
OT.append(U(OTC, 'Sipahis', [M('Sipahi', '8 3 4 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Thrusting Spear', 'Horse'], rules=['Open Order'],
    options=[('Light armour', 2), ('Heavy armour (replaces light armour; every other unit; Conquest only)', 3), ('Drilled', 1)])],
    'Hand weapon, shield, bow and thrusting spear. May have light armour (+2 pts). Every other unit of Sipahis may have heavy armour (+3 pts) and may be Drilled (+1 pt). Open Order. With heavy armour they are Eastern Shock Cavalry; otherwise subject to Eastern Shock Cavalry rule 1. Ghazi armies: 0-2 Sipahi units, which may not take heavy armour; Conquest armies: at least one unit of Sipahis must be chosen.', page='53'))
OT.append(U(TKC, 'Turkoman Cavalry', [M('Turkoman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Parthian Shot', 'Feigned Flight'], options=[('Thrusting spear', 2), GHZ])],
    'Hand weapon, shield and bow. May have thrusting spear (+2 pts). Skirmishers, Parthian Shot and Feigned Flight. Turkoman Cavalry are chosen in Ghazi armies.', page='53'))
OT.append(U(TKC, 'Akincis Cavalry', [M('Akinci', '8 2 3 3 3 1 3 1 5', 15, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Parthian Shot', 'Feigned Flight'], options=[('Thrusting spear', 2)])],
    'Hand weapon, shield and bow. May have thrusting spear (+2 pts). Skirmishers, Parthian Shot and Feigned Flight. Akincis are chosen in Conquest armies.', page='53'))
OT.append(U(JAN, 'Janissaries', [M('Janissary', '5 3 4 3 3 1 4 1 7', 12, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow'], rules=['Open Order', 'Mixed Order (Chivalry)', 'Camels', 'Ottoman Wagon Tabor', 'Janissary Panic'],
    options=[('Exchange bow for halberd', 0), ('Drilled', 1), ('Bow in addition to halberd', 2), ('Exchange bow for crossbow (0-2 units)', 2), ('Exchange bow for handgun (0-2 units)', 2),
             ('Stakes (+30 pts per unit)', 0), ('Camels (+10 pts per unit)', 0), ('Solak Janissaries (one unit; +3 pts)', 3)])],
    'Hand weapon, shield, and either bow or halberd. May be Drilled (+1 pt). Halberdiers may have bows (+2 pts). In 0-2 units, models without halberds may exchange bow for either crossbow (+2 pts), or handgun (+2 pts). Janissary Halberdiers may combine in Mixed Order with Janissaries solely armed with missile weapons. May have Stakes (+30 pts per unit), or Camels (+10 pts per unit), or defend an Ottoman Wagon Tabor. One unit may be Solak Janissaries (+3 pts), who are Stubborn; the Solaks must be led by the Army General and must be the smallest Janissary unit in the army. Open Order (count Rank Bonus up to +2 in open ground). Janissaries may re-roll their first failed Panic test. Can only be chosen if an Army General has been chosen as well. Conquest armies only.', page='53'))
OT.append(U(VOL, 'Volunteers (Gonullu, Azab, Yaya)', [M('Volunteer', '5 2 2 3 3 1 2 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Open Order', 'Warband'],
    options=[('Exchange javelins for throwing spear', 1), ('Exchange javelins for bow', 1), ('Stakes (+20 pts per unit)', 0), ('Camels (+10 pts per unit)', 0), GHZ])],
    'Hand weapon, javelins, and shield. May take throwing spear (+1 pt), or bow (+1 pt) instead of javelins. Deployment options: may either place Stakes (+20 pts per unit), or have Camels (+10 pts per unit). Formed Volunteers: Open Order, Warband; either Stakes or Camels.', page='53'))
OT.append(U(VOL, 'Volunteer Skirmishers', [M('Volunteer Skirmisher', '5 2 2 3 3 1 2 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Skirmishers (Chivalry)', 'Warband'],
    options=[('Exchange javelins for sling', 0), ('Exchange javelins for bow', 1), ('Exchange javelins for crossbow (0-2 units)', 4), ('Exchange javelins for handgun (0-2 units)', 4), GHZ])],
    'Volunteers may be designated as Skirmishers (free). Skirmishers may take either sling (free), or bow (+1 pt) instead of javelins. 0-2 Skirmisher units may take crossbow (+4 pts), or handgun (+4 pts) instead of javelins. Volunteer Skirmisher models with handguns and crossbows may not outnumber Volunteer Skirmisher models with other weapons. Handguns are not available in Ghazi armies.', page='53'))
OT.append(U(VAS2, 'Serbian Vlastelas', [M('Vlastela', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Lance', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['First Charge (Chivalry)', 'Allies and Mercenaries (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 1), ('Full plate armour (replaces heavy armour)', 1), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, lance, heavy armour, shield, and warhorse. May have partial plate or full plate armour instead of heavy armour (+1 pt), and cloth barding (+4 pts). First Charge. Vlastelas must always pursue enemy units that they have defeated in close combat. 0-2 units.', mx=2, page='53'))
OT.append(U(VAS2, 'Balkan or Anatolian Tribesmen', [M('Mountain Tribesman', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Open Order', 'Mixed Weapons'], options=[('Shield (replaces buckler)', 1)])],
    'Use the Mountain Tribesmen entry (see the rulebook, page 130). Double-handed weapons may not be chosen. 0-2 units. Stats from the rulebook Mountain Tribesmen entry.', mx=2, page='53'))
OT.append(artillery_cat('53', cat=ART, units_note=' Conquest Ottoman artillery: Master Gunners (+20 pts per cannon) and frontal plates (+10 pts per cannon) may be added (documented only); the artillery may be placed in the 3" intervals between the Tabor wagons.'))
OT.append(wagon_tabor_cat('53', ' Ottoman Wagon Tabor: in Conquest Ottoman armies the Janissaries replace the regular wagon defenders; the Army General, the Army Standard Bearer and all the Janissaries must deploy inside; the wagons are paid for out of the Janissary allowance.', cat=JAN)); OT[-1]['mx'] = 1
OT_V = multi('OT', 'The Ottoman Turks', {
 GH: (L(Characters=25, **{'Turkoman_&_Akincis_Cavalry': (50, 100), 'Volunteers': 15, 'Vassals': 100}), 'Ghazi Ottomans c.1280-1361. Characters up to 25%, Turkoman Cavalry at least 50%, Volunteers up to 15% (no handguns), Ottoman Cavalry 0-2 Sipahi units (may not take heavy armour), Vassals 0-2 units of Mountain Tribesmen. Ghazi special rule: any unit may be upgraded to Ghazis for +1 pt per model; Ghazis may re-roll their first failed Panic test.'),
 CQ: (L(Characters=25, **{'Ottoman_Cavalry': (25, 100), 'Turkoman_&_Akincis_Cavalry': 15, 'Volunteers': 25, 'Janissaries': 33, 'Vassals': 50, 'Artillery': 10}), 'Conquest Ottomans 1361-1517. Characters up to 25%, Ottoman Cavalry at least 25% (at least one unit of Sipahis), Akincis up to 15% (10% minimum if no Infantry including Vassals are taken), Volunteers up to 25% (10% minimum if any Infantry including Vassals are taken), Janissaries up to 33%, Vassals up to 50%, Artillery up to 10%. Special rule: all Ottoman artillery may be equipped with Master Gunners at +20 pts per cannon.')})
LISTS.append(('OT', 'The Ottoman Turks (Armies of Chivalry)', 'Ottoman_Turks_Chivalry.cat', OT, OT_V, 'THE OTTOMAN TURKS c.1280-1517 (Armies of Chivalry, pp.52-53). Mehterhane: the Mehterhane characters must be placed in the same unit as the Army General; the unit is immune to panic and each Mehterhane model adds 1" to the General\'s Leadership radius (max +3"). Camels: place kneeling or standing camel models in base contact with the rear of the unit; formed units with Camels cause fear in enemy cavalry; if the unit charges or flees the camels are removed and it no longer causes fear. Vassals documented only: 0-2 Byzantine Regular Pronoiarios (Last Byzantines list), 0-2 Balkan Cavalry (Serbians from Hungary and/or Wallachian Calarasi), 0-1 Voynuks (Regular & Militia infantry from Moldavia/Wallachia), 0-2 Vassal Archers (Archers, Hungary list).'))
UNAV += [('OT', n, [GH]) for n in ('Kapikulu', 'Akincis Cavalry', 'Janissaries', 'Serbian Vlastelas', 'Light Artillery', 'Wagon Tabor')] + [('OT', 'Turkoman Cavalry', [CQ])]
OPTAV += [('OT', n, o, [GH]) for n, o in (('Turkoman Cavalry', GHZ[0]), ('Volunteers (Gonullu, Azab, Yaya)', GHZ[0]), ('Volunteer Skirmishers', GHZ[0]))]
OPTAV += [('OT', 'Sipahis', 'Heavy armour (replaces light armour; every other unit; Conquest only)', [CQ]), ('OT', 'Volunteer Skirmishers', 'Exchange javelins for handgun (0-2 units)', [CQ])]
OPTRULE += [('OT', n, GHZ[0], 'Ghazi') for n in ('Turkoman Cavalry', 'Volunteers (Gonullu, Azab, Yaya)', 'Volunteer Skirmishers')]
OPTRULE += [('OT', 'Janissaries', 'Solak Janissaries (one unit; +3 pts)', 'Stubborn'), ('OT', 'Janissaries', 'Stakes (+30 pts per unit)', 'Stakes'), ('OT', 'Volunteers (Gonullu, Azab, Yaya)', 'Stakes (+20 pts per unit)', 'Stakes'),
            ('OT', 'Janissaries', 'Drilled', 'Drilled'), ('OT', 'Kapikulu', 'Drilled', 'Drilled'), ('OT', 'Sipahis', 'Drilled', 'Drilled'), ('OT', 'Beylerbegh', 'Army Standard Bearer (no spear)', 'Army Standard')]
FLAT += [('OT', 'Janissaries', 'Stakes (+30 pts per unit)', 30), ('OT', 'Janissaries', 'Camels (+10 pts per unit)', 10), ('OT', 'Volunteers (Gonullu, Azab, Yaya)', 'Stakes (+20 pts per unit)', 20), ('OT', 'Volunteers (Gonullu, Azab, Yaya)', 'Camels (+10 pts per unit)', 10)]
OPT_ONCE += [('OT', [('Beylerbegh', 'Army Standard Bearer (no spear)')]), ('OT', [('Janissaries', 'Solak Janissaries (one unit; +3 pts)')])]
PTSLIM += []
UNIT_MAX_IN += [('OT', 'Sipahis', 2, [GH])]
# ====================================================================== THE LAST BYZANTINES (book pp.54-55)
BY = []; AM = 'Allies & Mercenaries'
BYO = [('Shield', 2), ('Light armour', 3), ('Heavy armour', 4), ('Throwing spear', 2), ('Thrusting spear', 2), ('Ride a warhorse', 16), ('Lance (mounted)', 6), ('Barding (half, -1 M)', 4), ('Barding (plate, -1 M)', 6)]
PERM = ('Permanent Mercenaries (+2 pts per model; 1 unit per 1,000 pts)', 2)
BY.append(U(CH, 'Megas Domestikos', [M('Megas Domestikos', '4 5 5 4 3 3 5 2 9', 135, weapons=['Hand Weapon'], rules=['Army General'], options=BYO)],
    'Hand weapon. May ride a warhorse (+16 pts). May have shield (+2 pts), light armour (+3 pts) or heavy armour (+4 pts), and throwing or thrusting spear (+2 pts). Mounted characters may have lance (+6 pts), and half-barding (+4 pts), or plate barding (+6 pts). The Megas Domestikos is the Army General. 0-1.', mx=1, page='55'))
BY.append(U(CH, 'Noble', [M('Noble', '4 4 4 4 3 2 4 2 8', 55, weapons=['Hand Weapon'], options=BYO + [('Army Standard Bearer (no spear/lance)', 25)])],
    'Hand weapon. May ride a warhorse (+16 pts). May have shield (+2 pts), light armour (+3 pts) or heavy armour (+4 pts), and throwing or thrusting spear (+2 pts). Mounted characters may have lance (+6 pts), and half-barding (+4 pts), or plate barding (+6 pts). One Noble without spear/lance may be upgraded to Army Standard Bearer (+25 pts).', page='55'))
KV = ['Hand Weapon', 'Thrusting Spear', 'Light Armour', 'Shield']
BY.append(U(CAV, 'Guards (Mounted)', [M('Guard', '8 4 3 3 3 1 4 1 8', 23, mn=5, weapons=KV + ['Horse'], rules=['Eastern Shock Cavalry (if heavy armour)', 'Open Order (if no heavy armour)'], options=[('Heavy armour (replaces light armour)', 1), ('Lance', 4), ('Barding (half, -1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, thrusting spear, light armour, and shield. May have heavy armour (+1 pt), lance (+4 pts), and either half-barding (+4 pts) or plate barding (+6 pts). Mounted Kavallarioi with heavy armour are Eastern Shock Cavalry, except Kavallarioi with lances who may count their rank bonus up to a maximum of +1. Mounted Kavallarioi without heavy armour are Open Order. If Elite Pronoiarios or Guards are chosen, at least one unit of Regular Pronoiarios must be chosen as well. 0-1 unit (mounted or dismounted).', mx=1, page='55'))
BY.append(U(CAV, 'Guards (Dismounted)', [M('Dismounted Guard', '4 4 3 3 3 1 4 1 8', 12, mn=5, weapons=KV, options=[('Heavy armour (replaces light armour)', 1)])],
    'Guards may fight on foot (-11 pts, reduce Movement to 4). Hand weapon, thrusting spear, light armour, and shield, and may have heavy armour (+1 pt). 0-1 unit (mounted or dismounted).', mx=1, page='55'))
BY.append(U(CAV, 'Elite Pronoiarios (Mounted)', [M('Elite Pronoiarios', '8 3 3 3 3 1 3 1 7', 19, mn=5, weapons=KV + ['Horse'], rules=['Eastern Shock Cavalry (if heavy armour)', 'Open Order (if no heavy armour)'], options=[('Heavy armour (replaces light armour)', 1)])],
    'Hand weapon, thrusting spear, light armour, and shield. May have heavy armour (+1 pt). Mounted Kavallarioi with heavy armour are Eastern Shock Cavalry; without heavy armour they are Open Order.', page='55'))
BY.append(U(CAV, 'Elite Pronoiarios (Dismounted)', [M('Dismounted Elite Pronoiarios', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=KV, options=[('Heavy armour (replaces light armour)', 1)])],
    'Every other Elite Pronoiarios unit may fight on foot (-11 pts, reduce Movement to 4). Hand weapon, thrusting spear, light armour, and shield, and may have heavy armour (+1 pt).', page='55'))
BY.append(U(CAV, 'Regular Pronoiarios', [M('Regular Pronoiarios', '8 3 3 3 3 1 3 1 6', 17, mn=5, weapons=KV + ['Horse'], rules=['Open Order'])],
    'Hand weapon, thrusting spear, light armour, and shield. Mounted Kavallarioi without heavy armour are Open Order.', page='55'))
for nm, st, pt in (('Regular', '4 3 3 3 3 1 3 1 7', 7), ('Irregular', '4 2 2 3 3 1 2 1 6', 4)):
    BY.append(U(INF, f'{nm} Hoplitai', [M(f'{nm} Hoplites', st, pt, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=([('Exchange throwing spear for thrusting spear', 0)] + ([('Light armour', 1)] if nm == 'Regular' else [])) )],
        'Hand weapon, throwing or thrusting spear, and shield.' + (' Regulars may have light armour (+1 pt).' if nm == 'Regular' else ''), page='55'))
for nm, st, pt in (('Regular', '4 3 3 3 3 1 3 1 7', 7), ('Irregular', '4 2 2 3 3 1 2 1 6', 4)):
    BY.append(U(SKI, f'{nm} Psiloi', [M(f'{nm} Psiloi', st, pt, mn=5, weapons=['Hand Weapon', 'Buckler', 'Javelin'], rules=['Skirmishers (Chivalry)'], options=[('Exchange javelins for sling', 0), ('Exchange javelins/sling for bow', 2)] + ([('Exchange javelins/sling for crossbow (one unit)', 4), ('Light armour (Palaeologan only)', 1)] if nm == 'Regular' else []))],
        'A hand weapon, buckler, and either javelins or sling. May exchange sling or javelins for bow (+2 pts).' + (' One Regular Psiloi unit may take crossbow (+4 pts) instead of javelins/sling. Palaeologan Regular Psiloi may take light armour (+1 pt).' if nm == 'Regular' else '') + ' Skirmishers.', page='55'))
BY.append(U(AM, 'Skythikoi & Turkopoloi', [M('Horse Archer', '8 3 4 3 3 1 3 1 6', 23, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Nomad Cavalry'], options=[('Buckler', 2), ('Throwing spear', 1), ('Exchange for javelins (+1 pt)', 1), PERM])],
    'Hand weapon and bow. May have buckler (+2 pts), and throwing spear (+1 pt) or javelins (+1 pt). Skirmishers. Nomad Cavalry. Allies & Mercenaries; may be Permanent Mercenaries (Nikaean, Trapezuntine, Palaeologan).', page='55'))
BY.append(U(AM, 'Latinikoi Knights', [M('Latinikoi Knight', '8 4 3 3 3 1 4 1 7', 31, mn=5, weapons=['Hand Weapon', 'Lance', 'Heavy Armour', 'Shield', 'Warhorse'], rules=['First Charge (Chivalry)', 'Impetuous'], options=[('Partial plate armour (replaces heavy armour)', 2), ('Cloth barding (-1 M)', 4), PERM])],
    'Hand weapon, lance, heavy armour, shield, and warhorse. May have partial plate armour (+2 pts), and take cloth barding (+4 pts) for their mounts. First Charge. Impetuous. 0-3 units. Allies & Mercenaries; may be Permanent Mercenaries (Nikaean, Morean, Epirote).', mx=3, page='55'))
BY.append(U(AM, 'Latinikoi Spearmen', [M('Latinikoi Spearman', '4 3 2 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Shield', 'Thrusting Spear'], rules=['Mixed Order (Chivalry)'], options=[('Light armour', 1), ('Heavy armour (replaces light armour)', 2)])],
    'Hand weapon, shield and thrusting spear. May have light armour (+1 pt) or heavy armour (+2 pts). Spearmen and Crossbowmen may use Mixed Order. Latinikoi Infantry (spearmen and crossbowmen together) 0-1 unit; may only be taken if Latinikoi Knights are taken as well.', mx=1, page='55'))
BY.append(U(AM, 'Latinikoi Crossbowmen', [M('Latinikoi Crossbowman', '4 2 2 3 3 1 2 1 6', 10, mn=5, weapons=['Hand Weapon', 'Shield', 'Crossbow'], rules=['Mixed Order (Chivalry)', 'Open Order (when not in Mixed Order)'], options=[('Light armour', 1)])],
    'Hand weapon, shield and a crossbow. May have light armour (+1 pt). Mixed Order with Latinikoi Spearmen; Open Order when not in Mixed Order. May only be taken if Latinikoi Knights are taken as well.', mx=1, page='55'))
BY.append(U(AM, 'Turkoman Cavalry', [M('Turkoman', '8 3 3 3 3 1 3 1 7', 18, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Parthian Shot', 'Feigned Flight'], options=[('Thrusting spear', 2)])],
    'See the Turkoman Cavalry entry in the Ottoman Turks list: hand weapon, shield and bow; thrusting spear (+2 pts); Skirmishers, Parthian Shot and Feigned Flight. 0-3 units. Nikaean and Palaeologan armies.', mx=3, page='55'))
BY.append(U(AM, 'Alan Cavalry', [M('Alan', '8 3 3 3 3 1 4 1 6', 21, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Nomad Cavalry'], options=[('Thrusting spear', 2), ('Light armour', 2), ('Shield', 2), PERM])],
    'As Alans, use the Tartar Warrior profile in the Armies of Medieval Russia list: hand weapon and bow; thrusting spear (+2 pts), light armour (+2 pts) and shield (+2 pts). May be Open Order or Skirmishers. 0-2 units. Palaeologan armies (may be Permanent Mercenaries).', mx=2, page='55'))
BY.append(U(AM, 'Balkan or Anatolian Tribesmen', [M('Mountain Tribesman', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Open Order', 'Mixed Weapons'], options=[('Shield (replaces buckler)', 1), PERM])],
    'To represent Balkan and Anatolian tribesmen, 0-3 units of Mountain Tribesmen or Barbarian Warriors may be chosen (see the rulebook, page 130). Mountain Tribesmen stats used; Barbarian Warriors not built. Trapezuntine, Morean and Epirote armies (may be Permanent Mercenaries).', mx=3, page='55'))
BY.append(U(AM, 'Balkan Cavalry', [M('Balkan Cavalryman', '8 3 3 3 3 1 4 1 7', 17, mn=5, weapons=['Horse', 'Lance', 'Shield'], rules=['Open Order'], options=[('Light armour', 3), PERM])],
    'To represent Balkan Cavalry, 0-3 units of Cumans, Serbians (see Kingdom of Hungary list) and/or Wallachians (see Moldavian/Wallachian list) may be chosen. The Serbian profile is used here (horse, lance and shield; light armour +3 pts). Trapezuntine, Morean and Epirote armies (may be Permanent Mercenaries).', mx=3, page='55'))
BYV = lambda extra: (L(Characters=25, Infantry=25, Cavalry=33, **{'Allies_&_Mercenaries': 75}), 'Characters up to 25%, Infantry up to 25%, Cavalry up to 33%, Allies & Mercenaries up to 75%. ' + extra)
PMT = 'Permanent Mercenaries: one Mercenary unit per 1,000 army points may be upgraded to Permanent Mercenaries (+2 pts per model); +1 Leadership; they do not take the Allies & Mercenaries test; they still cannot use the General\'s Leadership or the Standard Bearer\'s re-roll. '
BY_V = multi('BY', 'The Last Byzantines', {
 'Nikaean Byzantines (1204-1261)': BYV('Nikaean armies: Regular & Elite Pronoiarios, Regular & Irregular Psiloi and Hoplitai, and Turkoman Cavalry. ' + PMT + 'Permanent Mercenaries: Latinikoi and Skythikoi.'),
 'Trapezuntine Byzantines (1204-1461)': BYV('Regular Pronoiarios, Regular & Irregular Psiloi and Hoplitai, and Barbarian Warriors. ' + PMT + 'Permanent Mercenaries: Balkan Cavalry, Mountain Tribesmen, and Skythikoi & Turkopoloi.'),
 'Morean Byzantines (1204-1461)': BYV('Regular Pronoiarios, Regular & Irregular Psiloi and Hoplitai, and Barbarian Warriors. ' + PMT + 'Permanent Mercenaries: Balkan Cavalry, Mountain Tribesmen, and one unit of Latinikoi troops.'),
 'Epirote Byzantines (1204-1318)': BYV('Epiriote armies: Regular & Elite Pronoiarios, Regular & Irregular Psiloi and Hoplitai. ' + PMT + 'Permanent Mercenaries: Latinikoi, Balkan Cavalry, and Mountain Tribesmen.'),
 'Palaeologan Byzantines (1259-1453)': BYV('Palaeologan armies: Guards, Elite & Regular Pronoiarios, Regular & Irregular Psiloi and Hoplitai, and Turkoman Cavalry. ' + PMT + 'Permanent Mercenaries: Skythikoi & Turkopoloi and Alans. Palaeologan special rule: Regular Psiloi may take light armour (+1 pt).')})
LISTS.append(('BY', 'The Last Byzantines (Armies of Chivalry)', 'Last_Byzantines_Chivalry.cat', BY, BY_V, 'THE LAST BYZANTINES 1204-1461 (Armies of Chivalry, pp.54-55). All Byzantine armies use the same army composition; unless a troop type is mentioned for a particular army it may not be used. Only troops mentioned as Permanent Mercenaries may be upgraded to Permanent Mercenaries (+2 pts per model, one Mercenary unit per 1,000 army points, +1 Leadership, no Allies & Mercenaries test at the start of the first turn). Latinikoi Knights are Impetuous with First Charge.'))
NK, TR, MR, EPI, PAL = list(VAR['BY'].keys())
_all = [NK, TR, MR, EPI, PAL]
def _only(unit, ok): return ('BY', unit, [v for v in _all if v not in ok])
UNAV += [_only('Guards (Mounted)', [PAL]), _only('Guards (Dismounted)', [PAL]),
         _only('Elite Pronoiarios (Mounted)', [NK, EPI, PAL]), _only('Elite Pronoiarios (Dismounted)', [NK, EPI, PAL]),
         _only('Skythikoi & Turkopoloi', [NK, TR, PAL]), _only('Latinikoi Knights', [NK, MR, EPI]), _only('Latinikoi Spearmen', [NK, MR, EPI]), _only('Latinikoi Crossbowmen', [NK, MR, EPI]),
         _only('Turkoman Cavalry', [NK, PAL]), _only('Alan Cavalry', [PAL]), _only('Balkan or Anatolian Tribesmen', [TR, MR, EPI]), _only('Balkan Cavalry', [TR, MR, EPI])]
OPTAV += [('BY', 'Regular Psiloi', 'Light armour (Palaeologan only)', [PAL])]
RATIOS += []
# ====================================================================== HUSSITES (book p.56)
HS = []
HSC = lambda foot: [('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4)] + ([('Halberd (dismounted or with war wagon)', 4), ('Double-handed weapon (dismounted or with war wagon)', 4)] if foot else [])
HS.append(U(CH, 'General', [M('General', '4 4 3 4 3 3 4 2 10', 180, weapons=['Hand Weapon', 'Partial Plate Armour'], rules=['Army General', 'Stubborn'], options=HSC(True))],
    'Hand weapon and partial plate armour. May ride a horse (free) or a warhorse (+4 pts). May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted or with a war-wagon. A warhorse may have cloth barding (+4 pts). Army General. Stubborn. 0-1.', mx=1, page='56'))
HS.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 3 4 3 2 4 2 8', 90, weapons=['Hand Weapon', 'Partial Plate Armour'], rules=['Army Standard', 'Stubborn'], options=[('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon and partial plate armour. May have a horse (free), a warhorse (+4 pts), or be with a war wagon. The warhorse may have cloth barding (+4 pts). Army Standard Bearer. Stubborn. 0-1.', mx=1, page='56'))
HS.append(U(CH, 'Captain', [M('Captain', '4 4 3 4 3 2 4 2 8', 65, weapons=['Hand Weapon', 'Partial Plate Armour'], rules=['Stubborn'], options=[('Lance', 4)] + HSC(True))],
    'Hand weapon and partial plate armour. May have a lance (+4 pts), and a horse (free) or warhorse (+4 pts). May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted or with a war wagon. The warhorse may have cloth barding (+4 pts). Stubborn.', page='56'))
HS.append(U(CAV, 'Bohemian Nobles', [M('Noble', '8 4 3 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Lance', 'Heavy Armour', 'Shield', 'Warhorse'], options=[('Partial plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4)])],
    'Hand weapon, lance, heavy armour, shield, and a warhorse. May wear partial plate armour (free). The warhorse may have cloth barding (+4 pts). 0-1 unit.', mx=1, page='56'))
HS.append(U(CAV, 'Heavy Cavalry', [M('Heavy Cavalryman', '8 3 3 3 3 1 3 1 7', 23, mn=5, weapons=['Horse', 'Thrusting Spear', 'Light Armour', 'Shield'], rules=['Stubborn'])],
    'Horse, thrusting spear, light armour, and shield. Stubborn.', page='56'))
HS.append(U(CAV, 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 6', 14, mn=5, weapons=['Horse', 'Hand Weapon', 'Light Crossbow'], rules=['Skirmishers (Chivalry)'])],
    'Horse, hand weapon, light crossbow. Skirmishers.', page='56'))
HS.append(U(INF, 'Flailmen/Halberdiers', [M('Flailman/Halberdier', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Halberd', 'Light Armour'], rules=['Stubborn'], options=[('Heavy armour (replaces light armour)', 2), ('Pavise', 1)])],
    'Halberd and light armour. May wear heavy armour (+2 pts) and carry a pavise (+1 pt). Stubborn.', page='56'))
HS.append(U(ARC, 'Crossbowmen/Handgunners', [M('Crossbowman/Handgunner', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Crossbow', 'Light Armour'], rules=['Open Order', 'Mixed Order (Chivalry)', 'Stubborn (if in Mixed Order)'], options=[('Exchange crossbow for handgun', 0), ('Pavise', 1), ('Mixed Order with Flailmen/Halberdiers (+2 pts)', 2)])],
    'Crossbow or handgun, light armour. May carry a pavise (+1 pt). Open Order. May be in Mixed Order with Flailmen/Halberdiers (+2 pts). Crossbowmen and Handgunners in Mixed Order are Stubborn.', page='56'))
_a = artillery('56', units_note=' May have one gun per 1,000 army points. Stubborn.'); _a['models'][0]['rules'].append('Stubborn'); HS.append(_a)
_w = war_wagon('56', ' Stubborn.'); _w['models'][0]['pts'] = 150; _w['models'][0]['rules'].append('Stubborn'); HS.append(_w)
HS_V = single('HS', 'The Hussites', L(Characters=25, Cavalry=25, Infantry=(50, 75)), 'Characters 0-25%, Cavalry 0-25%, Infantry 50-75% (artillery and war wagons from the Infantry allocation). Allies: 0-25% of the army may be Polish allies (documented only).')
LISTS.append(('HS', 'The Hussites (Armies of Chivalry)', 'Hussites_Chivalry.cat', HS, HS_V, 'ARMIES OF THE HUSSITES 1419-1471 (Armies of Chivalry, p.56). Polish allies (0-25%) are documented only.'))
PTSLIM += [('HS', 'Light Artillery', 1000, [])]
OPTRULE += [('HS', 'Crossbowmen/Handgunners', 'Mixed Order with Flailmen/Halberdiers (+2 pts)', 'Mixed Order (Chivalry)')]
# ====================================================================== THE SWISS (book p.57)
SW = []; CS = 'Cavalry/Support'
SW.append(U(INF, 'Swiss Pikemen', [M('Swiss Pikeman', '4 4 3 3 3 1 3 1 8', 13, mn=5, weapons=['Pike'], rules=['Stubborn', 'Medieval Phalanx'], options=[('Light armour', 1), ('Heavy armour', 2), ('Gewalthut (one unit; +25 pts)', 0), ('Captain instead of Leader (+20 pts per unit)', 0)])],
    'Pike. May wear light armour (+1 pt) or heavy armour (+2 pts). Stubborn and Medieval Phalanx. The Gewalthut costs an additional +25 pts (one unit; it must begin the game as the largest unit in the army; see Cantonal Standards). Pike and halberd units may purchase a Captain for 20 pts instead of a Leader.', page='57'))
SW.append(U(INF, 'Swiss Halberdiers', [M('Swiss Halberdier', '4 4 3 3 3 1 3 1 8', 12, mn=5, weapons=['Halberd'], rules=['Stubborn'], options=[('Light armour', 1), ('Heavy armour', 2), ('Open Order (+1 pt; Movement 5)', 1), ('Captain instead of Leader (+20 pts per unit)', 0)])],
    'Halberd. May wear light armour (+1 pt) or heavy armour (+2 pts). Stubborn. May be Open Order (+1 pt) with a Movement of 5 and a Rank Bonus of up to +2 in open ground. A Captain may be purchased for 20 pts instead of a Leader.', page='57'))
SW.append(U(CS, 'Swiss/Allied Men-at-Arms', [M('Man-at-Arms', '8 4 3 3 3 1 4 1 7', 30, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)'], options=[('Full plate armour (replaces partial plate armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, partial or full plate armour, lance, and warhorse. May have cloth barding (+4 pts) or plate barding (+6 pts). May count a Rank Bonus of up to +1 in combat.', page='57'))
SW.append(U(CS, 'Duke', [M('Duke', '8 5 3 4 3 2 5 2 8', 75, weapons=['Hand Weapon', 'Full Plate Armour', 'Lance', 'Warhorse'], options=[('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon, full plate armour, lance, and warhorse. May have cloth barding (+4 pts) or plate barding (+6 pts). The Swiss themselves have no Characters; if one or more units of Allied Men-at-Arms are purchased, they may select an Allied Duke. The Duke\'s Leadership can only apply to any Allied Men-at-Arms units that he chooses to join. 0-1.', mx=1, page='57'))
SW.append(U(CS, 'Swiss/Allied Retainers', [M('Retainer', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Thrusting Spear', 'Horse'], rules=['Combined Formation (Chivalry)'])],
    'Hand weapon, heavy armour, thrusting spear, and horse. May be in a Combined Formation (filling in the rear ranks) with Swiss/Allied Men-at-Arms.', page='57'))
SW.append(U(CS, 'Mounted Crossbowmen', [M('Mounted Crossbowman', '8 3 3 3 3 1 3 1 6', 14, mn=5, weapons=['Light Crossbow', 'Hand Weapon', 'Horse'], rules=['Skirmishers (Chivalry)'], options=[('Light armour', 2)])],
    'Light crossbow and hand weapon. May have light armour (+2 pts). Skirmishers.', page='57'))
SW.append(U(CS, 'Skirmishers', [M('Skirmisher', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Light Crossbow', 'Hand Weapon'], rules=['Skirmishers (Chivalry)'], options=[('Exchange for handgun (every second unit)', 2), ('Exchange for crossbow (every second unit)', 3)])],
    'Light crossbow and hand weapon. Every second unit may upgrade to handgun (+2 pts) or crossbow (+3 pts). Skirmishers. May have up to one unit for every unit of Swiss Pikemen.', page='57'))
SW.append(artillery_cat('57', cat=CS, units_note=' May have one gun per 1,000 army points.'))
SW.append(multi_barrelled('57', ' May have one gun per 1,000 army points.')); SW[-1]['cat'] = CS
SW_V = single('SW', 'The Swiss', L(Infantry=(66, 100), **{'Cavalry/Support': 33}), 'Infantry 66-100%, Cavalry/Support 0-33%. The Swiss have no Characters (Command by Committee).')
LISTS.append(('SW', 'The Swiss (Armies of Chivalry)', 'Swiss_Chivalry.cat', SW, SW_V, 'THE SWISS 1422-1522 (Armies of Chivalry, p.57). Cantonal Standards: the Gewalthut must begin the game as the largest unit in the army (other units may be as large) and should contain one or more flags in addition to its unit standard. While the Gewalthut is in good order (neither destroyed, fleeing, nor off the table) all formed Swiss infantry units within 12" of it may re-roll failed Break tests. The Gewalthut gains an additional +1 combat results bonus as if it had an Army Standard. If it loses its standards to a victorious opponent, they are worth 300 Victory points. Command By Committee: no Swiss characters are used; pike and halberd units may purchase a Captain for 20 pts instead of a Leader. A Captain is treated as a unit leader and the unit may add +1 to its Leadership; his two attacks are always made at Strength 4.'))
OPT_ONCE += [('SW', [('Swiss Pikemen', 'Gewalthut (one unit; +25 pts)')])]
FLAT += [('SW', 'Swiss Pikemen', 'Gewalthut (one unit; +25 pts)', 25), ('SW', 'Swiss Pikemen', 'Captain instead of Leader (+20 pts per unit)', 20), ('SW', 'Swiss Halberdiers', 'Captain instead of Leader (+20 pts per unit)', 20)]
OPTRULE += [('SW', 'Swiss Pikemen', 'Gewalthut (one unit; +25 pts)', 'Cantonal Standards'), ('SW', 'Swiss Halberdiers', 'Open Order (+1 pt; Movement 5)', 'Open Order')]
OPTSTAT += [('SW', 'Swiss Halberdiers', 'Open Order (+1 pt; Movement 5)', 'M', 5)]
RATIOS += [('SW', 'Skirmishers', ['Swiss Pikemen'], 1)]
PTSLIM += [('SW', 'Light Artillery', 1000, ['Multi-barrelled Artillery']), ('SW', 'Multi-barrelled Artillery', 1000, ['Light Artillery'])]
# ====================================================================== FRENCH ORDONNANCE (book pp.58-59)
FO = []
FOB = [('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
FO.append(U(CH, 'Army General', [M('Army General', '4 5 3 3 3 3 5 2 9', 150, weapons=['Hand Weapon', 'Full Plate Armour', 'Double-handed Weapon'], rules=['Army General'], options=[('Exchange double-handed weapon for halberd', 0), ('Ride a warhorse (with lance)', 0)] + FOB)],
    'Hand weapon and full plate armour. Has a halberd or a double-handed weapon if on foot. Has a lance and warhorse if mounted. The warhorse may have cloth barding (+4 pts), or plate barding (+6 pts). Army General. 0-1.', mx=1, page='58'))
FO.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 3 3 2 5 2 8', 80, weapons=['Hand Weapon', 'Full Plate Armour'], rules=['Army Standard'], options=[('Ride a warhorse', 0)] + FOB + [('Oriflamme (Army Standard, King-led army only)', 50)])],
    'Hand weapon and full plate armour. Has a warhorse if mounted. The warhorse may have cloth barding (+4 pts), or plate barding (+6 pts). Army Battle Standard. If the army is led by the King himself the Oriflamme may be carried as the army\'s battle standard (+50 pts); it may only be accompanied by a unit of Ordonnance Gendarmes, which is immune to panic; if surrendered to a victorious opponent it is worth 250 Victory points. 0-1.', mx=1, page='58'))
FO.append(U(CAV, 'Ordonnance Gendarmes (Mounted)', [M('Mounted Gendarme', '8 4 3 3 3 1 4 1 8', 35, mn=5, weapons=['Hand Weapon', 'Full Plate Armour', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)', 'Combined Formation (Chivalry)'], options=FOB + [('Veteran', 3), ('Upgrade to WS5 (every second unit)', 3)])],
    'Hand weapon, full plate armour, lance and warhorse. The warhorse may have cloth barding (+4 pts), or plate barding (+6 pts). First Charge. Combined Formation; when mounted may include Coustilliers. May be Veteran (+3 pts). Mounted Gendarmes gain up to a +1 Rank Bonus if supported by Coustilliers. Every second unit of Ordonnance Gendarmes may be upgraded to WS5 (+3 pts). For every Ordonnance Gendarme model there must be one Coustillier model and at least one Ordonnance Longbowman model (not enforced).', page='58'))
FO.append(U(CAV, 'Ordonnance Gendarmes (Dismounted)', [M('Dismounted Gendarme', '4 4 3 3 3 1 4 1 8', 18, mn=5, weapons=['Hand Weapon', 'Full Plate Armour', 'Halberd'], rules=['Different Weapons'], options=[('Exchange halberd for double-handed weapon', 0), ('Veteran', 3), ('Upgrade to WS5 (every second unit)', 3)])],
    'Hand weapon and full plate armour. Has a halberd or a double-handed weapon. Different Weapons. May be Veteran (+3 pts). Every second unit of Ordonnance Gendarmes may be upgraded to WS5 (+3 pts).', page='58'))
FO.append(U(CAV, 'Ordonnance Coustilliers', [M('Coustillier', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Horse', 'Thrusting Spear', 'Hand Weapon', 'Partial Plate Armour'], rules=['Combined Formation (Chivalry)'], options=[('Veteran', 2)])],
    'Horse, thrusting spear, hand weapon and partial plate armour. Combined Formation; may be included in a unit of Gendarmes. May be Veteran (+2 pts).', page='59'))
FO.append(U(CAV, 'Ordonnance Longbowmen (Mounted)', [M('Mounted Longbowman', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Thrusting Spear', 'Horse'], rules=['Stakes'], options=[('Veteran', 2)])],
    'Hand weapon and heavy armour; when mounted they have a thrusting spear and a horse. Stakes. May be Veteran (+2 pts).', page='59'))
FO.append(U(ARC, 'Ordonnance Longbowmen (Dismounted)', [M('Dismounted Longbowman', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Long Bow'], rules=['Stakes'], options=[('Stakes (+20 pts per unit)', 0), ('Veteran', 2)])],
    'Hand weapon, heavy armour and longbow. May have stakes (+20 pts per unit). Stakes. May be Veteran (+2 pts).', page='59'))
FO.append(U(ARC, 'Francs-Archers', [M('Franc-Archer', '4 2 2 3 3 1 3 1 5', 4, mn=5, weapons=['Bow', 'Hand Weapon'], rules=['Chicken', 'Stakes'], options=[('Light armour', 1), ('Buckler', 1), ('Stakes (+20 pts per unit)', 0)])],
    'Bow and hand weapon. May have light armour (+1 pt), a buckler (+1 pt), and stakes (+20 pts per unit). Chicken: Francs-archers fear any formed troops with a Leadership of 7 or more. Stakes.', page='59'))
FO.append(U(INF, 'Partisanmen', [M('Partisanman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Halberd', 'Hand Weapon', 'Partial Plate Armour'], options=[('Full plate armour (replaces partial plate armour)', 4)])],
    'Halberd, hand weapon, and partial plate armour. May upgrade to full plate armour (+4 pts).', page='59'))
FO.append(U(ARC, 'Crossbowmen', [M('Crossbowman', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], rules=['Stakes', 'Open Order'], options=[('Stakes (+20 pts per unit)', 0), ('Buckler', 1), ('Pavise', 1)])],
    'Crossbow, hand weapon, and light armour. May have stakes (+20 pts per unit), a buckler (+1 pt), or a pavise (+1 pt). Stakes. Open Order.', page='59'))
FO.append(U(SKI, 'Handgunners', [M('Handgunner', '5 3 3 3 3 1 3 1 6', 10, mn=5, weapons=['Handgun', 'Hand Weapon', 'Light Armour'], rules=['Skirmishers (Chivalry)'])],
    'Handgun, hand weapon, and light armour. Skirmishers. May have one unit for every 750 points in the army.', page='59'))
FO.append(U(SKI, 'Bideaux', [M('Bideaut', '5 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Throwing Spear', 'Javelin', 'Hand Weapon', 'Buckler'], rules=['Skirmishers (Chivalry)', 'Feigned Flight'])],
    'Throwing spears, javelins, hand weapon, and buckler. Skirmishers. Feigned Flight.', page='59'))
FO.append(artillery('59', master=True, units_note=' May have one gun per 500 army points. One crewman per gun may be upgraded to a Master Gunner (+20 pts); up to two Master Gunners are allowed in the army (not enforced).'))
FO.append(multi_barrelled('59', ' May have one gun per 500 army points (light and multi-barrelled together).'))
FO_V = single('FO', 'French Ordonnance Armies', L(Characters=25, Cavalry=(25, 50), Infantry=(25, 75)), 'Characters 0-25%, Cavalry 25-50%, Infantry 25-75% (artillery from the Infantry allocation), Mercenaries 0-20%. For every Ordonnance Gendarme model there must be one Coustillier model and at least one Ordonnance Longbowman model (not enforced). Mercenaries (documented only): a Swiss mercenary contingent can only comprise Swiss Pikemen and/or skirmishers.')
LISTS.append(('FO', 'French Ordonnance Armies (Armies of Chivalry)', 'French_Ordonnance_Chivalry.cat', FO, FO_V, 'FRENCH ORDONNANCE ARMIES 1445-1503 (Armies of Chivalry, pp.58-59). Keeper of the Oriflamme: if the army is led by the King himself, the Oriflamme may be carried as the battle standard (+50 pts). It may only be accompanied by a unit of Ordonnance Gendarmes; that unit is immune to panic; if surrendered, the banner is worth 250 Victory points; its powers are lost when the Battle Standard Bearer is killed. Chicken: Francs-archers fear any formed troops with a Leadership of 7 or more. Swiss mercenaries (Swiss Pikemen and/or skirmishers) are documented only.'))
PTSLIM += [('FO', 'Light Artillery', 500, ['Multi-barrelled Artillery']), ('FO', 'Multi-barrelled Artillery', 500, ['Light Artillery']), ('FO', 'Handgunners', 750, [])]
OPT_ONCE += [('FO', [('Army Standard Bearer', 'Oriflamme (Army Standard, King-led army only)')])]
OPTRULE += [('FO', 'Army Standard Bearer', 'Oriflamme (Army Standard, King-led army only)', 'Keeper of the Oriflamme')]
OPTRULE += [('FO', n, 'Veteran', 'Veteran') for n in ('Ordonnance Gendarmes (Mounted)', 'Ordonnance Gendarmes (Dismounted)', 'Ordonnance Coustilliers', 'Ordonnance Longbowmen (Mounted)', 'Ordonnance Longbowmen (Dismounted)')]
OPTRULE += [('FO', 'Ordonnance Longbowmen (Dismounted)', 'Stakes (+20 pts per unit)', 'Stakes'), ('FO', 'Francs-Archers', 'Stakes (+20 pts per unit)', 'Stakes'), ('FO', 'Crossbowmen', 'Stakes (+20 pts per unit)', 'Stakes')]
FLAT += [('FO', 'Ordonnance Longbowmen (Dismounted)', 'Stakes (+20 pts per unit)', 20), ('FO', 'Francs-Archers', 'Stakes (+20 pts per unit)', 20), ('FO', 'Crossbowmen', 'Stakes (+20 pts per unit)', 20)]
# ====================================================================== BURGUNDY (book pp.60-61)
BU = []
BUC = [('Halberd (dismounted)', 4), ('Double-handed weapon (dismounted)', 4), ('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4), ('Barding (plate, -1 M)', 6)]
BUF = ['Hand Weapon', 'Full Plate Armour']
BU.append(U(CH, 'Duke/General', [M('General', '4 6 3 4 3 3 6 2 9', 160, weapons=BUF, rules=['Army General', 'Stubborn (if dismounted)'], options=BUC)],
    'Hand weapon and full plate armour. May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted. May have a lance (+4 pts) and must have a horse (free) or warhorse (+4 pts) if mounted. The warhorse may have plate barding (+6 pts). Army General. Stubborn if dismounted. 0-1.', mx=1, page='60'))
BU.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 4 3 2 5 2 8', 100, weapons=BUF, rules=['Army Standard', 'Stubborn (if dismounted)'], options=[('Ride a horse', 0), ('Ride a warhorse', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon and full plate armour. Must have a horse (free) or warhorse (+4 pts) if mounted. The warhorse may have plate barding (+6 pts). Army Standard Bearer. Stubborn if dismounted. 0-1.', mx=1, page='60'))
BU.append(U(CH, 'Captain', [M('Captain', '4 5 3 4 3 2 5 2 8', 75, weapons=BUF, rules=['Stubborn (if dismounted)'], options=BUC)],
    'Hand weapon and full plate armour. May have a halberd (+4 pts) or a double-handed weapon (+4 pts) if dismounted. May have a lance (+4 pts) and must have a horse (free) or warhorse (+4 pts) if mounted. The warhorse may have plate barding (+6 pts). Stubborn if dismounted.', page='60'))
BU.append(U(CAV, 'Knights/Ordonnance Gendarmes (Mounted)', [M('Mounted Knight', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=BUF + ['Lance', 'Warhorse'], rules=['First Charge (Chivalry)'], options=[('Barding (plate, -1 M)', 6), ('Household Gendarmes (WS5; one unit)', 2)])],
    'Hand weapon and full plate armour. Armed with a lance and a warhorse. The warhorse may have plate barding (+6 pts). One unit may be upgraded to WS5 (+2 pts) as Household Gendarmes. First Charge.', page='61'))
BU.append(U(CAV, 'Knights/Ordonnance Gendarmes (Dismounted)', [M('Dismounted Knight', '4 4 3 3 3 1 4 1 8', 16, mn=5, weapons=BUF, rules=['Stubborn'], options=[('Halberd', 2), ('Double-handed weapon', 2), ('Household Gendarmes (WS5; one unit)', 2)])],
    'Hand weapon and full plate armour. May have a halberd (+2 pts) or a double-handed weapon (+2 pts). One unit may be upgraded to WS5 (+2 pts) as Household Gendarmes. Stubborn.', page='61'))
BU.append(U(CAV, 'Feudal Knights (Mounted)', [M('Mounted Feudal Knight', '8 2 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Lance', 'Warhorse'])],
    'Hand weapon and heavy armour. Armed with a lance and a warhorse.', page='61'))
BU.append(U(CAV, 'Feudal Knights (Dismounted)', [M('Dismounted Feudal Knight', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Hand Weapon', 'Heavy Armour'], rules=['Stubborn'], options=[('Halberd', 2), ('Double-handed weapon', 2)])],
    'Hand weapon and heavy armour. May have a halberd (+2 pts) or a double-handed weapon (+2 pts). Stubborn.', page='61'))
BU.append(U(CAV, 'Coustilliers (Mounted)', [M('Mounted Coustillier', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Thrusting Spear', 'Heavy Armour', 'Horse'], rules=['Combined Formation (Chivalry)'])],
    'Thrusting spear, heavy armour, and horse. Mounted Coustilliers may be in the rear ranks of a Combined Formation with Mounted Knights/Ordonnance Gendarmes or Mounted Feudal Knights.', page='61'))
BU.append(U(CAV, 'Coustilliers (Dismounted)', [M('Dismounted Coustillier', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Thrusting Spear', 'Heavy Armour'], options=[('Exchange thrusting spear for halberd', 1)])],
    'Thrusting spear and heavy armour. May exchange thrusting spear for halberd (+1 pt). May be in Mixed Order with Archers/Ordonnance Longbowmen, Crossbowmen or Handgunners.', page='61'))
BU.append(U(CAV, 'Italian Light Cavalry', [M('Italian Light Cavalryman', '8 3 3 3 3 1 3 1 6', 16, mn=5, weapons=['Light Crossbow', 'Hand Weapon', 'Light Armour', 'Horse'], rules=['Skirmishers (Chivalry)'])],
    'Light crossbow, hand weapon, light armour, and horse. Skirmishers.', page='61'))
BU.append(U(INF, 'Household Foot', [M('Household Foot', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Halberd', 'Heavy Armour'], rules=['Veteran'], options=[('Partial plate armour (replaces heavy armour)', 2)])],
    'Halberd and heavy armour. May wear partial plate armour (+2 pts). Veteran. May be in Mixed Order with Archers/Ordonnance Longbowmen, Crossbowmen, or Handgunners. 0-1 unit.', mx=1, page='61'))
BU.append(U(ARC, 'Archers/Ordonnance Longbowmen', [M('Archer', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Long Bow', 'Hand Weapon', 'Light Armour'], rules=['Open Order (if not combined or mixed)'], options=[('Heavy armour (replaces light armour)', 2), ('Hand and a half sword (+2 pts, treat as halberd)', 2), ('Stakes (+20 pts per unit)', 0), ('Veteran (one unit)', 1)])],
    'Longbow, hand weapon, and light armour. May wear heavy armour (+2 pts). May have a hand and a half sword (+2 pts, treat as halberd). If not in a Combined Formation or Mixed Order, may have Stakes (+20 pts per unit) or be in Open Order (free). One unit may be Veteran (+1 pt). Ordonnance Longbowmen may be in a Combined Formation with Ordonnance Pikemen. One unit of Archers/Ordonnance Longbowmen or Handgunners may be skirmishers for every 1,000 army points.', page='61'))
BU.append(U(INF, 'Low Countries Pikemen', [M('Low Countries Pikeman', '4 3 3 3 3 1 2 1 6', 10, mn=5, weapons=['Pike', 'Heavy Armour'], rules=['Medieval Phalanx'])],
    'Pike and heavy armour. Low Countries pikemen are a Medieval Phalanx.', page='61'))
BU.append(U(INF, 'Ordonnance Pikemen', [M('Ordonnance Pikeman', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Pike', 'Heavy Armour'], rules=['Medieval Phalanx (if not in Combined Formation)', 'Combined Formation (Chivalry)'], options=[('Buckler', 1)])],
    'Pike and heavy armour. May have a buckler (+1 pt). Ordonnance Pikemen are a Medieval Phalanx if not in a Combined Formation (with Ordonnance Longbowmen).', page='61'))
BU.append(U(ARC, 'Crossbowmen', [M('Crossbowman', '4 3 3 3 3 1 3 1 7', 12, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], rules=['Open Order (if not in Mixed Order)'], options=[('Pavise', 1)])],
    'Crossbow, hand weapon, and light armour. May have a pavise (+1 pt). If not in Mixed Order, may be in Open Order (free).', page='61'))
BU.append(U(ARC, 'Handgunners', [M('Handgunner', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Handgun', 'Hand Weapon', 'Light Armour'], rules=['Open Order (if not in Mixed Order)'], options=[('Pavise', 1)])],
    'Handgun, hand weapon, and light armour. May have a pavise (+1 pt). If not in Mixed Order, may be in Open Order (free). One unit of Archers or Handgunners may be skirmishers per 1,000 army points.', page='61'))
BU.append(artillery('61', master=True, units_note=' Up to one gun for every 500 army points. May upgrade one crewman in the army to a Master Gunner (+20 pts).'))
BU.append(multi_barrelled('61', ' Up to one gun for every 500 army points (light and multi-barrelled together).'))
BU_V = single('BU', 'Late Medieval Burgundy & Burgundian Ordonnance', L(Characters=25, Cavalry=(25, 75), Infantry=(25, 75)), 'Characters 0-25%, Cavalry 25-75%, Infantry 25-75%. Artillery: one gun per 500 army points, bought from the Infantry allocation. Allies: 0-25% may be Wars of the Roses English (documented only).')
LISTS.append(('BU', 'Late Medieval Burgundy (Armies of Chivalry)', 'Burgundy_Chivalry.cat', BU, BU_V, 'LATE MEDIEVAL BURGUNDY & BURGUNDIAN ORDONNANCE 1453-1477 (Armies of Chivalry, pp.60-61). Special Formations: Ordonnance Longbowmen may be in a Combined Formation with Ordonnance Pikemen. Mounted Coustilliers may be in the rear ranks of a Combined Formation with Mounted Knights/Ordonnance Gendarmes or Mounted Feudal Knights. Household Foot, Dismounted Knights/Ordonnance Gendarmes, Dismounted Feudal Knights, or Dismounted Coustilliers may be in Mixed Order with Archers/Ordonnance Longbowmen, Crossbowmen, or Handgunners. One unit of Archers/Ordonnance Longbowmen or Handgunners may be skirmishers for every 1,000 army points. Wars of the Roses English allies documented only.'))
PTSLIM += [('BU', 'Light Artillery', 500, ['Multi-barrelled Artillery']), ('BU', 'Multi-barrelled Artillery', 500, ['Light Artillery'])]
OPT_ONCE += [('BU', [('Knights/Ordonnance Gendarmes (Mounted)', 'Household Gendarmes (WS5; one unit)'), ('Knights/Ordonnance Gendarmes (Dismounted)', 'Household Gendarmes (WS5; one unit)')]), ('BU', [('Archers/Ordonnance Longbowmen', 'Veteran (one unit)')])]
OPTSTAT += [('BU', 'Knights/Ordonnance Gendarmes (Mounted)', 'Household Gendarmes (WS5; one unit)', 'WS', 5), ('BU', 'Knights/Ordonnance Gendarmes (Dismounted)', 'Household Gendarmes (WS5; one unit)', 'WS', 5)]
OPTRULE += [('BU', 'Archers/Ordonnance Longbowmen', 'Stakes (+20 pts per unit)', 'Stakes'), ('BU', 'Archers/Ordonnance Longbowmen', 'Veteran (one unit)', 'Veteran')]
FLAT += [('BU', 'Archers/Ordonnance Longbowmen', 'Stakes (+20 pts per unit)', 20)]
# ====================================================================== WARS OF THE ROSES (book pp.62-63)
WR = []
WRC = [('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4), ('Halberd (dismounted)', 4), ('Double-handed weapon (dismounted)', 4), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
WR.append(U(CH, 'Army General', [M('Army General', '4 6 3 4 3 3 6 2 9', 160, weapons=BUF, rules=['Army General', 'Stubborn (if dismounted)'], options=WRC)],
    'Hand weapon and full plate armour. May have a lance (+4 pts), and must have a horse (free) or warhorse (+4 pts) if mounted. May have a halberd (+4 pts) or double-handed weapon (+4 pts) if dismounted. The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Army General. Stubborn when dismounted. 0-1.', mx=1, page='62'))
WR.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '4 5 3 4 3 2 5 2 8', 100, weapons=BUF, rules=['Army Standard', 'Stubborn (if dismounted)'], options=[('Ride a horse', 0), ('Ride a warhorse', 4), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon and full plate armour. Must have a horse or warhorse (+4 pts) if mounted. The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Army Standard Bearer. Stubborn when dismounted. 0-1.', mx=1, page='62'))
WR.append(U(CH, 'Nobles', [M('Noble', '4 5 3 4 3 2 5 2 8', 75, weapons=BUF, rules=['Stubborn (if dismounted)'], options=WRC)],
    'Hand weapon and full plate armour. May have a lance (+4 pts), and must have a horse (free) or warhorse (+4 pts) if mounted. May have a halberd (+4 pts) or double-handed weapon (+4 pts) if dismounted. The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Stubborn when dismounted.', page='62'))
WR.append(U(CAV, 'Men-at-Arms (Mounted)', [M('Mounted Man-at-Arms', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour', 'Lance', 'Warhorse'], rules=['First Charge (Chivalry)', 'Combined Formation (Chivalry)'], options=[('Full plate armour (replaces partial plate armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'Hand weapon and partial plate armour. May wear full plate armour (free). Lance and warhorse. Any mounted unit may add cloth barding (+4 pts) or plate barding (+6 pts). May have up to +1 Rank Bonus. First Charge. May be the front rank(s) of a Combined Formation with Currours.', page='62'))
WR.append(U(CAV, 'Men-at-Arms (Dismounted)', [M('Dismounted Man-at-Arms', '4 4 3 3 3 1 4 1 8', 15, mn=5, weapons=['Hand Weapon', 'Partial Plate Armour'], rules=['Stubborn'], options=[('Full plate armour (replaces partial plate armour)', 2), ('Halberd', 3), ('Double-handed weapon', 3)])],
    'Hand weapon and partial plate armour. May wear full plate armour (+2 pts). May have a halberd (+3 pts) or double-handed weapon (+3 pts). Stubborn. May be in Mixed Order with Retinue Longbowmen.', page='62'))
WR.append(U(CAV, 'Currours', [M('Currour', '8 3 3 3 3 1 3 1 7', 20, mn=5, weapons=['Thrusting Spear', 'Heavy Armour', 'Horse'], rules=['Combined Formation (Chivalry)'])],
    'Thrusting spear, heavy armour, and horse. May be the rear rank(s) of a Combined Formation with Mounted Men-at-Arms.', page='62'))
WR.append(U(CAV, 'Staves/Hobilars', [M('Stave/Hobilar', '8 2 2 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Horse'], rules=['Open Order'], options=[('Light armour', 2), ('Thrusting spear', 2)])],
    'Hand weapon and horse. May have light armour (+2 pts) and thrusting spear (+2 pts). Open Order.', page='63'))
WR.append(U(CAV, 'Irish Cavalry', [M('Irish Horseman', '8 3 3 3 3 1 3 1 6', 15, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield', 'Horse'], rules=['Skirmishers (Chivalry)'])],
    'Hand weapon, javelins, shield, and horse. Skirmishers. 0-1 unit (Irish Cavalry or Border Horse). Availability: Lancaster, Yorkist Pretenders.', mx=1, page='63'))
WR.append(U(CAV, 'Border Horse', [M('Border Horseman', '8 3 3 3 3 1 3 1 6', 15, mn=5, weapons=['Throwing Spear', 'Hand Weapon', 'Light Armour', 'Horse'], rules=['Skirmishers (Chivalry)'])],
    'Throwing spear (a boar spear), hand weapon, light armour, and horse. Skirmishers. 0-1 unit (Irish Cavalry or Border Horse). Availability: Lancaster, Richard III.', mx=1, page='63'))
WR.append(U(INF, 'Retinue Billmen', [M('Retinue Billman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Halberd', 'Heavy Armour'], rules=['Mixed Order (Chivalry)'])],
    'Halberd and heavy armour. May be in Mixed Order with Retinue Longbowmen.', page='63'))
WR.append(U(ARC, 'Retinue Longbowmen', [M('Retinue Longbowman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Long Bow', 'Light Armour', 'Hand Weapon'], rules=['Stakes', 'Mixed Order (Chivalry)'], options=[('Buckler', 1), ('Stakes (+20 pts per unit; not in Mixed Order)', 0)])],
    'Longbow, light armour, and hand weapon. May have a buckler (+1 pt). May have Stakes (+20 pts per unit) if not in Mixed Order. Stakes. May be in Mixed Order with Dismounted Men-at-Arms or Retinue Billmen.', page='63'))
WR.append(U(INF, 'Shire Billmen', [M('Shire Billman', '4 2 2 3 3 1 3 1 6', 6, mn=5, weapons=['Halberd', 'Light Armour'], rules=['Mixed Order (Chivalry)'])],
    'Halberd and light armour. May be in Mixed Order with Shire Longbowmen. Availability: Lancaster, York, Richard III and Henry Tudor.', page='63'))
WR.append(U(INF, 'Border Spearmen', [M('Border Spearman', '4 2 2 3 3 1 3 1 6', 6, mn=5, weapons=['Thrusting Spear', 'Light Armour'], rules=['Mixed Order (Chivalry)'])],
    'Thrusting spear and light armour. May be in Mixed Order with Shire Longbowmen. Availability: Lancaster, York, Richard III and Henry Tudor.', page='63'))
WR.append(U(INF, 'Welsh Spearmen', [M('Welsh Spearman', '4 2 2 3 3 1 3 1 6', 6, mn=5, weapons=['Thrusting Spear', 'Light Armour', 'Shield'], rules=['Mixed Order (Chivalry)'], options=[('Exchange thrusting spear for throwing spear', 0)])],
    'Thrusting or throwing spear and shield (light armour as the entry reads). May be in Mixed Order with Welsh Longbowmen. Availability: Lancaster, York, Richard III and Henry Tudor.', page='63'))
WR.append(U(ARC, 'Shire/Welsh Archers', [M('Archer', '4 2 2 3 3 1 3 1 6', 6, mn=5, weapons=['Long Bow', 'Hand Weapon'], rules=['Stakes', 'Mixed Order (Chivalry)'], options=[('Stakes (+20 pts per unit; not in Mixed Order)', 0)])],
    'Longbow and hand weapon. May have Stakes (+20 pts per unit) if not in Mixed Order. Stakes. Shire Longbowmen may be in Mixed Order with Shire Billmen or Border Spearmen; Welsh Longbowmen with Welsh Spearmen. Availability: Lancaster, York, Richard III and Henry Tudor.', page='63'))
WR.append(U(INF, 'Local Levies/Rebellious Peasants', [M('Levy/Peasant', '4 1 1 3 3 1 2 1 5', 3, mn=5, weapons=['Improvised Weapon'], rules=['Peasants (Chivalry)'])],
    'Improvised weapons. Fear formed foot units they don\'t outnumber by more than two to one. Fear formed cavalry units. Casualties from artillery cause a Panic test. Availability: Lancaster, York, Richard III and Henry Tudor.', page='63'))
SPW = 'Special Units'
WR.append(U(SPW, 'Irish Galloglaich', [M('Galloglaich', '4 4 3 3 3 1 3 1 7', 12, mn=5, weapons=['Double-handed Weapon', 'Heavy Armour'], rules=['Veteran'])],
    'Double-handed weapon and heavy armour. Veteran. Availability: Lancaster and Yorkist Pretenders.', page='63'))
WR.append(U(SPW, 'Irish Bonnachts and Kerns', [M('Bonnacht/Kern', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband', 'Open Order'])],
    'Hand weapon, javelin, and buckler. Warband. Open Order. Every 2nd unit may be Skirmishers. Availability: Lancaster and Yorkist Pretenders.', page='63'))
WR.append(U(SPW, 'Mercenary Pikemen', [M('Mercenary Pikeman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Pike', 'Heavy Armour'], rules=['Medieval Phalanx'], options=[('Stubborn (Yorkist Pretenders only)', 2)])],
    'Pike and heavy armour. Medieval Phalanx. Yorkist Pretenders may be Stubborn (+2 pts). Availability: York, Lancaster and Yorkist Pretenders.', page='63'))
WR.append(U(SPW, 'Continental Mercenaries', [M('Mercenary', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Light Armour'], options=[('Heavy armour (replaces light armour)', 1), ('Halberd', 2), ('Thrusting spear', 1), ('Crossbow', 5), ('Handgun', 4), ('Pavise (crossbow/handgun, not in Mixed Order)', 1)])],
    'Hand weapon and light armour. May upgrade to heavy armour (+1 pt). May have only one choice of halberd (+2 pts), thrusting spear (+1 pt), crossbow (+5 pts) or handgun (+4 pts). Crossbowmen and Handgunners may have pavises (+1 pt) if not in Mixed Order. Mixed Order: melee-weapon Continental Mercenaries with missile-weapon Continental Mercenaries. Availability: York, Lancaster, Tudor and Yorkist Pretenders.', page='63'))
WR.append(U(SPW, 'Breton Javelinmen', [M('Breton', '5 3 3 3 3 1 3 1 6', 9, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], rules=['Open Order', 'Feigned Flight'])],
    'Hand weapon, throwing spear and javelins if formed, javelins only if skirmishing, and buckler. Open Order or Skirmishers. Feigned Flight. Availability: Lancaster and Tudor.', page='63'))
WR.append(artillery('63', units_note=' Up to one gun for every 750 army points.')); WR[-1]['cat'] = SPW
WR.append(multi_barrelled('63', ' Up to one gun for every 750 army points.')); WR[-1]['cat'] = SPW
_lim = lambda pretender: L(Characters=25, Cavalry=25 if pretender else 50, Infantry=(0, 25) if pretender else (25, 75), **{'Special_Units': (25, 75) if pretender else 25})
WR_V = multi('WR', 'Wars of the Roses English', {
 'Lancaster': (_lim(False), 'Characters 0-25%, Cavalry 0-50%, Infantry 25-75%, Special Units 0-25%.'),
 'York': (_lim(False), 'Characters 0-25%, Cavalry 0-50%, Infantry 25-75%, Special Units 0-25%.'),
 'Richard III': (_lim(False), 'Characters 0-25%, Cavalry 0-50%, Infantry 25-75%, Special Units 0-25%.'),
 'Henry Tudor': (_lim(False), 'Characters 0-25%, Cavalry 0-50%, Infantry 25-75%, Special Units 0-25%.'),
 'Yorkist Pretenders': (_lim(True), 'Characters 0-25%, Cavalry 0-25%, Infantry 0-25%, Special Units 25-75%.')})
LISTS.append(('WR', 'Wars of the Roses English (Armies of Chivalry)', 'Wars_of_the_Roses_Chivalry.cat', WR, WR_V, 'WARS OF THE ROSES ENGLISH 1455-1487 (Armies of Chivalry, pp.62-63). Five army compositions: Lancaster, York, Richard III, Henry Tudor and the Yorkist Pretenders; availability of some troop types is restricted to specific armies. Mixed Order: Retinue Longbowmen - Dismounted Men-at-Arms; Retinue Longbowmen - Retinue Billmen; Shire Longbowmen - Shire Billmen or Border Spearmen; Welsh Longbowmen - Welsh Spearmen; Continental Mercenaries (melee weapons) - Continental Mercenaries (missile weapons).'))
LAN, YOR, RIC, TUD, PRE = 'Lancaster', 'York', 'Richard III', 'Henry Tudor', 'Yorkist Pretenders'
_w = [LAN, YOR, RIC, TUD, PRE]
def _wo(unit, ok): return ('WR', unit, [v for v in _w if v not in ok])
UNAV += [_wo('Irish Cavalry', [LAN, PRE]), _wo('Border Horse', [LAN, RIC]),
         _wo('Shire Billmen', [LAN, YOR, RIC, TUD]), _wo('Border Spearmen', [LAN, YOR, RIC, TUD]), _wo('Welsh Spearmen', [LAN, YOR, RIC, TUD]), _wo('Shire/Welsh Archers', [LAN, YOR, RIC, TUD]), _wo('Local Levies/Rebellious Peasants', [LAN, YOR, RIC, TUD]),
         _wo('Irish Galloglaich', [LAN, PRE]), _wo('Irish Bonnachts and Kerns', [LAN, PRE]), _wo('Mercenary Pikemen', [YOR, LAN, PRE]), _wo('Continental Mercenaries', [YOR, LAN, TUD, PRE]), _wo('Breton Javelinmen', [LAN, TUD])]
OPTAV += [('WR', 'Mercenary Pikemen', 'Stubborn (Yorkist Pretenders only)', [PRE])]
OPTRULE += [('WR', 'Mercenary Pikemen', 'Stubborn (Yorkist Pretenders only)', 'Stubborn'), ('WR', 'Retinue Longbowmen', 'Stakes (+20 pts per unit; not in Mixed Order)', 'Stakes'), ('WR', 'Shire/Welsh Archers', 'Stakes (+20 pts per unit; not in Mixed Order)', 'Stakes')]
FLAT += [('WR', 'Retinue Longbowmen', 'Stakes (+20 pts per unit; not in Mixed Order)', 20), ('WR', 'Shire/Welsh Archers', 'Stakes (+20 pts per unit; not in Mixed Order)', 20)]
PTSLIM += [('WR', 'Light Artillery', 750, ['Multi-barrelled Artillery']), ('WR', 'Multi-barrelled Artillery', 750, ['Light Artillery'])]
UNIT_MAX_IN += []
PAIRS += [('WR', ['Irish Cavalry', 'Border Horse'], 'irish-or-border')]
# ====================================================================== ITALIAN CONDOTTA (book pp.35-37)
IC = []
ICC = plates(True, 2, 4) + [('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4), ('Halberd (dismounted)', 4), ('Double-handed weapon (dismounted)', 4), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
ICM = [('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)]
IC.append(U(CH, 'Army General: Condottiere', [M('Condottiere', '8 6 3 4 3 3 6 2 9', 160, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General'], options=[('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4)] + ICM)],
    'Hand weapon, heavy armour and shield. May have a lance (+4 pts); horse (free) or warhorse (+4 pts). May wear partial or full plate armour (free). The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Army General (take either the Condottiere or a Feudal General). 0-1.', mx=1, page='35'))
IC.append(U(CH, 'Army General: Feudal General', [M('Feudal General', '8 5 3 3 3 3 5 2 9', 135, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army General'], options=[('Lance', 4), ('Ride a horse', 0), ('Ride a warhorse', 4)] + ICM)],
    'Hand weapon, heavy armour and shield. May have a lance (+4 pts); horse (free) or warhorse (+4 pts). May wear partial or full plate armour (free). The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Army General (take either the Condottiere or a Feudal General). A Feudal General is required for the Familia Ducale option. 0-1.', mx=1, page='35'))
IC.append(U(CH, 'Army Standard Bearer', [M('Army Standard Bearer', '8 5 3 4 3 2 5 2 8', 90, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], rules=['Army Standard'], options=[('Ride a horse', 0), ('Ride a warhorse', 4)] + ICM)],
    'Hand weapon, heavy armour and shield. Horse (free) or warhorse (+4 pts). May wear partial or full plate armour (free). The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). Army Standard Bearer. 0-1.', mx=1, page='35'))
IC.append(carrocio('35', 'Early armies only, and only if no Army Standard Bearer is chosen.'))
IC.append(U(CH, 'Colonello', [M('Colonello', '4 5 3 3 3 2 5 2 8', 75, weapons=['Hand Weapon', 'Heavy Armour', 'Shield'], options=ICC + [(GEN_LABEL, 25)])],
    'Hand weapon, heavy armour and shield. May have a lance (+4 pts); horse (free) or warhorse (+4 pts). On foot: halberd or double-handed weapon (+4 pts). May wear partial plate (mounted free, dismounted +2 pts) or full plate armour (mounted free, dismounted +4 pts). The warhorse may have cloth barding (+4 pts) or plate barding (+6 pts). If no other Army General is taken, a single Colonello may be made Army General (+25 pts).', page='35'))
IC.append(U(CAV, 'Mercenary Knights', [M('Mercenary Knight', '8 4 3 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Heavy Armour', 'Lance', 'Shield', 'Warhorse'], rules=['First Charge (Chivalry)'], options=ICM + [('Casa (WS5; one unit)', 2)])],
    'Hand weapon, heavy armour, lance, shield and warhorse. May wear partial or full plate armour (free). Cloth barding (+4 pts) or plate barding (+6 pts). First Charge. Rank Bonus up to +1. 0-1 unit may upgrade to Casa (+2 pts, WS5) and cannot outnumber any other Mercenary Knights unit. 1+ unit.', page='36'))
IC.append(U(CAV, 'Feudal Knights', [M('Feudal Knight', '8 3 3 3 3 1 3 1 7', 24, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Lance', 'Shield', 'Horse'], options=[('Heavy armour (replaces light armour)', 1), ('Partial plate armour (replaces light armour)', 2), ('Familia Ducale (WS4, Ld8; Milanese armies, Feudal General)', 5)])],
    'Hand weapon, light armour, lance, shield and horse. May have heavy armour (+1 pt) or partial plate armour (+2 pts). Rank Bonus +1. One unit in Milanese armies may upgrade to Familia Ducale (WS4, Ld8; +5 pts per model) if a Feudal General is used. 0-2 units. Early: Naples, Milan; Late: Venetian Greek, Milan.', mx=2, page='36'))
IC.append(U(CAV, 'German Mercenary Knights', [M('Mercenary Knight', '8 3 3 3 3 1 3 1 7', 22, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Heavy Armour', 'Shield', 'Horse'], rules=['Allies and Mercenaries (Chivalry)'],
    options=[('Partial plate armour (replaces heavy armour)', 0), ('Full plate armour (replaces heavy armour)', 0), ('Cloth barding (-1 M)', 4), ('Barding (plate, -1 M)', 6)])],
    'As the German/Bohemian Mercenary Knights in the Kingdom of Hungary list: hand weapon, thrusting spear, heavy armour, shield and horse. Partial or full plate (free). Cloth (+4 pts) or plate (+6 pts) barding. Rank Bonus up to +2. All Early armies.', page='36'))
IC.append(U(CAV, 'Mounted Crossbowmen', [M('Mounted Crossbowman', '8 3 3 3 3 1 3 1 6', 14, mn=5, weapons=['Light Crossbow', 'Hand Weapon', 'Horse'], rules=['Skirmishers (Chivalry)'], options=[('Light armour', 2)])],
    'Light crossbow and hand weapon. May have light armour (+2 pts). Skirmishers.', page='36'))
IC.append(U(CAV, 'Stradiotti', [M('Stradiot', '8 3 3 3 3 1 3 1 7', 23, mn=5, weapons=['Hand Weapon', 'Bow', 'Shield', 'Thrusting Spear', 'Horse'], rules=['Skirmishers (Chivalry)', 'Parthian Shot', 'Feigned Flight'], options=[('Light armour (Open Order)', 2)])],
    'Hand weapon, bow, shield and thrusting spear. May have light armour (+2 pts) and become Open Order. Skirmishers, Parthian Shot, Feigned Flight. Late Venetian armies only; 0-2 units (1+ in Venetian Greek).', mx=2, page='36'))
IC.append(U(CAV, 'Hungarian Light Cavalry', [M('Hungarian/Cuman', '8 2 3 3 3 1 4 1 6', 20, mn=5, weapons=['Hand Weapon', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Nomad Cavalry'], options=[('Buckler', 2)])],
    'See the Hungarian/Cuman Cavalry entry in the Kingdom of Hungary list. Florence, Naples and Papal States only. 0-1 unit.', mx=1, page='36'))
IC.append(U(CAV, 'Turkish Light Cavalry', [M('Akinci', '8 2 3 3 3 1 3 1 5', 15, mn=5, weapons=['Hand Weapon', 'Shield', 'Bow', 'Horse'], rules=['Skirmishers (Chivalry)', 'Parthian Shot', 'Feigned Flight'], options=[('Thrusting spear', 2)])],
    'See the Akincis entry in the Ottoman Turks list. Late Naples, Venice and Venetian Greek armies. 0-1 unit.', mx=1, page='36'))
IC.append(U(INF, 'Militia Crossbowmen', [M('Militia Crossbowman', '4 2 3 3 3 1 3 1 6', 9, mn=5, weapons=['Crossbow', 'Hand Weapon'], options=[('Light armour', 1), ('Pavise', 1)])],
    'Crossbow and hand weapon. May have light armour (+1 pt) and a pavise (+1 pt). Combined Formation with Militia Spearmen; if they carry a pavise they are Open Order.', page='37'))
IC.append(U(INF, 'Militia Spearmen', [M('Militia Spearman', '4 2 3 3 3 1 3 1 6', 6, mn=5, weapons=['Thrusting Spear', 'Shield', 'Hand Weapon'], rules=['Combined Formation (Chivalry)'], options=[('Light armour', 1), ('Pavise', 1)])],
    'Thrusting spear, shield and hand weapon. May have light armour (+1 pt) and a pavise (+1 pt). Combined Formation with Militia Crossbowmen when they carry a pavise.', page='37'))
IC.append(U(INF, 'Militia Pikemen', [M('Militia Pikeman', '4 2 2 3 3 1 3 1 7', 8, mn=5, weapons=['Pike', 'Hand Weapon'], rules=['Medieval Phalanx'], options=[('Light armour', 1)])],
    'Pike and hand weapon. May have light armour (+1 pt). Medieval Phalanx; up to +2 rank bonus on the charge turn and +3 later or if charged. Late armies only.', page='37'))
IC.append(U(INF, 'Guardsmen/Provisionati', [M('Guardsman/Provisionato', '4 3 3 3 3 1 4 1 8', 13, mn=5, weapons=['Halberd', 'Heavy Armour'], rules=['Veteran', 'Stubborn'])],
    'Halberd and heavy armour. Veteran, Stubborn. 0-1 unit. Naples, Papal States, Milan and Venice.', mx=1, page='37'))
IC.append(U(ARC, 'Mercenary Crossbowmen', [M('Mercenary Crossbowman', '4 3 3 3 3 1 3 1 7', 12, mn=5, weapons=['Crossbow', 'Hand Weapon', 'Light Armour'], options=[('Pavise', 1), ('Open Order', 0)])],
    'Crossbow, hand weapon and light armour. May have a pavise (+1 pt). May be Open Order.', page='37'))
IC.append(U(INF, 'Mercenary Pikemen', [M('Mercenary Pikeman', '4 3 3 3 3 1 3 1 7', 11, mn=5, weapons=['Pike', 'Heavy Armour'], rules=['Medieval Phalanx'])],
    'Pike and heavy armour. Medieval Phalanx. Late armies only.', page='37'))
IC.append(U(INF, 'Mercenary Billmen', [M('Mercenary Billman', '4 3 3 3 3 1 3 1 7', 10, mn=5, weapons=['Halberd', 'Hand Weapon', 'Partial Plate Armour'], options=[('Full plate armour (replaces partial plate armour)', 4)])],
    'Halberd, hand weapon and partial plate armour. May have full plate armour (+4 pts). Late armies only.', page='37'))
IC.append(U(SKI, 'Skirmishers', [M('Skirmisher', '5 3 3 3 3 1 3 1 6', 7, mn=5, weapons=['Light Crossbow', 'Hand Weapon'], rules=['Skirmishers (Chivalry)'], options=[('Light armour', 1), ('Exchange for handgun (every second unit; Late only)', 3), ('Exchange for crossbow (every second unit)', 4)])],
    'Light crossbow and hand weapon. Every second unit may upgrade to handgun (+3 pts) or crossbow (+4 pts). May have light armour (+1 pt). Skirmishers. Up to one unit per Militia Spearmen or Mercenary Pikemen unit; handguns Late only; Late Venetian and Milanese armies must have 1+ units of Handgunners.', page='37'))
IC.append(U(INF, 'Javelinmen/Swordsmen', [M('Javelinman/Swordsman', '5 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Shield'], rules=['Open Order'], options=[('Exchange shield for buckler', 0), ('Javelins', 1)])],
    'Hand weapon, light armour, shield or buckler. May have javelins (+1 pt). Open Order. Rank Bonus up to +2 in the open. 0-1 unit.', mx=1, page='37'))
IC.append(artillery('37', units_note=' 0-1 light or multi-barrelled gun per 750 army points (bought from the Infantry allocation).'))
IC.append(multi_barrelled('37', ' 0-1 light or multi-barrelled gun per 750 army points (bought from the Infantry allocation).'))
IC_V = multi('IC', 'Italian Condotta', {
 'Early Army (1320-1400)': (L(Characters=25, Cavalry=(25, 75), Infantry=50), 'Characters 0-25%, Cavalry 25-75%, Infantry 0-50% (Artillery from the Infantry allocation, 0-1 light or multi-barrelled gun per 750 pts), Allies 0-25% (Free Companies, documented only). The state (Naples, Milan, Florence, Papal States, Venice etc.) restrictions on troop entries are documented in the unit text and are not enforced.'),
 'Late Army (1400-1495)': (L(Characters=25, Cavalry=(25, 75), Infantry=50), 'Characters 0-25%, Cavalry 25-75%, Infantry 0-50% (Artillery from the Infantry allocation, 0-1 light or multi-barrelled gun per 750 pts), Allies 0-25% (Free Companies; Swiss for Late Venetian/Florentine armies; documented only). The state restrictions on troop entries are documented in the unit text and are not enforced.')})
LISTS.append(('IC', 'Italian Condotta (Armies of Chivalry)', 'Italian_Condotta_Chivalry.cat', IC, IC_V, 'ITALIAN CONDOTTA ARMIES 1320-1495 (Armies of Chivalry, pp.35-37). Early Army 1320-1400 and Late Army 1400-1495. Free Companies and Swiss allies documented only; Venetian, Florentine, Milanese, Neapolitan and Papal state restrictions documented in unit text only.'))
EA, LA = list(VAR['IC'].keys())
UNAV += [('IC', n, [EA]) for n in ('Militia Pikemen', 'Mercenary Pikemen', 'Mercenary Billmen', 'Stradiotti')] + [('IC', 'German Mercenary Knights', [LA]), ('IC', 'Carrocio', [LA])]
OPTAV += [('IC', 'Skirmishers', 'Exchange for handgun (every second unit; Late only)', [LA])]
PAIRS += [('IC', ['Army General: Condottiere', 'Army General: Feudal General'], 'condottiere-or-feudal')]
OPT_ONCE += [('IC', [('Colonello', GEN_LABEL)]), ('IC', [('Mercenary Knights', 'Casa (WS5; one unit)')]), ('IC', [('Feudal Knights', 'Familia Ducale (WS4, Ld8; Milanese armies, Feudal General)')])]
OPTRULE += [('IC', 'Colonello', GEN_LABEL, 'Army General (Chariot Wars)')]
OPTSTAT += [('IC', 'Mercenary Knights', 'Casa (WS5; one unit)', 'WS', 5), ('IC', 'Feudal Knights', 'Familia Ducale (WS4, Ld8; Milanese armies, Feudal General)', 'WS', 4)]
PTSLIM += [('IC', 'Light Artillery', 750, ['Multi-barrelled Artillery']), ('IC', 'Multi-barrelled Artillery', 750, ['Light Artillery'])]
GEN['IC'] = (['Army General: Condottiere', 'Army General: Feudal General'], [('Colonello', GEN_LABEL)])
