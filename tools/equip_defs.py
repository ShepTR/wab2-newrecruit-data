#!/usr/bin/env python3
"""Equipment definitions from the WAB2 rulebook (Weapons and Armour, pp.91-98) and a definition link on every equipment option.
1. Rewrites the shared hand-to-hand weapon, armour, shield and barding profiles with the rulebook wording.
2. Adds Horse / Warhorse rules and an 'Encumbrance' rule.
3. Links each equipment option to its profile/rule; options with no shared definition get a local rule built from the army-list text.
Usage: python3 equip_defs.py <outdir>   (idempotent)"""
import sys, os, re, glob, hashlib, html
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
g = open(GST, encoding='utf8').read()

MAXN = ('Saves never improve beyond 3+ for infantry and for cavalry without barded mounts, or 2+ for cavalry riding barded mounts, '
        'whatever the modifiers (rulebook p.96). Encumbrance: infantry with a save of 4+ or better -1" movement; cavalry with a save of 3+ '
        '(ignoring barding) -1"; cavalry with metal barding another -1" (p.96).')
STAR = ' * Either with or without shield: a shield adds no bonus (p.97).'
HW = {  # name -> new Effects text
 'Hand Weapon': 'Swords, axes, clubs, hammers and all similar weapons wielded in one hand are comparable in effect: a hand weapon is the basic weapon and no special rules apply. '
                'Troops with a weapon in each hand (two swords, or a sword and long dagger) have +1 extra attack in hand-to-hand combat, whatever their Attacks value (p.91). No warrior may ever have a Strength above 5 (p.91).',
 'Dagger': 'All troops carry daggers or knives as a last resort. Enemy wounded by daggers receive a +1 armour save modifier (one pip better); if they otherwise have no save they save on a 6. '
           'E.g. a 5 or 6 save becomes 4, 5 or 6 (p.91). Troops so armed are at a disadvantage compared to those properly prepared for combat.',
 'Improvised Weapon': 'Bow staves, crossbow butts, javelins, weapons wrested from the enemy, or rocks and rough clubs. Enemy wounded by improvised weapons receive a +1 armour save modifier; '
                      'if they otherwise have no save they save on a 6 (p.91). Troops so armed are at a disadvantage compared to those properly prepared for combat.',
 'Double-handed Weapon': 'Large axes, swords, hammers and clubs needing two hands. Troops that carry shields cannot use them in hand-to-hand combat (shields are assumed slung or abandoned). '
                         'Always strike last in hand-to-hand combat regardless of Initiative or charging; if both sides have double-handed weapons normal priorities apply (charger first, otherwise higher Initiative). '
                         '+2 Strength on all hits (maximum Strength 5); the enemy armour save is reduced by the higher Strength as normal (p.92).',
 'Halberd': 'A heavy-bladed weapon on a sturdy shaft. Two hands are needed: troops that carry shields cannot use them in hand-to-hand combat. +1 Strength on all hits (maximum Strength 5); the enemy armour save is reduced by the higher Strength as normal (p.92).',
 'Throwing Spear': 'Hand-to-hand weapon, thrown just before combat and used again as a hand weapon. Infantry fight in two ranks in the first round of each combat engagement, both when they charge and when charged; a second-rank model may fight only if the model in front is fighting to its front. '
                   'Cavalry may re-roll misses in the first round of each combat unless they charged or countercharged through or into difficult terrain. Skirmishing infantry may re-roll misses in the first round (p.92).',
 'Heavy Throwing Spear': 'A heavier throwing spear (e.g. pilum, saunion, angon, throwing axe) that penetrates shields and armour. Infantry fight in two ranks in the first round of each combat engagement (as throwing spears) and add +1 Strength in the first round. '
                         'Skirmishing infantry may re-roll misses in the first round (p.93).',
 'Thrusting Spear': 'A spear about ten feet long retained and thrust. Infantry fight in two ranks to their front if the unit did not move and the second-rank model\'s front-rank comrade is fighting exclusively to the front; a unit that charges cannot fight in two ranks. '
                    'Cavalry add +1 Strength when they charge or countercharge over open ground, in that turn\'s hand-to-hand combat only (p.93).',
 'Pike': 'An extremely long spear (16 ft or more); two hands are needed but shields or bucklers strapped to the forearm are allowed. Infantry fight in two ranks irrespective of movement and, if fighting exclusively to their front, '
         'always strike first regardless of Initiative or charging; if both sides are pike-armed normal priorities apply (p.94).',
 'Kontos': 'A very long cavalry spear needing two hands; riders cannot carry a full-sized shield but may have small shields or bucklers. Cavalry add +1 Strength when they charge or countercharge over open ground (that turn only) and always strike first against troops with shorter weapons '
           'if fighting exclusively to their front (not versus pikes; if both have kontos normal priorities apply). Neither bonus applies if charging through or into difficult terrain (p.94).',
 'Lance': 'The couched lance is the weapon of the charging cavalryman. Cavalry add +2 Strength when they charge or countercharge over open ground (that turn only; maximum Strength 5). Not if charging through or into difficult terrain. After the first charge the rider fights with a hand weapon (p.94).',
}
ARM = {  # name -> (infantry save, cavalry save, notes)
 'No Armour': ('None', '6', 'No armour, only a helmet or minimal clothing. Infantry have no save, but a shield turns this into a 6 (it still adds a pip); cavalry save on a 6 for the advantage of riding a horse (p.96). ' + MAXN),
 'Light Armour': ('6', '5 or 6', 'Breastplate or cuirass of metal, cloth or leather reinforced with metal, bone or horn plates, scales or lamellar (p.96). Infantry in light armour alone save on 6, cavalry on 5 or 6. ' + MAXN),
 'Heavy Armour': ('5 or 6', '4, 5 or 6', 'Light armour plus helmet, greaves, manica and further reinforcement (p.96). Infantry in heavy armour alone save on 5 or 6; cavalry on 4, 5 or 6, which becomes 3, 4, 5 or 6 with a shield (a large shield adds nothing more). ' + MAXN),
 'Cataphract Armour': ('-', '3, 4, 5 or 6*', 'Armour covering the rider from head to foot (horn, lamellar or overlapping scales); cataphracts have no need of shields (p.96). Cavalry save on 3, 4, 5 or 6 with or without a shield.' + STAR + ' Troops so equipped are also affected by the Cataphracts special rule (p.104). ' + MAXN),
 'Partial Plate Armour': ('4, 5 or 6', '3, 4, 5 or 6*', 'Mail with plates extending over it (p.97). Infantry save on 4, 5 or 6, or 3, 4, 5 or 6 with a shield (a large shield adds nothing more). Cavalry as cataphract armour: 3, 4, 5 or 6 with or without shield.' + STAR + ' ' + MAXN),
 'Full Plate Armour': ('3, 4, 5 or 6*', '3, 4, 5 or 6*', 'Articulated metal plates enclosing the wearer from head to foot (p.97). Infantry and cavalry both save on 3, 4, 5 or 6 with or without a shield, so no shield bonus is applied.' + STAR + ' ' + MAXN),
}
SH = {  # name -> (bonus, note)
 'Shield': ('+1 pip to the armour saving throw', 'Close-combat troops carry shields. Troops with double-handed weapons or halberds cannot use their shields in hand-to-hand combat. No benefit where the armour already gives the maximum save or where marked * (p.97).'),
 'Large Shield': ('+2 pips to the armour saving throw', 'A shield covering a substantial part of the bearer\'s body, overlapping those of neighbours. Cannot bring a save above the maximums, so there is no benefit over a normal shield in some cases (p.97).'),
 'Pavise': ('+2 pips to the armour saving throw (when shot at from the front only)', 'A very large shield for missile troops, hung on the back or propped up. No bonus in other circumstances or in hand-to-hand combat; cannot bring a save above the maximums (p.98).'),
 'Buckler': ('+1 pip to the armour saving throw', 'A very small shield favoured by lightly equipped troops. Infantry and cavalry in skirmish formation add the pip against all wounds; other troops add it in hand-to-hand combat only, not against shooting (p.98).'),
 'Full Metal Barding': ('+1 pip to the cavalry armour saving throw', 'Metal barding (often just "barding" in army lists) covers the whole mount. Cavalry with metal barding lose a further 1" movement (p.96, 98).'),
 'Half Metal Barding': ('+1 pip to the cavalry armour saving throw', 'Metal barding covering the front half of the mount: +1 pip only when hit from the front or fighting hand-to-hand to the front, not from the side or rear. Cavalry with metal barding lose a further 1" movement (p.96, 98).'),
 'Full Cloth Barding': ('+1 pip to the cavalry armour saving throw', 'Padded cloth or felt barding covering the whole mount: +1 pip in hand-to-hand combat only, not against shooting. "Barding" alone in an army list means metal barding (p.98).'),
 'Half Cloth Barding': ('+1 pip to the cavalry armour saving throw', 'Padded cloth barding covering the front half of the mount: +1 pip in hand-to-hand combat when fighting to the front only, not from the side or rear, not against shooting (p.98).'),
}
n = 0
def set_char(block, ctype_name, newtext):
    return re.sub(r'(<characteristic name="' + re.escape(ctype_name) + r'"[^>]*>)[^<]*(</characteristic>)', lambda m: m.group(1) + esc(newtext) + m.group(2), block, count=1)
def fix_profile(m):
    global n
    blk = m.group(0); name = html.unescape(re.match(r'<profile id="[^"]*" name="([^"]*)"', blk).group(1))
    if name in HW: blk = set_char(blk, 'Effects', HW[name]); n += 1
    elif name in ARM:
        i, c, nt = ARM[name]
        blk = set_char(set_char(set_char(blk, 'Infantry Save', i), 'Cavalry Save', c), 'Notes', nt); n += 1
    elif name in SH:
        b, nt = SH[name]; blk = set_char(set_char(blk, 'Bonus', b), 'Note', nt); n += 1
    return blk
sp = re.search(r'<sharedProfiles>.*?</sharedProfiles>', g, re.S).group(0)
sp2 = re.sub(r'<profile id="[^"]*" name="[^"]*".*?</profile>', fix_profile, sp, flags=re.S)
g = g.replace(sp, sp2, 1)
print('rewrote', n, 'shared definitions')

RULES = {
 'Horse': ('Rulebook p.95-96; Hannibal p.7', 'Mounted models ride a horse (Movement 8" before armour and barding penalties). A cavalry model\'s armour save is one pip better than the infantry equivalent (p.95).'),
 'Warhorse': ('Hannibal p.7', 'A warhorse is a heavier mount: M8 WS3 BS0 S3 I3 A1, in place of the ordinary horse. As for a horse, the rider\'s armour save is one pip better than the infantry equivalent (p.95).'),
 'Encumbrance': ('Rulebook p.96', 'Movement values printed in army lists are unencumbered. Infantry with an armour save of at least 4+ lose 1"; cavalry with a save of 3+ (ignoring barding) lose 1"; cavalry with metal barding lose a further 1" regardless of save. The M value shown on the model already includes this and updates as you choose equipment.'),
}
for rn, (src, tx) in RULES.items():
    if f'id="{hid("rule", rn)}"' in g: continue
    g = g.replace('  </sharedRules>', f'    <rule id="{hid("rule", rn)}" name="{rn}" hidden="false">\n      <description>{esc(tx)} ({src})</description>\n    </rule>\n  </sharedRules>', 1)
open(GST, 'w', encoding='utf8').write(g)
PROFILES = set(re.findall(r'<profile id="[^"]*" name="([^"]*)"', re.search(r'<sharedProfiles>(.*?)</sharedProfiles>', g, re.S).group(1)))
SRULES = set(re.findall(r'<rule id="[^"]*" name="([^"]*)"', re.search(r'<sharedRules>(.*?)</sharedRules>', g, re.S).group(1)))

MAP = {'javelins': 'Javelin', 'javelin': 'Javelin', 'light armour': 'Light Armour', 'light': 'Light Armour', 'heavy armour': 'Heavy Armour',
       'shield': 'Shield', 'large shield': 'Large Shield', 'buckler': 'Buckler', 'thrusting spear': 'Thrusting Spear',
       'throwing spear': 'Throwing Spear', 'heavy throwing spear': 'Heavy Throwing Spear', 'pilum': 'Heavy Throwing Spear',
       'sling': 'Sling', 'composite bow': 'Bow', 'bow': 'Bow', 'cataphract armour': 'Cataphract Armour', 'partial plate armour': 'Partial Plate Armour',
       'full plate armour': 'Full Plate Armour', 'kontos': 'Kontos', 'lance': 'Lance', 'halberd': 'Halberd', 'double handed weapon': 'Double-handed Weapon',
       'double-handed weapon': 'Double-handed Weapon', 'light crossbow': 'Light Crossbow', 'hand-and-a half sword': 'Halberd', 'pavise': 'Pavise',
       'barding': 'Full Metal Barding', 'cloth barding': 'Full Cloth Barding', 'cloth barded': 'Full Cloth Barding', 'dagger': 'Dagger', 'long bow': 'Long Bow', 'longbow': 'Long Bow'}
RMAP = {'drilled': 'Drilled', 'stubborn': 'Stubborn', 'veteran': 'Veteran', 'stakes': 'Stakes', 'mixed armour': 'Mixed Armour', 'riding horses': 'Horse',
        'mounted on horses': 'Horse', 'ride a horse': 'Horse', 'ride a warhorse': 'Warhorse', 'stratagem': 'Strategem', 'mounted on a warhorse': 'Warhorse', 'warhorse': 'Warhorse', 'horse': 'Horse'}
def targets(label):
    l = html.unescape(label).lower()
    prof, rules = [], []
    head = re.sub(r'\s*\(.*', '', l)
    for t in re.split(r' and |, ', head):
        t = re.sub(r'^(exchange .+ for (a |an )?|may have |upgraded to )', '', t).strip()
        if t in MAP and MAP[t] in PROFILES and MAP[t] not in prof: prof.append(MAP[t])
        for k, v in RMAP.items():
            if t.startswith(k) and v in SRULES and v not in rules: rules.append(v)
    m = re.match(r'exchange .+ for (?:a |an )?(.+)$', l)
    if m:
        t = re.sub(r'\s*\(.*', '', m.group(1))
        if t in MAP and MAP[t] in PROFILES and MAP[t] not in prof: prof.append(MAP[t])
    m = re.search(r'\(replaces ([a-z ]+?)[;)]', l)
    return prof, rules
SKIP = re.compile(r'^(Leader|Standard bearer|Musician|Centurion)')
linked = local = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(m):
        global linked, local
        blk = m.group(0)
        if 'def-link' in blk: return blk
        notes = ' '.join(html.unescape(x) for x in re.findall(r'name="Equipment and options[^"]*"[^>]*>.*?<characteristic[^>]*>(.*?)</characteristic>', blk, re.S))
        def do_opt(o):
            global linked, local
            ob = o.group(0); label = html.unescape(o.group(2))
            if SKIP.match(label): return ob
            prof, rules = targets(label)
            links = ''.join(f'            <infoLink id="{hid(o.group(1), "d", p)}" name="{p}" hidden="false" targetId="{hid("prof", p)}" type="profile"/>\n' for p in prof)
            links += ''.join(f'            <infoLink id="{hid(o.group(1), "d", r)}" name="{r}" hidden="false" targetId="{hid("rule", r)}" type="rule"/>\n' for r in rules)
            rule = ''
            if not prof and not rules:
                key = re.sub(r'\s*\(.*', '', label).split(' and ')[0].strip().lower()
                sent = [x.strip() for x in re.split(r'(?<=[.)])\s+', notes) if key and key[:12] in x.lower()]
                txt = (' '.join(sent[:2]) if sent else f'{label} (see the unit\'s Equipment and options text).')
                rule = (f'          <rules>\n            <rule id="{hid(o.group(1), "def")}" name="{esc(label)}" hidden="false">\n              <description>{esc(txt)}</description>\n            </rule>\n          </rules>\n')
                local += 1
            else: linked += 1
            add = '          <!-- def-link -->\n' + rule + (f'          <infoLinks>\n{links}          </infoLinks>\n' if links else '')
            return ob.replace('          <costs>', add + '          <costs>', 1)
        # unit-level options (8 spaces) and character model-level options (12 spaces)
        blk = re.sub(r'(?<=\n)        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n', do_opt, blk, flags=re.S)
        blk = re.sub(r'(?<=\n)            <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade">\n.*?\n            </selectionEntry>\n', lambda o: do_opt(o).replace('\n          <', '\n          <'), blk, flags=re.S)
        return blk
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('option definition links:', linked, 'with shared definition;', local, 'with local army-list definition')
