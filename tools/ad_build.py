#!/usr/bin/env python3
"""Add the Alexander the Great (Warhammer Historical) army lists: Rise of Macedon, Alexandrian Imperial, Greek Mercenaries, Thracians, Illyrians,
The End of Persia, The Frontier Horsemen and the Indian army (Classical/Mountain/Republican/Mauryan). Book page = printed page number.
Usage: python3 ad_build.py <outdir>   (then sh tools/ad_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import ad_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'alexander the great')
REV = '11'
CW.WEAPON_MAP.update({'Broadsword': 'Hand Weapon', 'Longbow': 'Long Bow', 'Javelins': 'Javelin', 'Two-handed Weapon': 'Double-handed Weapon'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('Alexander the Great ' + page, txt)
RULES = {
 'Alexander Common Rules': R('pp.4-9', 'The army lists in Alexander the Great are used like those in the other Warhammer Ancient Battles books. UNIT SIZES: minimum five models (three chariots), no upper limit unless stated; one model per unit may be a Leader (+5 pts), a Standard Bearer (+5 pts) and a Musician (+5 pts) unless stated otherwise. COMBINED FORMATION: a unit that mixes weapon types in ranks (archers behind pikemen etc.) uses the Combined Formations rule. CAVALRY COUNTER CHARGES: a cavalry unit charged to the front by enemy cavalry may counter charge (counts as charging for its weapons but does not move; cavalry with a move of less than 6" and cavalry against infantry may not). SKIRMISHERS & RANK BONUS: formed units do not lose their rank bonus when charged by skirmishers in open order. ELEPHANTS: elephants cannot be pursued; elephants, chariots and characters have flanks and a rear; rampaging elephants count as 50% victory points. XYSTON: a cavalry thrusting spear that always strikes first, even when not charging; a kontos or pike strikes first against a xyston. Mounted models with xyston or kontos may not carry shields; mounted models may not use large shields; foot models may not combine a pike with a large shield. The Army Standard Bearer may not take a xyston, spear, pike, kontos etc. OPTIONAL RULES (book only, not built): Mixed Armour, Elephants (skirmishers vs elephants, proximity, un-crewed), Subordinate Generals, Persian Prepared Ground and scythed chariot Out of Control.'),
 'Macedonian & Trained Phalanx': R('p.6', 'Macedonian phalanx and trained phalanx: the benefits need at least 16 models in the unit and a +1 rank bonus. The unit may About Face but not Right Face or Left Face. A Drilled phalanx keeps its benefits until reduced below 12 models and may turn 90 degrees. Oracles: a Macedonian army using oracles gets D6 per 1,000 pts.'),
 "Alexander's Eagle": R('p.20', 'Alexander may choose to re-roll the Oracle dice at the start of the game (he must abide by the second roll), or force the other player to deploy first.'),
 'Kontos (Alexander)': R('p.21', 'A kontos strikes first against a xyston, and cannot be used with a shield when mounted.'),
 'Polemarch': R('p.79', 'If a Polemarch is present Greek mercenary troops make Leadership tests using their paymaster\'s Army General and gain all benefits of the Army Battle Standard; if he is killed all Greek mercenaries must pass a Panic test (ignored if the Army General is killed). Greek mercenaries otherwise use the paymaster\'s General and Army Battle Standard.'),
 'Rhomphaia': R('p.82', 'Halberd; +1 Strength; counts as shieldless. Only Mountain (Highland) tribesmen may take it.'),
 'Rolling Wagons': R('p.83', 'Wagons may not move normally; they are rolled downhill in the Shooting phase. They must be placed on a hill and a warrior unit must be within 3" to launch them. They move straight ahead 3D6" and are removed at the end of the roll or on hitting an obstacle. Units in the path suffer D6 Strength 5 impact hits. Large targets; drilled troops may open lanes. Troops fighting behind wagons count as in soft cover. Highland armies only.'),
 'The Great King': R('p.92', 'If the Great King flees off the table the army checks for panic as if he was killed. Units within 12" gain +1 Leadership (instead of using his Leadership for psychology and Break tests). Certain units may only be included if the Great King is the General. He may only join Persian troops, and automatically flees if involved in a losing close combat that involves the enemy army general.'),
 'Half-Barded Armour': R('p.92', 'Half-barding gives +1 save to the front only, and -1 Movement.'),
 'Scythed Chariots (End of Persia)': R('p.93', 'May be fielded in units of fewer than three models, with no leaders, musicians or standards. A scythed chariot counts as three models for unit size. Maximum four scythed chariot models per 2,000 pts. 7 M, 5 S, 4 T, 1 W, 3 I, D6+2 A, Ld 5; the driver has WS3 BS3 S3 T3 W1 I3 A1 Ld7, a dagger and heavy armour.'),
 'Elephants (Alexander)': R('p.7', 'Elephants cannot be pursued; they have flanks and a rear; a rampaging elephant gives 50% victory points. Indian elephants carry no towers; crews gain a 5+ save. Used to elephants troops are unaffected by elephant fear.'),
 'Brahman Priest': R('p.114', 'The Priest must be attached to an infantry unit at the start of the game and may not leave. If he is killed D6 members of his following immediately commit suicide and are removed; at the start of each turn D6 followers commit suicide or desert. A Brahman or unit led by one will not pursue a broken enemy. Brahman priests hate all foreigners and may not accompany an army that includes Persian or Greek allies.'),
 'Rathamasaula': R('p.111', 'Man-pushed anti-elephant cart: no impact hits on normal troops, but against elephants D3 wounds with no saves. Charges up to 8" depending on remaining crewmen; cannot march. The crew may not fight on the turn it charges; if charged the crew defend from behind and are -1 to hit.'),
 'War Wagons': R('p.111', 'Treated as Heavy chariots but do not cause fear, no double moves or impact hits. The wagon\'s attacks represent the oxen: front only, hits only on 6s. Crewmen attack separately and fight from inside the wagon with a 5+ save. Not with elephants or large chariots. Each wagon counts as one model; crews may not have standards, musicians or leaders.'),
 'Wagon Laager (Republican)': R('p.114', 'Wagons are deployed up to 12" from the baseline end-to-end in a straight line. They may not be moved, are immune to psychology, and cannot be broken. Each may hold up to four skirmishing infantry or characters. Units behind wagons count as in soft cover but may not use massed archery; large targets; defenders gain a 5+ save. Attackers need 6s to hit units behind unoccupied wagons or skirmishers inside until they win a round of combat. Empty wagons are destroyed if an enemy unit of five or more models remains in contact at the end of the Combat phase.'),
 'Large Chariots': R('p.112', 'Count as Heavy Chariots and cause D3 Strength 4 impact hits. Two unarmed drivers, two warriors and two shield bearers, giving a 3+ save.'),
 'Elephant and Chariot Escorts': R('p.110', 'One unit of escorts per chariot unit or elephant. Each elephant escort unit up to eight escorts, each chariot or wagon escort unit up to four escorts per chariot or wagon in the unit.'),
}
FIRSTCHAR = {'ROM': 'Alexander the Great', 'IMP': 'Alexander the Great', 'GM': 'Polemarch', 'TH': 'Thracian King', 'IL': 'Illyrian Warlord', 'PE': 'Great King', 'FH': 'Army General', 'IN': 'King (Danda)'}
def comp_text(variants):
    out = ['ARMY COMPOSITIONS (pick one in the Army composition list):'] if len(variants) > 1 else ['ARMY COMPOSITION:']
    for vn, lim, txt in variants:
        out.append(f'[{vn.split(": ", 1)[-1]}]')
        for c, d in lim.items():
            out.append(f"  {c}: " + ', '.join(('at least' if k == 'min' else 'up to') + f' {v}%' for k, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = SPUB; RB.SRC = 'Alexander the Great'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Alexander the Great" shortName="AG" publisher="Warhammer Historical Wargames" publicationDate="2008"/>\n  </publications>', 1)
    s = re.sub(r'gameSystemRevision="\d+"', f'gameSystemRevision="{REV}"', s, count=1) if 'gameSystemRevision' in s else s
    s = re.sub(r'(<gameSystem [^>]*?)revision="\d+"', lambda m: m.group(1) + f'revision="{REV}"', s, count=1)
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
        first = next(u for u in units if u['name'] == FIRSTCHAR[key])
        first['models'][0]['rules'].append('Alexander Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Alexander the Great army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'AG {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
