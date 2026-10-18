#!/usr/bin/env python3
"""Add the Shieldwall (Warhammer Historical, 2002) army lists: Northmen, English, Caledonians, Welsh, Hibernians and Western Franks, each as its own
catalogue named "(Shieldwall)" with one army composition per kingdom/sub-list. Book page = printed page number.
Usage: python3 sw_build.py <outdir>   (then sh tools/sw_all.sh <outdir> for the post-processing chain)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import sw_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'shieldwall')

CW.WEAPON_MAP.update({'Pilum': 'Heavy Throwing Spear', 'Longbow': 'Long Bow', 'Two-handed Weapon': 'Double-handed Weapon', 'Javelins': 'Javelin'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('Shieldwall ' + page, txt)
RULES = {
 'Shieldwall Common Rules': R('pp.4-5', 'The army lists in Shieldwall are used in the same way as the Roman & Barbarian lists in Warhammer Ancient Battles; each has its own force composition and additional rules. UNIT SIZES: the minimum size for a regiment is five infantry or cavalry models; there is no upper limit. One model per unit may be upgraded to a leader (+5 pts), one to a standard bearer (+5 pts) and one to a musician (+5 pts) unless stated otherwise. WHAT YOU SEE IS WHAT YOU GET: unless your opponent agrees otherwise, the models you use must show the options you take. SHIELDWALL: units may form a shieldwall instead of moving. As long as the unit is in a shieldwall, all enemy attacks from the front of the unit (shooting and hand-to-hand) suffer a -1 to hit modifier. The unit benefits from the shieldwall as long as it does not move or lose a round of close combat. Characters on foot in a unit with Shieldwall gain the benefits as well. CAVALRY COUNTER CHARGES: a new charge reaction that may only be taken by cavalry units that are charged to the front by enemy cavalry. The unit counts as charging for the purposes of using its weapons (e.g. +1 S with thrusting spears). Cavalry with a move of less than 6" may not counter-charge. The unit does not move, and does not count as charging for deciding who strikes first. Cavalry may not counter-charge infantry. RANK BONUSES & DIFFICULT TERRAIN: units may only count their rank bonus in close combat if both they and their opponent are in clear, open terrain and neither is behind an obstacle (hills and fords count as clear terrain and do not negate a rank bonus). REFORMING IN COMBAT: a unit fighting to the flank or rear may reform at the end of the Close Combat phase as long as it did not break and is not also engaged on another facing. It must reform so that it faces the unit engaging it, with its centre in base contact with the centre of the enemy unit. A reformed unit still loses its rank bonus for the duration of the combat if it was charged by an enemy unit containing five or more models. SKIRMISHERS AND RANK BONUSES: formed units do not lose their rank bonus if charged by a unit of five or more models in skirmish formation (also to cavalry in skirmish formation, but not to chariots). FALL BACK IN GOOD ORDER: a side that outnumbers the other by over two to one (overwhelming odds) and loses a combat and fails its Break test falls back in good order instead of fleeing; drilled troops, units in skirmish formation and cavalry that lose a combat but pass their Break test may fall back in good order if they wish. The fall back move is made as for a flee move, except: friends within 12" do not take a Panic test; the unit rallies automatically at the end of the move and may immediately reform; it may be pursued but if caught is not wiped out (the pursuer counts as having charged in the next Close Combat phase); it may not declare a charge in its next turn but may otherwise move and shoot normally; a unit that falls back off the table is lost; units can fall back in good order from a Ferocious Charge. MOUNTED MODELS (models chosen from the Shieldwall lists): a model may be mounted on a horse (M8 prior to armour penalties) or on a warhorse (M8 WS3 BS0 S3 I3 A1); mounted models may not use a double-handed weapon. ARMY STANDARD BEARER: may not take double-handed weapons or additional hand weapons as options. LEADERSHIP & WARBAND PSYCHOLOGY: if a unit with Warband psychology is joined by a character who does not have Warband psychology, the unit must use either its own Ld or the character\'s; it cannot use the character\'s Ld and add on the Warband rank bonus.'),
 'Fury of the Norsemen': R('p.5', 'Such units cause fear in any unit that has a Ld value, before modification, of 7 or less. The affected unit may use its modified Leadership value when taking the test.'),
 'Werod': R('p.5', 'If the general is killed whilst with such a unit roll a D6. On a 4+ the unit immediately tries to charge the nearest enemy unit in sight, if not engaged. The unit is immune to psychology and Break tests. If its opponent is eliminated, the unit charges the next nearest enemy unit, etc.'),
 'Warband Psychology (rule 2)': R('Rulebook p.109', 'Subject to Warband psychology rule 2: if the unit charges and defeats the enemy in the first round of combat, the enemy are automatically broken and flee without a Break test if the warband outnumbers the enemy.'),
 'Berserkers (Shieldwall)': R('p.12', 'A unit of Hirdmen can contain up to three Berserkers. They must be placed with a unit at the beginning of the battle, do not count as hidden, and must be represented by a suitably ferocious model in the front rank of the unit. You may choose to remove a Berserker model as a casualty if the unit suffers missile or close combat casualties, but do not have to unless the Berserker(s) is the only model(s) left in the unit or it was targeted in close combat. Berserkers may not leave their unit, other than when they berserk. If there is an enemy unit visible within the charge arc of the unit containing the Berserkers at the start of a Viking turn and within 12" then there is a chance the Berserkers will go berserk: roll 2D6 for each model; if the number rolled is equal to or greater than the distance to the nearest enemy the Berserker charges immediately (move the Berserker into contact with the enemy as he charges). If the unit is engaged in close combat at the start of its turn the Berserker automatically goes berserk at the start of the Viking player\'s turn. Berserkers always charge the closest enemy (randomly determined if two enemy units are equally close). The Berserker automatically causes D6 Strength 5 hits on the enemy unit which he attacks and is then removed from play. If the enemy unit suffers 25% casualties from the attacks, it must take an immediate Panic test.'),
 'Godi': R('p.13', 'The Godi and any unit he is with is immune to psychology and Break tests. As soon as the Godi is killed the unit tests as normal.'),
 'Army General (English)': R('p.22', 'Army General. Any friendly English unit within 12" of the Army General ignores Warband Psychology rule 2.'),
 'Abbod': R('p.23', 'A unit that the Abbod accompanies re-rolls any misses in the first round of any combat.'),
 'Combined Units (English)': R('p.22', 'Prior to deployment, the English army may split up the single unit of Huscarls, and any units of Thegns, and combine them with units of Ceorls such that no more than 25% of the unit are Huscarls, or 50% are Thegns. Thegns and Huscarls may not be mixed. Huscarls and Thegns must be positioned in the front ranks. If the unit then contains more than one leader, musician or standard, the excess models are replaced by rank & file figures. As long as half or more of the front rank are Huscarls or Thegns, the unit uses the Leadership and Psychology rules of these figures rather than the Leadership and Psychology rules of the Ceorls. Half of all missile hits inflicted on a combined unit count as being inflicted on the Huscarls or Thegns. In close combat, enemy models in base combat with a Huscarl or Thegn must fight against them, with the exception of challenges. If excess casualties are inflicted, these carry over to lesser troops. The last Huscarls/Thegns removed are the leader, musician and standard; this occurs even if there are other models remaining in the unit. The armies of Anglia and Northumbria may combine spear and shield-armed Gebur with Thegns and Huscarls in the same way as Ceorls.'),
 'Huscarl Hatred': R('p.22', 'If the Army General dies, then Huscarls become subject to Hatred for the rest of the battle as described in the Warhammer Ancient Battles rules.'),
 'Veterans (Wessex)': R('p.20', 'All units of Thegns may, once per battle, choose to re-roll all their to hit dice for close combat or for shooting. However, the unit must re-roll all of its dice (not just the failures) and must abide by the result.'),
 'Offeiriad': R('p.53', 'You may re-roll rally attempts of any unit the Priest is accompanying.'),
 'Bishop': R('p.72', 'Any unit the Bishop is with may re-roll failed Panic tests.'),
 'Jomsviking Bribe': R('p.78', 'Each turn roll a dice. On a 1 the Jomsvikings or Adventurers have accepted a bribe from the enemy and may not move that turn.'),
 'Unreliable Mercenaries': R('pp.78-79', 'Although in the main loyal and obedient, sometimes mercenaries would think they knew better than their employer! Roll a dice the first time a player wishes to move, charge, or shoot with each unit. If a 1 is rolled the unit remains stationary and may not shoot, but may defend itself if attacked in close combat, including shooting against a charging unit. On a 2-6, the unit may act as the player wishes. Once a unit has successfully moved or shot, it no longer needs to take this test and may be moved normally.'),
 'Mercenary Rally': R('p.79', 'Any unit that chooses to flee or fire & flee as a charge reaction rallies automatically at the end of its move and may reform facing in any direction. This means that should the charging enemy encounter them, the unit is not destroyed, and may instead fight in the Close Combat phase. Their opponents still count as charging.'),
 'Raiders': R('p.29', 'Although strategically the Caledonians were more often than not on the defensive, tactically they were frequently the attackers. The commander of a Caledonian army may always choose whether he moves first or second.'),
 'Choice of Terrain (Welsh)': R('p.52', 'If players agree to randomly choose the terrain, the player commanding a Welsh army may always select one additional item of terrain which he may place anywhere other than the opponent\'s deployment zone.'),
 'Hibernian Ambush': R('p.61', 'At the beginning of the battle, before units are placed, a commander of an Hibernian army may keep one unit off the battlefield. The commander writes down where the unit is hidden: either a village, wood, etc, or an area of ground hidden by a hill or similar. Once all units have been deployed the commander of the Hibernian army may either place the unit in his own deployment area or keep it in ambush. As soon as an enemy unit is within 8" he must deploy the unit, although he may deploy the unit earlier if he wishes. If the unit is deployed in the Hibernian player\'s turn it may charge, move, fire and attack normally in that turn. Whilst hidden a unit is immune to all psychology tests.'),
}
# army-level rules attached to the characters of the lists
ATTACH = {('CA', 'Righ'): ['Raiders'], ('CA', 'Mormaer'): ['Raiders'], ('WE', 'Teyrn'): ['Choice of Terrain (Welsh)'], ('WE', 'Uchelwyr'): ['Choice of Terrain (Welsh)'],
          ('HI', 'Ri Ruirech'): ['Hibernian Ambush'], ('HI', 'Ri Tuathe'): ['Hibernian Ambush'], ('EN', 'Huscarls'): ['Huscarl Hatred']}
FIRSTCHAR = {'NO': 'Konnungr', 'EN': 'Cyning', 'CA': 'Righ', 'WE': 'Teyrn', 'HI': 'Ri Ruirech', 'FR': 'Rex/Dux'}

def comp_text(variants):
    out = ['ARMY COMPOSITIONS (pick one in the Army composition list):']
    for vn, lim, txt in variants:
        out.append(f'[{vn.split(" - ", 1)[-1]}]')
        for c, d in lim.items():
            out.append(f"  {c}: " + ', '.join(('at least' if k == 'min' else 'up to') + f' {v}%' for k, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = SPUB; RB.SRC = 'Shieldwall'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Shieldwall" shortName="SW" publisher="Warhammer Historical Wargames" publicationDate="2002"/>\n  </publications>', 1)
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
        first['models'][0]['rules'].append('Shieldwall Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', 'gameSystemRevision="10"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Shieldwall army list book (Warhammer Historical).')
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
    RB.patch_gst(gst, [(f'SW {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
