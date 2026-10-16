# Rulebook (WAB 2nd Ed.) Roman and Barbarian army lists, transcribed from book pp.172-189.
# Model stats order: M WS BS S T W I A Ld
def M(name, stats, pts, mn=1, mx=None, weapons=(), rules=(), options=(), key=None):
    return dict(name=name, stats=stats.split(), pts=pts, mn=mn, mx=mx,
                weapons=list(weapons), rules=list(rules), options=list(options), key=key or name)
def U(cat, name, models, notes, mx=None, page=None):
    return dict(cat=cat, name=name, models=models, notes=notes, mx=mx, page=page)

WARHORSE = 'Warhorse profile: M8 WS3 BS0 S3 T- W- I3 A1 Ld-.'
RIDE = 'May ride a horse at no cost, or a Warhorse (+8 pts). Light armour +2, shield +2 or large shield +3 (on foot only).'
CHOPT = [('Light armour', 2), ('Shield', 2), ('Large shield (on foot)', 3), ('Warhorse', 8)]
OFFOPT = CHOPT[:3] + [('Throwing spear (if mounted)', 2), ('Warhorse', 8)]

ROMAN = []
R = ROMAN
R.append(U('Characters', 'Army General', [M('Army General', '4 5 5 3 3 3 6 2 9', 135, weapons=['Hand Weapon'],
    rules=['Drilled', 'Stubborn', 'Army General (Roman list)'], options=CHOPT)],
    'Sword. ' + RIDE + ' Friendly units within 12" may use his Leadership. ' + WARHORSE, mx=1, page='174'))
R.append(U('Characters', 'Army Standard Bearer', [M('Army Standard Bearer', '4 4 4 4 3 2 4 2 8', 65, weapons=['Hand Weapon'],
    rules=['Drilled', 'Stubborn', 'Army Standard'], options=CHOPT)],
    'Sword. ' + RIDE + ' Friendly units within 12" may re-roll failed Break tests. ' + WARHORSE, mx=1, page='174'))
R.append(U('Characters', 'Senior Officer (Legate)', [M('Senior Officer (Legate)', '4 5 5 3 3 3 6 2 9', 110, weapons=['Hand Weapon'],
    rules=['Drilled', 'Stubborn'], options=OFFOPT)],
    'Sword. Horse at no cost or Warhorse +8 pts. ' + WARHORSE, page='175'))
R.append(U('Characters', 'Junior Officer (Tribune)', [M('Junior Officer (Tribune)', '4 4 4 3 3 2 5 2 8', 55, weapons=['Hand Weapon'],
    rules=['Drilled', 'Stubborn'], options=OFFOPT)],
    'Sword. Horse at no cost or Warhorse +8 pts. ' + WARHORSE, page='175'))
LEG_UP = [('Standard bearer', 5), ('Musician', 5), ('Centurion (leader; unit +1 Ld)', 10)]
R.append(U('Legionaries', 'Veteran Legionaries', [M('Veteran Legionary', '4 4 4 3 3 1 4 1 8', 20, mn=5,
    weapons=['Hand Weapon', 'Heavy Throwing Spear', 'Large Shield', 'Light Armour'],
    rules=['Drilled', 'Stubborn', 'Veteran', 'Testudo', 'Centurions'],
    options=[('Javelins', 2), ('Heavy armour (replaces light)', 2)] + LEG_UP)],
    'Sword, pilum (heavy throwing spear), large shield, light armour. Veteran special rule included in cost.', page='176'))
R.append(U('Legionaries', 'Regular Legionaries', [M('Regular Legionary', '4 3 3 3 3 1 3 1 7', 16, mn=5,
    weapons=['Hand Weapon', 'Heavy Throwing Spear', 'Large Shield', 'Light Armour'],
    rules=['Drilled', 'Stubborn', 'Testudo', 'Centurions'],
    options=[('Javelins', 1), ('Heavy armour (replaces light)', 2)] + LEG_UP)],
    'Sword, pilum, large shield, light armour.', page='177'))
R.append(U('Legionaries', 'Raw Recruits', [M('Raw Recruit', '4 3 3 3 3 1 3 1 7', 11, mn=5,
    weapons=['Hand Weapon', 'Heavy Throwing Spear', 'Large Shield', 'Light Armour'],
    rules=['Testudo', 'Centurions'], options=[('Javelins', 1)] + LEG_UP)],
    'Sword, pilum, large shield, light armour. Not Drilled or Stubborn.', page='177'))
AUX_UP = [('Standard bearer', 5), ('Musician', 5), ('Leader', 5)]
R.append(U('Auxiliaries', 'Auxiliary Cavalry (Equites Alares)', [M('Auxiliary Cavalryman', '8 3 3 3 3 1 3 1 7', 20, mn=5,
    weapons=['Hand Weapon', 'Throwing Spear', 'Javelin', 'Light Armour', 'Shield'], options=[('Drilled', 2)] + AUX_UP)],
    'Sword, throwing spear, javelins, light armour and shield. Drilled +2 pts per model.', page='178'))
R.append(U('Auxiliaries', 'Auxiliary Infantry (Cohortes Pedites)', [M('Auxiliary Infantryman', '4 3 3 3 3 1 3 1 7', 8, mn=5,
    weapons=['Hand Weapon', 'Throwing Spear', 'Shield'],
    options=[('Javelins', 1), ('Light armour', 2), ('Thrusting spear (replaces throwing spear)', 0), ('Drilled', 1)] + AUX_UP)],
    'Sword, throwing spear, shield. Light Infantry. Drilled +1 pt per model.', page='178'))
R.append(U('Auxiliaries', 'Auxiliary Archers', [M('Auxiliary Archer', '4 2 3 3 3 1 3 1 7', 8, mn=5,
    weapons=['Hand Weapon', 'Bow'], options=[('Light armour', 2), ('Buckler', 1)] + AUX_UP)],
    'Sword, composite bow (Bow). Light Infantry.', page='178'))
CREW = '4 3 3 3 3 1 3 1 7'
def crew(n, extra_max, armour=True):
    o = [('Light armour', 2)] if armour else []
    return [M('Crew', CREW, 0, mn=n, mx=n, key='crew', weapons=['Hand Weapon'], rules=['Stubborn'], options=o),
            M('Additional Crew', CREW, 8, mn=0, mx=extra_max, key='xcrew', weapons=['Hand Weapon'], rules=['Stubborn'], options=o)]
R.append(U('Special Units', 'Light Bolt Thrower (Scorpio)',
    [M('Scorpio', '- - - - 6 2 - - -', 20, mx=1, key='machine', options=[('Mounted in cart (Carroballista, M8)', 10)])] + crew(2, 2),
    'Bolt Thrower: range 36", Strength 4 (-1 per rank), no save, D3 wounds per hit. Two-man crew, swords, stubborn. Carroballista (+10): moves 8", cannot fire on the turn it moves, cannot march or charge.', page='179'))
R.append(U('Special Units', 'Bolt Thrower (Ballista)',
    [M('Ballista', '- - - - 6 2 - - -', 30, mx=1, key='machine')] + crew(3, 2),
    'Bolt Thrower: range 48", Strength 5 (-1 per rank), no save, D4 wounds per hit. Three-man crew, swords, stubborn.', page='179'))
R.append(U('Special Units', 'Small Stone Thrower (Tormenta)',
    [M('Small Stone Thrower', '- - - - 7 3 - - -', 40, mx=1, key='machine')] + crew(3, 1, armour=False),
    'Stone Thrower: range 48", Strength 6, no save, D3 wounds per hit. Three-to-four man Auxiliary Infantry crew, stubborn. One stone thrower allowed per two bolt shooters.', page='180'))
R.append(U('Special Units', 'Marines', [M('Marine', '4 3 3 3 3 1 3 1 7', 8, mn=5,
    weapons=['Hand Weapon', 'Javelin', 'Shield'],
    options=[('Light armour', 3), ('Throwing spear', 1), ('Sling', 1), ('Drilled and Stubborn', 5)] + AUX_UP)],
    'Sword, javelins, shield. Light Infantry.', page='180'))
R.append(U('Special Units', 'Camelry (Dromedarii)', [M('Camelman', '6 3 3 3 3 1 3 1 7', 11, mn=5,
    weapons=['Hand Weapon', 'Buckler'],
    options=[('Thrusting spear', 2), ('Kontos', 4), ('Javelins', 2), ('Composite bow', 4), ('Light armour', 4), ('Barding', 8), ('Shield (replaces buckler)', 2)] + AUX_UP)],
    'Sword, buckler. Cause fear in horsed cavalry and chariots. Maximum one camel unit.', mx=1, page='181'))

BARB = []
B = BARB
WL = [('Thrusting spear', 2), ('Throwing spear', 2), ('Javelins', 2), ('Light armour', 3), ('Shield', 2), ('Horse (M8, free)', 0), ('Light chariot', 0)]
B.append(U('Characters', 'Warlord', [M('Warlord', '5 6 6 4 4 3 6 3 7', 140, weapons=['Hand Weapon'], rules=['Warband', 'Army General (Barbarian list)'], options=WL)],
    'Sword. Army General: units within 12" may use his Leadership. Horse free (M8) or light chariot at additional cost.', mx=1, page='183'))
B.append(U('Characters', 'Battle Standard', [M('Battle Standard Bearer', '5 4 4 4 3 1 4 2 5', 50, weapons=['Hand Weapon'], rules=['Warband', 'Army Standard (Barbarian list)'], options=WL)],
    'Sword. Units within 12" may re-roll failed Break tests.', mx=1, page='183'))
B.append(U('Characters', 'Shaman', [M('Shaman', '5 4 4 4 3 2 4 2 5', 75, weapons=['Dagger'], rules=['Warband', 'Fear', 'Hatred'])],
    'Large sharp knife or sickle; no options. Causes fear. The Shaman and any warband he joins are subject to hatred of the enemy.', mx=1, page='183'))
B.append(U('Characters', 'Chieftain', [M('Chieftain', '5 5 5 4 4 2 5 3 6', 70, weapons=['Hand Weapon'], rules=['Warband'], options=WL)],
    'Sword. Horse free (M8) or light chariot at additional cost.', page='184'))
WB_UP = [('Standard bearer', 5), ('Musician', 5), ('Leader', 5)]
B.append(U('Warriors', 'Warriors', [M('Warrior', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Mixed Weapons'], options=WB_UP)],
    'Shields and a mixture of weapons (Mixed Weapons rule). At least one third of the army points must be Warriors.', page='185'))
B.append(U('Warriors', 'Fanatic Warriors', [M('Fanatic Warrior', '5 3 3 3 3 1 3 1 5', 9, mn=5, weapons=['Hand Weapon', 'Javelin', 'Shield'], rules=['Warband', 'Frenzy', 'Mixed Weapons'], options=WB_UP)],
    'Shields and a mixture of weapons. Frenzy.', mx=1, page='185'))
B.append(U('Cavalry and Chariots', 'Chariots', [M('Chariot', '8 4 4 3 4 1 4 2 6', 36, mn=3, weapons=['Hand Weapon', 'Javelin', 'Light Armour'], rules=['Chariots'],
    options=[('Shield', 4), ('Thrusting spear', 4), ('Throwing spear', 4)] + WB_UP)],
    'Light chariot pulled by two horses, with a driver and a noble warrior (swords; the warrior has light armour and javelins). Not subject to Warband rules. Warband minimum 3 chariots.', page='186'))
B.append(U('Cavalry and Chariots', 'Barbarian Noble Cavalry', [M('Noble Cavalryman', '8 4 4 3 3 1 4 1 7', 25, mn=5, weapons=['Hand Weapon', 'Javelin', 'Light Armour', 'Shield'], rules=['Warband', 'Mixed Weapons'],
    options=[('Throwing spear', 4), ('Thrusting spear', 4)] + WB_UP)],
    'Light armour, shields, mixed weapons. Affected by the Warband rules.', page='186'))
B.append(U('Cavalry and Chariots', 'Light Cavalry', [M('Light Cavalryman', '8 3 3 3 3 1 3 1 6', 12, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Mixed Weapons'],
    options=[('Shield (replaces buckler)', 1)] + WB_UP)],
    'Buckler, mixed weapons. Not affected by the Warband rules.', page='187'))
B.append(U('Supporting Infantry', 'Skirmishers', [M('Skirmisher', '5 2 3 3 3 1 3 1 5', 3, mn=5, weapons=['Hand Weapon', 'Javelin'], rules=['Mixed Weapons'],
    options=[('Sling (replaces mixed weapons)', 1), ('Bow (replaces mixed weapons)', 2), ('Buckler', 1)] + WB_UP)],
    'Daggers, clubs, javelins and slings (Mixed Weapons rule). Must deploy and remain in skirmish formation.', page='188'))
B.append(U('Supporting Infantry', 'Mountain Tribesmen', [M('Mountain Tribesman', '5 3 3 3 3 1 3 1 5', 5, mn=5, weapons=['Hand Weapon', 'Javelin', 'Buckler'], rules=['Mixed Weapons'],
    options=[('Shield (replaces buckler)', 1)] + WB_UP)],
    'Buckler; mixture of swords, javelins and axes. Fight in open order.', page='188'))
B.append(U('Supporting Infantry', 'Warhounds', [
    M('Packmaster', '5 4 4 3 3 1 4 1 6', 8, mn=1, mx=1, key='pm', weapons=['Hand Weapon'], rules=['Warband'], options=[('Javelins', 1), ('Light armour', 2)]),
    M('Warhound', '6 4 0 3 3 1 3 1 3', 5, mn=1, mx=6, key='hound', rules=['Warband'])],
    'Packmaster has a sword; warhounds rely on their teeth. Packmasters and warhounds are skirmishers. Missile hits are randomly divided between packmaster and hounds. One packmaster and up to six warhounds.', mx=1, page='188'))

# Army selection (percent of roster points)
ROMAN_LIMITS = {'Characters': ('max', 25), 'Legionaries': ('min', 25), 'Auxiliaries': ('max', 75), 'Special Units': ('max', 25)}
BARB_LIMITS = {'Characters': ('max', 33), 'Warriors': ('min', 33), 'Cavalry and Chariots': ('max', 33), 'Supporting Infantry': ('max', 33)}

RULES = {
 'Testudo': ('Roman rulebook list', 'A unit at least 2 ranks deep and 4 models wide may form testudo. Declare at the start of the turn. The unit may not charge or march. While in testudo it has a 2+ armour save against missile attacks.'),
 'Centurions': ('Roman rulebook list', 'One model per Legionary unit may be upgraded to a Centurion (leader) for +10 pts instead of +5. A Centurion adds +1 Leadership to the unit. Auxiliary leaders do not give this bonus.'),
 'Army Standard': ('Roman rulebook list', 'Units within 12" may re-roll failed Break tests. If the Army Standard is captured the enemy scores 400 victory points instead of 200. Roman units hate the unit that captures it until it is recaptured.'),
 'Army General (Roman list)': ('Roman rulebook list', 'Units within 12" of the General may use his Leadership.'),
 'Army General (Barbarian list)': ('Barbarian rulebook list', 'Units within 12" of the Warlord may use his Leadership.'),
 'Army Standard (Barbarian list)': ('Barbarian rulebook list', 'Units within 12" of the Battle Standard may re-roll failed Break tests.'),
 'Mixed Weapons': ('Barbarian rulebook list', 'Barbarians with mixed weapons count as armed with javelins and hand weapons.'),
}
ROMAN_NOTES = ('ROMAN ARMY LIST (WAB 2nd Edition, pp.172-181)\n'
  'Characters up to 1/4 of points; Legionaries at least 1/4; Auxiliaries up to 3/4; Special Units up to 1/4.\n'
  'Units must have at least 5 models; no maximum. One model per unit may be a standard bearer (+5), musician (+5) or leader (+5; Legionary Centurion +10).\n'
  'No more special units than legionary and auxiliary units combined.\n'
  'Roman characters may lead allied Barbarian units (not vice versa). Allies come from the Barbarian list (not enforced here).')
BARB_NOTES = ('BARBARIAN ARMY LIST (WAB 2nd Edition, pp.182-189)\n'
  'Covers Gallic, British and Germanic armies c.500 BC-500 AD. Characters up to 1/3 of points; Warriors at least 1/3; Cavalry and Chariots up to 1/3; Supporting Infantry up to 1/3.\n'
  'Warbands of at least 5 models (chariots 3). Standard bearer, musician, leader +5 each. Supporting Infantry: no maximum size.\n'
  'ADAPTING THE LIST (p.189; not enforced):\n'
  'Gauls: may field warriors in open order.\n'
  'Germans: no chariots or mountain tribesmen; noble cavalry may not take light armour but are Fearsome; noble cavalry and warriors may be stubborn +2/model; warriors may take thrusting spears +1 (such troops must be upgraded to stubborn); non-fanatic warriors may take throwing spears +2.\n'
  'Dacians: no chariots; any warriors may be replaced by Mountain Tribesmen; warriors and mountain tribesmen may take halberds +2 per model; mountain tribesmen may have a bow +2 if no falx.\n'
  'Ancient Britons: no noble cavalry or bows; chariots come from the warrior points allowance, one per eight infantry warriors; chariots within 6" of friendly light cavalry cannot be targeted by enemy missile fire.')
