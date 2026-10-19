# The Art of War (Warhammer Historical, Far East) army lists. Book page = printed page number (pdf page - 2). Model stats order: M WS BS S T W I A Ld
import copy
from rb_data import M, U
LISTS = []; VAR = {}; AVAIL = []; UNAV = []; OPTAV = []; OPTRULE = []; OPTSTAT = []; RATIOS = []; OPT_ONCE = []; PAIRS = []
SECOND = {}; UNIT_MAX_IN = []; GEN = {}; COND_CHARS = []; COSTV = []; STATV = []; EXCL = []
FLAT = []; PTSLIM = []; MODLIM = []; HIRDMEN_LE_BONDIR = []
CH, CHT, INF, SPU, CAV, MOB, ALL = 'Characters', 'Chariotry', 'Infantry', 'Special Units', 'Cavalry', 'Mobs', 'Allies and Mercenaries'
PUB = 'The Art of War'

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

UP = [('Standard bearer', 5), ('Musician', 5), ('Leader', 5)]
HORSE = ('Ride a horse', 0)
LAM = ('Lamellar armour (5+ save; counts as light armour for movement)', 4)
PMAX = 'Percentage limits are by points. "May only have one selected option per 1,000 points" for Special Units is documented only.'
def char(name, stats, pts, weapons, rules, options, note, mx=None, page=None, mname=None):
    return U(CH, name, [M(mname or name, stats, pts, weapons=weapons, rules=rules, options=options)], note, mx=mx, page=page)

# ====================================================================== EARLY CHINESE (book pp.12-14)
PRE, LAT, SAN = 'Pre-Shang and Early Shang', 'Later Shang', 'Army of Sanxingdui'
EC = []
ecopt = [('Shield', 2), ('Dagger axe (counts as halberd)', 2), ('Light armour', 3)]
EC.append(char('King (Wang)', '4 5 5 4 3 3 6 3 9', 140, ['Hand Weapon'], ['Army General', 'Casting the Oracle Bones'], ecopt + [('Frightening Masks (fear)', 20)],
    'Army Commander. Armed with a hand weapon. May have a shield (+2), dagger axe (+2) and light armour (+3). May ride in a two-horse light chariot bought from the list below (not enforced; characters may not have chariots in the Pre-Shang list). Army General. Casting the Oracle Bones. Frightening Masks (+20, Army of Sanxingdui only): the character causes fear.', mx=1, page='13'))
EC.append(char('Duke (Gong)', '4 5 5 4 3 2 5 2 9', 128, ['Hand Weapon'], ['Army General', 'Casting the Oracle Bones'], ecopt + [('Frightening Masks (fear)', 20)],
    'Army Commander. Armed with a hand weapon. May have a shield (+2), dagger axe (+2) and light armour (+3). May ride in a two-horse light chariot (not enforced). Army General. Casting the Oracle Bones. Frightening Masks (+20, Army of Sanxingdui only).', mx=1, page='13'))
EC.append(char('Fuhao (Warrior Consort)', '4 5 5 4 3 2 6 2 9', 185, ['Hand Weapon', 'Bow', 'Light Armour'], ['Army General', 'Casting the Oracle Bones', 'Fearsome (Art of War)', 'Warrior of Legend'], [],
    'Special character. Armed with a hand weapon, bow and light armour. May ride in a two-horse light chariot bought at additional cost. Army General. Casting the Oracle Bones. Fearsome. Warrior of Legend. Not available to the Army of Sanxingdui. The grave of Fuhao was discovered in 1976 at the Royal tombs in Anyang. 0-1.', mx=1, page='14'))
EC.append(char('Army Standard Bearer (Qi Canren Deren)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Thrusting spear', 2), ('Light armour', 2)],
    'Armed with a hand weapon. May have a shield (+2), thrusting spear (+2) and light armour (+2). May ride in a two-horse light chariot (not enforced). Army Standard Bearer. 0-1.', mx=1, page='13'))
EC.append(char('Nobles (Guizu)', '4 5 5 4 4 1 5 2 8', 50, ['Hand Weapon', 'Bow'], [], [('Shield', 2), ('Axe (counts as double-handed weapon)', 2), ('Thrusting spear', 2), ('Light armour', 2)],
    'Armed with a hand weapon and bow. May have a shield (+2), axe (+2) or thrusting spear (+2) and light armour (+2). May ride in a two-horse light chariot (not enforced).', page='13'))
EC.append(U(CHT, 'Chariots (Xiao Zhanche)', [M('Light Chariot', '8 4 4 3 4 1 4 2 8', 45, weapons=['Hand Weapon', 'Bow', 'Light Armour'], rules=['Light Chariots'])],
    'One crewman armed with a hand weapon, bow and light armour riding in a two-horse light chariot with unarmed driver. Light Chariots. Not available to the Pre-Shang and Early Shang or the Army of Sanxingdui compositions (the Sanxingdui use Elephants instead).', page='13'))
EC.append(U(CHT, 'Chariot Retinue (Zhanche Huweizhe)', [M('Chariot Retinue', '5 4 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops', 'Chariot Runners (Art of War)'], options=[('Dagger axe (counts as halberd; replaces shield)', 0), ('Light armour', 2), ('Thrusting spear (replaces dagger axe)', 0)] + UP)],
    'Armed with a hand weapon and shield or dagger axe. May have light armour (+2). May have thrusting spear instead of dagger axe. Light Infantry. Chariot Runners: up to one unit of 10 models per chariot fielded; initially deployed within 6" of the chariot model. In the Army of Sanxingdui the Retinue becomes an Elephant Retinue (the Chariot Runner rules apply to Elephants instead).', page='13'))
EC.append(U(INF, 'Royal Guard (Lu)', [M('Royal Guard', '4 4 3 3 3 1 4 1 8', 9, mn=5, weapons=['Hand Weapon', 'Shield', 'Halberd'], rules=['Royal Guard (Art of War)'], options=[('Light armour', 2), ('Bow', 2), ('Thrusting spear (replaces axe)', 0)] + UP)],
    'Armed with a hand weapon, shield and axe. May have light armour (+2), bow (+2), or thrusting spear instead of axe. Royal Guard. May only be fielded if the King is Army Commander. 0-1.', mx=1, page='13'))
EC.append(U(INF, 'Clan Warriors (Zhong)', [M('Clan Warrior', '4 4 3 3 3 1 4 1 7', 7, mn=5, weapons=['Hand Weapon', 'Shield'], options=[('Light armour', 2), ('Bow (replaces shield)', 1), ('Dagger axe (counts as halberd; replaces shield)', 1)] + UP)],
    'Armed with a hand weapon and shield. May have light armour (+2). May have bow or dagger axe instead of shield (+1).', page='14'))
EC.append(U(INF, 'Impressed Peasants (Qiang Zhide Nongmin)', [M('Peasant', '4 2 2 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon'], rules=['Light Troops', 'Peasants (Art of War)'], options=[('Dagger axe (counts as halberd)', 3)] + UP)],
    'Armed with a hand weapon or farm implements. May have dagger axe (+3). Light Infantry. Peasants: may only declare a charge if they have a leader or character in the unit; fear all other enemy troops except other peasants until an enemy unit is broken in close combat.', page='14'))
EC.append(U(SPU, 'Elephant (Xiang)', [M('Elephant', '6 4 0 6 5 5 3 4 4', 140, key='el', rules=['Elephants (Art of War)']),
    M('Driver', '4 2 2 3 3 1 3 1 7', 0, mn=1, mx=1, key='drv', weapons=['Hand Weapon']),
    M('Elephant Crewman', '4 2 2 3 3 1 3 1 7', 0, mn=0, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Javelins', 0), ('Bow', 2), ('Light armour', 2)])],
    'An unarmed driver and up to two crew armed with javelins or bows (+2 pts) per crewman. Crew may have light armour (+2 pts). Elephants. Designer\'s note: although elephants were present in Shang and Pre-Shang China there is no definite evidence they were used for warfare; offered for speculating "what if". 0-1 (the Army of Sanxingdui may have up to one per 1,000 points).', mx=1, page='14'))
EC.append(U(SPU, 'Barbarian Allies (Yemande Mengguo)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra cost. Skirmishers.', page='14'))
ECV = variants('EC', 'Early Chinese', {
 PRE: (L(Characters=25, Infantry=(50, 0), Special_Units=25), 'PRE-SHANG AND EARLY SHANG DYNASTY (Xia and earlier, or Early Shang before chariots, c.1300 BCE). Characters up to 25% (at least one army commander, the character with the highest Leadership; characters may not have chariots). Infantry at least 50%. Special Units up to 25% (one selected option per 1,000 points). No chariotry.'),
 LAT: (L(Characters=25, Chariotry=50, Infantry=(25, 0), Special_Units=25), 'LATER SHANG DYNASTY (after the introduction of chariots c.1300 BCE). Characters up to 25% (at least one army commander). Chariotry up to 50%. Infantry at least 25%. Special Units up to 25% (one selected option per 1,000 points).'),
 SAN: (L(Characters=25, Chariotry=50, Infantry=(25, 0), Special_Units=25), 'ARMY OF SANXINGDUI. Characters up to 25% (one army commander; no chariots, but may be mounted on Elephants instead, the points taken from the Chariots section). May take Frightening Masks (+20 pts: the character causes fear). Chariotry up to 50%: no chariots, but Elephants may be taken instead (Chariot Retinue becomes Elephant Retinue; Chariot Runners rules apply to Elephants). Infantry at least 25%. Special Units up to 25%, with up to 1 Elephant per 1,000 points. Fuhao is not available.')})
EC_NOTES = ('EARLY CHINESE (The Art of War, pp.12-14): Pre-Shang and Early Shang, Later Shang and the Army of Sanxingdui. Special rules: Auspicious Conditions (roll a D6 at the start of the game: 1 = automatically fail the first D3 Leadership tests; 6 = automatically pass them), Casting the Oracle Bones, Off with their heads!. ' + PMAX)
LISTS.append(('EC', 'Early Chinese (Art of War)', 'Early_Chinese_Art_of_War.cat', EC, ECV, EC_NOTES))
UNAV += [('EC', 'Chariots (Xiao Zhanche)', [PRE, SAN]), ('EC', 'Fuhao (Warrior Consort)', [SAN]), ('EC', 'Elephant (Xiang)', [PRE, LAT]), ('EC', 'Royal Guard (Lu)', [])][:3] if False else []
UNAV += [('EC', 'Chariots (Xiao Zhanche)', [PRE, SAN]), ('EC', 'Fuhao (Warrior Consort)', [SAN]), ('EC', 'Chariot Retinue (Zhanche Huweizhe)', [PRE])]
OPTAV += [('EC', 'King (Wang)', 'Frightening Masks (fear)', [SAN]), ('EC', 'Duke (Gong)', 'Frightening Masks (fear)', [SAN])]
OPTRULE += [('EC', 'King (Wang)', 'Frightening Masks (fear)', 'Fear'), ('EC', 'Duke (Gong)', 'Frightening Masks (fear)', 'Fear')]
PAIRS.append(('EC', ['King (Wang)', 'Duke (Gong)', 'Fuhao (Warrior Consort)'], 'ec-gen'))
RATIOS.append(('EC', 'Chariot Retinue (Zhanche Huweizhe)', ['Chariots (Xiao Zhanche)'], 1))
PTSLIM += [('EC', 'Elephant (Xiang)', 1000, [SAN])]
UNAV[:] = [x for x in UNAV if not (x[0] == 'EC' and x[1] == 'Elephant (Xiang)')]

# ====================================================================== EARLY EASTERN TRIBES (book pp.15-17)
BT, ET_, ST, WT, NT = 'Basic Tribe', 'Tribes of the East (Dong Yi)', 'Tribes of the South (Man Yi)', 'Tribes of the West (Rong Yi)', 'Tribes of the North (Di Yi)'
TRIB = 'Tribal Warriors'
EE = []
EE.append(char('Warlord (Junfa)', '5 6 6 4 4 3 6 3 7', 140, ['Hand Weapon'], ['Army General', 'Hidden Ambush Force'], [('Shield', 2), ('Axe (counts as double-handed weapon)', 2), ('Dagger axe (counts as halberd)', 2), ('Light armour', 3)],
    'Armed with a hand weapon. May have a shield (+2 pts), axe (+2) or dagger axe (+2) and light armour (+3). Army General. Subject to the Psychology of the group they join. If the army has an Army General, he may take a Leadership test to play Hidden Ambush Force. 0-1. The army should include at least one character to lead it.', mx=1, page='16'))
EE.append(char('Totem Bearer (Dudengxingxiang)', '5 4 4 4 3 2 4 2 5', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Light armour', 3)],
    'Armed with a hand weapon. May have a shield (+2 pts) and light armour (+3). Army Standard Bearer. Subject to the Psychology of the group they join. Not available in the Tribes of the East or West, which have a Totem instead.', page='16'))
EE.append(U(CH, 'Stone Dolman (Totem)', [M('Stone Dolman', '- - - - 5 3 - - -', 15, key='totem', rules=['Army Standard', 'Totem (Art of War)'])],
    'Tribes of the East only: the Totem is a stone dolman (+15 pts) instead of a Totem Bearer. Functions like an Army Standard Bearer but cannot move or be destroyed; deployed outside the enemy deployment zone on a 50mm x 50mm square or round base.', mx=1, page='17'))
EE.append(U(CH, 'Spirit Stone (Totem)', [M('Spirit Stone', '- - - - 5 3 - - -', 15, key='totem', rules=['Army Standard', 'Totem (Art of War)'])],
    'Tribes of the West only: the Totem is a spirit stone (+15 pts) instead of a Totem Bearer. Functions like an Army Standard Bearer but cannot move or be destroyed; deployed outside the enemy deployment zone on a 50mm x 50mm square or round base.', mx=1, page='17'))
EE.append(char('Tribal Shaman (Buluo Huanjiao)', '4 4 4 4 3 2 5 2 8', 75, ['Improvised Weapon'], ['Spirit of the Shaman', 'Fear'], [('Buckler', 1)],
    'Armed with an improvised weapon. May have a buckler (+1 pt). Spirit of the Shaman (causes fear; roll a D6 for the unit he is with at the start of the game). Subject to the Psychology of the group they join. Shamanic Challenge. 0-1.', mx=1, page='16'))
EE.append(char('Chieftains (Shouling)', '5 5 5 4 4 2 5 3 6', 70, ['Hand Weapon'], [], [('Shield', 2), ('Axe (counts as double-handed weapon)', 2), ('Dagger axe (counts as halberd)', 2), ('Light armour', 3)],
    'Armed with a hand weapon. May have a shield (+2 pts), axe (+2) or dagger axe (+2) and light armour (+3). Subject to the Psychology of the group they join. In the Tribes of the North may ride in a chariot (not enforced).', page='16'))
EE.append(U(TRIB, 'Tribal Warriors (Buluo Zhanshi)', [M('Tribal Warrior', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Warband'],
    options=[('Light armour', 3), ('Thrusting or throwing spears', 2), ('Javelins', 2), ('Thrusting spear (included)', 0), ('Throwing spear (included)', 0), ('Dagger axe (counts as halberd)', 1), ('Stubborn', 3)] + UP)],
    'Armed with shields and hand weapons. May have light armour (+3 pts), thrusting or throwing spears (+2 pts) and javelins (+2 pts). Warband. Tribal variants: East - thrusting spears and may be Stubborn (+3); South - skirmishers with throwing spears, no light armour; West - throwing spears, Light Infantry, not subject to the Warband rules; North - thrusting spears, may take dagger axes (+1). At least 33% of the army points.', page='16'))
EE.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Tribal Skirmisher', '5 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Javelin', 'Improvised Weapon'], rules=['Skirmishers (Art of War)'], options=[('Buckler or shield', 1)] + UP)],
    'Armed with javelins and improvised weapons. May have bucklers or shields (+1 pt). Skirmishers.', page='16'))
EE.append(U(INF, 'Tribal Archers (Buluo Gongjianshu)', [M('Tribal Archer', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Short Bow', 'Improvised Weapon'], rules=['Skirmishers (Art of War)'],
    options=[('Compound bow (replaces short bow)', 2), ('Light armour', 3), ('Poisoned arrows (South; automatic wound on a 6 to hit, armour saves allowed)', 1)] + UP)],
    'Armed with a short bow and improvised weapons. May have compound bow instead of short bow (+2 pts), light armour (+3). Skirmishers. Tribes of the South: poisoned arrows (+1 pt) cause an automatic wound if they roll a 6 to hit; armour saves are allowed.', page='16'))
EE.append(U(INF, 'Tribespeople (Buluo Minzhong)', [M('Tribesperson', '4 1 2 3 3 1 3 1 5', 3, mn=5, weapons=['Improvised Weapon'], options=UP)],
    'Armed with improvised weapons and rocks (range 4", Strength 3). In situations where they needed to defend their homes or flocks, tribespeople would have fought as well.', page='16'))
EE.append(U(CHT, 'Chariots (Zhanche)', [M('Light Chariot', '8 4 4 3 4 1 4 2 6', 34, weapons=['Hand Weapon'], rules=['Light Chariots'], options=[('Shield', 4), ('Axe (counts as double-handed weapon)', 2), ('Light armour', 3)])],
    'Tribes of the North only. Warrior armed with a hand weapon riding in a two-horse light chariot with driver. May have shield (+4 pts), axe (+2 pts) and light armour (+3 pts) each. Light Chariots. One chariot squadron of three Light Chariot models per 1,000 points (not enforced), and chariots for characters.', page='17'))
EEV = variants('EE', 'Early Eastern Tribes', {
 BT: (L(Characters=33, Tribal_Warriors=(33, 0), Infantry=50), 'BASIC TRIBE. Characters up to 33% (at least one character to lead). Tribal Warriors at least 33%. Infantry up to 50% (Skirmishers, Archers and Tribespeople). Tribal Warriors may take thrusting or throwing spears (+2) and javelins (+2).'),
 ET_: (L(Characters=33, Tribal_Warriors=(33, 0), Infantry=50), 'THE TRIBES OF THE EAST (Dong Yi). Favoured terrain: Temperate. Tribal Warriors are armed with thrusting spears and can be made Stubborn (+3). Their Totem is a stone dolman (+15 pts) instead of a Totem Bearer.'),
 ST: (L(Characters=33, Tribal_Warriors=(33, 0), Infantry=50), 'THE TRIBES OF THE SOUTH (Man Yi). Favoured terrain: Tropical. Tribal Warriors are skirmishers armed with throwing spears. Tribal Archers may have poisoned arrows (+1 pt). May not take light armour.'),
 WT: (L(Characters=33, Tribal_Warriors=(33, 0), Infantry=50), 'THE TRIBES OF THE WEST (Rong Yi). Favoured terrain: Mountains. Tribal Warriors are armed with throwing spears and are treated like Light Infantry and are not subject to the Warband rules (documented). Their Totem is a spirit stone (+15 pts) instead of a Totem Bearer.'),
 NT: (L(Characters=33, Tribal_Warriors=(33, 0), Infantry=50), 'THE TRIBES OF THE NORTH (Di Yi). Favoured terrain: Steppes. Tribal Warriors are armed with thrusting spears; may take dagger axes (+1 pt). May take chariots for characters and one chariot squadron of three Light Chariot models per 1,000 points.')})
EE_NOTES = ('EARLY EASTERN TRIBES (The Art of War, pp.15-17). Special rules: Army General - Hidden Ambush Force, Totems, Spirit of the Shaman (D6 table: 1 Snake - the unit does not move in the first turn and cannot move until it passes a Leadership test; 2 Bear - may not march but may re-roll missed To Wound rolls; 3 Deer - formed unit may make a free 4" move at the start of the game; 4 Wolf - Frenzy; 5 Eagle - may Fall Back in Good Order even if outnumbered; 6 Buffalo - Stubborn), Shamanic Challenge. ' + PMAX)
LISTS.append(('EE', 'Early Eastern Tribes (Art of War)', 'Early_Eastern_Tribes_Art_of_War.cat', EE, EEV, EE_NOTES))
UNAV += [('EE', 'Totem Bearer (Dudengxingxiang)', [ET_, WT]), ('EE', 'Stone Dolman (Totem)', [BT, ST, WT, NT]), ('EE', 'Spirit Stone (Totem)', [BT, ET_, ST, NT]), ('EE', 'Chariots (Zhanche)', [BT, ET_, ST, WT])]
OPTAV += [('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Thrusting or throwing spears', [BT]), ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Javelins', [BT]),
          ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Thrusting spear (included)', [ET_, NT]), ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Throwing spear (included)', [ST, WT]),
          ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Dagger axe (counts as halberd)', [NT]), ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Stubborn', [ET_]),
          ('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Light armour', [BT, ET_, WT, NT]),
          ('EE', 'Tribal Archers (Buluo Gongjianshu)', 'Poisoned arrows (South; automatic wound on a 6 to hit, armour saves allowed)', [ST]),
          ('EE', 'Tribal Archers (Buluo Gongjianshu)', 'Light armour', [BT, ET_, WT, NT])]
for u in ('Warlord (Junfa)', 'Totem Bearer (Dudengxingxiang)', 'Chieftains (Shouling)'):
    OPTAV.append(('EE', u, 'Light armour', [BT, ET_, WT, NT]))
OPTRULE += [('EE', 'Tribal Warriors (Buluo Zhanshi)', 'Stubborn', 'Stubborn')]
PAIRS.append(('EE', ['Totem Bearer (Dudengxingxiang)', 'Stone Dolman (Totem)', 'Spirit Stone (Totem)'], 'ee-totem'))

# ====================================================================== HAN: YELLOW SCARVES (book pp.112-115)
YS = []
YS.append(char('Celestial Master (Tien Shi)', '4 5 5 3 3 2 6 2 9', 140, ['Hand Weapon'], ['Army General', 'Charisma (Art of War)', 'Sacred Chant (Art of War)', 'Invulnerable to Weapons (Art of War)'], [('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), lamellar armour (+4), horse (free, M8). May ride in a four-horse heavy chariot (below, not enforced). Army General. Charisma. Sacred Chant. Invulnerable to Weapons. 0-1.', mx=1, page='112'))
YS.append(char('Libationers (Chi Jiu)', '4 4 3 3 3 2 5 2 5', 50, ['Hand Weapon'], ['Invulnerable to Weapons (Art of War)'], [('Shield', 2), ('Light armour', 2), HORSE, ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free, M8). Army General - if no other Army General is taken, a Libationer may be made Army General for +25 pts. Invulnerable to Weapons. The Yellow Scarves named their leaders Libationers after the fellows who led the toast at banquets.', page='113'))
YS.append(char('Priests (Dao Shi)', '4 2 2 3 3 1 3 1 7', 60, ['Hand Weapon'], ['Rouse the Mobs (Art of War)'], [],
    'Armed with a hand weapon. Rouse the Mobs - Mobs may use the Priest\'s Leadership for the Rouse the Mobs test. The Mob becomes Invulnerable to Weapons if the Priest is present in the front rank.', page='113'))
YS.append(char('Chieftains (Shouling)', '4 5 3 3 3 2 5 2 8', 75, ['Hand Weapon'], [], [('Shield', 2), ('Light armour', 2), ('Compound bow', 2), HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), compound bow (+2), horse (free, M8). As uprisings gained momentum they tended to attract nobles and other powerful leaders.', page='113'))
YS.append(char('Sacred Banner Bearer (Shensengde Hengfusizushou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard', 'Stubborn', 'Invulnerable to Weapons (Art of War)'], [('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), lamellar armour (+4) and horse (free, M8). Army Standard Bearer. Stubborn. Invulnerable to Weapons. 0-1.', mx=1, page='113'))
YS.append(U(CH, 'Heavy Chariot (Shuang Lun Zhan Che)', [M('Heavy Chariot', '6 4 4 3 4 2 4 4 8', 67, weapons=['Hand Weapon', 'Halberd', 'Crossbow'], rules=['Chariots'], options=[('Crew light armour (+2 pts each)', 4)])],
    'Two crewmen with hand weapons, one armed with a spear tipped halberd and one armed with a crossbow, riding in a four-horse heavy chariot with driver. Crew may have light armour (+2 pts each). Heavy Chariots cause D3 Strength 4 Impact Hits. Crossbows used from chariots may only fire once.', page='113'))
YS.append(char('Hero (Ying Xiong)', '4 5 5 4 4 1 5 2 8', 55, ['Hand Weapon'], ['Warrior of Legend', 'Independent Character (Art of War)'], [('Exotic weapons (count as additional hand weapons)', 2), ('Spear tipped halberd', 2), HORSE,
    ('Strongman (Strength 5, Wounds 2)', 15), ('Swift as the Wind (Movement 6)', 5), ('Skilled Archer (compound bow instead of exotic weapons or halberd)', 2)],
    'Armed with a hand weapon. May have exotic weapons (+2 pts, count as additional hand weapons) or spear tipped halberd (+2). May have horse (free, M8). One speciality: Strongman (S5, W2; +15), Swift as the Wind (M6; +5) or Skilled Archer (compound bow; +2). Warrior of Legend. Independent Character: although a hero may accompany and lead a unit, his Leadership cannot be used by the unit; he cannot use the Army General or Sacred Banner Bearer for Leadership tests. Dodge Save: disdaining armour they receive a 5+ special dodge save not modified by Strength. 0-1.', mx=1, page='113'))
YS.append(U(INF, 'Disciples (Zhuisuizhe)', [M('Disciple', '4 4 3 3 3 1 3 1 8', 12, mn=5, weapons=['Hand Weapon', 'Halberd'], rules=['Invulnerable to Weapons (Art of War)'], options=[('Swords and shields (replaces halberd)', 0), ('Light armour', 2)] + UP)],
    'Armed with a spear tipped halberd or swords and shields. May have light armour (+2 pts). Invulnerable to weapons. 0-1.', mx=1, page='113'))
YS.append(U(INF, 'Followers of Dao', [M('Follower of Dao', '4 3 3 3 3 1 3 1 7', 8, mn=5, weapons=['Hand Weapon'], rules=['Invulnerable to Weapons (Art of War)'], options=[('Thrusting spear', 1), ('Spear tipped halberds', 2), ('Light armour', 2)] + UP)],
    'Armed with a hand weapon. May have thrusting spear (+1 pt) or spear tipped halberds (+2 pts). May have light armour (+2 pts). Invulnerable to weapons.', page='113'))
YS.append(U(INF, 'Deserters (Daobing)', [M('Deserter', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon'], options=[('Swords and shields', 1), ('Spear tipped halberd', 1), ('Bows', 2), ('Crossbows', 3), ('Light armour', 2)] + UP)],
    'Armed with a hand weapon. May have swords and shields or spear tipped halberd (+1 pt) or bows (+2 pts) or crossbows (+3 pts), may have light armour (+2 pts).', page='114'))
YS.append(U(INF, 'Peasants (Nong Fu)', [M('Peasant', '4 2 2 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Warband Psychology (rule 1)', 'Light Troops'], options=[('Thrusting spear', 2)] + UP)],
    'Armed with farm implements and rocks (count as hand weapons/javelins, 4" range). May have thrusting spear (+2 pts). Warband Rule 1. Light Infantry. May only charge if led by a character.', page='114'))
YS.append(U(MOB, 'Yellow Scarves Mobs (Baomin)', [M('Mob', '4 2 2 3 3 1 2 1 3', 3, mn=5, weapons=['Improvised Weapon'], rules=['Warband Psychology (rule 1)', 'Mobs (Art of War)'], options=[])],
    'Armed with improvised weapons and bright yellow headscarves. Mobs and any characters with their unit are subject to Warband Psychology Rule 1. Mobs cannot Fall Back in Good Order unless they outnumber by more than 3 to 1. They cannot benefit from the Leadership value of characters (other than Libationers), nor use the re-roll benefit of the Army Standard. A Priest\'s Leadership may however be used to Rouse the Mob. Mob Deployment: deployed last before characters, on the player\'s table edge or the furthest possible distance from the enemy. Rousing the Mob and Fear of horses: see the book. 0-3.', mx=3, page='114'))
YS.append(U(SPU, 'Light Cavalry Archers (Gong Jian Zhuang Jia Shibing)', [M('Light Cavalry Archer', '8 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with hand weapon and bow. May have light armour (+2 pts). Light Cavalry. 0-1.', mx=1, page='115'))
YS.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 4, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May have javelin and buckler at no extra points. Skirmishers.', page='115'))
YS.append(U(SPU, 'Looted Light Bolt Thrower (She Mao Jian Shou)', [M('Light Bolt Thrower', '- - - - 6 2 - - -', 50, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'The machine is equipped with two crew armed with a hand weapon. May have light armour (+2 pts). Bolt Thrower: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. 0-1.', mx=1, page='115'))
YS.append(char('Zhang Zhue', '4 4 4 4 4 2 5 2 9', 180, ['Hand Weapon', 'Halberd'], ['Army General', 'Charisma (Art of War)', 'Warrior of Legend', 'Frenzy', 'Invulnerable to Weapons (Art of War)', 'Healing Potions (Art of War)'], [],
    'Special character. Armed with a hand weapon, heavy halberd and lamellar armour and horse (free, M8). Army General. Charisma. Warrior of Legend. Frenzy. Invulnerable to Weapons. Healing Potions: ignores one wound caused on any unit he is included with per turn. 0-1; replaces the Celestial Master as Army General.', mx=1, page='115'))
YSV = variants('YS', 'Yellow Scarves Religious Cultists', {'Yellow Scarves': (L(Characters=25, Infantry=(25, 0), Mobs=(25, 0), Special_Units=25),
 'HAN DYNASTY - RELIGIOUS CULTISTS - YELLOW SCARVES. Characters up to 25%. Infantry at least 25%. Mobs at least 25%. Special Units up to 25% (only one selected option per 1,000 points).')})
YS_NOTES = ('YELLOW SCARVES RELIGIOUS CULTISTS (The Art of War, pp.112-115). Special rules: Charisma (a character with this ability provides his Leadership as Army General until he or his unit flees or breaks; then a Panic test as for the death of the General), Sacred Chant (at the start of his turn the player may announce a Sacred Chant: all units become immune to Panic tests and each model gains one additional attack for that one turn; once only), Invulnerable to Weapons (units or characters may re-roll any Panic tests and are subject to the Stubborn rules). Rousing the Mob: at the start of the first turn the mob takes a Leadership test; if passed subtract the dice roll from its Leadership: 0-3 the Mob moves forward at least 4" and is subject to all Warband Psychology rules, 4-8 the same plus doubled attacks in the first round of all combats; if failed the mob counts as Levies. Fear of horses: a Mob successfully charged by cavalry, chariots, elephants, camels, war wagons etc. must take a Fear test. ' + PMAX)
LISTS.append(('YS', 'Han Dynasty: Yellow Scarves Religious Cultists (Art of War)', 'Han_Yellow_Scarves_Art_of_War.cat', YS, YSV, YS_NOTES))
OPTRULE += [('YS', 'Libationers (Chi Jiu)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['YS'] = (['Celestial Master (Tien Shi)', 'Zhang Zhue'], [('Libationers (Chi Jiu)', 'Army General (+25 pts; if no other Army General)')])
PAIRS.append(('YS', ['Celestial Master (Tien Shi)', 'Zhang Zhue'], 'ys-gen'))
OPTRULE += [('YS', 'Hero (Ying Xiong)', 'Strongman (Strength 5, Wounds 2)', 'Strongman (Art of War)')]
OPTSTAT += [('YS', 'Hero (Ying Xiong)', 'Strongman (Strength 5, Wounds 2)', 'S', 5), ('YS', 'Hero (Ying Xiong)', 'Strongman (Strength 5, Wounds 2)', 'W', 2),
            ('YS', 'Hero (Ying Xiong)', 'Swift as the Wind (Movement 6)', 'M', 6)]

# ====================================================================== HAN: THREE KINGDOMS (book pp.116-119)
TK = []
TK.append(char('Yang Warlord', '4 6 6 4 4 3 6 3 8', 140, ['Hand Weapon'], ['Army General', 'Heroic Combat (Art of War)'], [('Heavy halberd (+2 Strength on the charge for cavalry)', 3), LAM, HORSE, ('Ride a warhorse', 8), ('Barding', 4)],
    'Armed with a hand weapon. May have a heavy halberd (+3 pts), lamellar armour (+4), horse (free, M8), warhorse (+8), barding for horse (+4). Army General. Heroic Combat. 0-1 Warlord (Yang or Yin).', mx=1, page='116'))
TK.append(char('Yin Warlord', '4 5 5 3 3 2 6 1 9', 140, ['Hand Weapon'], ['Army General', 'Military Strategist (Art of War)'], [('Light armour', 2), HORSE],
    'Armed with a hand weapon. May have light armour (+2 pts), horse (free, M8). Army General. Military Strategist. 0-1 Warlord (Yang or Yin).', mx=1, page='116'))
TK.append(char('General (Jiang Jun)', '4 5 3 3 3 2 5 2 8', 75, ['Hand Weapon'], ['Heroic Combat (Art of War)'], [('Shield', 2), ('Light armour', 2), HORSE, ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free, M8). Heroic Combat. If no other Army General is taken, the General may be made Army General for +25 pts. Generals who acted on the warlord\'s orders are treated as subsidiary characters.', page='116'))
TK.append(char('Army Standard Bearer (Jun Dui Zhang Qi Shou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Light armour', 2), LAM, HORSE, ('Barding', 4)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), lamellar armour (+4) and horse (free, M8), barding for horse (+4). Army Standard Bearer. 0-1.', mx=1, page='116'))
TK.append(char('Army Musician (Jun Dui Yue Shi)', '0 3 3 3 3 1 4 1 8', 20, ['Hand Weapon'], ['Army Musician (Art of War)'], [('Light armour', 2)],
    'Armed with a hand weapon and very big drum or gong! May have light armour (+2 pts). Army Musician. 0-1.', mx=1, page='116'))
TK.append(char('Military Strategist (Jun Shi Jia)', '4 2 2 3 3 1 3 1 7', 25, ['Hand Weapon'], ['Military Strategist (Art of War)'], [],
    'Armed with a hand weapon. Military Strategist. 0-1. Military advisors to famous warlords usually wore civilian garb.', mx=1, page='116'))
TK.append(char('Liu Bei', '4 6 5 3 3 3 6 3 10', 225, ['Hand Weapon', 'Hand Weapon'], ['Army General', 'Heroic Combat (Art of War)', 'Warrior of Legend', 'Military Strategist (Art of War)', 'Sworn Brotherhood - First Brother', 'Steadfast (Art of War)'], [],
    'Special character. Armed with a pair of double-edged swords (counts as additional hand weapon), lamellar armour and horse (free, M8). Army General. Heroic Combat. Warrior of Legend. Military Strategist. Sworn Brotherhood - First Brother. Quality: Steadfast. 0-1.', mx=1, page='118'))
TK.append(char('Guan Yu', '4 5 5 4 4 3 5 3 9', 125, ['Hand Weapon', 'Halberd'], ['Army Standard', 'Heroic Combat (Art of War)', 'Warrior of Legend', 'Sworn Brotherhood - Second Brother', 'Courage (Art of War)'], [],
    'Special character. Armed with a Green Crescent moon halberd (counts as a heavy halberd), lamellar armour and horse (free, M8). Army Standard Bearer. Heroic Combat. Warrior of Legend. Sworn Brotherhood - Second Brother. Quality: Courage - any unit or character within 6" of Guan Yu at the Combat Resolution phase becomes Stubborn for that turn. 0-1.', mx=1, page='119'))
TK.append(char('Zhang Fei', '4 5 5 3 3 2 5 2 9', 110, ['Hand Weapon', 'Kontos'], ['Army Standard', 'Heroic Combat (Art of War)', 'Warrior of Legend', 'Sworn Brotherhood - Third Brother', 'Impetuous'], [],
    'Special character. Armed with an 18-span Serpent Headed Spear (counts as a kontos), lamellar armour and horse (free, M8). Army Standard Bearer. Heroic Combat. Warrior of Legend. Sworn Brotherhood - Third Brother. Quality: Impetuous. 0-1. The Brotherhood of the Peach Garden (Liu Bei, Guan Yu, Zhang Fei) must fight on the same side; taken together the First Brother is Army General, the Second the Army Standard Bearer and the Third a Champion; see the book.', mx=1, page='119'))
TK.append(char('Cao Cao', '4 6 5 3 3 3 6 3 10', 225, ['Hand Weapon', 'Halberd'], ['Army General', 'Heroic Combat (Art of War)', 'Warrior of Legend', 'Military Strategist (Art of War)', 'Guile (Art of War)'], [],
    'Special character. Armed with a crescent moon halberd (counts as a heavy halberd), lamellar armour and horse (free, M8). Army General. Heroic Combat. Warrior of Legend. Military Strategist. Quality: Guile - he may counteract any one Ruse per game before a player attempts their Leadership roll; may roll an additional D6 when fleeing. 0-1.', mx=1, page='119'))
TK.append(char('Zhuge Liang', '4 4 4 3 3 2 5 2 10', 200, ['Hand Weapon'], ['Army General', 'Military Strategist (Art of War)', 'Master Strategist (Art of War)'], [],
    'Special character. Armed with a Noble Sword (+1 Strength on all hits), lamellar armour and horse (free, M8). Army General. Military Strategist. Quality: Master Strategist - he can hold two Ruses instead of one per 1,000 pts. 0-1.', mx=1, page='119'))
TK.append(U(CH, 'Red Hare', [M('Red Hare', '9 3 0 3 - - 4 1 -', 15, rules=['Warhorse'])],
    'A superb horse from the Romance of the Three Kingdoms. May be assigned to a Warlord, General or special character at the start of the game. Warhorse. 0-1.', mx=1, page='119'))
TK.append(U(CAV, 'Guard Cavalry (Weiso Qibing)', [M('Guard Cavalryman', '8 4 4 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Stubborn', 'Knights Rank Bonus'], options=[('Heavy halberd (instead of thrusting spear)', 1), ('Bow', 3)] + UP)],
    'Armed with hand weapon, thrusting spear, lamellar armour and barding. May take a heavy halberd instead of thrusting spear (+1 pt). May have bow (+3 pts). Stubborn. May count rank bonus of up to +1 even though cavalry. 0-1.', mx=1, page='117'))
TK.append(U(CAV, 'Heavy Cavalry (Daliang Qibing)', [M('Heavy Cavalryman', '8 4 4 3 3 1 3 1 8', 30, mn=5, weapons=['Hand Weapon', 'Thrusting Spear'], rules=['Knights Rank Bonus'], options=[('Bow', 3)] + UP)],
    'Armed with a hand weapon, thrusting spear, lamellar armour and barding. May have bow (+3 pts). May count rank bonus of up to +1 even though cavalry. 0-1.', mx=1, page='117'))
TK.append(U(CAV, 'Light Cavalry Lancers (Chi Mao Zhuang Jia Shibing)', [M('Light Cavalry Lancer', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Halberd'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with hand weapons and spear tipped halberds. May have light armour (+2 pts). Light Cavalry.', page='117'))
TK.append(U(CAV, 'Light Cavalry Archers (Gong Jian Zhuang Jia Shibing)', [M('Light Cavalry Archer', '8 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Bow'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with bows. May have light armour (+2 pts). Light Cavalry.', page='117'))
TK.append(U(CAV, 'Light Cavalry Crossbow (Shi Gong Zhuang Jia Shibing)', [M('Light Cavalry Crossbowman', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Improvised Weapon', 'Light Crossbow'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with horse crossbows and improvised weapons. May have light armour (+2 pts). Light Cavalry. The horse crossbow has a range of 24", Strength 3 and a -1 save modifier; if they move in their Movement phase they are unable to fire that turn.', page='117'))
TK.append(U(INF, 'Halberdiers (Chi Ji Shibing)', [M('Halberdier', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Halberd'], rules=['Combined Formation (Art of War)'], options=[('Light armour', 2)] + UP)],
    'Armed with spear tipped halberds. May have light armour (+2 pts). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.', page='117'))
TK.append(U(INF, 'Spearmen (Chi Mao Shibing)', [M('Spearman', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Shield'], rules=['Combined Formation (Art of War)'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1)] + UP)],
    'Armed with a hand weapon, thrusting spear and shield. May have light armour (+2 pts) and large shield (+1 pt). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.', page='117'))
TK.append(U(INF, 'Swordsmen (Chi Jian Zhe)', [M('Swordsman', '4 3 3 3 3 1 3 1 7', 6, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1)] + UP)],
    'Armed with a hand weapon and shield. May have light armour (+2 pts) and large shield (+1 pt). Light Infantry.', page='117'))
TK.append(U(INF, 'Archers (Gong Jian Shou)', [M('Archer', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Bow', 'Improvised Weapon'], rules=['Light Troops', 'Combined Formation (Art of War)'], options=[('Light armour', 2)] + UP)],
    'Armed with a bow and improvised weapon. May have light armour (+2 pts). Light Infantry. May also be in Combined Formation with Spearmen or Halberdiers.', page='117'))
TK.append(U(INF, 'Crossbow (Nu Shou)', [M('Crossbowman', '4 3 3 3 3 1 3 1 7', 9, mn=5, weapons=['Crossbow', 'Improvised Weapon'], rules=['Light Troops', 'Volley Firing (Art of War)', 'Combined Formation (Art of War)'], options=[('Light armour', 2)] + UP)],
    'Armed with a crossbow and improvised weapon. May have light armour (+2 pts). Light Infantry. Volley Firing. May also be in Combined Formation with Spearmen or Halberdiers.', page='117'))
TK.append(U(SPU, 'Nomad Cavalry (Xiongnu/Wuhuan) (Hu)', [M('Nomad Cavalryman', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Throwing spear', 1), ('Shield', 2)] + UP)],
    'Armed with a hand weapon and bow. May have throwing spear (+1 pt) and shield (+2 pts). Light Cavalry. Nomad Cavalry.', page='118'))
TK.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 4, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='118'))
TK.append(U(SPU, 'Elites (Jing Ying Shibing)', [M('Elite', '4 4 3 3 3 1 4 1 8', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Double-handed sword (instead of hand weapon and shield)', 0)] + UP)],
    'Armed with a hand weapon and shield. May have light armour (+2 pts) and upgrade to large shield (+1 pt). May have double-handed sword instead of hand weapon and shield for no extra cost. Light Infantry.', page='118'))
TK.append(U(SPU, 'Light Bolt Thrower (She Mao Jian Shou)', [M('Light Bolt Thrower', '- - - - 6 2 - - -', 50, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Two crew armed with a hand weapon. May have light armour (+2 pts). Bolt Thrower: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit.', page='118'))
TK.append(U(SPU, 'Stone Thrower (Reng Shi Shou)', [M('Stone Thrower', '- - - - 7 7 - - -', 75, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=5, mx=5, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'Five crew armed with a hand weapon. May have light armour (+2 pts). Stone Thrower: range 48", Strength 7, no save, D3 wounds per hit.', page='118'))
TKV = variants('TK', 'Three Kingdoms', {'Three Kingdoms': (L(Characters=25, Cavalry=33, Infantry=(33, 0), Special_Units=25),
 'THREE KINGDOMS ARMY. Characters up to 25% (0-1 Warlord, Yang or Yin). Cavalry up to 33%. Infantry at least 33%. Special Units up to 25% (only one selected option per 1,000 points). Army variants (allies are documented only): the Army of Wei may take Wuhuan (Eastern Steppe Nomads) and Yellow Scarves; the Army of Shu-Han may take Xi Yi (Early Eastern Tribes); the Army of Wu may take Man Yi (Early Eastern Tribes).')})
TK_NOTES = ('THREE KINGDOMS (The Art of War, pp.116-119). Special rules: Heroic Combat (see the Heroic Combat section), Military Strategist (a single Ruse per 1,000 points, 50 pts each, paid from the Special Units allowance and not counted in victory points unless used; not built), Army Musician (units within 18" may re-roll rally attempts, Flee dice and Panic tests; used once), Sworn Brotherhood, the Brotherhood of the Peach Garden. Steadfast (Liu Bei): may re-roll one Leadership test during a game; never subject to a further re-roll. Guile, Courage, Master Strategist and Impetuous as given on the characters. ' + PMAX)
LISTS.append(('TK', 'Han Dynasty: Three Kingdoms (Art of War)', 'Han_Three_Kingdoms_Art_of_War.cat', TK, TKV, TK_NOTES))
OPTRULE += [('TK', 'General (Jiang Jun)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['TK'] = (['Yang Warlord', 'Yin Warlord', 'Liu Bei', 'Cao Cao', 'Zhuge Liang'], [('General (Jiang Jun)', 'Army General (+25 pts; if no other Army General)')])
PAIRS.append(('TK', ['Yang Warlord', 'Yin Warlord', 'Liu Bei', 'Cao Cao', 'Zhuge Liang'], 'tk-gen'))

# ====================================================================== HAN DYNASTY (book pp.106-108)
CC = 'Chariotry & Cavalry'
WHI, WHE, WHW, EH = 'Western Han - Army of Internal Suppression', 'Western Han - Expeditionary or Route Army', 'Western Han - Army of the Western District (Xi Yu)', 'Eastern Han - Army of Internal Suppression'
HN = []
HN.append(char('Yang General (Jiang Jun)', '4 6 6 4 4 3 6 3 8', 140, ['Hand Weapon'], ['Army General'], [('Spear tipped halberd', 2), ('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a spear tipped halberd (+2 pts), shield (+2), light armour (+2), lamellar armour (+4), horse (free, M8). May ride in a four-horse heavy chariot (not enforced). Army General. 0-1 General (Yang or Yin): the heroic upfront school of generalship.', mx=1, page='107'))
HN.append(char('Yin General (Jiang Jun)', '4 5 5 3 3 2 6 1 9', 140, ['Hand Weapon'], ['Army General', 'Military Strategist (Art of War)'], [('Shield', 2), ('Light armour', 2), HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free, M8). May ride in a four-horse heavy chariot (not enforced). Army General. Military Strategist. 0-1 General (Yang or Yin): leads by superior strategy.', mx=1, page='107'))
HN.append(char('Major (Xiao Wei)', '4 5 3 3 3 2 5 2 8', 75, ['Hand Weapon'], [], [('Shield', 2), ('Light armour', 2), HORSE, ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free, M8). May ride in a four-horse heavy chariot (not enforced). If no other Army General is taken, the Major may be made Army General for +25 pts.', page='107'))
HN.append(char('Army Standard Bearer (Jun Dui Zhang Qi Shou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), lamellar armour (+4) and horse (free, M8). May ride in a four-horse heavy chariot (not enforced). Army Standard Bearer. 0-1.', mx=1, page='107'))
HN.append(char('Army Musician (Jun Dui Yue Shi)', '0 3 3 3 3 1 4 1 8', 20, ['Hand Weapon'], ['Army Musician (Art of War)'], [('Light armour', 2)],
    'Armed with a hand weapon and very big drum or gong! May have light armour (+2 pts). Army Musician. 0-1.', mx=1, page='107'))
HN.append(char('Military Strategist (Jun Shi Jia)', '4 2 2 3 3 1 3 1 7', 25, ['Hand Weapon'], ['Military Strategist (Art of War)'], [],
    'Armed with a hand weapon. Military Strategist. 0-1.', mx=1, page='107'))
HN.append(U(CC, 'Heavy Chariots (Shuang Lun Zhan Che)', [M('Heavy Chariot', '6 4 4 3 4 2 4 4 8', 66, weapons=['Hand Weapon', 'Halberd', 'Crossbow'], rules=['Chariots'], options=[('Crew light armour (+2 pts each)', 4), ('Crew heavy armour (+4 pts each)', 8)])],
    'Two crewmen with hand weapons - one armed with a spear tipped halberd and one armed with a crossbow, riding in a four-horse heavy chariot with driver. Crew may have light armour (+2 pts each) or heavy armour (+4 pts each). Chariots. Not available in the Eastern Han (Army of Internal Suppression) or the Army of the Western District.', page='107'))
HN.append(U(CC, 'Light Cavalry Lancers (Chi Mao Zhuang Jia Shibing)', [M('Light Cavalry Lancer', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Halberd'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with hand weapons and spear tipped halberds. May have light armour (+2 pts). Light Cavalry.', page='107'))
HN.append(U(CC, 'Light Cavalry Archers (Gong Jian Zhuang Jia Shibing)', [M('Light Cavalry Archer', '8 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Bow', 'Improvised Weapon'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with bows and improvised weapons. May have light armour (+2 pts). Light Cavalry.', page='107'))
HN.append(U(CC, 'Light Cavalry Crossbow (Shi Gong Zhuang Jia Shibing)', [M('Light Cavalry Crossbowman', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Improvised Weapon', 'Light Crossbow'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with horse crossbows and improvised weapons. May have light armour (+2 pts). Light Cavalry. The horse crossbow has a range of 24", Strength 3 and a -1 save modifier; if they move in their Movement phase they are unable to fire that turn.', page='108'))
for nm, st, pts, tx, rl, opts, pg in (
    ('Halberdiers (Chi Ji Shibing)', '4 3 3 3 3 1 3 1 7', 7, 'Armed with spear tipped halberds. May have light armour (+2 pts). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.', ['Combined Formation (Art of War)'], [('Light armour', 2)], '108'),
    ('Spearmen (Chi Mao Shibing)', '4 3 3 3 3 1 3 1 7', 7, 'Armed with a hand weapon, thrusting spear and shield. May have light armour (+2 pts) and large shield (+1 pt). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.', ['Combined Formation (Art of War)'], [('Light armour', 2), ('Large shield (replaces shield)', 1)], '108'),
    ('Swordsmen (Chi Jian Zhe)', '4 3 3 3 3 1 3 1 7', 6, 'Armed with a hand weapon and shield. May have light armour (+2 pts) and large shield (+1 pt). Light Infantry.', ['Light Troops'], [('Light armour', 2), ('Large shield (replaces shield)', 1)], '108'),
    ('Archers (Gong Jian Shou)', '4 3 3 3 3 1 3 1 7', 7, 'Armed with an improvised weapon and a bow. May have light armour (+2 pts). Light Infantry. May also be in Combined Formation with Spearmen and Halberdiers.', ['Light Troops', 'Combined Formation (Art of War)'], [('Light armour', 2)], '108'),
    ('Crossbow (Nu Shou)', '4 3 3 3 3 1 3 1 7', 9, 'Armed with an improvised weapon and a crossbow. May have light armour (+2 pts). Light Infantry. Volley Firing. May also be in Combined Formation with Spearmen and Halberdiers.', ['Light Troops', 'Volley Firing (Art of War)', 'Combined Formation (Art of War)'], [('Light armour', 2)], '108')):
    w = {'Halberdiers (Chi Ji Shibing)': ['Halberd'], 'Spearmen (Chi Mao Shibing)': ['Hand Weapon', 'Thrusting Spear', 'Shield'], 'Swordsmen (Chi Jian Zhe)': ['Hand Weapon', 'Shield'],
         'Archers (Gong Jian Shou)': ['Improvised Weapon', 'Bow'], 'Crossbow (Nu Shou)': ['Improvised Weapon', 'Crossbow']}[nm]
    HN.append(U(INF, nm, [M(nm.split(' (')[0].rstrip('s') if nm != 'Crossbow (Nu Shou)' else 'Crossbowman', st, pts, mn=5, weapons=w, rules=rl, options=opts + UP)], tx, page=pg))
HN.append(U(SPU, 'Nomad Cavalry (Xiongnu) (Hu)', [M('Nomad Cavalryman', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Throwing spear', 1), ('Shield', 2)] + UP)],
    'Armed with a hand weapon and bow. May have throwing spear (+1 pt) and shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry.', page='108'))
HN.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='108'))
HN.append(U(SPU, 'Straw Dogs (Convicts) (Qiu Fan)', [M('Straw Dog', '4 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon'], rules=['Skirmishers (Art of War)', 'Straw Dogs (Art of War)'], options=[('Javelin and shield', 2)] + UP)],
    'Armed with a hand weapon. May have javelin and shield (+2 pts). Skirmishers. Straw Dogs: if the unit flees or is destroyed, it does not cause panic in any other unit. Amnestied convicts were used as conscripts for line forces.', page='108'))
HN.append(U(SPU, 'Elites (Jing Ying Shibing)', [M('Elite', '4 4 3 3 3 1 4 1 8', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Double-handed sword (instead of hand weapon and shield)', 0), ('Left Handed Fighting Style', 2)] + UP)],
    'Armed with a hand weapon and shield. May have light armour (+2 pts) and large shield (+1 pt). May have two handed sword instead of hand weapon and shield for no extra cost. May use Left Handed Fighting Style (+2 pts): reduces an opponent\'s Initiative and saving throw by 1. Light Infantry.', page='108'))
HN.append(U(SPU, 'Light Bolt Thrower (She Mao Jian Shou)', [M('Light Bolt Thrower', '- - - - 6 2 - - -', 50, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'The machine is equipped with two crew armed with a hand weapon. May have light armour (+2 pts). Bolt Thrower: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit.', page='108'))
HN.append(U(SPU, 'Stone Thrower (Reng Shi Shou)', [M('Stone Thrower', '- - - - 7 7 - - -', 75, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=5, mx=5, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'The machine is equipped with five crew armed with a hand weapon. May have light armour (+2 pts). Stone Thrower: range 48", Strength 7, no save, D3 wounds per hit.', page='108'))
HNV = variants('HN', 'Han Dynasty', {
 WHI: (L(Characters=25, Chariotry_and_Cavalry=25, Infantry=(33, 0), Special_Units=25), 'WESTERN HAN DYNASTY - ARMY OF INTERNAL SUPPRESSION. Characters up to 25%. Chariotry & Cavalry up to 25%. Infantry at least 33%. Special Units up to 25% (two selected options per 1,000 points).'),
 WHE: (L(Characters=25, Chariotry_and_Cavalry=(25, 0), Infantry=(25, 0), Special_Units=25), 'WESTERN HAN DYNASTY - EXPEDITIONARY OR ROUTE ARMY. Characters up to 25%. Chariotry & Cavalry at least 25%. Infantry at least 25%. Special Units up to 25% (one selected option per 1,000 points). Alternatively may take up to 25% of the points value with Eastern Steppe Nomads as allies (documented only).'),
 WHW: (L(Characters=25, Chariotry_and_Cavalry=(25, 0), Infantry=(25, 0), Special_Units=25), 'WESTERN HAN DYNASTY - ARMY OF THE WESTERN DISTRICT (XI YU). Characters up to 25%. Chariotry & Cavalry at least 25% (no units of Chariots). Infantry at least 25%. Special Units up to 25% (one selected option per 1,000 points). Alternatively may take up to 25% of the points value with Eastern Steppe Nomads as allies (documented only).'),
 EH: (L(Characters=25, Chariotry_and_Cavalry=25, Infantry=(33, 0), Special_Units=25), 'EASTERN HAN DYNASTY - ARMY OF INTERNAL SUPPRESSION. Characters up to 25%. Chariotry & Cavalry up to 25% (no units of Chariots). Infantry at least 33%. Special Units up to 25% (one selected option per 1,000 points). Alternatively may take up to 25% of the points value with Eastern Steppe Nomads as allies (documented only).')})
HN_NOTES = ('HAN DYNASTY (The Art of War, pp.106-108). Special rule: Left Handed Fighting Style (nominated Elite units reduce an opponent\'s Initiative and saving throw by 1). Military Strategist and Ruses: see Three Kingdoms notes (not built). ' + PMAX)
LISTS.append(('HN', 'Han Dynasty (Art of War)', 'Han_Dynasty_Art_of_War.cat', HN, HNV, HN_NOTES))
UNAV += [('HN', 'Heavy Chariots (Shuang Lun Zhan Che)', [WHW, EH])]
OPTRULE += [('HN', 'Major (Xiao Wei)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['HN'] = (['Yang General (Jiang Jun)', 'Yin General (Jiang Jun)'], [('Major (Xiao Wei)', 'Army General (+25 pts; if no other Army General)')])
PAIRS.append(('HN', ['Yang General (Jiang Jun)', 'Yin General (Jiang Jun)'], 'hn-gen'))

# ====================================================================== RED EYEBROWS REBELS (book pp.109-111)
RE = []
RE.append(char('Rebel Leader (Fanpanzhe Lingxiu)', '4 6 6 4 4 3 6 3 7', 120, ['Hand Weapon'], ['Army General'], [('Spear tipped halberd', 2), ('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a spear tipped halberd (+2 pts), shield (+2), light armour (+2), lamellar armour (+4), horse (free, M8). Army General. 0-1.', mx=1, page='109'))
RE.append(char('Magistrates (Defangfa Gaun)', '4 4 3 3 3 2 5 2 5', 50, ['Hand Weapon'], [], [('Shield', 2), ('Light armour', 2), HORSE, ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free, M8). Army General - if no other Army General is taken, a Magistrate may be made Army General for +25 pts. Warband Rule 1 if accompanying Peasants or a Mob. The Red Eyebrows, being simple farming folk, did not know of any higher grade titles than those found at local government level.', page='109'))
RE.append(char('Chieftains (Shouling)', '4 5 3 3 3 2 5 2 8', 75, ['Hand Weapon'], [], [('Shield', 2), ('Light armour', 2), ('Compound bow', 2), HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), compound bow (+2), horse (free, M8).', page='109'))
RE.append(char('Army Standard Bearer (Jun Dui Zhang Qi Shou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Light armour', 2), LAM, HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), lamellar armour (+4) and horse (free, M8). Army Standard Bearer. 0-1. A unit subject to No Flags, No Trumpets may not take banners or musicians.', mx=1, page='110'))
RE.append(char('Maverick Heroes (Wuxia)', '4 5 5 4 4 1 5 2 8', 55, ['Hand Weapon'], ['Warrior of Legend', 'Independent Character (Art of War)'], [('Exotic weapons (count as additional hand weapons)', 2), ('Spear tipped halberd', 2), HORSE,
    ('Strongman (Strength 5, Wounds 2)', 15), ('Swift as the Wind (Movement 6)', 5), ('Skilled Archer (compound bow instead of exotic weapons or halberd)', 2)],
    'Armed with a hand weapon. May have exotic weapons (+2 pts, count as additional hand weapons) or spear tipped halberd (+2). May have horse (free, M8). One speciality: Strongman (S5, W2; +15), Swift as the Wind (M6; +5) or Skilled Archer (compound bow; +2). Warrior of Legend. Independent Character. Dodge Save: disdaining armour they receive a 5+ special dodge save not modified by Strength. 0-3.', mx=3, page='110'))
RE.append(U(INF, 'Deserters (Daobing)', [M('Deserter', '4 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Halberd'], rules=['No Flags, No Trumpets (Art of War)', 'Looting (Art of War)'], options=[('Swords and shields (replaces halberds)', 0), ('Light armour', 2), ('Improvised weapon and bow (replaces halberds or swords and shields)', 1), ('Improvised weapon and crossbow (replaces halberds or swords and shields)', 2)])],
    'Armed with spear tipped halberds or swords and shields. May have light armour (+2 pts). May exchange spear tipped halberds or swords and shields for improvised weapon and either bow (+1 pt) or crossbow (+2 pts). No Flags No Trumpets. Looting.', page='110'))
RE.append(U(INF, 'Peasants (Nong Fu)', [M('Peasant', '4 2 2 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Warband Psychology (rule 1)', 'Light Troops', 'Simple Minded (Art of War)', 'No Flags, No Trumpets (Art of War)', 'Looting (Art of War)'], options=[('Spear tipped halberds', 2)])],
    'Armed with farm implements and rocks (count as hand weapons/javelins with a 4" range). May have spear tipped halberds (+2 pts). Warband Rule 1. Light Infantry. Simple Minded. No Flags, No Trumpets. Looting.', page='110'))
RE.append(U(INF, 'Red Eyebrow Mobs (Baomin)', [M('Mob', '4 2 2 3 3 1 2 1 3', 3, mn=5, weapons=['Improvised Weapon'], rules=['Warband Psychology (rule 1)', 'No Flags, No Trumpets (Art of War)', 'Looting (Art of War)', 'Mobs (Art of War)'], options=[])],
    'Armed with improvised weapons. No Flags No Trumpets. Looting. Mobs and any Magistrates with their unit are subject to Warband Psychology Rule 1. Mobs cannot Fall Back in Good Order unless they outnumber by more than 3 to 1. They cannot benefit from the Leadership value of characters (other than Magistrates with the mob itself), nor use the re-roll benefit of the Army Standard. Mob Deployment: deployed last before characters, on the player\'s table edge or the furthest possible distance from the enemy. Rousing the Mob (0-3: Warband Psychology and moves forward at least 4"; 4-6: also hates the enemy, Hatred rules 2 and 3 only). The army must include at least one Mob per 1,000 points (not enforced).', page='110'))
RE.append(U(SPU, 'Light Cavalry Lancers (Chi Mao Zhuang Jia Shibing)', [M('Light Cavalry Lancer', '8 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Hand Weapon', 'Halberd'], rules=['Light Troops'], options=[('Light armour', 2)])],
    'Lancers are armed with hand weapons and spear tipped halberds. May have light armour (+2 pts). Light Cavalry. 0-1.', mx=1, page='111'))
RE.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)])],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='111'))
RE.append(U(SPU, 'Escaped Convicts (Qiu Fan)', [M('Straw Dog', '4 3 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon'], rules=['Skirmishers (Art of War)', 'Looting (Art of War)'], options=[('Javelin and shield', 2)])],
    'Armed with a hand weapon. May have javelin and shield (+2 pts). Skirmishers. Looting.', page='111'))
REV = variants('RE', 'Red Eyebrows Rebels', {'Red Eyebrows': (L(Characters=25, Infantry=(33, 0), Special_Units=25),
 'HAN DYNASTY REBEL ARMY - RED EYEBROWS (HONGSEDE MEIMAO). Characters up to 25%. Infantry at least 33% and must include at least one Mob per 1,000 points. Special Units up to 25% (one selected option per 1,000 points).')})
RE_NOTES = ('RED EYEBROWS REBELS (The Art of War, pp.109-111). Special rules: Looting (a unit with this ability can take the shields and weapons of a better equipped enemy if it catches and destroys them in a pursuit or close combat; lost if the unit flees), No Flags, No Trumpets (no banners or musicians, so no combat bonus modifications or Musician roll-off), Simple Minded (the unit must take a Leadership test whenever it wishes to charge; on a failure it stays where it is; subject to the rules for Stubborn if formed). Fear of horses: a Mob successfully charged by cavalry, chariots, elephants, camels, war wagons etc. must take a Fear test. ' + PMAX)
LISTS.append(('RE', 'Han Dynasty: Red Eyebrows Rebels (Art of War)', 'Han_Red_Eyebrows_Art_of_War.cat', RE, REV, RE_NOTES))
OPTRULE += [('RE', 'Magistrates (Defangfa Gaun)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['RE'] = (['Rebel Leader (Fanpanzhe Lingxiu)'], [('Magistrates (Defangfa Gaun)', 'Army General (+25 pts; if no other Army General)')])
OPTSTAT += [('RE', 'Maverick Heroes (Wuxia)', 'Strongman (Strength 5, Wounds 2)', 'S', 5), ('RE', 'Maverick Heroes (Wuxia)', 'Strongman (Strength 5, Wounds 2)', 'W', 2),
            ('RE', 'Maverick Heroes (Wuxia)', 'Swift as the Wind (Movement 6)', 'M', 6)]

# ====================================================================== ZHOU DYNASTY (book pp.28-31)
WZ, SA = 'Western Zhou period', 'Spring and Autumn period'
ZH = []
RC = ' Rightful Conduct (Spring and Autumn period only).'
ZH.append(char('Duke (Gong)', '4 6 6 4 4 3 6 3 9', 150, ['Hand Weapon'], ['Army General', 'Rightful Conduct (Art of War)'], [('Noble Sword', 2), ('Shield', 2), ('Light armour', 2), ('Heavy armour', 4)],
    'Armed with a hand weapon. May have a Noble Sword (+2 pts), shield (+2), light armour (+2), heavy armour (+4). May ride in a four-horse heavy chariot bought at an additional cost from the Chariotry list (not enforced). Army General.' + RC + ' 0-1 Army Commander.', mx=1, page='29'))
ZH.append(char('Marquis (Hao)', '4 5 5 3 3 2 6 2 9', 100, ['Hand Weapon'], ['Rightful Conduct (Art of War)'], [('Noble Sword', 2), ('Shield', 2), ('Light armour', 2), ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon. May have a Noble Sword (+2 pts), shield (+2), light armour (+2). May ride in a four-horse heavy chariot bought from the Chariotry list (not enforced). If no other Army General is taken, the Marquis may be made Army General for +25 pts.' + RC + ' 0-1. Designer\'s note: during the Zhou Dynasty armies would be led at the highest level by a duke representing the state; the King did not indulge in combat.', mx=1, page='29'))
ZH.append(char('Army Standard Bearer (Jun Dui Zhang Qi Shou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard', 'Rightful Conduct (Art of War)'], [('Shield', 2), ('Light armour', 2)],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2). May ride in a four-horse heavy chariot or two-horse light chariot bought from the Chariotry list (not enforced). Army Standard Bearer.' + RC + ' 0-1.', mx=1, page='29'))
ZH.append(char('Nobles (Guizu)', '4 5 5 4 4 1 5 2 8', 50, ['Hand Weapon'], ['Rightful Conduct (Art of War)'], [('Shield', 2), ('Axe', 2), ('Thrusting spear', 2), ('Light armour', 2)],
    'Armed with a hand weapon. May have a shield (+2 pts), axe (+2) or thrusting spear (+2) and light armour (+2). May ride in a four-horse heavy chariot or two-horse light chariot bought from the Chariotry list (not enforced).' + RC, page='29'))
ZH.append(char('Army Musician (Jun Dui Yue Shi)', '0 3 3 3 3 1 4 1 8', 20, ['Hand Weapon'], ['Army Musician (Art of War)'], [('Light armour', 2)],
    'Armed with a hand weapon and very big drum or gong! May have light armour (+2 pts). Army Musician. 0-1.', mx=1, page='29'))
ZH.append(char('Military Strategist (Jun Shi Jia)', '4 2 2 3 3 1 3 1 7', 25, ['Hand Weapon'], ['Military Strategist (Art of War)'], [],
    'Armed with a hand weapon. Military Strategist. 0-1.', mx=1, page='29'))
ZH.append(char('Duke of Song', '4 4 3 3 3 2 4 1 8', 156, ['Hand Weapon', 'Halberd', 'Light Armour', 'Bow'], ['Army General', 'Rightful Conduct (Art of War)', 'Meddlesome (Art of War)'], [],
    'Special Character (Spring and Autumn period only). Armed with a hand weapon, dagger axe and light armour, with a four-horse heavy chariot (S3 T4 W2 I4 A4, animal skin carapace which acts as a shield) with unarmed driver and archer with light armour. Army General. Rightful Conduct. Meddlesome: before any unit may charge it must test on the Duke of Song\'s Leadership; if failed, it may not charge. If the Duke is fleeing at any time or is slain he is not an influence and they may charge as normal. Cost includes the chariot (not modelled separately).', mx=1, page='31'))
ZH.append(U(CHT, 'Heavy Chariots (Shuang Lun Zhan Che)', [M('Heavy Chariot', '6 4 4 3 4 2 4 4 8', 66, weapons=['Hand Weapon', 'Halberd', 'Bow'], rules=['Chariots'], options=[('Crew light armour (+2 pts each)', 4)])],
    'Two crewmen with hand weapons - one armed with a dagger axe or thrusting spear and one armed with a bow riding in a four-horse heavy chariot with unarmed driver. The chariot is armoured with an animal skin carapace which acts as a shield. Crew may have light armour (+2 pts each). Chariots.', page='30'))
ZH.append(U(CHT, 'Light Chariots (Xiao Zhanche)', [M('Light Chariot', '8 4 4 3 4 1 4 2 8', 45, weapons=['Hand Weapon', 'Bow'], rules=['Light Chariots'], options=[('Crew light armour (+2 pts each)', 2)])],
    'One crewman armed with a hand weapon and bow riding in a two-horse light chariot with unarmed driver. Crew may have light armour (+2 pts each). Light Chariots.', page='30'))
ZH.append(U(CHT, 'Chariot Retinue', [M('Chariot Retinue', '5 4 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops', 'Chariot Runners (Art of War)'], options=[('Dagger axe (counts as halberd; replaces shield)', 0), ('Light armour', 2)] + UP)],
    'Armed with a hand weapon and shield or dagger axe. May have light armour (+2 pts). Light Infantry. Chariot Runners: up to one unit of 10 models per chariot fielded; initially deployed within 6" of the chariot model.', page='30'))
ZH.append(U(INF, 'Noble Guard (Lu)', [M('Guard', '4 4 3 3 3 1 4 1 8', 15, mn=5, weapons=['Hand Weapon', 'Shield', 'Thrusting Spear', 'Light Armour'], rules=['Drilled (Art of War)', 'Stubborn (Art of War)'], options=[('Dagger axe (instead of thrusting spear and shield)', 0)] + UP, key='guard')],
    'Armed with a hand weapon, shield, thrusting spear and light armour. May have dagger axe instead of thrusting spear and shield. May only be fielded if a Duke is the Army Commander. Drilled. Stubborn. Must be the smallest Infantry unit fielded (not enforced). 0-1. The Zhou had an elite group known as the Tiger Guards.', mx=1, page='30'))
for nm, mname, st, pts, w, rl, opts, tx in (
    ('Armoured Halberdiers (Kui Jia Chi Ji Shibing)', 'Halberdier', '4 3 3 3 3 1 3 1 7', 9, ['Halberd', 'Light Armour'], ['Long Handled Weapons (Art of War)', 'Combined Formation (Art of War)'], [('Long handled dagger axe', 2)],
     'Armed with dagger axe and light armour. May make dagger axe long handled (+2 pts). Long Handled Weapons. Combined Formation.'),
    ('Armoured Spearmen (Kui Jia Chi Map Shibing)', 'Spearman', '4 3 3 3 3 1 3 1 7', 9, ['Hand Weapon', 'Thrusting Spear', 'Shield', 'Light Armour'], ['Long Handled Weapons (Art of War)', 'Combined Formation (Art of War)'], [('Large shield (replaces shield)', 1), ('Long handled spear', 2)],
     'Armed with a hand weapon, thrusting spear, shield and light armour. May have large shield (+1 pt). May make spear long handled (+2 pts). Long Handled Weapons. Combined Formation.'),
    ('Halberdiers (Chi Ji Shibing)', 'Halberdier', '4 3 3 3 3 1 3 1 7', 7, ['Halberd'], ['Combined Formation (Art of War)'], [],
     'Armed with dagger axe. Combined Formation.'),
    ('Spearmen (Chi Mao Shibing)', 'Spearman', '4 3 3 3 3 1 3 1 7', 7, ['Hand Weapon', 'Thrusting Spear', 'Shield'], ['Combined Formation (Art of War)'], [('Large shield (replaces shield)', 1)],
     'Armed with a hand weapon, thrusting spear and shield. May have large shield (+1 pt). Combined Formation.'),
    ('Swordsmen (Chi Jian Zhe)', 'Swordsman', '4 3 3 3 3 1 3 1 7', 6, ['Hand Weapon', 'Shield'], ['Light Troops'], [('Light armour', 2)],
     'Armed with a hand weapon and shield. May have light armour (+2 pts). Light Infantry. 0-1.'),
    ('Archers (Gong Jian Shou)', 'Archer', '4 3 3 3 3 1 3 1 7', 7, ['Bow'], ['Combined Formation (Art of War)'], [],
     'Armed with a bow. Combined Formation. Archers must be added to groups of Spearmen or Halberdiers and cannot be fielded separately (not enforced).')):
    ZH.append(U(INF, nm, [M(mname, st, pts, mn=5, weapons=w, rules=rl, options=opts + UP)], tx, mx=(1 if nm.startswith('Swordsmen') else None), page='30'))
ZH.append(U(SPU, 'Nomad Cavalry (Quanrong) (Hu)', [M('Nomad', '8 3 3 3 3 1 3 1 5', 16, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[])],
    'Armed with a hand weapon and compound bow, rides a horse. Light Cavalry. Allies. 0-1.', mx=1, page='31'))
ZH.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)])],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers. Allies.', page='31'))
ZHV = variants('ZH', 'Zhou Dynasty', {
 WZ: (L(Characters=25, Chariotry=33, Infantry=(33, 0), Special_Units=25), 'ZHOU DYNASTY - WESTERN ZHOU PERIOD. Characters up to 25%. Chariotry up to 33%. Infantry at least 33%. Special Units up to 25% (one selected option per 1,000 points). Rightful Conduct and the Duke of Song apply to the Spring and Autumn period only (not enforced).'),
 SA: (L(Characters=25, Chariotry=25, Infantry=(25, 0), Special_Units=25), 'ZHOU DYNASTY - SPRING AND AUTUMN PERIOD. Characters up to 25%. Chariotry up to 25%. Infantry at least 25%. Special Units up to 25% (one selected option per 1,000 points). Rightful Conduct applies.')})
ZH_NOTES = ('ZHOU DYNASTY (The Art of War, pp.28-31). Special rules: Heroic Combat (Zhou nobles seek out a worthy opponent; stylised opening duels), Rightful Conduct (Spring and Autumn only: any character with it must accept any Challenge or Heroic Combat offered; must test Leadership to restrain from pursuing a fleeing enemy character or unit containing one; restraining adds bonus VPs, destroying loses them: 3 Wounds 150 VPs, 2 Wounds 100 VPs, 1 Wound 50 VPs). Archers must be added to Spearmen or Halberdiers. ' + PMAX)
LISTS.append(('ZH', 'Zhou Dynasty (Art of War)', 'Zhou_Dynasty_Art_of_War.cat', ZH, ZHV, ZH_NOTES))
UNAV += [('ZH', 'Duke of Song', [WZ]), ('ZH', 'Light Chariots (Xiao Zhanche)', [])]
UNAV = [u for u in UNAV if not (u[0] == 'ZH' and u[2] == [])]
OPTRULE += [('ZH', 'Marquis (Hao)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['ZH'] = (['Duke (Gong)', 'Duke of Song'], [('Marquis (Hao)', 'Army General (+25 pts; if no other Army General)')])
PAIRS.append(('ZH', ['Duke (Gong)', 'Duke of Song'], 'zh-gen'))

# ====================================================================== EARLY HORSE NOMADS (book p.32)
HM = []
HM.append(char('Warlord (Junfa)', '5 6 6 3 3 3 6 3 7', 140, ['Hand Weapon', 'Compound Bow', 'Horse'], ['Army General'], [('Shield', 2), ('Axe', 2), ('Dagger axe', 2), ('Light armour', 3)],
    'Armed with a hand weapon and compound bow. Rides a horse. May have a shield (+2 pts), axe (+2 pts) or dagger axe (+2 pts) and light armour (+3 pts). May ride a horse (free; Movement 8"). Army General. 0-1. The army should include at least one character to lead it.', mx=1, page='32'))
HM.append(char('Totem Bearer (Dudeng Xingxiang)', '5 4 4 3 3 2 4 2 5', 50, ['Hand Weapon', 'Compound Bow'], ['Army Standard'], [('Shield', 2), ('Axe', 2), ('Light armour', 3), HORSE],
    'Armed with a hand weapon and compound bow. May have a shield (+2 pts), axe (+2 pts) and light armour (+3 pts). May ride a horse (free; Movement 8"). Army Standard Bearer.', page='32'))
HM.append(char('Shaman (Wu)', '5 3 3 3 3 2 4 1 5', 60, ['Improvised Weapon'], ['Shaman (Art of War)', 'Causes Fear'], [HORSE],
    'Armed with an improvised weapon. May ride a horse (free; Movement 8"). Shaman. The Shaman causes fear in the enemy. 0-1.', mx=1, page='32'))
HM.append(char('Chieftains (Shouling)', '5 5 5 3 3 2 5 3 6', 60, ['Hand Weapon', 'Compound Bow'], [], [('Shield', 2), ('Axe', 2), ('Dagger axe', 2), ('Light armour', 3), HORSE],
    'Armed with a hand weapon and compound bow. May have a shield (+2 pts), axe (+2 pts) or dagger axe (+2 pts) and light armour (+3 pts). May ride a horse (free; Movement 8").', page='32'))
HM.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad', '8 3 3 3 3 1 3 1 5', 16, mn=5, weapons=['Hand Weapon', 'Compound Bow', 'Horse'], rules=['Skirmishers (Art of War)'], options=[('Shield', 2), ('Light armour', 3)] + UP)],
    'Armed with a hand weapon and compound bow. Rides a horse. May have a shield (+2 pts) and light armour (+3 pts each). Skirmishers.', page='32'))
HM.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 4, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Skirmishers (Art of War)'], options=[('Shield', 2), ('Buckler', 1), ('Compound bow (replaces javelins)', 2)] + UP)],
    'Armed with hand weapons and javelins. May have shields (+2 pts) or bucklers (+1 pt). May exchange javelins for compound bows (+2 pts). Skirmishers.', page='32'))
HM.append(U(INF, 'Tribespeople (Buluo Minzhong)', [M('Tribesperson', '4 1 2 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon', 'Rocks'], rules=[], options=UP)],
    'Armed with a hand weapon and rocks (range 4", Strength 3). In situations where they needed to defend their homes or flocks, the tribespeople would have been capable of defending themselves.', page='32'))
HMV = variants('HM', 'Early Horse Nomads', {'Early Horse Nomads': (L(Characters=33, Cavalry=(33, 0), Infantry=33),
 'EARLY HORSE NOMADS. Characters up to 33% (the army should include at least one character to lead it). Cavalry at least 33%. Infantry up to 33%.')})
LISTS.append(('HM', 'Early Horse Nomads (Art of War)', 'Early_Horse_Nomads_Art_of_War.cat', HM, HMV,
 'EARLY HORSE NOMADS (The Art of War, p.32): the mounted nomads (hu / Quanrong) who raided China from the 5th century BCE. ' + PMAX))

# ====================================================================== WARRING STATES (book pp.41-46)
WS = []
WS.append(char('Yang General (Jiang Jun)', '4 6 6 4 4 3 6 3 8', 140, ['Hand Weapon'], ['Army General'], [('Noble Sword', 2), ('Shield', 2), ('Light armour', 2), HORSE],
    'Armed with a hand weapon. May have a Noble Sword (+2 pts), shield (+2), light armour (+2), horse (free; Movement 8"). May ride in a four-horse heavy chariot bought from the Chariotry list (not enforced). Army General. 0-1 General (Yang or Yin): the heroic upfront school of generalship.', mx=1, page='42'))
WS.append(char('Yin General (Jiang Jun)', '4 5 5 3 3 2 6 1 9', 140, ['Hand Weapon'], ['Army General', 'Military Strategist (Art of War)'], [('Shield', 2), ('Light armour', 2), HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2), horse (free; Movement 8"). May ride in a four-horse heavy chariot bought from the Chariotry list (not enforced). Army General. Military Strategist. 0-1 General (Yang or Yin): leads by superior strategy; some generals went to the extreme of being unarmed and unarmoured.', mx=1, page='42'))
WS.append(char('Colonel (Si Ma)', '4 5 4 3 3 2 5 2 8', 75, ['Hand Weapon', 'Bow'], [], [('Shield', 2), ('Light armour', 2), HORSE, ('Army General (+25 pts; if no other Army General)', 25)],
    'Armed with a hand weapon and bow. May have a shield (+2 pts), light armour (+2), horse (free; Movement 8"). May ride in a four-horse heavy chariot bought from the Chariotry list (not enforced). If no other Army General is taken, the Colonel may be made Army General for +25 pts.', page='42'))
WS.append(char('Army Standard Bearer (Jun Dui Zhang Qi Shou)', '4 4 4 4 3 2 5 2 8', 75, ['Hand Weapon'], ['Army Standard'], [('Shield', 2), ('Light armour', 2), HORSE],
    'Armed with a hand weapon. May have a shield (+2 pts), light armour (+2) and horse (free; Movement 8"). May ride in a four-horse heavy chariot bought from the Chariotry list (not enforced). Army Standard Bearer. 0-1.', mx=1, page='42'))
WS.append(char('Army Musician (Jun Dui Yue Shi)', '0 3 3 3 3 1 4 1 8', 20, ['Hand Weapon'], ['Army Musician (Art of War)'], [('Light armour', 2)],
    'Armed with a hand weapon and very big drum or gong! May have light armour (+2 pts). Army Musician. 0-1.', mx=1, page='42'))
WS.append(char('Military Strategist (Jun Shi Jia)', '4 2 2 3 3 1 3 1 7', 25, ['Hand Weapon'], ['Military Strategist (Art of War)'], [],
    'Armed with a hand weapon. Military Strategist. 0-1.', mx=1, page='42'))
WS.append(U(CC, 'Chariots (Shuang Lun Zhan Che)', [M('Heavy Chariot', '6 4 4 3 4 2 4 4 8', 66, weapons=['Hand Weapon', 'Halberd', 'Crossbow'], rules=['Chariots', 'Long Handled Weapons (Art of War)'], options=[('Crew light armour (+2 pts each)', 4), ('Crew heavy armour (+4 pts each)', 8), ('Long handled halberd', 2)])],
    'Two crewmen with hand weapons - one armed with a spear tipped halberd and one armed with a crossbow riding in a four-horse heavy chariot with driver. Crew may have light armour (+2 pts each) or heavy armour (+4 pts each). May make spear tipped halberd long-handled (+2 pts). Chariots. Long Handled Weapons.', page='42'))
WS.append(U(CC, 'Chariot Retinue', [M('Chariot Retinue', '5 4 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops', 'Chariot Runners (Art of War)'], options=[('Dagger axe (counts as halberd; replaces shield)', 0), ('Light armour', 2)] + UP)],
    'Armed with a hand weapon and shield or dagger axe. May have light armour (+2 pts). Light Infantry. Chariot Runners: up to one unit of 10 models per chariot fielded; initially deployed within 6" of the chariot model.', page='42'))
WS.append(U(CC, 'Light Cavalry Lancers (Chi Mao Zhuang Jia Shibing)', [M('Lancer', '7 3 3 3 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Halberd'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with hand weapons and spear tipped halberds. May have light armour (+2 pts). Light Cavalry. 0-1.', mx=1, page='42'))
WS.append(U(CC, 'Light Cavalry Archers (Gong Jian Zhuang Jia Shibing)', [M('Archer', '7 3 3 3 3 1 3 1 7', 14, mn=5, weapons=['Bow', 'Improvised Weapon'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with bows. May have light armour (+2 pts). Light Cavalry. 0-1.', mx=1, page='43'))
WS.append(U(CC, 'Light Cavalry Crossbow (Shi Gong Zhuang Jia Shibing)', [M('Crossbow', '7 3 3 3 3 1 3 1 7', 16, mn=5, weapons=['Improvised Weapon', 'Light Crossbow'], rules=['Light Troops'], options=[('Light armour', 2)] + UP)],
    'Armed with horse crossbows and improvised weapons. May have light armour (+2 pts). Light Cavalry. The horse crossbow has a range of 24", Strength 3 and a -1 save modifier; if they move in their Movement phase they are unable to fire that turn. 0-1.', mx=1, page='43'))
WS.append(U(INF, 'Guards (Wei So)', [M('Guard', '4 4 4 3 3 1 4 1 8', 18, mn=5, weapons=['Hand Weapon', 'Shield', 'Light Armour'], rules=['Drilled (Art of War)', 'Stubborn (Art of War)'], options=[('Heavy armour', 1), ('Large shield (replaces shield)', 1), ('Double-handed sword (instead of hand weapon and shield)', 0), ('Thrusting spear', 1), ('Spear tipped halberd', 2)] + UP)],
    'Armed with a hand weapon, shield and light armour. May have heavy armour (+1 pt) and upgrade to large shield (+1 pt). May have double-handed sword instead of hand weapon and shield for no extra cost. May have thrusting spear (+1 pt) or spear tipped halberd (+2 pts). Drilled. Stubborn. 0-1.', mx=1, page='43'))
for nm, mname, st, pts, w, rl, opts, tx in (
    ('Halberdiers (Chi Ji Shibing)', 'Halberdier', '4 3 3 3 3 1 3 1 7', 7, ['Halberd'], ['Combined Formation (Art of War)'], [('Light armour', 2)],
     'Armed with spear tipped halberds. May have light armour (+2 pts). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.'),
    ('Spearmen (Chi Mao Shibing)', 'Spearman', '4 3 3 3 3 1 3 1 7', 7, ['Hand Weapon', 'Thrusting Spear', 'Shield'], ['Combined Formation (Art of War)'], [('Light armour', 2), ('Large shield (replaces shield)', 1)],
     'Armed with a hand weapon, thrusting spear and shield. May have light armour (+2 pts) and large shield (+1 pt). Combined Formation: may have up to 50% Archers or Crossbowmen in the unit.'),
    ('Swordsmen (Chi Jian Zhe)', 'Swordsman', '4 3 3 3 3 1 3 1 7', 6, ['Hand Weapon', 'Shield'], ['Light Troops'], [('Light armour', 2), ('Large shield (replaces shield)', 1)],
     'Armed with a hand weapon and shield. May have light armour (+2 pts) and upgrade to large shield (+1 pt). Light Infantry.'),
    ('Archers (Gong Jian Shou)', 'Archer', '4 3 3 3 3 1 3 1 7', 7, ['Bow', 'Improvised Weapon'], ['Light Troops', 'Combined Formation (Art of War)'], [('Light armour', 2)],
     'Armed with a bow and improvised weapon. May have light armour (+2 pts). Light Infantry. May also be in Combined Formation with Spearmen or Halberdiers.'),
    ('Crossbow (Nu Shou)', 'Crossbowman', '4 3 3 3 3 1 3 1 7', 9, ['Crossbow', 'Improvised Weapon'], ['Light Troops', 'Volley Firing (Art of War)', 'Combined Formation (Art of War)'], [('Light armour', 2)],
     'Armed with a crossbow and improvised weapon. May have light armour (+2 pts). Volley Firing. Light Infantry. May also be in Combined Formation with Spearmen or Halberdiers.'),
    ('Massed Levy (Zhengshou Qunzhong)', 'Levy', '4 2 2 3 3 1 2 1 5', 4, ['Halberd'], ['Levies (Art of War)'], [('Sword and shield (replaces dagger axe)', 0), ('Light armour', 2)],
     'Armed with a dagger axe. May have sword and shield instead of dagger axe. May have light armour (+2 pts). Levies. Warring States forces made use of massed levies to bulk up their armies; enemy prisoners of war and defectors were often incorporated into armies as wholesale units and are considered the same as Massed Levy.')):
    WS.append(U(INF, nm, [M(mname, st, pts, mn=5, weapons=w, rules=rl, options=opts + UP)], tx, page='43'))
WS.append(U(SPU, 'Elites (Jing Ying Shibing)', [M('Elite', '4 4 3 3 3 1 4 1 8', 8, mn=5, weapons=['Hand Weapon', 'Shield'], rules=['Light Troops'], options=[('Light armour', 2), ('Large shield (replaces shield)', 1), ('Double-handed sword (instead of hand weapon and shield)', 0)] + UP)],
    'Armed with a hand weapon and shield. May have light armour (+2 pts) and upgrade to large shield (+1 pt). May have double-handed sword instead of hand weapon and shield for no extra cost. Light Infantry.', page='44'))
WS.append(U(SPU, 'Straw Dogs (Convicts) (Qiu Fan)', [M('Straw Dog', '4 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon'], rules=['Skirmishers (Art of War)', 'Straw Dogs (Art of War)'], options=[('Javelin and buckler', 2)] + UP)],
    'Armed with a hand weapon. May have javelin and buckler (+2 pts). Skirmishers. Straw Dogs: if the unit flees or is destroyed, it does not cause panic to any other unit.', page='44'))
WS.append(U(SPU, 'Light Bolt Thrower (She Mao Jian Shou)', [M('Light Bolt Thrower', '- - - - 6 2 - - -', 50, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=2, mx=2, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'The machine is equipped with two crew armed with hand weapons. May have light armour (+2 pts). Bolt Thrower: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit.', page='44'))
WS.append(U(SPU, 'Stone Thrower (Reng Shi Shou)', [M('Stone Thrower', '- - - - 7 7 - - -', 75, key='machine'),
    M('Crew', '4 3 3 3 3 1 3 1 7', 0, mn=5, mx=5, key='crew', weapons=['Hand Weapon'], options=[('Light armour', 2)])],
    'The machine is equipped with five crew armed with hand weapons (crew cost is printed as "??" in the book; treated as 0). May have light armour (+2 pts). Stone Thrower: range 48", Strength 7, no save, D3 wounds per hit.', page='44'))
WS.append(U(SPU, 'Tortoise Wagon (Wugui Yunhuoche)', [M('Tortoise Wagon', '6 - - - 6 4 - - -', 50, key='wagon')],
    'An infantry unit can be supplied with a Tortoise Wagon, a form of travelling pavise allowing infantry units to cross the beaten zone of enemy crossbow fire. A Tortoise Wagon can provide an infantry unit of maximum six model frontage with hard cover, to the front of the unit only. A unit with a Tortoise Wagon may only move at a maximum of 6". (Not attached to a unit here; field one per supported infantry unit.)', page='44'))
WS.append(U(SPU, 'Repeat Firing Crossbow Chariots (Chongfu Fashe Shi Zi Gong)', [M('Repeat Firing Crossbow Chariot', '6 4 4 4 4 2 4 4 8', 120, weapons=['Hand Weapon', 'Repeat Crossbow'], rules=['Chariots'], options=[('Crew light armour (+2 pts each)', 4), ('Crew heavy armour (+4 pts each)', 8)])],
    'Two crewmen with hand weapons armed with a repeat firing crossbow riding in a four-horse heavy chariot with driver. Crew may have light armour (+2 pts each) or heavy armour (+4 pts each). Chariots. Each turn the chariot moves it may fire D6 crossbow bolts at Strength 4; on a 1 the device is jammed and may not fire that turn. 0-1.', mx=1, page='44'))
WS.append(char('Meng Tian', '4 6 5 3 3 3 6 3 10', 200, ['Noble Sword', 'Halberd', 'Light Armour', 'Horse'], ['Army General', 'Warrior of Legend', 'Military Strategist (Art of War)', 'Stubborn (Art of War)'], [],
    'Special Character. Armed with a Noble sword, spear tipped halberd, light armour and horse (free; Movement 8"). May have a four-horse heavy chariot bought from the main list (not enforced). Army General. Warrior of Legend. Military Strategist. Stubborn. Famous general of the Qin state who secured the Ordos Loop from nomadic horse raiders, leading to the Great Wall.', mx=1, page='45'))
WS.append(U(SPU, 'Eastern Shaman (Wu)', [M('Shaman', '5 3 3 3 3 2 4 1 5', 50, weapons=['Hand Weapon'], rules=['Eastern Shaman (Art of War)', 'Causes Fear'], options=[])],
    'Armed with a hand weapon. No options. Eastern Shaman - the Shaman causes fear. 0-1. Army of Chu (if a Military Strategist is not taken), Army of Qi and Army of Yan (may not take a Military Strategist) only.', mx=1, page='46'))
WS.append(U(SPU, 'Nomad Cavalry (Xiongnu) (Hu)', [M('Xiongnu', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Throwing spear', 1), ('Shield', 2)] + UP)],
    'Armed with a hand weapon and bow. May have throwing spear (+1 pt) and shield (+2 pts). Allies. Light Cavalry. Steppe Nomad Cavalry. 0-1. Armies of Zhao, Qin and Wei only.', mx=1, page='46'))
WS.append(U(SPU, 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [M('Foot Barbarian', '5 2 3 3 3 1 4 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Allies. Skirmishers. 0-1. Armies of Chu and Qi only.', mx=1, page='46'))
WS.append(U(SPU, 'Repeating Crossbow (Chongfu Fashe Shi Zi Gong)', [M('Repeating Crossbowman', '4 3 3 4 3 1 3 1 7', 15, mn=5, weapons=['Hand Weapon', 'Repeating Crossbow'], rules=['Light Troops', 'Repeating Crossbow (Art of War)'], options=[('Light armour', 2)] + UP)],
    'Armed with a hand weapon and repeating crossbow. May have light armour (+2 pts). Light Infantry. Repeating Crossbow. 0-1. Army of Hann only.', mx=1, page='46'))
CAPSTD = L(Characters=25, Chariotry_and_Cavalry=25, Infantry=(33, 0), Special_Units=25)
CAP33 = L(Characters=25, Chariotry_and_Cavalry=33, Infantry=(33, 0), Special_Units=25)
WSB = 'Characters up to 25%. Special Units up to 25% (two selected options per 1,000 points). Infantry at least 33%. '
WSV = variants('WS', 'Warring States', {
 'Generic state': (CAPSTD, 'WARRING STATES (no state variant). Characters up to 25%. Chariotry & Cavalry up to 25%. Infantry at least 33%. Special Units up to 25% (two selected options per 1,000 points).'),
 'Army of Zhao': (CAP33, 'ARMY OF ZHAO. ' + WSB + 'Chariotry & Cavalry up to 33%. May have 0-2 Light Cavalry Archers instead of 0-1. May take 0-1 Nomad Cavalry allies as a Special Unit.'),
 'Army of Qin': (CAPSTD, 'ARMY OF QIN. ' + WSB + 'Chariotry & Cavalry up to 25%. Swordsmen may become subject to Frenzy when charges are declared, losing any shields and light armour (not enforced). May have 0-2 Light Cavalry Lancers instead of 0-1. May take 0-1 Nomad Cavalry allies as a Special Unit.'),
 'Army of Yan': (CAPSTD, 'ARMY OF YAN. ' + WSB + 'Chariotry & Cavalry up to 25%. Infantry units may have additional drummers (+5 pts; the unit automatically wins a drawn combat by 1 point). May have an Eastern Shaman (Wu) but may not take a Military Strategist. Infantry units (other than Massed Levy) may be made Stubborn (+3 pts). Drummers and Stubborn are documented only.'),
 'Army of Chu': (CAPSTD, 'ARMY OF CHU. ' + WSB + 'Chariotry & Cavalry up to 25%. May make 0-1 unit of Crossbow into Guards, Drilled with heavy armour (+4 pts) (documented only). May take 0-1 Foot Barbarians allies as a Special Unit. May take an Eastern Shaman (Wu) if a Military Strategist is not taken.'),
 'Army of Qi': (CAPSTD, 'ARMY OF QI. ' + WSB + 'Chariotry & Cavalry up to 25%. May give 0-1 Elite units Noble Swords instead of swords (+1 pt); must be used in Skirmish formation (documented only). May take 0-1 Foot Barbarians allies as a Special Unit. May take 0-1 Eastern Shaman (Wu).'),
 'Army of Hann': (CAPSTD, 'ARMY OF HANN. ' + WSB + 'Chariotry & Cavalry up to 25%. May take 0-1 Repeating Crossbow unit as a Special Unit. May give units Inspiring Red Banners (+15 pts) (documented only). May give 0-1 Halberdier or Spear unit heavy armour (+3 pts) (documented only).'),
 'Army of Wei': (CAP33, 'ARMY OF WEI. ' + WSB + 'Chariotry & Cavalry up to 33%. May take 0-1 Nomad Cavalry allies as a Special Unit. May give infantry units (other than Massed Levy) heavy armour (+3 pts) (documented only).')})
WS_NOTES = ('WARRING STATES (The Art of War, pp.41-46). The generic list plus the Armies of Zhao, Qin, Yan, Chu, Qi, Hann and Wei (state variants on p.45). State variants that change the available special units or the Chariotry & Cavalry cap are enforced; frenzy, drummers, stubborn, heavy armour upgrades and Inspiring Red Banners (hongse de hengfu: before the battle roll a D3 per unit for +1 combat resolution bonuses, +15 pts) are documented only. Warring States generals may be Yang or Yin; Military Strategists may use Ruses (see Three Kingdoms notes; not built). The Battle of Chengpu scenario (p.33) is not built. ' + PMAX)
LISTS.append(('WS', 'Warring States (Art of War)', 'Warring_States_Art_of_War.cat', WS, WSV, WS_NOTES))
_ST = ['Generic state', 'Army of Zhao', 'Army of Qin', 'Army of Yan', 'Army of Chu', 'Army of Qi', 'Army of Hann', 'Army of Wei']
UNAV += [('WS', 'Eastern Shaman (Wu)', [c for c in _ST if c not in ('Army of Chu', 'Army of Qi', 'Army of Yan')]),
         ('WS', 'Nomad Cavalry (Xiongnu) (Hu)', [c for c in _ST if c not in ('Army of Zhao', 'Army of Qin', 'Army of Wei')]),
         ('WS', 'Foot Barbarians (Qiang/Yi/Yueh) (Hu)', [c for c in _ST if c not in ('Army of Chu', 'Army of Qi')]),
         ('WS', 'Repeating Crossbow (Chongfu Fashe Shi Zi Gong)', [c for c in _ST if c != 'Army of Hann'])]
OPTRULE += [('WS', 'Colonel (Si Ma)', 'Army General (+25 pts; if no other Army General)', 'Army General (Chariot Wars)')]
GEN['WS'] = (['Yang General (Jiang Jun)', 'Yin General (Jiang Jun)', 'Meng Tian'], [('Colonel (Si Ma)', 'Army General (+25 pts; if no other Army General)')])
PAIRS.append(('WS', ['Yang General (Jiang Jun)', 'Yin General (Jiang Jun)'], 'ws-gen'))

# ====================================================================== EASTERN STEPPE NOMADS (book pp.68-79)
SN = ' If mounted on a horse, counts as Steppe Nomad Cavalry.'
WU = []
WU.append(char('Army General (Kunmo)', '5 6 6 4 4 3 6 3 9', 185, ['Hand Weapon', 'Light Armour', 'Thrusting Spear', 'Bow'], ['Army General'], [('Throwing spear (replaces thrusting spear)', 0), ('Buckler', 1), HORSE],
    'Armed with a hand weapon, light armour, thrusting spear and bow. May have a throwing spear instead of thrusting spear, buckler (+1 pt), horse (free; Movement 8"). Army General.' + SN + ' 0-1.', mx=1, page='69'))
WU.append(char('Chieftain (Shouling)', '5 4 4 4 3 2 4 2 8', 55, ['Hand Weapon', 'Light Armour', 'Thrusting Spear', 'Bow'], [], [('Throwing spear (replaces thrusting spear)', 0), ('Buckler', 1), HORSE],
    'Armed with a hand weapon, light armour, thrusting spear and bow. May have a throwing spear instead of a thrusting spear, buckler (+1 pt), horse (free; Movement 8").' + SN, page='69'))
WU.append(char('War Banner Bearer (Zhanzheng Hengfu)', '5 4 4 4 3 2 4 2 8', 85, ['Hand Weapon', 'Light Armour'], ['Army Standard'], [('Buckler', 1), HORSE],
    'Hand weapon and light armour. May have a buckler (+1 pt) and horse (free; Movement 8"). Army Standard Bearer.' + SN + ' 0-1.', mx=1, page='69'))
WU.append(U(CAV, 'Nobles (Guizu)', [M('Noble', '8 4 4 3 3 1 4 1 8', 32, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Bow', 'Light Armour'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Throwing spear (replaces thrusting spear)', 0), ('Buckler', 1)] + UP)],
    'Armed with a hand weapon, thrusting spear, bow and light armour. May have throwing spear instead of thrusting spear, buckler (+1 pt). Light Cavalry. Steppe Nomad Cavalry. 0-2.', mx=2, page='69'))
WU.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad cavalry', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Javelin or throwing spear', 1), ('Buckler', 1), ('Shield (replaces buckler)', 2), ('Fast Pass', 0)] + UP)],
    'Armed with a hand weapon and bow. May have javelin or throwing spear (+1 pt), buckler (+1 pt) or shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. Horse Archers may have the Fast Pass ability (see the Art of War special rules). At least 2 units required (not enforced).', page='69'))
WU.append(U(INF, 'Tribal Warriors (Buluo Zhanshi)', [M('Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Javelin and buckler (replaces bow)', 0), ('Upgrade buckler to shield', 1), ('Throwing spears instead of javelins', 0)] + UP)],
    'Armed with a hand weapon and bow. May have javelin and buckler at no extra points. May upgrade buckler to shield (+1 pt). May have throwing spears instead of javelins at no extra points. Light Infantry. 0-1.', mx=1, page='69'))
WU.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='69'))
WU.append(U(SPU, 'Tribal Auxiliaries (Tochari)', [M('Tochari', '5 2 3 3 3 1 4 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='69'))
WUV = variants('WU', 'Wusun', {'Wusun': (L(Characters=25, Cavalry=(50, 0), Infantry=25, Special_Units=25),
 'WUSUN. Characters up to 25%. Cavalry at least 50%. Infantry up to 25%. Special Units up to 25% (one selected option per 1,000 points). May have up to 25% Allies (Eastern Han from the Han Chinese list) instead of selected options (documented only). Horse Archers may have the Fast Pass ability.')})
LISTS.append(('WU', 'Eastern Steppe Nomads: Wusun (Art of War)', 'Steppe_Wusun_Art_of_War.cat', WU, WUV,
 'WUSUN (The Art of War, p.69): Ili basin nomads allied to the Han from 110 BCE. Allies (up to 25% instead of selected options): Eastern Han from the Han Chinese list (documented only). Caravans and Yurts (common Special Units section at the end of the Eastern Steppe Nomads chapter) are covered in the Xiongnu catalogue notes. ' + PMAX))
GEN['WU'] = (['Army General (Kunmo)'], [])

# ---------------------------------------------------------------------- XIONGNU (pp.70-71)
XN = []
BARD = ('Barding', 4)
XN.append(char('Army General (Shanyu)', '5 6 6 4 4 3 6 3 9', 190, ['Hand Weapon', 'Light Armour', 'Thrusting Spear', 'Bow'], ['Army General', 'Fearsome (Art of War)'], [('Throwing spear (replaces thrusting spear)', 0), ('Noble Sword', 2), ('Shield', 2), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon, light armour, thrusting spear and bow. May have a throwing spear instead of a thrusting spear, Noble Sword (+2 pts), shield (+2 pts), lamellar armour instead of light armour (+2 pts), horse (free; Movement 8"). The horse may have barding (+4 pts). Army General. Fearsome.' + SN + ' 0-1.', mx=1, page='70'))
XN.append(char('Chieftain (Shouling)', '5 4 4 4 3 2 4 2 8', 55, ['Hand Weapon', 'Light Armour', 'Thrusting Spear', 'Bow'], ['Fearsome (Art of War)'], [('Shield', 2), ('Throwing spear (replaces thrusting spear)', 0), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon, light armour, thrusting spear and bow. May have a shield (+2 pts), throwing spear instead of a thrusting spear, lamellar armour (+2 pts, replaces light armour), horse (free; Movement 8"). The horse may have barding (+4 pts). Fearsome.' + SN, page='70'))
XN.append(char('War Banner Bearer (Zhanzheng Hengfu)', '5 4 4 4 3 2 4 2 8', 85, ['Hand Weapon', 'Light Armour'], ['Army Standard', 'Fearsome (Art of War)'], [('Shield', 2), ('Noble Sword', 2), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon and light armour. May have a shield (+2 pts), Noble Sword (+2 pts), lamellar armour (+2 pts, replaces light armour) and horse (free; Movement 8"). Horse may have barding (+4 pts). Army Standard Bearer. Fearsome.' + SN + ' 0-1.', mx=1, page='71'))
XN.append(char('Modun', '4 6 6 4 4 3 6 2 10', 200, ['Hand Weapon', 'Bow', 'Thrusting Spear', 'Lamellar Armour'], ['Army General', 'Warrior of Legend', 'Fearsome (Art of War)', 'Nomad Cavalry'], [HORSE],
    'Special Character. Armed with a hand weapon, bow, thrusting spear and lamellar armour. May ride a horse (free; Movement 8"). Army General. Warrior of Legend. Fearsome. Steppe Nomad Cavalry. Founder of the Xiongnu empire.', mx=1, page='71'))
XN.append(U(CAV, 'Nobles (Guizu)', [M('Noble', '8 4 4 3 3 1 4 1 8', 35, mn=5, weapons=['Hand Weapon', 'Light Armour', 'Thrusting Spear', 'Bow'], rules=['Light Troops', 'Nomad Cavalry', 'Fearsome (Art of War)'], options=[('Throwing spear (replaces thrusting spear)', 0), ('Lamellar armour (replaces light armour)', 2), ('Shield', 2)] + UP)],
    'Armed with a hand weapon, light armour, thrusting spear and bow. May have throwing spear instead of thrusting spear, lamellar armour (+2 pts, replaces light armour) and shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. Fearsome. 0-2.', mx=2, page='71'))
XN.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad cavalry', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Javelin or throwing spear', 1), ('Buckler', 1), ('Shield (replaces buckler)', 2)] + UP)],
    'Armed with a hand weapon and bow. May have javelin or throwing spear (+1 pt), buckler (+1 pt) or shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. At least 2 units required (not enforced).', page='71'))
XN.append(U(INF, 'Tribal Warriors (Buluo Zhanshi)', [M('Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Javelin and buckler (replaces bow)', 0), ('Upgrade buckler to shield', 1), ('Throwing spears instead of javelins', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. May upgrade buckler to shield (+1 pt). May have throwing spears instead of javelins at no extra points. Light Infantry. 0-1.', mx=1, page='71'))
XN.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='71'))
XN.append(U(SPU, 'Eagleshooter Cavalry (She Diao Zhe)', [M('Eagleshooter', '8 3 4 3 3 1 4 1 7', 26, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry', 'Fearsome (Art of War)', 'Eagleshooters (Art of War)'], options=[('Throwing spear', 2), ('Shield', 2)] + UP)],
    'Armed with a hand weapon and bow. May have throwing spear (+2 pts) and shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. Fearsome. Must be the smallest unit of cavalry in the army (not enforced). Eagleshooters: sharpshooters who ignore the -1 modifier for shooting at long range. 0-1.', mx=1, page='71'))
XN.append(U(SPU, 'Tribal Auxiliaries (Qiang)', [M('Qiang', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='71'))
XNV = variants('XN', 'Xiongnu', {'Xiongnu': (L(Characters=25, Cavalry=100, Infantry=25, Special_Units=25),
 'XIONGNU. Characters up to 25%. Cavalry: any amount. Infantry up to 25%. Special Units up to 25% (one selected option per 1,000 points). May have up to 25% Allies instead of selected options: Qiang Allies from the Early Chinese Tribes list, Wuhuan Allies from the Eastern Steppe Nomads list (documented only).')})
LISTS.append(('XN', 'Eastern Steppe Nomads: Xiongnu (Art of War)', 'Steppe_Xiongnu_Art_of_War.cat', XN, XNV,
 'XIONGNU (The Art of War, pp.70-71). Special rule: Fearsome (see the Art of War rules). Allies documented only: Qiang (Early Chinese Tribes list) and Wuhuan (Eastern Steppe Nomads list). The Shanyu\'s light armour option is printed as "light armour (+2 pts)" in addition to "lamellar armour instead of light armour (+2 pts)"; read as the lamellar upgrade only. ' + PMAX))
GEN['XN'] = (['Army General (Shanyu)', 'Modun'], [])
PAIRS.append(('XN', ['Army General (Shanyu)', 'Modun'], 'xn-gen'))

# ---------------------------------------------------------------------- YUEZHI (pp.72-73)
YZ = []
KON = ('Kontos instead of throwing spear (if mounted)', 0)
YZ.append(char('Army General (Yabgu)', '5 6 6 4 4 3 6 3 9', 185, ['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Bow'], ['Army General', 'Massed Cavalry (Art of War)'], [KON, ('Buckler', 1), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon, throwing spear, light armour and bow. May have a kontos instead of a throwing spear if mounted, buckler (+1 pt), lamellar armour (+2 pts, replaces light armour), horse (free; Movement 8"). The horse may have barding (+4 pts). Army General.' + SN + ' Massed Cavalry. 0-1.', mx=1, page='73'))
YZ.append(char('Chieftain (Shouling)', '5 4 4 4 3 2 4 2 8', 55, ['Hand Weapon', 'Throwing Spear', 'Light Armour', 'Bow'], ['Massed Cavalry (Art of War)'], [KON, ('Buckler', 1), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon, throwing spear, light armour and bow. May have a kontos instead of a throwing spear if mounted, buckler (+1 pt), lamellar armour (+2 pts, replaces light armour), horse (free; Movement 8"). The horse may have barding (+4 pts).' + SN + ' Massed Cavalry.', page='73'))
YZ.append(char('War Banner Bearer (Zhanzheng Hengfu)', '5 4 4 4 3 2 4 2 8', 85, ['Hand Weapon', 'Light Armour'], ['Army Standard', 'Massed Cavalry (Art of War)'], [('Shield', 2), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon and light armour. May have a shield (+2 pts), lamellar armour (+2 pts, replaces light armour) and horse (free; Movement 8"). Horse may have barding (+4 pts). Army Standard Bearer.' + SN + ' Massed Cavalry. 0-1.', mx=1, page='73'))
YZ.append(U(CAV, 'Nobles (Guizu)', [M('Noble', '8 4 4 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Kontos', 'Bow', 'Light Armour'], rules=['Light Troops', 'Nomad Cavalry', 'Massed Cavalry (Art of War)'], options=[('Throwing spear instead of kontos', 0), ('Buckler', 1), ('Lamellar armour (replaces light armour)', 2), BARD] + UP)],
    'Armed with a sword, kontos, bow and light armour. May have a throwing spear instead of kontos, buckler (+1 pt), lamellar armour (+2 pts, replaces light armour), barding for horse (+4 pts). Light Cavalry. Steppe Nomad Cavalry. Massed Cavalry. 0-2.', mx=2, page='73'))
YZ.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad cavalry', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Javelin or throwing spear', 1), ('Buckler', 1), ('Shield (replaces buckler)', 2)] + UP)],
    'Armed with a hand weapon and bow. May have javelin or throwing spear (+1 pt), buckler (+1 pt) or shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. At least 2 units required (not enforced).', page='73'))
YZ.append(U(INF, 'Tribal Warriors (Buluo Zhanshi)', [M('Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Javelin and buckler (replaces bow)', 0), ('Upgrade buckler to shield', 1), ('Throwing spears instead of javelins', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. May upgrade buckler to shield (+1 pt). May have throwing spears instead of javelins at no extra points. Light Infantry. 0-1.', mx=1, page='73'))
YZ.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='73'))
YZ.append(U(SPU, 'Tribal Auxiliaries (Tokari)', [M('Tokari', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='73'))
YZV = variants('YZ', 'Yuezhi', {'Yuezhi': (L(Characters=25, Cavalry=100, Infantry=25, Special_Units=25),
 'YUEZHI. Characters up to 25%. Cavalry: any amount. Infantry up to 25%. Special Units up to 25% (one selected option per 1,000 points). May have up to 25% Allies instead of selected options: Han Chinese from the Han Chinese list (documented only).')})
LISTS.append(('YZ', 'Eastern Steppe Nomads: Yuezhi (Art of War)', 'Steppe_Yuezhi_Art_of_War.cat', YZ, YZV,
 'YUEZHI (The Art of War, pp.72-73). Special rule: Massed Cavalry (see the Art of War rules). Allies documented only: Han Chinese from the Han Chinese list. ' + PMAX))
GEN['YZ'] = (['Army General (Yabgu)'], [])

# ---------------------------------------------------------------------- XIANBEI (pp.74-75)
XB = []
ESC = 'Eastern Shock Cavalry (Art of War)'
KON2 = ('Kontos (if mounted)', 2)
XB.append(char('Army General (Khan)', '5 6 6 4 4 3 6 3 9', 185, ['Hand Weapon', 'Throwing Spear', 'Lamellar Armour', 'Buckler', 'Bow'], ['Army General', ESC], [KON2, ('Shield (replaces buckler)', 1), HORSE, BARD],
    'Armed with a hand weapon, throwing spear, lamellar armour, buckler and bow. May have a kontos (+2 pts) if mounted, shield instead of buckler (+1 pt), horse (free; Movement 8"). The horse may have barding (+4 pts). Army General. Eastern Shock Cavalry. 0-1.', mx=1, page='74'))
XB.append(char('Chieftain (Shouling)', '5 4 4 4 3 2 4 2 8', 60, ['Hand Weapon', 'Throwing Spear', 'Lamellar Armour', 'Bow'], [ESC], [KON2, ('Buckler', 1), HORSE, BARD],
    'Armed with a hand weapon, throwing spear, lamellar armour and bow. May have a kontos (+2 pts) if mounted, buckler (+1 pt), horse (free; Movement 8"). The horse may have barding (+4 pts). Eastern Shock Cavalry.', page='74'))
XB.append(char('War Banner Bearer (Zhanzheng Hengfu)', '5 4 4 4 3 2 4 2 8', 85, ['Hand Weapon', 'Light Armour'], ['Army Standard', ESC], [('Shield', 2), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon and light armour. May have a shield (+2 pts), lamellar armour (+2 pts, replaces light armour) and horse (free; Movement 8"). Horse may have barding (+4 pts). Army Standard Bearer. Eastern Shock Cavalry. 0-1.', mx=1, page='75'))
XB.append(U(CAV, 'Nobles (Guizu)', [M('Noble', '8 4 4 3 3 1 4 1 8', 34, mn=5, weapons=['Hand Weapon', 'Kontos', 'Lamellar Armour', 'Bow'], rules=['Light Troops', 'Nomad Cavalry', ESC], options=[('Throwing spear instead of kontos', 0), ('Buckler', 1), BARD] + UP)],
    'Armed with a hand weapon, kontos, lamellar armour and bow. May have throwing spear instead of kontos, buckler (+1 pt), barding for the horse (+4 pts). Eastern Shock Cavalry. 0-2.', mx=2, page='75'))
XB.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad cavalry', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Javelin or throwing spear', 1), ('Buckler', 1), ('Shield (replaces buckler)', 2)] + UP)],
    'Armed with a hand weapon and bow. May have javelin or throwing spear (+1 pt), buckler (+1 pt) or shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. At least 2 units required (not enforced).', page='75'))
XB.append(U(INF, 'Tribal Warriors (Buluo Zhanshi)', [M('Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Javelin and buckler (replaces bow)', 0), ('Upgrade buckler to shield', 1), ('Throwing spears instead of javelins', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. May upgrade buckler to shield (+1 pt). May have throwing spears instead of javelins at no extra point. Light Infantry. 0-1.', mx=1, page='75'))
XB.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='75'))
XB.append(U(SPU, 'Heavy Cavalry (Daliang Qibing)', [M('Heavy Cavalry', '8 4 4 3 3 1 4 1 8', 30, mn=5, weapons=['Hand Weapon', 'Thrusting Spear', 'Lamellar Armour', 'Barding'], rules=['Rank Bonus Cavalry (Art of War)'], options=[('Bow', 3)] + UP)],
    'Armed with a hand weapon, thrusting spear, lamellar armour and barding. May have bow (+3 pts). May count rank bonus of up to +1 even though cavalry.', page='75'))
XBV = variants('XB', 'Xianbei', {'Xianbei': (L(Characters=25, Cavalry=100, Infantry=25, Special_Units=25),
 'XIANBEI. Characters up to 25%. Cavalry: any amount. Infantry up to 25%. Special Units up to 25% (one selected option per 1,000 points). May have up to 25% Allies instead of selected options: Wuhuan Allies from the Eastern Steppe Nomads list (documented only).')})
LISTS.append(('XB', 'Eastern Steppe Nomads: Xianbei (Art of War)', 'Steppe_Xianbei_Art_of_War.cat', XB, XBV,
 'XIANBEI (The Art of War, pp.74-75). Special rule: Eastern Shock Cavalry (see the Art of War rules). Allies documented only: Wuhuan from the Eastern Steppe Nomads list. ' + PMAX))
GEN['XB'] = (['Army General (Khan)'], [])

# ---------------------------------------------------------------------- WUHUAN (pp.76-77)
WH = []
WH.append(char('Army General (Khan)', '5 6 6 4 4 3 6 3 9', 185, ['Hand Weapon', 'Halberd', 'Lamellar Armour', 'Buckler', 'Bow'], ['Army General', ESC], [('Throwing spear', 2), ('Shield', 2), ('Kontos instead of dagger axe (if mounted)', 0), ('Noble Sword', 2), HORSE, BARD],
    'Armed with a hand weapon, dagger axe, lamellar armour, buckler and bow. May have a throwing spear (+2 pts), shield (+2 pts), kontos instead of dagger axe if mounted, Noble Sword (+2 pts), horse (free; Movement 8"). The horse may have barding (+4 pts). Army General. Eastern Shock Cavalry. 0-1.', mx=1, page='77'))
WH.append(char('Chieftain (Shouling)', '5 4 4 4 3 2 4 2 8', 60, ['Hand Weapon', 'Halberd', 'Lamellar Armour', 'Buckler', 'Bow'], [ESC], [('Throwing spear', 2), ('Shield', 2), ('Kontos instead of dagger axe (if mounted)', 0), HORSE, BARD],
    'Armed with a hand weapon, dagger axe, lamellar armour, buckler and bow. May have a throwing spear (+2 pts), shield (+2 pts), kontos instead of dagger axe if mounted, horse (free; Movement 8"). The horse may have barding (+4 pts). Eastern Shock Cavalry.', page='77'))
WH.append(char('War Banner Bearer (Zhanzheng Hengfu)', '5 4 4 4 3 2 4 2 8', 85, ['Hand Weapon', 'Light Armour'], ['Army Standard', ESC], [('Shield', 2), ('Lamellar armour (replaces light armour)', 2), HORSE, BARD],
    'Armed with a hand weapon and light armour. May have a shield (+2 pts), lamellar armour (+2 pts, replaces light armour) and horse (free; Movement 8"). Horse may have barding (+4 pts). Army Standard Bearer. Eastern Shock Cavalry. 0-1.', mx=1, page='77'))
WH.append(U(CAV, 'Nobles (Guizu)', [M('Noble', '8 4 4 3 3 1 4 1 8', 29, mn=5, weapons=['Hand Weapon', 'Bow', 'Light Armour'], rules=['Light Troops', 'Nomad Cavalry', ESC], options=[('Lamellar armour (replaces light armour)', 2), ('Dagger axe or kontos', 2), ('Shield', 2)] + UP)],
    'Armed with a sword, bow and light armour. May have lamellar armour (+2 pts, replaces light armour), dagger axe or kontos (+2 pts) and shield (+2 pts). Eastern Shock Cavalry. 0-2.', mx=2, page='77'))
WH.append(U(CAV, 'Horse Archers (Ma Gongjian Shu)', [M('Nomad cavalry', '8 3 4 3 3 1 4 1 7', 24, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops', 'Nomad Cavalry'], options=[('Javelin or throwing spear', 1), ('Buckler', 1), ('Shield (replaces buckler)', 2)] + UP)],
    'Armed with a hand weapon and bow. May have javelin or throwing spear (+1 pt), buckler (+1 pt) or shield (+2 pts). Light Cavalry. Steppe Nomad Cavalry. At least 2 units required (not enforced).', page='77'))
WH.append(U(INF, 'Tribal Warriors (Buluo Zhanshi)', [M('Warrior', '5 3 3 3 3 1 3 1 7', 7, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Light Troops'], options=[('Javelin and buckler (replaces bow)', 0), ('Upgrade buckler to shield', 1), ('Throwing spears instead of javelins', 0)] + UP)],
    'Armed with a hand weapon and bow. May have javelin and buckler at no extra points. May upgrade buckler to shield (+1 pt). May have throwing spears instead of javelins at no extra points. Light Infantry. 0-1.', mx=1, page='77'))
WH.append(U(INF, 'Tribal Skirmishers (Buluo Chongdu)', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Bow'], rules=['Skirmishers (Art of War)'], options=[('Javelin and buckler (replaces bow)', 0)] + UP)],
    'Armed with a hand weapon and bow. May exchange bow for javelin and buckler at no extra points. Skirmishers.', page='77'))
WH.append(U(SPU, 'Han Chinese Auxiliaries (Fuzhude)', [M('Auxiliary', '5 3 3 3 3 1 4 1 5', 6, mn=5, weapons=['Improvised Weapon', 'Halberd'], rules=['Light Troops'], options=[('Sword and shield (replaces spear-tipped halberd)', 0)] + UP)],
    'Armed with an improvised weapon and spear-tipped halberd. May have sword and shield instead of spear-tipped halberd. Light Infantry.', page='77'))
WHV = variants('WH', 'Wuhuan', {'Wuhuan': (L(Characters=25, Cavalry=(50, 0), Infantry=25, Special_Units=25),
 'WUHUAN. Characters up to 25%. Cavalry at least 50%. Infantry up to 25%. Special Units up to 25% (one selected option per 1,000 points). May have up to 25% Allies instead of selected options: Han Chinese from the Han Chinese list (documented only).')})
LISTS.append(('WH', 'Eastern Steppe Nomads: Wuhuan (Art of War)', 'Steppe_Wuhuan_Art_of_War.cat', WH, WHV,
 'WUHUAN (The Art of War, pp.76-77). Special rule: Eastern Shock Cavalry. Allies documented only: Han Chinese from the Han Chinese list. ' + PMAX))
GEN['WH'] = (['Army General (Khan)'], [])

# ---------------------------------------------------------------------- ALL TRIBES - Caravan and Yurt Camp (p.78): added to each steppe list
CARAVAN = lambda: U(SPU, 'Caravan', [M('Caravan', '- - - - 5 2 - - -', 50, key='machine'), M('Defender', '4 3 3 3 3 1 3 1 7', 0, mn=3, mx=3, key='crew', weapons=['Hand Weapon', 'Bow'])],
    'Each Caravan has a crew of three Defenders armed with hand weapons and bows. Mounted on a 4.7" (120mm) round base with pack animals and Defenders; carrying important trade goods out of all proportion to its size. Where table quarters normally count as Victory Points, they are not counted if a Caravan is used and the Caravan is worth 200 Victory Points; the opposing player can claim them with a unit in contact with the Caravan at the end of the game. The owner either gives it to the opposing player to defend as an objective in their deployment area (Raid) or deploys it in their own area as an objective (Aid). All the Defenders form a single unit that must remain with the wagons unless they break or flee, in which case they auto-break and are removed from play. 0-1.', mx=1, page='78')
YURTCAMP = lambda: U(SPU, 'Yurt Camp (Ger)', [M('Yurt', '- - - - 5 2 - - -', 5, mn=3, mx=5, key='yurt'), M('Defender', '4 2 3 3 3 1 2 1 7', 4, mn=0, mx=20, key='defender', weapons=['Hand Weapon', 'Bow'], options=[('Javelins instead of bow', 0)])],
    'Yurt camp consisting of 3-5 Yurts. Each Yurt may have up to four Defenders armed with hand weapons and bows (may exchange bow for javelins). Yurt Deployment: the whole camp is deployed as one unit and must be placed on the table as the first unit; Yurts are deployed 3" apart in a circle or semi-circle with at least one Yurt touching the Nomad player\'s table edge. Yurts do not block line of sight. Defender Deployment: all Defenders are Skirmishers, count as one unit and may not take a Standard or a Musician; they are placed behind the Yurts and may not leave voluntarily; while inside they count as being behind soft cover. Victory Points: each undefended Yurt at the end of the game gives the opponent +5 Victory points. 0-1.', mx=1, page='78')
for _l in LISTS:
    if _l[0] in ('WU', 'XN', 'YZ', 'XB', 'WH'):
        _l[3].append(CARAVAN()); _l[3].append(YURTCAMP())
