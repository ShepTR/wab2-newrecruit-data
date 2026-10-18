#!/usr/bin/env python3
"""Add the El Cid (Warhammer Historical, 2007) army lists: Christian Spain, Al-Andalus and The African Invaders, each as its own
catalogue named "(El Cid)" with one army composition per period. Book page = printed page number.
Usage: python3 el_build.py <outdir>   (then sh tools/el_all.sh <outdir> for the post-processing chain)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import el_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'el cid')

CW.WEAPON_MAP.update({'Pilum': 'Heavy Throwing Spear', 'Longbow': 'Long Bow', 'Two-handed Weapon': 'Double-handed Weapon', 'Javelins': 'Javelin'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('El Cid ' + page, txt)
RULES = {
 'El Cid Common Rules': R('pp.3-4', 'The army lists in El Cid are used in the same way as the Roman and Barbarian lists in Warhammer Ancient Battles; each has a number of army options for a period of history, each with its own force composition and additional rules. UNIT SIZES: minimum five infantry or cavalry models, no upper limit; one model per unit may be a Leader (+5 pts), one a Standard Bearer (+5 pts), one a Musician (+5 pts) unless stated otherwise. WYSIWYG: the models must show the options taken. CAVALRY COUNTER CHARGES: a cavalry unit charged to the front by enemy cavalry may counter charge: it counts as charging for its weapons (e.g. +1S for thrusting spears) but does not move and does not count as charging for deciding who strikes first; cavalry with a move of less than 6" may not counter charge, and cavalry may not counter charge infantry. RANK BONUSES & DIFFICULT TERRAIN: a rank bonus counts only if both units are in clear, open terrain (hills and fords count as clear) and neither is behind an obstacle. REFORMING IN COMBAT: a unit fighting to the flank or rear may reform at the end of the Close Combat phase if it did not break and is not engaged on another facing, facing the unit engaging it with its centre in base contact with the enemy centre; it still loses its rank bonus if charged by an enemy unit of five or more models. SKIRMISHERS & RANK BONUS: formed units do not lose their rank bonus if charged by a unit of five or more models in skirmish formation (including cavalry, but not chariots). FALL BACK IN GOOD ORDER: overwhelming odds (over 2:1 in models) - the side with overwhelming odds that loses and fails its Break test falls back in good order instead of fleeing; drilled troops, skirmishers and cavalry that lose a combat but pass their Break test may choose to fall back in good order; no Panic tests for friends within 12", automatic rally at the end of the move with an immediate reform, may be pursued but are not wiped out (the pursuer counts as having charged next turn), may not charge next turn, a unit falling off the table is lost, and units can fall back from a Ferocious Charge. Missile hits against mixed units use the saving throw of the majority of models (best save if equal) and casualties are removed in roughly equal proportions. MOUNTED MODELS: a horse raises Movement to 8" before armour penalties; a warhorse has the profile M8 WS3 BS0 S3 I3 A1. BOWS: all bows in the army lists are composite bows unless noted. COMBINED FORMATION: see the Combined Formation rule. Andalusian Allies: units from the Al-Andalus list that become subject to the Aliados y Mercenarios rules (documented only, not built).'),
 'Combined Formation (El Cid)': R('p.4', 'Units that can do this are indicated in the army list; typically archers take up the rear ranks of the unit, shooting over the heads of the troops in front. The archers lose their Light Troop status if applicable and are treated as normal troops for movement and rank bonuses. The archers may shoot using the Massed Archery rules (rulebook p.23) as well as any special rules of the unit. A unit may stand & shoot or fire & flee using massed archery.'),
 'Bloodthirsty': R('p.9', 'Bloodthirsty troops and characters are fervent, religiously-motivated warriors. 1. At the start of each turn roll a D6 for each unit not bound by a compulsory movement rule: on 2-6 it moves normally; on a 1 it must surge forward: charge the nearest enemy if within reach, otherwise move towards the nearest enemy at least 4" if possible (faster if the player wishes); if blocked it moves as far as it can; if facing away it turns or wheels to face the nearest enemy and moves as far as it can towards them. 2. Bloodthirsty troops and characters must always pursue an enemy that flees or falls back in good order and may not hold back. 3. They may not disengage from combat or voluntarily fall back in good order. 4. In the Ransom scenario they must roll a 6 to capture an enemy character alive (on a 1-5 the enemy is killed instead).'),
 'Cantador (El Cid)': R('p.12', 'The Cantador may lead a single formed unit (not skirmishers). After deployment, but before the first move, roll a D6: 1 - his voice is drowned out, no effect. 2-3 - the unit may add D3" to its movement for ONE move, march or charge during the battle (declared before the dice are thrown; doubled for charging or marching). 4-5 - the unit may re-roll failed Panic tests during the battle. 6 - the unit and any attached characters may re-roll any misses in the unit\'s first round of combat (warhorses may not).'),
 'Bishop (El Cid)': R('p.12', 'Any unit led by the Bishop may re-roll failed Panic tests.'),
 'Crusading Bishop': R('p.10', 'The Bishop may be upgraded to a Crusading Bishop for +40 pts: Leadership 9, and subject to Hatred of the enemy (Hatred does not extend to warhorses); any unit he leads is also subject to Hatred of the enemy. Crusading Bishops are Bloodthirsty, as is the unit they lead. A Crusading Bishop cannot re-roll failed Panic tests.'),
 'Andalusian Horsemen': R('p.37', 'Cavalry noted as Andalusian Horsemen may reform their unit formation without penalty after movement, including after a march or double pace move but not charging. A unit reforming in skirmish formation must possess a Musician as normal (rulebook p.56). A reforming unit cannot fire in the Shooting phase. The unit reforms around its leader, musician or standard bearer, and no model may move more than its permitted distance. Mounted characters accompanying an Andalusian Horsemen unit do not impede the unit\'s ability to reform.'),
 'Qadi': R('p.40', 'The Qadi can lead a single formed unit (not skirmishers). This unit may re-roll failed Rally attempts during the battle, as long as the Qadi is still alive and leading. Later Taifas: if no other Army General is chosen the Qadi may be made Army General for +50 pts; any unit led by the Qadi-General may also re-roll failed Panic tests, but the Qadi-General loses the ability to re-roll failed Rally attempts.'),
 'Mounted Crossbow (El Cid)': R('p.42', 'The light crossbow used by Andalusian mounted crossbowmen has a range of 24", Strength 3 and a -1 save modifier. If they move in their Movement phase they are unable to fire that turn (they are assumed to have halted to reload).'),
 'Imam': R('p.50', 'The Imam may lead a unit of either Black Guard or Berber Spearmen (with or without Berber Archers). He cannot lead any other unit. The Imam is subject to Hatred of the enemy as described in the psychology section of the game rules. Any unit led by the Imam also becomes subject to Hatred of the enemy.'),
 'African Drummers': R('p.46', 'Almoravid and Almohad armies included large numbers of Saharan drummers. Certain units may feature two Musician models (rather than one) for the normal cost of +5 pts per model. Any unit so equipped automatically wins a drawn combat by one point, rather than resorting to a musical roll-off. Only Hasham Guard Cavalry, Berber Cavalry, Camel Riders, Black Guard, Berber Spearmen and Berber Archers may take an additional drummer. A Berber Archer or combined Berber Archers/Spearmen unit with two drummers may use Massed Archery even if it has moved up to its normal movement in a turn; a -1 to hit penalty still applies to units that move & shoot.'),
 'Camel Riders (El Cid)': R('p.51', 'Camels cause fear in all cavalry (and chariots, should they happen to meet one).'),
 'Aliados y Mercenarios': R('p.54', 'Aliados y Mercenarios units may have a Leader, Standard & Musician as normal. A single Aliados y Mercenarios unit may be personally led by the Army General and is then exempt from these special rules and treated like a regular unit from the General\'s army. Aliados y Mercenarios units may not benefit from the special abilities of the Army General or Army Battle Standard, although they may be led by any appropriate character and use his Leadership and any special abilities. Roll a dice the first time a player wishes to move, charge or shoot with each unit of Aliados y Mercenarios: on a 1 the unit remains stationary and may not shoot, but can defend itself if attacked in close combat, including shooting against a charging unit; on a 2-6 the unit can act as the player wishes. Once it has successfully moved or shot, it no longer has to take this test. Aliados y Mercenarios units are treated as part of their employer\'s army for taking and causing Panic tests.'),
}
ATTACH = {}
FIRSTCHAR = {'CS': 'Infante', 'AA': 'Amir', 'AF': 'Sayyid'}
def comp_text(variants):
    out = ['ARMY COMPOSITIONS (pick one in the Army composition list):']
    for vn, lim, txt in variants:
        out.append(f'[{vn.split(" - ", 1)[-1]}]')
        for c, d in lim.items():
            out.append(f"  {c}: " + ', '.join(('at least' if k == 'min' else 'up to') + f' {v}%' for k, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = SPUB; RB.SRC = 'El Cid'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="El Cid" shortName="EC" publisher="Warhammer Historical Wargames" publicationDate="2007"/>\n  </publications>', 1)
    pools = sorted({c for (_, _), cs in D.SECOND.items() for c in cs})
    for c in pools:
        if f'id="{hid("cat", c)}"' not in s:
            s = s.replace('  </categoryEntries>', f'    <categoryEntry id="{hid("cat", c)}" name="{c}" hidden="false"/>\n  </categoryEntries>', 1)
    open(gst, 'w', encoding='utf8').write(s)
    cache = os.path.join(OUT, 'tools', 'variants.json')
    variants = json.load(open(cache, encoding='utf8')) if os.path.exists(cache) else {}
    allunits = [u for _, _, _, us, _, _ in D.LISTS for u in us]
    CW.clean(allunits)
    for key, name, fn, units, vs, notes in D.LISTS:
        for u in units:
            for m in u['models']:
                m['rules'] = [RULE_MAP.get(r, r) for r in m['rules']]
                m['rules'] += ATTACH.get((key, u['name']), [])
        first = next(u for u in units if u['name'] == FIRSTCHAR[key])
        first['models'][0]['rules'].append('El Cid Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', 'gameSystemRevision="10"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the El Cid army list book (Warhammer Historical).')
        # secondary pool categories
        for u in units:
            sec = D.SECOND.get((key, u['name']))
            if not sec: continue
            uid = hid(hid('catalogue', name), u['name'], 'unit')
            m = re.search(r'(    <selectionEntry id="%s"[^>]*type="unit">\n.*?<categoryLinks>\n.*?)(      </categoryLinks>\n)' % re.escape(uid), x, re.S)
            links = ''.join(f'        <categoryLink id="{hid(uid, "pool", c)}" name="{c}" hidden="false" targetId="{hid("cat", c)}" primary="false"/>\n' for c in sec)
            x = x.replace(m.group(0), m.group(1) + links + m.group(2), 1)
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    cf = os.path.join(OUT, 'tools', 'cond_limits.json')
    conds = json.load(open(cf, encoding='utf8')) if os.path.exists(cf) else []
    for key, unit in D.COND_CHARS:
        fn = next(f for k, n, f, *_ in D.LISTS if k == key)
        e = {'file': fn, 'category': 'Characters', 'kind': 'max', 'value': 25, 'unit': unit}
        if e not in conds: conds.append(e)
    json.dump(conds, open(cf, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'EC {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
