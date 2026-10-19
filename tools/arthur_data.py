# The Age of Arthur (Warhammer Historical) army lists. Book page = printed page number (pdf page - 2). Model stats order: M WS BS S T W I A Ld
import copy
from rb_data import M, U
LISTS = []; VAR = {}; AVAIL = []; UNAV = []; OPTAV = []; OPTRULE = []; OPTSTAT = []; RATIOS = []; OPT_ONCE = []; PAIRS = []
SECOND = {}; UNIT_MAX_IN = []; GEN = {}; COND_CHARS = []; COSTV = []; STATV = []; EXCL = []
FLAT = []; PTSLIM = []; MODLIM = []; HIRDMEN_LE_BONDIR = []
CH, COM, UNC = 'Characters', 'Common Warriors', 'Uncommon Warriors'
PUB = 'The Age of Arthur'

def variants(key, title, comps):
    VAR[key] = {}; out = []
    for c, (lim, txt) in comps.items():
        VAR[key][c] = f'{PUB}: {title}' if len(comps) == 1 else f'{PUB}: {title} - {c}'
        out.append((VAR[key][c], lim, txt))
    return out

def L(**kw):
    out = {}
    for k, v in kw.items():
        cat = k.replace('_', ' ')
        if isinstance(v, tuple):
            lo, hi = v; d = {}
            if lo: d['min'] = lo
            if hi and hi < 100: d['max'] = hi
            out[cat] = d
        else: out[cat] = {'max': v}
    return out

# ---------------------------------------------------------------- Character Advantages (book pp.17-20)
ADV_COST = {'Angones et Franciscae': 30, 'Boats': 10, 'Born to the Purple': 30, 'Chieftain Chariot': 50, 'Fabricae': 15, 'Fearsome Blow': 20, 'Finest Armour': 15,
            'Finest Horses': 20, 'Goad': 15, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Knight Commander': 20, 'Loyalty': 40, 'Man of the People': 40,
            'Mounted Raider': 20, 'Piercing Dart': 5, 'Professional': 25, 'Salmon Leap': 15, 'Veteran': 10}
def adv_label(name, cost):
    return name if cost else name + ' (no cost)'
def adv_opts(advs):
    """advs: {name: cost}  ->  option tuples"""
    return [(adv_label(n, c), c) for n, c in advs.items()]
def adv_tables(key, units, comp_adv, only=()):
    """comp_adv: {composition: {advantage: cost}}.  Adds OPTRULE for every option and OPTAV where the option does not apply to all compositions."""
    labels = {}
    for comp, advs in comp_adv.items():
        for n, c in advs.items(): labels.setdefault((n, c), []).append(comp)
    for (n, c), comps in labels.items():
        lab = adv_label(n, c)
        for u in units:
            OPTRULE.append((key, u, lab, n + ' (Arthur)'))
            if len(comps) < len(comp_adv): OPTAV.append((key, u, lab, comps))
    return [(adv_label(n, c), c) for (n, c) in labels]
def adv_unique(comp_adv):
    seen = {}
    for advs in comp_adv.values():
        for n, c in advs.items(): seen[(n, c)] = 1
    return [(adv_label(n, c), c) for (n, c) in seen]

AGUP = ('Army General (upgrade)', 25)
ASBUP = ('Army Standard Bearer (upgrade)', 15)
UP = [('Standard bearer', 5), ('Musician', 5), ('Leader', 5)]
HORSE = ('Ride a horse', 8)
CHAR_ADV = 'Character Advantages: up to two for an Army General, one for any other character only if the army list allows it. Each advantage may be taken once per 1,000 points (or part thereof) in the army and once per character (not enforced).'
CHP = '(Army General only; Character Advantage)'

def adv_pick(key, comp_adv, units):
    return adv_tables(key, units, comp_adv)

# ====================================================================== common model builders
def foot_opts(extra=()): return list(extra)
def char(name, stats, pts, weapons, rules, options, note, mx=None, page=None, mname=None):
    return U(CH, name, [M(mname or name, stats, pts, weapons=weapons, rules=rules, options=options)], note, mx=mx, page=page)

# ====================================================================== ROMANO-BRITISH CIVITATES (book pp.21-31)
def civ_chars(advs, vortigern=False, brittany=False, twilight=False):
    sw = ['Hand Weapon']
    base = [('Shield', 2), ('Light armour', 3), ('Javelins', 2), ('Throwing spear', 4), HORSE, ('Large shield (replaces shield)', 3)]
    out = []
    if not vortigern:
        out.append(char('Dux/Comes', '5 5 5 4 4 3 5 3 9', 150, sw, ['Army General'], base + advs,
            'Sword. May have shield (+2), light armour (+3), javelins (+2), throwing spear (+4). May be mounted on a horse (M7, +8). If on foot, may have a large shield (+3). Army General. Up to two Character Advantages from the composition. ' + CHAR_ADV, page='26'))
    if not brittany and not vortigern or vortigern:
        out.append(char('Magnate', '5 5 4 3 3 3 4 2 9', 100, sw, ['Army General'], base + [('Heavy throwing spear (replaces throwing spear; on foot)', 4)] + advs,
            'Sword. Same options as the Dux/Comes; if on foot may also have a heavy throwing spear (+4). Army General. Up to two Character Advantages from the composition. 0-1. A powerful Romano-British aristocrat, landowner or official.', mx=1, page='26'))
    out.append(char('Tribune', '5 5 4 4 3 2 5 2 9', 110, sw, [], base + [('Heavy throwing spear (replaces throwing spear; on foot)', 4), AGUP, ASBUP] + advs,
        'Sword. Same options as the Magnate. One Tribune may be upgraded to Army General (+25 pts) if there is no Dux/Comes (or Magnate); one may be upgraded to Army Standard Bearer (+15). Only one Tribune may lead a unit. One Character Advantage (two if Army General).', page='26'))
    out.append(char('Decurio', '5 4 4 3 3 2 4 2 8', 45, sw, [], base + [('Heavy throwing spear (replaces throwing spear; on foot)', 4), ASBUP],
        'Sword. As the Tribune for equipment; one Decurio may be upgraded to Army Standard Bearer (+15). No Character Advantages.', page='26'))
    return out
def civ_troops(vortigern=False, mil_cat=COM):
    t = []
    cm = [('Large shield (replaces shield)', 2), ('Javelins', 1), ('Light armour', 2), ('Heavy throwing spears (replace throwing spear)', 2), ('Thrusting spear (replaces throwing spear)', 0)] + UP
    t.append(U(COM, 'Commanipulares', [M('Commanipulares', '4 4 4 3 3 1 4 1 8', 12, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Shieldwall (Arthur)'], options=cm)],
        'Sword, throwing or thrusting spear and shield. On foot: large shield (+2), javelins (+1), light armour (+2), heavy throwing spears (+2). May form Shieldwall. 0-1 unit of Commanipulares (foot or mounted).', mx=1, page='27'))
    t.append(U(COM, 'Commanipulares (Mounted)', [M('Mounted Commanipulares Cavalryman', '7 4 4 3 3 1 4 1 8', 22, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], options=[('Javelins', 1), ('Light armour', 2), ('Thrusting spear (replaces throwing spear)', 0)] + UP)],
        'Sword, throwing or thrusting spear, shield, horse. May have javelins (+1) and light armour (+2). Light Cavalry. 0-1 unit of Commanipulares (foot or mounted).', mx=1, page='27'))
    t.append(U(mil_cat, 'Milites', [M('Milites', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Shield'], rules=['Shieldwall (Arthur)'], options=[('Large shield (replaces shield)', 1), ('Javelins', 1), ('Thrusting spear (replaces throwing spear)', 0)] + UP)],
        'Throwing or thrusting spear and shield. May exchange shields for large shields (+1) and have javelins (+1). May form Shieldwall.', page='27'))
    t.append(U(mil_cat, 'Milites (Sagittari)', [M('Sagittarius', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon', 'Bow', 'Buckler'], options=UP)],
        'Up to one unit of Milites on foot may be trained as Sagittari (archers): hand weapons, composite bows and bucklers, no further equipment. Light Infantry. 0-1 unit.', mx=1, page='27'))
    t.append(U(mil_cat, 'Equites', [M('Equites Cavalryman', '7 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], options=[('Throwing spear', 2)] + UP)],
        'Mounted Milites: javelins, shield, horse. May have throwing spears (+2). Light Cavalry.', page='27'))
    t.append(U(COM, 'Pedyt', [M('Pedyt', '4 2 3 3 3 1 2 1 6', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Shieldwall (Arthur)'], options=[('Large shield (replaces shield)', 1)] + UP)],
        'Thrusting spear and shield. May exchange shield for large shield (+1). May form Shieldwall. Poorly-trained Romano-British spearmen.', page='27'))
    t.append(U(UNC, 'Rustici', [M('Peasant', '5 2 3 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Skirmishers (Arthur)'], options=[('Sling (replaces javelins)', 0), ('Short bow (replaces javelins)', 0)] + UP)],
        'Javelins, sling or shortbow. Skirmishers.', page='27'))
    return t
CIV_COMMON = 'Units of Commanipulares, Milites (including Sagittari and Equites) and Pedyt may have a Leader (+5), Musician (+5) and Standard (+5).'

TW, BRT = 'Twilight of Britannia', 'Brittany'
CIV_ADV = {TW: {'Born to the Purple': 30, 'Fabricae': 15, 'Fearsome Blow': 20, 'Finest Armour': 15, 'Finest Horses': 20, 'Knight Commander': 20, 'Loyalty': 40, 'Man of the People': 40, 'Professional': 25, 'Veteran': 10},
           BRT: {'Boats': 10, 'Fearsome Blow': 20, 'Finest Armour': 15, 'Finest Horses': 20, 'Knight Commander': 20, 'Loyalty': 40, 'Mounted Raider': 20, 'Professional': 25, 'Veteran': 10}}
CIC = ['Dux/Comes', 'Magnate', 'Tribune']
adv1 = adv_unique(CIV_ADV)
RC = civ_chars(adv1) + civ_troops()
RC = [u for u in RC if not (u['name'] == 'Bishop')]
RC.insert(4, char('Bishop', '5 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE],
    'Hand weapon. May have shield (+2), light armour (+3), horse (M7, +8). Christian Priest. No Character Advantages. 0-1. In Brittany armies, a Dux/Comes must be accompanied by a Bishop (not enforced).', mx=1, page='26'))
RCV = variants('RC', 'Romano-British Civitates', {
 TW: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=20), 'TWILIGHT OF BRITANNIA (c.410-450). Characters up to 33% (led by a Dux/Comes, Magnate or a Tribune upgraded to Army General). Common warriors at least 33% (Commanipulares, Milites incl. Sagittari and Equites, Pedyt). Uncommon up to 20% (Rustici). Allies up to 33% from one list: Franks (Early Merovingian: Franci led by 0-1 Dux or Antrustio) or Saxons (Sea Raiders: Geoguth led by 0-1 Atheling or Thegn). Advantages: Born to the Purple, Fabricae, Fearsome Blow, Finest Armour, Finest Horses, Knight Commander, Loyalty, Man of the People, Professional, Veteran.'),
 BRT: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=20), 'BRITTANY. Characters up to 33% (Dux/Comes or a Tribune upgraded to Army General; no Magnate). Common warriors at least 33% (Commanipulares, Milites incl. Sagittari and Equites, Pedyt). Uncommon up to 20% (Rustici). Allies up to 25% from one list: Franks (Early Merovingian) or Saxons (Sea Raiders). If the army includes a Dux/Comes it must also include a Bishop. Advantages: Boats, Fearsome Blow, Finest Armour, Finest Horses, Knight Commander, Loyalty, Mounted Raider, Professional, Veteran.')})
RC_NOTES = ('ROMANO-BRITISH CIVITATES: TWILIGHT OF BRITANNIA AND BRITTANY (The Age of Arthur, pp.21-31). ' + CIV_COMMON + ' Allies are documented only. Special rules in the book: Allies, Christian Priest, Shieldwall, Light Troops, Character Advantages.')
LISTS.append(('RC', 'Romano-British Civitates: Twilight of Britannia and Brittany (Age of Arthur)', 'Romano_British_Civitates_Arthur.cat', RC, RCV, RC_NOTES))
UNAV.append(('RC', 'Magnate', [BRT]))
adv_tables('RC', CIC, CIV_ADV)
GEN['RC'] = (['Dux/Comes', 'Magnate'], [('Tribune', AGUP[0])])
PAIRS.append(('RC', ['Dux/Comes', 'Magnate'], 'rc-gen'))
OPTRULE += [('RC', 'Tribune', AGUP[0], 'Army General'), ('RC', 'Tribune', ASBUP[0], 'Army Standard'), ('RC', 'Decurio', ASBUP[0], 'Army Standard')]
OPT_ONCE.append(('RC', [('Tribune', ASBUP[0]), ('Decurio', ASBUP[0])]))

# ---- Age of Vortigern (own catalogue: Milites are Uncommon here)
VOR = 'Age of Vortigern'
VORADV = {VOR: {'Fabricae': 15, 'Fearsome Blow': 20, 'Finest Horses': 20, 'Finest Armour': 15, 'Knight Commander': 20}}
vadv = adv_unique(VORADV)
RV = civ_chars(vadv, vortigern=True) + civ_troops(vortigern=True, mil_cat=UNC)
# Dux not available; Magnate (Vortigern) is there
RV = [u for u in RV if u['name'] != 'Dux/Comes']
for u in RV:
    if u['name'] == 'Commanipulares': u['cat'] = COM
RV.insert(3, char('Bishop', '5 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE,
    ('Saint Germanus (Army General, Man of the People, Loyalty)', 70)],
    'Hand weapon. May have shield (+2), light armour (+3), horse (M7, +8). Christian Priest. No Character Advantages except via Saint Germanus: a Bishop may be upgraded to Army General (+70 pts) with Man of the People and Loyalty; no allies, and any number of points may be spent on Commanipulares and Pedyt. 0-1.', mx=1, page='26'))
RVV = variants('RV', 'Romano-British Civitates: Age of Vortigern', {
 VOR: (L(Characters=25, Common_Warriors=50, Uncommon_Warriors=25), 'AGE OF VORTIGERN (c.425-460). Characters up to 25% (no Dux/Comes). Common warriors up to 50% (Commanipulares, Pedyt). Uncommon up to 25% (Milites, Rustici). Allies up to 50% from one list: Scots-Irish (Ceithern led by Curadh or Toiseach), Saxons (Geoguth) or British and Welsh Kingdoms (Combrogi led by Tiern or Uchelwyr); Saxon allied units may have Leader, Standard and Musician free (documented). Advantages: Fabricae, Fearsome Blow, Finest Horses, Finest Armour, Knight Commander. Saint Germanus option: no allies, any number of points on Commanipulares and Pedyt.')})
RV_NOTES = ('ROMANO-BRITISH CIVITATES: AGE OF VORTIGERN (The Age of Arthur, pp.21-31). ' + CIV_COMMON + ' Allies are documented only.')
LISTS.append(('RV', 'Romano-British Civitates: Age of Vortigern (Age of Arthur)', 'Romano_British_Vortigern_Arthur.cat', RV, RVV, RV_NOTES))
adv_tables('RV', ['Magnate', 'Tribune'], VORADV)
GEN['RV'] = (['Magnate'], [('Tribune', AGUP[0]), ('Bishop', 'Saint Germanus (Army General, Man of the People, Loyalty)')])
OPTRULE += [('RV', 'Tribune', AGUP[0], 'Army General'), ('RV', 'Tribune', ASBUP[0], 'Army Standard'), ('RV', 'Decurio', ASBUP[0], 'Army Standard'),
            ('RV', 'Bishop', 'Saint Germanus (Army General, Man of the People, Loyalty)', 'Army General'),
            ('RV', 'Bishop', 'Saint Germanus (Army General, Man of the People, Loyalty)', 'Man of the People (Arthur)'),
            ('RV', 'Bishop', 'Saint Germanus (Army General, Man of the People, Loyalty)', 'Loyalty (Arthur)')]
OPT_ONCE.append(('RV', [('Tribune', ASBUP[0]), ('Decurio', ASBUP[0])]))
for k in ('RC', 'RV'):
    PAIRS.append((k, ['Commanipulares', 'Commanipulares (Mounted)'], k.lower() + '-comm'))

# ====================================================================== BRITISH AND WELSH KINGDOMS (book pp.36-40)
BK, WN, WW, DM = 'British Kingdoms', 'Welsh Kingdoms in the North', 'Welsh Kingdoms in the West', 'Dumnonia and the South-West'
BW_ADV = {BK: {'Boats': 10, 'Fearsome Blow': 20, 'Finest Armour': 15, 'Finest Horses': 20, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Knight Commander': 20, 'Loyalty': 40, 'Man of the People': 40, 'Mounted Raider': 20, 'Piercing Dart': 5, 'Veteran': 10},
          WW: {'Fearsome Blow': 20, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Mounted Raider': 20, 'Piercing Dart': 5, 'Veteran': 10},
          WN: {'Fearsome Blow': 20, 'Finest Horses': 20, 'Goad': 15, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Mounted Raider': 0, 'Piercing Dart': 5, 'Veteran': 10},
          DM: {'Fearsome Blow': 20, 'Finest Horses': 20, 'Hail of Blows': 20, 'Javelin Hurling': 0, 'Piercing Dart': 5, 'Veteran': 10}}
BWO = adv_unique(BW_ADV)
bsw = ['Hand Weapon', 'Javelin', 'Shield']
bch = [('Light armour', 3), ('Throwing spears', 4), HORSE]
BW = []
BW.append(char('Rex', '5 6 5 4 4 3 6 3 9', 170, bsw, ['Army General'], bch + BWO, 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), horse (M7, +8). Army General. Up to two Character Advantages. 0-1. ' + CHAR_ADV + ' Not available in Dumnonia and the South-West.', mx=1, page='39'))
BW.append(char('Tiern', '5 5 4 4 4 2 5 2 8', 75, bsw, [], bch + [AGUP, ASBUP] + BWO, 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), horse (+8). One Tiern may be upgraded to Army Standard Bearer (+15); if no Rex, one Tiern may be upgraded to Army General (+25). One Character Advantage, two if Army General (Dumnonia: one, two if Army General).', page='39'))
BW.append(char('Uchelwyr', '5 4 4 4 4 2 4 2 7', 55, bsw, [], bch + [ASBUP], 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), horse (+8). One Uchelwyr may be upgraded to Army Standard Bearer (+15). No Character Advantages.', page='39'))
BW.append(char('Sacerdot', '5 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE], 'Hand weapon. May have shield (+2), light armour (+3), horse (+8). Christian Priest. No Character Advantages. 0-1.', mx=1, page='39'))
BW.append(char('Bard', '5 4 4 4 3 2 4 2 7', 65, bsw, ['Bard (Arthur)'], bch, 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), horse (+8). Bard. No Character Advantages. 0-1.', mx=1, page='39'))
BW.append(U(COM, 'Teulu', [M('Teulu', '5 4 4 4 3 1 4 1 6', 14, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Warband Psychology (rules 1 & 2)', 'Run for the Woods (Arthur)'], options=[('Light armour', 3), ('Thrusting spear (replaces throwing spear)', 0)] + UP)],
    'Sword, throwing spear, javelins and shield. May have light armour (+3). On foot they are Light Infantry (but in the British Kingdoms composition they lose that status and fight as ordinary heavy infantry with up to a +3 rank bonus). Warband rules 1 and 2. Run for the Woods in the Welsh and Dumnonian compositions. Welsh Kingdoms in the West: thrusting spears may be taken at no cost. 0-1 Teulu unit (foot or mounted).', mx=1, page='40'))
BW.append(U(COM, 'Teulu (Mounted)', [M('Mounted Teulu Cavalryman', '7 4 4 4 3 1 4 1 8', 24, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Run for the Woods (Arthur)'], options=[('Light armour', 3)] + UP)],
    'Sword, throwing spear, javelins, shield and horse. May have light armour (+3). Light Cavalry. 0-1 Teulu unit (foot or mounted).', mx=1, page='40'))
BW.append(U(COM, 'Combrogi', [M('Combrogi', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband Psychology (rules 1 & 2)', 'Run for the Woods (Arthur)'], options=[('Throwing spears', 1), ('Thrusting spears (Welsh Kingdoms in the West; replaces throwing spears)', 1)] + UP)],
    'Hand weapon, javelins and shield. May have throwing spears (+1). Light Infantry on foot (not in the British Kingdoms composition, where they are ordinary heavy infantry with up to +3 rank bonus). Warband rules 1 and 2. Run for the Woods in the Welsh and Dumnonian compositions.', page='40'))
BW.append(U(COM, 'Combrogi (Mounted)', [M('Mounted Combrogi Cavalryman', '6 3 3 3 3 1 3 1 7', 13, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Run for the Woods (Arthur)'], options=[('Throwing spears', 1), ('Ride a horse (replaces ponies)', 3)] + UP)],
    'Hand weapon, javelins, shield and ponies. May have throwing spears (+1). May exchange ponies for horses (+3 per model, M7). Light Cavalry.', page='40'))
BW.append(U(UNC, 'Pagenses', [M('Pagenses', '5 2 3 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Skirmishers (Arthur)', 'Concealment (Arthur)', 'Run for the Woods (Arthur)'], options=[('Sling (replaces javelins)', 0), ('Short bow (replaces javelins)', 0)] + UP)],
    'Hand weapon, javelins, sling or shortbow. Skirmishers. May use the Concealment special rule (Welsh and Dumnonian compositions).', page='40'))
ALLY_BW = 'Allies (documented only). '
BWV = variants('BW', 'British and Welsh Kingdoms', {
 BK: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=20), 'THE BRITISH KINGDOMS (400-550). Characters up to 33% (Rex, or a Tiern upgraded to Army General). Common warriors at least 33% (Teulu, Combrogi). Uncommon up to 20% (Pagenses). Allies up to 25% from one list: Scots-Irish (Scotti Raiders and Settlers or Dalriada; Ceithern led by Curadh or Toiseach) or Saxons (Sea Raiders or Early Anglo-Saxon Kingdoms; Geoguth and Duguth led by Atheling or Thegn). Special: Teulu and Combrogi on foot lose Light Infantry status (ordinary heavy infantry, up to +3 rank bonus); mounted Combrogi may exchange ponies for horses (+3).'),
 WW: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE WELSH KINGDOMS IN THE WEST. Characters up to 33% (Rex, or a Tiern upgraded to Army General). Common warriors at least 33% (Teulu, Combrogi). Uncommon up to 25% (Pagenses). Allies up to 33% from one list: Scots-Irish (Scotti Raiders and Settlers or Dalriada), Saxons (Early Anglo-Saxon Kingdoms or Later Anglian Kingdoms of the Heptarchy) or Romano-British Civitates - Brittany (Milites and Pedyt led by Tribune or Decurio). Special: Teulu, Combrogi and Pagenses have Run for the Woods; foot Teulu/Combrogi may choose thrusting spears (Teulu free, Combrogi +1); Pagenses may use Concealment.'),
 WN: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE WELSH KINGDOMS IN THE NORTH. Characters up to 33% (Rex, or a Tiern upgraded to Army General). Common warriors at least 33% (Teulu, Combrogi). Uncommon up to 25% (Pagenses). Allies up to 33% from one list: Scots-Irish (Dalriada), Saxons (Early Anglo-Saxon Kingdoms or Later Anglian Kingdoms) or the Picts (Early or Later Southern Pictish Kingdoms; Pictish Warriors led by Mormaer or Champion). Special: Run for the Woods; mounted Combrogi may exchange ponies for horses (+3); Pagenses may use Concealment.'),
 DM: (L(Characters=25, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'DUMNONIA AND THE SOUTH-WEST. Characters up to 25% (no Rex; led by a Tiern upgraded to Army General). Common warriors at least 33% (Teulu, Combrogi). Uncommon up to 25% (Pagenses). Allies up to 25% from one list: Scots-Irish (Scotti Raiders and Settlers), Saxons (Later Saxon Kingdoms of the Heptarchy) or Romano-British Civitates - Brittany (Milites and Pedyt led by 0-1 Tribune or 0-1 Decurio). Special: Run for the Woods; mounted Combrogi may exchange ponies for horses (+3); Pagenses may use Concealment.')})
BW_NOTES = ('BRITISH AND WELSH KINGDOMS (The Age of Arthur, pp.36-40). Units of Teulu and Combrogi may have a Leader (+5), Musician (+5) and Standard (+5). Allies are documented only. Run for the Woods: a unit may re-roll any failed Leadership or Break test taken in woods or difficult terrain (even if only partly in it), but a failed test may not be re-rolled more than once.')
LISTS.append(('BW', 'British and Welsh Kingdoms (Age of Arthur)', 'British_Welsh_Kingdoms_Arthur.cat', BW, BWV, BW_NOTES))
UNAV.append(('BW', 'Rex', [DM]))
adv_tables('BW', ['Rex', 'Tiern'], BW_ADV)
GEN['BW'] = (['Rex'], [('Tiern', AGUP[0])])
OPTRULE += [('BW', 'Tiern', AGUP[0], 'Army General'), ('BW', 'Tiern', ASBUP[0], 'Army Standard'), ('BW', 'Uchelwyr', ASBUP[0], 'Army Standard')]
OPT_ONCE.append(('BW', [('Tiern', ASBUP[0]), ('Uchelwyr', ASBUP[0])]))
PAIRS += [('BW', ['Teulu', 'Teulu (Mounted)'], 'bw-teulu')]
OPTAV += [('BW', 'Teulu', 'Thrusting spear (replaces throwing spear)', [WW]), ('BW', 'Combrogi', 'Thrusting spears (Welsh Kingdoms in the West; replaces throwing spears)', [WW]),
          ('BW', 'Combrogi (Mounted)', 'Ride a horse (replaces ponies)', [BK, WW, WN, DM])]
COSTV += [('BW', 'Teulu', {})] if False else []

# ====================================================================== SAXONS (book pp.44-51)
def sax_chars(advs, cyning=True, priest='christian', asb=True, ag_up=True):
    sb = ['Hand Weapon', 'Javelin', 'Buckler']
    o = [('Light armour', 3), ('Throwing spears', 4), HORSE]
    c = []
    if cyning:
        c.append(char('Cyning', '5 5 4 5 4 3 5 2 9', 175, sb, ['Army General', 'Saxon Buckler'], o + advs, 'Sword, javelins and Saxon buckler. May have light armour (+3), throwing spears (+4), horse (M7, +8). Army General. Up to two Character Advantages. 0-1. ' + CHAR_ADV, mx=1, page='49'))
    up = ([AGUP] if ag_up else []) + ([ASBUP] if asb else [])
    c.append(char('Atheling', '5 5 4 4 4 2 5 2 8', 95, sb, ['Saxon Buckler'], o + up + advs, 'Sword, javelins and Saxon buckler. May have light armour (+3), throwing spears (+4), horse (+8). One Atheling may be upgraded to Army Standard Bearer (+15); if no Cyning, one Atheling may be upgraded to Army General (+25). One Character Advantage (two if Army General).', page='49'))
    c.append(char('Thegn', '5 4 4 4 4 2 4 2 7', 60, sb, ['Saxon Buckler'], o + ([ASBUP] if asb else []), 'Sword, javelins and Saxon buckler. May have light armour (+3), throwing spears (+4), horse (+8). One Thegn may be upgraded to Army Standard Bearer (+15). No Character Advantages.', page='49'))
    return c
def sax_extra(wiglera, christian, scop=True):
    c = []
    if wiglera: c.append(char('Wiglera', '5 3 3 3 4 2 4 2 8', 70, ['Hand Weapon'], ['Pagan Priest (Arthur)'], [HORSE], 'Hand weapon. May be mounted on a horse (M7, +8). Pagan Priest. No Character Advantages. 0-1.', mx=1, page='49'))
    if christian: c.append(char('Christian Priest', '5 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE], 'Hand weapon. May have shield (+2), light armour (+3), horse (+8). Christian Priest. No Character Advantages. 0-1.', mx=1, page='49'))
    if scop: c.append(char('Scop', '5 4 4 4 3 2 4 2 7', 65, ['Hand Weapon', 'Javelin', 'Buckler'], ['Bard (Arthur)', 'Saxon Buckler'], [('Light armour', 3), ('Throwing spears', 4), HORSE], 'Sword, javelins and Saxon buckler. May have light armour (+3), throwing spears (+4), horse (+8). Bard. No Character Advantages. 0-1.', mx=1, page='49'))
    return c
def sax_troops(gedriht_cat=COM, geoguth_cat=COM, duguth=True, ceorls=False, fab=False):
    t = []
    la = [('Light armour', 3)]
    t.append(U(gedriht_cat, 'Gedriht', [M('Gedriht', '5 4 4 4 3 1 4 1 6', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Saxon Buckler'], options=la + UP)],
        'Sword, throwing spear, javelins and Saxon buckler. May have light armour (+3). Light Infantry. Warband rules 1 and 2. The warlord\'s hearthguard.', page='50'))
    t.append(U(gedriht_cat, 'Gedriht (Mounted)', [M('Mounted Gedriht Cavalryman', '7 4 4 4 3 1 4 1 8', 23, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], options=la + UP)],
        'As Gedriht, mounted on horses. May have light armour (+3). Light Cavalry.', page='50'))
    if duguth:
        t.append(U(COM, 'Duguth', [M('Duguth', '5 3 3 3 3 1 4 1 6', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Saxon Buckler'], options=UP + ([('Light armour (Fabricae)', 2)] if fab else []))],
            'Throwing spear, javelins, hand weapon and Saxon buckler. Light Infantry. Warband rules 1 and 2.', page='50'))
        t.append(U(COM, 'Duguth (Mounted)', [M('Mounted Duguth Cavalryman', '6 3 3 3 3 1 4 1 7', 14, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], options=[('Ride a horse (replaces ponies)', 3)] + UP)],
            'As Duguth, mounted on ponies; may upgrade to horses (+3 pts, M7). Light Cavalry.', page='50'))
    t.append(U(geoguth_cat, 'Geoguth', [M('Geoguth', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rule 1)', 'Fierce (Arthur)', 'Saxon Buckler'], options=[('Throwing spears', 1)] + UP + ([('Light armour (Fabricae)', 2)] if fab else []))],
        'Javelins, hand weapon and Saxon buckler. May have throwing spears (+1). Light Infantry, Fierce. Warband rules 1 and 2 (Fierce).', page='50'))
    t.append(U(geoguth_cat, 'Geoguth (Mounted)', [M('Mounted Geoguth Cavalryman', '6 3 3 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Fierce (Arthur)'], options=[('Throwing spears', 1), ('Ride a horse (replaces ponies)', 3)] + UP)],
        'As Geoguth, mounted on ponies; may upgrade to horses (+3 pts, M7). Light Cavalry, Fierce.', page='50'))
    if ceorls:
        t.append(U(UNC, 'Ceorls', [M('Yeoman', '4 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Warband Psychology (rules 1 & 2)'], options=UP)],
            'Thrusting spear and shield. Warband rules 1 and 2. Farmers and artisans; part-time warriors.', page='50'))
    t.append(U(UNC, 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Skirmishers (Arthur)'], options=[('Sling (replaces javelins)', 0), ('Short bow (replaces javelins)', 0)] + UP)],
        'Hand weapon and either sling, javelins or shortbow. Skirmishers.', page='50'))
    return t
SAXCOMMON = 'Units of Gedriht, Duguth and Geoguth may have a Leader (+5), Musician (+5) and Standard (+5).'
SXA = ('Saxon Buckler (Arthur) and Warband rules 1 and 2 apply. The optional larger-shield rules are documented only: ')
def sax_list(key, title, fn, comp, lim, txt, units, adv, notes):
    v = variants(key, title, {comp: (lim, txt)})
    LISTS.append((key, f'{title} (Age of Arthur)', fn, units, v, notes))
    adv_tables(key, [u['name'] for u in units if u['name'] in ('Cyning', 'Atheling')], {comp: adv})
    if any(u['name'] == 'Cyning' for u in units): GEN[key] = (['Cyning'], [('Atheling', AGUP[0])])
    else: GEN[key] = ([], [('Atheling', AGUP[0])])
    OPTRULE.append((key, 'Atheling', AGUP[0], 'Army General'))
    ao = [('Atheling', ASBUP[0]), ('Thegn', ASBUP[0])]
    if any(u['name'] == 'Atheling' and any(o[0] == ASBUP[0] for o in u['models'][0]['options']) for u in units):
        OPTRULE.extend([(key, 'Atheling', ASBUP[0], 'Army Standard'), (key, 'Thegn', ASBUP[0], 'Army Standard')])
        OPT_ONCE.append((key, ao))
    PAIRS.append((key, ['Gedriht', 'Gedriht (Mounted)'], key.lower() + '-ged')) if False else None
SEA_ADV = {'Boats': 0, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Loyalty': 40, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10}
EA_ADV = {'Fearsome Blow': 20, 'Finest Horses': 20, 'Hail of Blows': 20, 'Loyalty': 40, 'Mounted Raider': 20, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10}
SK_ADV = {'Fabricae': 15, 'Fearsome Blow': 20, 'Finest Horses': 20, 'Hail of Blows': 20, 'Loyalty': 40, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10}
AN_ADV = {'Fearsome Blow': 20, 'Finest Horses': 20, 'Hail of Blows': 20, 'Loyalty': 40, 'Mounted Raider': 0, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10}
# Sea Raiders
sr = sax_chars(adv_unique({'x': SEA_ADV}), cyning=False, asb=False) + sax_extra(True, False) + sax_troops(duguth=False)
sax_list('SR', 'Saxons: The Sea Raiders', 'Saxon_Sea_Raiders_Arthur.cat', 'The Sea Raiders', L(Characters=33, Common_Warriors=(50, 0), Uncommon_Warriors=10),
    'THE SEA RAIDERS. Characters up to 33% (no Cyning, Army Standard or Christian Priest; the army must be led by an Atheling upgraded to Army General). Common warriors at least 50% (Gedriht and Geoguth; no more than 33% of the points on Gedriht). Uncommon up to 10% (Skirmishers). Allies up to 25% from one list: Franks (Early Merovingian; Franci led by 0-1 Dux or Antrustio) or the Picts (Early Southern Pictish Kingdoms; Warriors led by Mormaer or Champion). More than one unit of Gedriht may be fielded; each Gedriht unit must be led by an Atheling or Thegn (not enforced).',
    sr, SEA_ADV, 'THE SAXONS: THE SEA RAIDERS (The Age of Arthur, pp.44-51). ' + SAXCOMMON)
# Early Anglo-Saxon
ea = sax_chars(adv_unique({'x': EA_ADV})) + sax_extra(True, True) + sax_troops()
sax_list('EA', 'Saxons: Early Anglo-Saxon Kingdoms', 'Saxon_Early_Anglo_Saxon_Arthur.cat', 'Early Anglo-Saxon Kingdoms', L(Characters=33, Common_Warriors=(50, 0), Uncommon_Warriors=10),
    'EARLY ANGLO-SAXON KINGDOMS. Characters up to 33% (the army may include either a Christian Priest or a Wiglera, but not both). Common warriors at least 50% (Gedriht, Geoguth, Duguth). Uncommon up to 10% (Skirmishers). Allies up to 25% from one list: Franks (Early Merovingian), Picts (Early Southern) or Romano-British Civitates - Twilight of Britannia (Milites and Pedyt led by 0-1 Tribune or 0-1 Decurio).',
    ea, EA_ADV, 'THE SAXONS: EARLY ANGLO-SAXON KINGDOMS (The Age of Arthur, pp.44-51). ' + SAXCOMMON)
PAIRS.append(('EA', ['Wiglera', 'Christian Priest'], 'ea-priest'))
# Heptarchy
sk = sax_chars(adv_unique({'x': SK_ADV})) + sax_extra(False, True) + sax_troops(duguth=True, ceorls=True, geoguth_cat=UNC, fab=True)
sax_list('SK', 'Saxons: Saxon Kingdoms of the Heptarchy', 'Saxon_Kingdoms_Heptarchy_Arthur.cat', 'Saxon Kingdoms of the Heptarchy', L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=33),
    'SAXON KINGDOMS OF THE HEPTARCHY. Characters up to 33% (any, except a Wiglera). Common warriors at least 33% (Gedriht, Duguth). Uncommon up to 33% (Ceorls, Geoguth, Skirmishers). Allies up to 25% from one list: Franks (Early Merovingian) or British and Welsh Kingdoms - Dumnonia and the South-West (Combrogi led by 0-1 Tiern or 0-1 Uchelwyr). Optional larger shields (documented only): replace all Saxon bucklers with shields, infantry become ordinary heavy infantry (+3 rank), M4, throwing spears may be exchanged for thrusting spears, Shieldwall allowed.',
    sk, SK_ADV, 'THE SAXONS: SAXON KINGDOMS OF THE HEPTARCHY (The Age of Arthur, pp.44-51). ' + SAXCOMMON)
# Anglian
an = sax_chars(adv_unique({'x': AN_ADV})) + sax_extra(True, True) + sax_troops(duguth=True, ceorls=True, geoguth_cat=UNC)
sax_list('AN', 'Saxons: Anglian Kingdoms of the Heptarchy', 'Saxon_Anglian_Kingdoms_Arthur.cat', 'Anglian Kingdoms of the Heptarchy', L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=33),
    'ANGLIAN KINGDOMS OF THE HEPTARCHY. Characters up to 33% (the army may include either a Christian Priest or a Wiglera, but not both). Common warriors at least 33% (Gedriht, Duguth). Uncommon up to 33% (Ceorls, Geoguth, Skirmishers). Allies up to 33% from one list: British and Welsh Kingdoms (Welsh Kingdoms in the North or West; Combrogi led by 0-1 Tiern or 0-1 Uchelwyr) or the Picts (Later Southern Pictish Kingdoms; Warriors led by 0-1 Mormaer or 0-1 Champion). Optional larger shields (documented only) as for the Saxon Kingdoms of the Heptarchy.',
    an, AN_ADV, 'THE SAXONS: ANGLIAN KINGDOMS OF THE HEPTARCHY (The Age of Arthur, pp.44-51). ' + SAXCOMMON)
PAIRS.append(('AN', ['Wiglera', 'Christian Priest'], 'an-priest'))

# ====================================================================== FRANKS (book pp.55-58)
FR_ADV = {'Angones et Franciscae': 30, 'Fabricae': 15, 'Finest Armour': 15, 'Finest Horses': 0, 'Hail of Blows': 20, 'Loyalty': 40, 'Mounted Raider': 20, 'Veteran': 10}
fo = [('Light armour', 3), ('Throwing spears', 4), ('Shortbow', 3), HORSE]
fsw = ['Hand Weapon', 'Javelin', 'Shield']
FR = []
FR.append(char('Rex', '5 6 4 4 4 3 5 3 9', 180, fsw, ['Army General'], fo + adv_unique({'x': FR_ADV}), 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), shortbow (+3), horse (M7, +8). Army General. Up to two Character Advantages. 0-1. ' + CHAR_ADV, mx=1, page='57'))
FR.append(char('Dux', '5 5 4 4 4 2 5 2 8', 95, fsw, [], fo + [AGUP, ASBUP] + adv_unique({'x': FR_ADV}), 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), shortbow (+3), horse (+8). One Dux may be upgraded to Army Standard Bearer (+15); if no Rex, one Dux may be upgraded to Army General (+25). One Character Advantage (two if Army General).', page='57'))
FR.append(char('Antrustio', '5 4 4 4 4 2 4 2 7', 60, fsw, [], fo + [ASBUP, ('Angones et Franciscae', 30)], 'Sword, javelins and shield. May have light armour (+3), throwing spears (+4), shortbow (+3), horse (+8). One Antrustio may be upgraded to Army Standard Bearer (+15). An Antrustio may take the Angones et Franciscae advantage if not upgraded to Army Standard Bearer.', page='57'))
FR.append(char('Christian Priest', '4 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE], 'Hand weapon. May have shield (+2), light armour (+3), horse (+8). Christian Priest. No Character Advantages. 0-1.', mx=1, page='57'))
FR.append(U(COM, 'Pueri', [M('Pueri', '5 4 4 3 3 1 4 1 6', 15, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Warband Psychology (rule 1)', 'Fierce (Arthur)'], options=[('Light armour', 3)] + UP)],
    'Sword, throwing spear, javelins and shield. May have light armour (+3). On foot Fierce, Warband rules 1 and 2. The number of Pueri units is not limited, but each Pueri unit must be led by an Antrustio, Dux or Rex, who must remain with the unit (not enforced).', page='57'))
FR.append(U(COM, 'Pueri (Mounted)', [M('Mounted Pueri Cavalryman', '7 4 4 3 3 1 4 1 8', 23, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Fierce (Arthur)'], options=[('Light armour', 3)] + UP)],
    'As Pueri, mounted on horses. Light Cavalry and Fierce. Must be led by an Antrustio, Dux or Rex.', page='57'))
FR.append(U(COM, 'Franci', [M('Franci', '5 3 3 3 3 1 4 1 6', 8, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Warband Psychology (rules 1 & 2)'], options=[('Light armour', 2)] + UP)],
    'Throwing spears, javelins, hand weapon and shield. Up to half of the units of Franci in the army may have light armour (+2; not enforced). Warband rules 1 and 2.', page='57'))
FR.append(U(COM, 'Franci (Mounted)', [M('Mounted Franci Cavalryman', '7 3 3 3 3 1 4 1 7', 17, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Shield'], rules=['Warband Psychology (rule 1)'], options=[('Light armour', 2)] + UP)],
    'As Franci, mounted on horses. Light Cavalry. Warband rule 1.', page='57'))
FR.append(U(UNC, 'Tribal Warriors', [M('Tribal Warrior', '5 3 3 3 3 1 3 1 5', 6, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband Psychology (rules 1 & 2)', 'Mixed Weapons (Arthur)'], options=UP)],
    'Mixed weapons and shield. Warband rules 1 and 2.', page='58'))
FR.append(U(UNC, 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Skirmishers (Arthur)'], options=[('Javelins (replaces shortbow)', 0), ('Sling (replaces shortbow)', 0)] + UP)],
    'Hand weapon and shortbow, javelins or sling. Skirmishers.', page='58'))
FRV = variants('FR', 'Franks: Early Merovingian Franks', {'Early Merovingian Franks': (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25),
 'EARLY MEROVINGIAN FRANKS (c.450-600). Characters up to 33% (Rex or Dux; advantages Angones et Franciscae, Fabricae, Finest Armour, Finest Horses (no cost), Hail of Blows, Loyalty, Mounted Raider, Veteran). Common warriors at least 33% (Pueri and Franci). Uncommon up to 25% (Tribal Warriors and Skirmishers). Allies up to 25% from one list: Saxons - The Sea Raiders (Geoguth led by 0-1 Atheling or 0-1 Thegn) or Romano-British Civitates - Brittany (Milites and Pedyt led by 0-1 Tribune or 0-1 Decurio).')})
LISTS.append(('FR', 'Franks: Early Merovingian Franks (Age of Arthur)', 'Franks_Early_Merovingian_Arthur.cat', FR, FRV,
    'THE FRANKS (The Age of Arthur, pp.55-58). An alternative to the Early Merovingian Franks list in Beyond the Golden Gate. Units of Pueri, Franci and Tribal Warriors may have a Leader (+5), Musician (+5) and Standard (+5). Allies are documented only.'))
adv_tables('FR', ['Rex', 'Dux'], {'x': FR_ADV})
OPTRULE += [('FR', 'Antrustio', 'Angones et Franciscae', 'Angones et Franciscae (Arthur)'), ('FR', 'Dux', AGUP[0], 'Army General'), ('FR', 'Dux', ASBUP[0], 'Army Standard'), ('FR', 'Antrustio', ASBUP[0], 'Army Standard')]
GEN['FR'] = (['Rex'], [('Dux', AGUP[0])])
OPT_ONCE.append(('FR', [('Dux', ASBUP[0]), ('Antrustio', ASBUP[0])]))

# ====================================================================== PICTS (book pp.59-69)
ES, LS, NP, AT = 'Early Southern Pictish Kingdoms', 'Later Southern Pictish Kingdoms', 'Picts of the North', 'The Attecotti'
PI_ADV = {ES: {'Boats': 0, 'Chieftain Chariot': 50, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Loyalty': 40, 'Mounted Raider': 0, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10},
          LS: {'Boats': 10, 'Finest Horses': 20, 'Loyalty': 40, 'Javelin Hurling': 10, 'Veteran': 10, 'Fearsome Blow': 20, 'Hail of Blows': 20, 'Mounted Raider': 20, 'Piercing Dart': 5},
          NP: {'Boats': 0, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Loyalty': 40, 'Mounted Raider': 20, 'Javelin Hurling': 0, 'Piercing Dart': 0, 'Veteran': 10},
          AT: {'Boats': 0, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Loyalty': 40, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Veteran': 10}}
PWO = adv_unique(PI_ADV)
pch = ['Hand Weapon', 'Javelin', 'Buckler']
po = [('Light armour', 3), ('Throwing spears', 4), HORSE]
PI = []
PI.append(char('Chieftain', '5 5 6 4 4 3 6 3 9', 160, pch, ['Army General'], po + [('Chieftain Chariot (see Character Advantages)', 0)][:0] + PWO, 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), horse (M7, +8). Army General. Up to two Character Advantages. 0-1. In a chariot (Chieftain Chariot advantage): M8 WS5 BS6 S4 T4 W3 I6 A4 Ld9. Not available to Picts of the North or the Attecotti. ' + CHAR_ADV, mx=1, page='65'))
PI.append(char('Mormaer', '5 4 5 4 4 2 5 3 8', 75, pch, [], po + [AGUP, ASBUP] + PWO, 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), horse (+8). If no Chieftain, one Mormaer may be upgraded to Army General (+25); one may be upgraded to Army Standard Bearer (+15). One Character Advantage (two if Army General). In a chariot: M8 WS4 BS5 S4 T4 W2 I5 A4 Ld8.', page='65'))
PI.append(char('Champion', '5 4 4 4 4 2 4 2 7', 50, pch, [], po + [ASBUP], 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), horse (+8). One Champion may be upgraded to Army Standard Bearer (+15). No Character Advantages.', page='65'))
PI.append(char('Magus', '5 3 3 3 4 2 4 1 7', 70, ['Hand Weapon'], ['Pagan Priest (Arthur)'], [HORSE], 'Staff or similar hand weapon. May be mounted on a horse (M7, +8). Pagan Priest. No Character Advantages. 0-1. In the Later Southern Pictish Kingdoms the army may include either a Magus or a Christian Priest, not both.', mx=1, page='65'))
PI.append(char('Christian Priest', '4 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE], 'Hand weapon. May have shield (+2), light armour (+3), horse (+8). Christian Priest. No Character Advantages. 0-1. Not available in the Early Southern Pictish Kingdoms or Picts of the North.', mx=1, page='65'))
PI.append(char('Bard', '5 4 4 3 4 2 4 1 7', 60, ['Hand Weapon', 'Javelin', 'Buckler'], ['Bard (Arthur)'], [('Light armour', 3), ('Throwing spears', 4), HORSE], 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), horse (+8). Bard. No Character Advantages. 0-1.', mx=1, page='65'))
PI.append(U(COM, 'Pictish Nobles', [M('Pictish Noble', '5 4 4 3 4 1 4 1 6', 13, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)'], options=[('Light armour', 3), ('Thrusting spears and shield (Later Southern; replace throwing spears and buckler)', 0)] + UP)],
    'Hand weapon, throwing spears, buckler and javelins. May have light armour (+3; not in the North or the Attecotti). Light Infantry. Warband rules 1 and 2. In the Attecotti army all Nobles and Warriors are Fierce. 0-1 unit of Nobles (foot or mounted).', mx=1, page='66'))
PI.append(U(COM, 'Pictish Nobles (Mounted)', [M('Mounted Pictish Noble Cavalryman', '6 4 4 3 4 1 4 1 7', 19, mn=5, weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Buckler'], options=[('Light armour', 3), ('Ride a horse (replaces ponies)', 3)] + UP)],
    'Hand weapon, throwing spears, buckler, javelins and ponies. May have light armour (+3). Ponies may be exchanged for horses (+3, M7) in the Early and Later Southern Pictish Kingdoms. Light Cavalry. Not in the North or the Attecotti (no horses). 0-1 unit of Nobles (foot or mounted).', mx=1, page='66'))
PI.append(U(COM, 'Pictish Warriors', [M('Pictish Warrior', '5 3 3 3 3 1 3 1 6', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Mixed Weapons (Arthur)'], options=[('Thrusting spears, javelins and shield (Later Southern; replace mixed weapons and buckler)', 1)] + UP)],
    'Mixed weapons and buckler. Light Infantry. Warband rules 1 and 2.', page='66'))
PI.append(U(COM, 'Pictish Warriors (Mounted)', [M('Mounted Pictish Warrior Cavalryman', '6 3 3 3 3 1 3 1 6', 11, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=[('Ride a horse (replaces ponies)', 3)] + UP)],
    'Javelins, buckler and ponies. Ponies may be exchanged for horses (+3, M7) in the Later Southern Pictish Kingdoms. Light Cavalry.', page='66'))
PI.append(U(UNC, 'Pictish Hunters', [M('Hunter', '5 2 3 3 3 1 3 1 6', 6, mn=5, weapons=['Hand Weapon', 'Short Bow'], rules=['Skirmishers (Arthur)', 'Concealment (Arthur)'], options=[('Javelins (replaces shortbow)', 0), ('Hunting crossbow (replaces shortbow or javelins; one unit)', 1)] + UP)],
    'Hand weapon and either shortbow or javelins. 0-1 unit may exchange its shortbows or javelins for hunting crossbows (+1 pt). Skirmishers. May use the Concealment special rule.', page='66'))
PI.append(U(UNC, 'Hunting Dogs', [M('Packmaster', '5 3 3 3 4 1 4 1 6', 12, mn=1, mx=1, key='pm', weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Skirmishers (Arthur)']),
    M('Hound', '6 3 0 3 3 1 3 1 3', 5, mn=0, mx=6, key='hound', rules=['Skirmishers (Arthur)'])],
    'The unit must be led by a single Packmaster and may include up to six Hunting Hounds. The Packmaster has javelins and a buckler; the hounds have their teeth. Warband. Skirmishers. Missile hits are randomly divided between the Packmaster and the hounds; the hounds use the Master\'s Leadership unless he is killed. 0-1 unit.', mx=1, page='66'))
PIV = variants('PI', 'Picts', {
 ES: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE EARLY SOUTHERN PICTISH KINGDOMS. Characters up to 33% (led by a Chieftain, or a Mormaer upgraded to Army General; no Christian Priest). Common warriors at least 33% (Nobles and Warriors). Uncommon up to 25% (Hunters and Hunting Dogs). Allies up to 25% from one list: Romano-British Civitates - Twilight of Britannia (Milites and Pedyt), Scots-Irish (Scotti Raiders and Settlers) or Saxons (Sea Raiders). Mounted Nobles may exchange ponies for horses (+3).'),
 LS: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE LATER SOUTHERN PICTISH KINGDOMS. Characters up to 33% (led by a Chieftain, or a Mormaer upgraded to Army General; either a Magus or a Christian Priest, not both). Common warriors at least 33% (Nobles and Warriors). Uncommon up to 25% (Hunters and Hunting Dogs). Allies up to 25% from one list: British and Welsh Kingdoms - the Welsh Kingdoms in the North, Scots-Irish (Dalriada) or Saxons (Anglian Kingdoms of the Heptarchy). Nobles and Warriors may exchange ponies for horses (+3). Optional Pictish thrusting spears (documented): Nobles and Warriors on foot become ordinary heavy infantry (up to +3 rank bonus, but only +2 for Leadership); Nobles exchange throwing spears and bucklers for thrusting spears and shields (free); Warriors exchange mixed weapons and bucklers for thrusting spears, javelins and shields (+1).'),
 NP: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE PICTS OF THE NORTH. Characters up to 33% (no Chieftain: led by a Mormaer upgraded to Army General; no Christian Priest). Common warriors at least 33% (Nobles and Warriors). Uncommon up to 25% (Hunters and Hunting Dogs). Allies up to 25% from the Scots-Irish (Dalriada). Nobles may not have light armour or horses.'),
 AT: (L(Characters=40, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE ATTECOTTI. Characters up to 40% (no Chieftain: led by a Mormaer upgraded to Army General). Common warriors at least 33% (Nobles and Warriors). Uncommon up to 25% (Hunters and Hunting Dogs). Allies up to 25% from the Scots-Irish (Dalriada). All Nobles and Warriors are Fierce (even if mounted; documented only). Nobles may not have light armour or horses.')})
PI_NOTES = ('THE PICTS (The Age of Arthur, pp.59-69). Units of Nobles and Warriors may have a Leader (+5), Musician (+5) and Standard (+5). Allies are documented only. Hunting Crossbow: range 24", Strength 3, no armour save modifier; may not move and shoot in the same turn.')
LISTS.append(('PI', 'The Picts (Age of Arthur)', 'Picts_Arthur.cat', PI, PIV, PI_NOTES))
adv_tables('PI', ['Chieftain', 'Mormaer'], PI_ADV)
OPTRULE += [('PI', 'Mormaer', AGUP[0], 'Army General'), ('PI', 'Mormaer', ASBUP[0], 'Army Standard'), ('PI', 'Champion', ASBUP[0], 'Army Standard')]
GEN['PI'] = (['Chieftain'], [('Mormaer', AGUP[0])])
OPT_ONCE.append(('PI', [('Mormaer', ASBUP[0]), ('Champion', ASBUP[0])]))
UNAV += [('PI', 'Chieftain', [NP, AT]), ('PI', 'Christian Priest', [ES, NP]), ('PI', 'Pictish Nobles (Mounted)', [NP, AT])]
OPTAV += [('PI', 'Pictish Nobles', 'Light armour', [ES, LS]), ('PI', 'Pictish Nobles (Mounted)', 'Light armour', [ES, LS]),
          ('PI', 'Pictish Nobles', 'Thrusting spears and shield (Later Southern; replace throwing spears and buckler)', [LS]),
          ('PI', 'Pictish Warriors', 'Thrusting spears, javelins and shield (Later Southern; replace mixed weapons and buckler)', [LS]),
          ('PI', 'Pictish Warriors (Mounted)', 'Ride a horse (replaces ponies)', [LS]), ('PI', 'Pictish Nobles (Mounted)', 'Ride a horse (replaces ponies)', [ES, LS])]
OPTAV[:] = [x for x in OPTAV if not (x[0] == 'PI' and x[1] == 'Pictish Nobles' and x[2] == 'Thrusting spears and shield (Later Southern; replace throwing spears and buckler)' and False)]
PAIRS += [('PI', ['Pictish Nobles', 'Pictish Nobles (Mounted)'], 'pi-nobles'), ('PI', ['Magus', 'Christian Priest'], 'pi-priest')]
# Chieftain / Mormaer in a chariot
for u in ('Chieftain', 'Mormaer'):
    OPTSTAT += [('PI', u, 'Chieftain Chariot', 'M', 8), ('PI', u, 'Chieftain Chariot', 'A', 4)]

# ====================================================================== SCOTS-IRISH (book pp.71-79)
RS, DA, KI = 'Scotti Raiders and Settlers', 'Dalriada', 'Kingdoms of Ireland'
SI_ADV = {RS: {'Boats': 0, 'Chieftain Chariot': 50, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Salmon Leap': 15, 'Veteran': 10},
          DA: {'Boats': 0, 'Fearsome Blow': 20, 'Goad': 15, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Salmon Leap': 15, 'Veteran': 10},
          KI: {'Boats': 10, 'Chieftain Chariot': 50, 'Fearsome Blow': 20, 'Finest Horses': 20, 'Goad': 15, 'Hail of Blows': 20, 'Javelin Hurling': 10, 'Piercing Dart': 5, 'Salmon Leap': 15, 'Veteran': 10}}
sio = [('Light armour', 3), ('Throwing spears', 4), ('Sling', 3), HORSE]
sic = ['Hand Weapon', 'Javelin', 'Buckler']
SI = []
SI.append(char('Ri Tuath', '5 6 6 4 4 3 6 3 9', 165, sic, ['Army General'], sio + adv_unique(SI_ADV), 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), sling (+3), horse (M7, +8). Army General. Up to two Character Advantages. In a chariot (Chieftain Chariot advantage): M8 WS6 BS6 S4 T4 W3 I6 A4 Ld9. Not available to Scotti Raiders and Settlers. ' + CHAR_ADV, mx=1, page='75'))
SI.append(char('Curadh', '5 5 5 4 4 2 5 3 8', 75, sic, [], sio + [AGUP, ASBUP, ('Light chariot with driver', 10)] + adv_unique(SI_ADV), 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), sling (+3), horse (+8), or ride in a light chariot with driver (+10; Kingdoms of Ireland, or an Army General with Chieftain Chariot). If no Ri Tuath, one Curadh may be upgraded to Army General (+25); one Curadh may carry the Army Standard (+15). A maximum of one Curadh per unit. One Character Advantage (two if Army General). In a chariot: M8 WS5 BS5 S4 T4 W2 I5 A4 Ld8.', page='76'))
SI.append(char('Toiseach', '5 4 4 4 4 2 4 2 7', 50, sic, [], sio + [ASBUP, ('Light chariot with driver', 10)], 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), sling (+3), horse (+8), or ride in a light chariot with driver (+10; Kingdoms of Ireland). One Toiseach may be upgraded to Army Standard Bearer (+15). No Character Advantages. In a chariot: M8 WS4 BS4 S4 T4 W2 I4 A3 Ld7.', page='76'))
SI.append(char('Druid', '5 3 3 3 4 2 4 1 8', 75, ['Hand Weapon'], ['Pagan Priest (Arthur)'], [HORSE], 'Hand weapon. May be mounted on a horse (M7, +8). Pagan Priest. A Druid may not be included in the same army as a Priest. No Character Advantages. 0-1. Not available to Dalriada.', mx=1, page='76'))
SI.append(char('Cruimther', '5 4 3 3 3 2 4 2 8', 70, ['Hand Weapon'], ['Christian Priest (Arthur)'], [('Shield', 2), ('Light armour', 3), HORSE], 'Hand weapon. May have shield (+2), light armour (+3), horse (+8). Christian Priest. A Cruimther may not be included in the same army as a Druid. No Character Advantages. 0-1.', mx=1, page='76'))
SI.append(char('Filidh', '5 4 4 3 4 2 4 1 7', 60, sic, ['Bard (Arthur)'], [('Light armour', 3), ('Throwing spears', 4), HORSE], 'Sword, javelins and buckler. May have light armour (+3), throwing spears (+4), horse (+8). Bard. No Character Advantages. 0-1.', mx=1, page='76'))
SI.append(U(COM, 'Fianna', [M('Fianna', '5 4 4 3 4 1 3 1 6', 11, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Mixed Weapons (Arthur)'], options=[('Light armour', 3), ('Hand weapon, javelins and throwing spears (replace mixed weapons)', 2)] + UP)],
    'Dismounted Fianna: mixed weapons and buckler. May have light armour (+3). May exchange mixed weapons for hand weapon, javelins and throwing spears (+2). Warband rules 1 and 2. 0-1 unit of Fianna (foot or mounted).', mx=1, page='76'))
SI.append(U(COM, 'Fianna (Mounted)', [M('Mounted Fianna Cavalryman', '6 4 4 3 4 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rule 1)'], options=[('Light armour', 3), ('Throwing spears', 2), ('Ride a horse (replaces ponies)', 3)] + UP)],
    'Javelins, swords, bucklers and ponies. May have light armour (+3) and throwing spears (+2); ponies may be exchanged for horses (+3, M7). Light Cavalry, Warband rule 1. 0-1 unit of Fianna (foot or mounted).', mx=1, page='76'))
SI.append(U(COM, 'Ceithern', [M('Ceithern', '5 3 3 3 3 1 2 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rules 1 & 2)', 'Mixed Weapons (Arthur)'], options=UP)],
    'Mixed weapons and bucklers. Warband rules 1 and 2. Foot soldiers.', page='77'))
SI.append(U(COM, 'Ridir (Mounted Ceithern)', [M('Ridir Cavalryman', '6 3 3 3 3 1 2 1 6', 11, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], options=UP)],
    'Javelins, hand weapons and bucklers. Light Cavalry. Not available to Dalriada.', page='77'))
SI.append(U(UNC, 'Tilgeyr', [M('Tilgeyr', '5 2 3 3 3 1 2 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Skirmishers (Arthur)'], options=[('Sling (replaces javelins)', 0)] + UP)],
    'Hand weapons and javelins or slings. Skirmishers.', page='77'))
SI.append(U(UNC, 'Irish Wolfhounds', [M('Arrchogad', '5 4 3 3 4 1 4 1 6', 12, mn=1, mx=1, key='pm', weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Warband Psychology (rule 1)', 'Skirmishers (Arthur)']),
    M('Wolfhound', '6 4 0 3 3 1 3 1 3', 6, mn=0, mx=6, key='hound', rules=['Skirmishers (Arthur)'])],
    'The unit must be led by a single Packmaster (Arrchogad) and may include up to six wolfhounds. The Arrchogad has hand weapon, javelins and a buckler; the hounds have their teeth. Warband rule 1. Skirmishers. Missile hits are randomly divided between the Arrchogad and the hounds; the hounds use his Leadership unless he is killed. 0-1 unit.', mx=1, page='77'))
SIV = variants('SI', 'Scots-Irish', {
 RS: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=20), 'SCOTS-IRISH RAIDERS AND SETTLERS. Characters up to 33% (no Ri Tuath: led by a Curadh upgraded to Army General). Common warriors at least 33% (Fianna and Ceithern). Uncommon up to 20% (Tilgeyr and Irish Wolfhounds). Allies up to 25% from one list: British and Welsh Kingdoms (British Kingdoms or Welsh Kingdoms in the West; Combrogi led by 0-1 Tiern or 0-1 Uchelwyr) or the Picts (Early or Later Southern Pictish Kingdoms or Picts of the North; Pictish Warriors led by Mormaer or Champion). Curadh and Toiseach may not ride in chariots (except a Curadh upgraded to Army General who takes Chieftain Chariot).'),
 DA: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=20), 'DALRIADA. Characters up to 33% (led by a Curadh upgraded to Army General; no Druid). Common warriors at least 33% (Fianna and Ceithern). Uncommon up to 20% (Tilgeyr and Irish Wolfhounds). Allies up to 25% from one list: British and Welsh Kingdoms (British Kingdoms or Welsh Kingdoms in the West) or the Picts (Early or Later Southern Pictish Kingdoms or Picts of the North). Mounted Ceithern may not be fielded; no characters in chariots; a King\'s Champion may be taken (documented).'),
 KI: (L(Characters=33, Common_Warriors=(33, 0), Uncommon_Warriors=25), 'THE KINGDOMS OF IRELAND. Characters up to 33% (40% if the army features a squadron of Heroes in Chariots), led by a Ri Tuath or a Curadh upgraded to Army General. Common warriors at least 33% (Fianna and Ceithern). Uncommon up to 25% (Tilgeyr and Irish Wolfhounds). Allies up to 25% from the Scots-Irish - Dalriada (Ceithern led by 0-1 Curadh or 0-1 Toiseach). Any Curadh and Toiseach may ride in chariots. A King\'s Champion may be taken; characters in chariots may form a chariot squadron (Heroes in Chariots; both documented).')})
SI_NOTES = ('THE SCOTS-IRISH (The Age of Arthur, pp.71-79). Units of Fianna and Ceithern may have a Leader (+5), Musician (+5) and Standard (+5). Allies are documented only. King\'s Champion: if the army is led by a Ri Tuath, a single Curadh may be designated King\'s Champion with up to three Character Advantages (no advantage more than once; points paid as normal); he may never refuse a challenge. Heroes in Chariots: a squadron of at least three characters in chariots deployed at the start of the battle (each chariot counts as two models; no Leader, Standard or Musician; see the book).')
LISTS.append(('SI', 'The Scots-Irish (Age of Arthur)', 'Scots_Irish_Arthur.cat', SI, SIV, SI_NOTES))
adv_tables('SI', ['Ri Tuath', 'Curadh'], SI_ADV)
OPTRULE += [('SI', 'Curadh', AGUP[0], 'Army General'), ('SI', 'Curadh', ASBUP[0], 'Army Standard'), ('SI', 'Toiseach', ASBUP[0], 'Army Standard')]
GEN['SI'] = (['Ri Tuath'], [('Curadh', AGUP[0])])
OPT_ONCE.append(('SI', [('Curadh', ASBUP[0]), ('Toiseach', ASBUP[0])]))
UNAV += [('SI', 'Ri Tuath', [RS]), ('SI', 'Druid', [DA]), ('SI', 'Ridir (Mounted Ceithern)', [DA])]
OPTAV += [('SI', 'Curadh', 'Light chariot with driver', [RS, KI]), ('SI', 'Toiseach', 'Light chariot with driver', [KI]), ('SI', 'Fianna (Mounted)', 'Ride a horse (replaces ponies)', [RS, DA, KI])]
PAIRS += [('SI', ['Fianna', 'Fianna (Mounted)'], 'si-fianna'), ('SI', ['Druid', 'Cruimther'], 'si-priest')]
for u, a in (('Curadh', 4), ('Toiseach', 3)):
    OPTSTAT += [('SI', u, 'Light chariot with driver', 'M', 8), ('SI', u, 'Light chariot with driver', 'A', a)]
for u in ('Ri Tuath', 'Curadh'):
    OPTSTAT += [('SI', u, 'Chieftain Chariot', 'M', 8), ('SI', u, 'Chieftain Chariot', 'A', 4)]
