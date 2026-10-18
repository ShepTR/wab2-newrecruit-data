#!/usr/bin/env python3
"""Add the Chariot Wars (Warhammer Historical) army lists: Sumerian & Akkadian, New Kingdom Egyptian, Hammurabic Babylonian, Hittite Empire,
Trojan War (Mycenaean/Minoan/Trojan), Israelite and Assyrian Empire (+ Babylonian). Book page = pdf page - 2.
Usage: python3 cw_build.py <outdir>   (run after hb_build.py and BEFORE the post-processing scripts; then run the whole post-processing chain)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_data as D
B = RB.B
hid, q, t = B.hid, B.q, B.t
OUT = RB.OUT
CPUB = hid('pub', 'chariot wars')

WEAPON_MAP = {'Composite Bow': 'Bow', 'Javelins': 'Javelin', 'Sword': 'Hand Weapon', 'Throw Sticks': 'Javelin'}
DROP_WEAPONS = {'Mixed Weapons'}
RULE_MAP = {'Army General': 'Army General (Chariot Wars)', 'Warband (psychology rules 1 & 2)': 'Warband Psychology (rules 1 & 2)',
            'Mixed Weapons': 'Mixed Weapons (Chariot Wars)', 'Chariot Runners': 'Chariot Runners (Chariot Wars)'}
DROP_RULES = {'Light Infantry', 'Light Cavalry', 'Light Troops', 'Skirmishers', 'Mixed archers/spearmen'}

RULES = {
 'Chariot Wars Common Rules': ('Chariot Wars p.3', 'Multiple troop types: when you pick a unit all models must be of the same type unless the list allows mixed units. What You See is What You Get: models must show the options taken unless the opponent agrees otherwise. Unit sizes: minimum five infantry or five cavalry models, or three chariot models; no upper limit; one model may be a Leader, one a Standard Bearer and another a Musician (+5 pts each). Throw sticks have the same effect as a javelin. Characters in chariots: the cost of the chariot is not included in the character\'s entry but is bought from a later entry in the same list; the points spent count against the points that may be spent on characters. The character replaces one crew member; characteristics of character and chariot remain unchanged and each is attacked separately. Roll to hit as normal for missile fire, then roll again for each hit scored; on a 1-4 the chariot is hit, on a 5-6 the character is hit. In hand-to-hand an enemy model in base contact can choose to attack the chariot or the character. A character mounted in a chariot with a shield bearer may add +2 to his armour save; in any other circumstances +1. A character in a chariot has the chariot\'s armour save if it is better than his own. Wounds are tracked separately. The character may dismount and fight on foot if the chariot is destroyed, but only if a suitable model is available; if no model is available the character is lost with the chariot. If the character is killed the chariot may move and fight on its own.'),
 'Army General (Chariot Wars)': ('Rulebook', 'Friendly units within 12" may use the Army General\'s Leadership.'),
 'Chariot Runners (Chariot Wars)': ('Chariot Wars p.3', 'Runners in skirmish formation may move into gaps between a unit of chariots and still count as being in unit coherency as long as they are within 2" of a chariot model in the unit or within 2" of another model in the unit. Chariot runners can use this tactic to charge an enemy that is already engaged by the chariots, by charging into the gaps between chariot models. Chariots can charge through a unit of chariot runners that is in skirmish formation, even if the gaps between the runners are not wide enough to let them through; simply push the runners aside until there is a wide enough gap for the chariot to fit through. These rules replace the Armies of Antiquity rules which allow chariot runners that are touching a chariot model to fight.'),
 'Mixed Weapons (Chariot Wars)': ('Chariot Wars p.3', 'Tribal contingents were rarely uniformly equipped; players may mix warriors in the unit so some are armed with different weapons. Whatever the models are carrying, a unit armed with mixed weapons counts as having hand weapons, javelins and bucklers.'),
 'Warband Psychology (rules 1 & 2)': ('Rulebook p.109', '"Subject to Warband psychology rules 1 & 2": 1. D6 test at start of turn: 2-6 pass, 1 surge forward towards nearest visible enemy by at least basic move and charge if within range. 2. If the unit charges and defeats the enemy in the first round of combat, the enemy are automatically broken and flee without a Break test if the warband outnumbers the enemy.'),
 'Onager Chariots': ('Chariot Wars p.9', 'Sumerian chariots were pulled by onagers (wild asses). At the start of the Sumerian player\'s turn roll a dice for each chariot unit. On a 1 the onagers are giving their drivers trouble and a further D6 is rolled: 1-3 "Giddy-up damn you!" the onagers refuse to move at all this turn and remain stationary; 4-6 "Whooa boy, whooooooa!" the onagers set off at a fair old clip: the unit must advance D6" straight ahead. The crew may turn this move into a charge if they wish, in which case the D6 roll is doubled; the unit must charge straight ahead and cannot wheel.'),
 'Egyptian Charioteers': ('Chariot Wars p.15', 'Egyptian charioteers do not suffer -1 to hit for shooting on the move and are able to shoot as they charge. This attack is made after any enemy charge reactions (any enemy that fire as a charge reaction do so before the charioteers). The attack counts as having taken place at short range. Enemy units that take 25% casualties must pass a Panic test or flee.'),
 'Chariot Archers (Assyrian)': ('Chariot Wars p.57', 'Chariot archers do not suffer the -1 to hit for shooting on the move. Automatic hits inflicted by a charging heavy chariot are added to the hits scored by the crew and happen at the same time.'),
 'Mounted Archers (second rank)': ('Chariot Wars p.57', 'Mounted archers in the second rank of the unit may shoot over the first rank.'),
 'Amorite Chief': ('Chariot Wars p.21', 'The Amorite Chief may only lead Amorites. Any Amorite unit within 12" of the Chief may use his Leadership when it takes a Leadership test.'),
 'Vassal King': ('Chariot Wars p.29', 'Any units within 12" of the Vassal King who are of the same nationality as him may use his Leadership when taking a Leadership test.'),
 'Legendary Warriors': ('Chariot Wars p.44', 'Heroes were mighty warriors of near legendary ability. They may re-roll one failed to hit and one failed to wound roll each combat phase. In addition they may re-roll a failed armour save if the wound suffered is their last one remaining (they can re-roll their last armour save). The General is the foremost hero in the army and benefits from this rule.'),
 'Sacred Ark': ('Chariot Wars p.49', 'The Sacred Ark may be chosen instead of an army standard bearer, only if the army does not include any chariots. The Ark and the Priests form a single unit and may not join other units. They should be placed on a single base and move and manoeuvre in the same manner as a heavy chariot. They may not charge. Any unit within 6" of the Ark may automatically rally. Any unit within sight of the Ark may re-roll any Break or Rally tests. If the Ark flees or is captured or destroyed, all units within sight must take an immediate Panic test. The Priests are treated as stubborn.'),
 'Camels': ('Chariot Wars p.51', 'Each camel carries two riders. Camels cause fear in cavalry and chariots.'),
 'Elamite Chariots': ('Chariot Wars p.60', 'Elamite chariots are four-horse heavy chariots, crewed by a driver armed with a sword. Elamite chariots may transport up to three infantry models per chariot. Only Babylonian armies may include Elamite Chariots or Cavalry.'),
 'Heavy Slingers': ('Chariot Wars p.58', 'Models in a unit can have different weapon combinations. Armoured slingers in the second rank may shoot at full effect as long as the unit does not move. Slingers may shoot even if not in skirmish formation. Enemy units may not use shields against sling shot hits. A unit of heavy slingers contains archers and slingers in equal proportions.'),
 'Mule Carts': ('Chariot Wars p.59', 'The entire unit must be equipped with the required number of cart models (each cart carries up to five soldiers). The infantry automatically dismount from the carts to fight or shoot, even if charged. The carts are non-combatant and always placed directly behind dismounted infantry; they do not count as chariots. When mounted on carts the unit may march move but may not charge. Dismounted infantry must remount to be able to flee. If the unit pursues they do so as infantry and the carts follow up behind.'),
 'Phalanx (Chariot Wars)': ('Chariot Wars p.61', 'As long as the unit has at least sixteen models and a rank bonus of at least +1: cavalry may not charge the front of the phalanx; phalanx models may charge and still fight in two ranks; all enemy attacks (shooting and hand-to-hand combat) at the front of the phalanx suffer -1 to hit. The only formation change allowed is an about face (180 degree turn). Phalanxes may wheel but cannot march or charge if they do so; they may drift 1" to the right when they march or charge. As soon as the unit is reduced to fewer than sixteen models or loses its rank bonus these rules no longer apply.'),
}
RULES.update(D.AS_RULES)

LISTS = [  # name, units, limits/variants, notes, file
 ('Sumerian & Akkadian (Chariot Wars)', D.SU, [('Sumerian & Akkadian', D.SU_LIMITS, 'Standard composition.')], D.SU_NOTES, 'Sumerian_Akkadian_Chariot_Wars.cat'),
 ('New Kingdom Egyptian (Chariot Wars)', D.EG, [('New Kingdom Egyptian', D.EG_LIMITS, 'Standard composition.')], D.EG_NOTES, 'Egyptian_New_Kingdom_Chariot_Wars.cat'),
 ('Hammurabic Babylonian (Chariot Wars)', D.HB, [('Hammurabic Babylonian', D.HB_LIMITS, 'Standard composition.')], D.HB_NOTES, 'Hammurabic_Babylonian_Chariot_Wars.cat'),
 ('Hittite Empire (Chariot Wars)', D.HT, [('Hittite Empire', D.HT_LIMITS, 'Standard composition.')], D.HT_NOTES, 'Hittite_Chariot_Wars.cat'),
 ('Trojan War (Chariot Wars)', D.TW, [('Trojan War', D.TW_LIMITS, 'Standard composition.')], D.TW_NOTES, 'Trojan_War_Chariot_Wars.cat'),
 ('Israelite (Chariot Wars)', D.IS, [('Israelite', D.IS_LIMITS, 'Standard composition.')], D.IS_NOTES, 'Israelite_Chariot_Wars.cat'),
 ('Assyrian Empire (Chariot Wars)', D.AS, D.AS_VARIANTS, D.AS_NOTES, 'Assyrian_Chariot_Wars.cat'),
]

def clean(units):
    for u in units:
        for m in u['models']:
            m['weapons'] = [WEAPON_MAP.get(w, w) for w in m['weapons'] if w not in DROP_WEAPONS]
            m['weapons'] = list(dict.fromkeys(m['weapons']))
            m['rules'] = [RULE_MAP.get(r, r) for r in m['rules'] if r not in DROP_RULES]
            nm = m['name']
            if ('Chariot' in nm and 'Runner' not in nm) or nm == 'Eqeta' or nm == 'Chariotry' or nm == 'Ark & four priests' and False:
                m['mn'] = max(m['mn'], 3)

def comp_text(variants):
    out = ['ARMY COMPOSITIONS:']
    for vn, lim, txt in variants:
        out.append(f'[{vn}]')
        for k, (t_, v) in lim.items():
            out.append(f"  {k}: {'at least' if t_ == 'min' else 'up to'} {v}%")
        out.append('  ' + txt.replace('\n', '\n  '))
    return '\n'.join(out)

def main():
    RB.PUB = CPUB; RB.SRC = 'Chariot Wars'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{CPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{CPUB}" name="Chariot Wars" shortName="CW" publisher="Warhammer Historical Wargames" publicationDate="2007"/>\n  </publications>', 1)
        open(gst, 'w', encoding='utf8').write(s)
    cache = os.path.join(OUT, 'tools', 'variants.json')
    variants = json.load(open(cache, encoding='utf8')) if os.path.exists(cache) else {}
    rules = dict(RULES)
    cats = set()
    for name, units, vars_, notes, fn in LISTS:
        clean(units)
        full = notes + '\n\n' + comp_text(vars_)
        x = RB.build_cat(name, units, full, None)
        x = x.replace('gameSystemRevision="1"', 'gameSystemRevision="7"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Chariot Wars army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        for u in units: cats.add(u['cat'])
        variants[fn] = [{'name': f'Chariot Wars: {vn}', 'limits': {c: {k: v} for c, (k, v) in lim.items()}} for vn, lim, txt in vars_]
        print('wrote', fn, len(units), 'units,', len(vars_), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    # categories and rules (patch_gst adds missing categories and rules; forces are rebuilt by collapse_forces from variants.json)
    RB.patch_gst(gst, [(f'CW {n}', u, {}) for n, u, v, nt, fn in LISTS], rules)
    s = open(gst, encoding='utf8').read()
    s = re.sub(r'  <forceEntries>(.*?)</forceEntries>', lambda m: m.group(0), s, flags=re.S)
    open(gst, 'w', encoding='utf8').write(s)

if __name__ == '__main__':
    main()
