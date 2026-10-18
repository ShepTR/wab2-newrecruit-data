#!/usr/bin/env python3
"""Add the Spartacus (Warhammer Historical, 2008) army lists: Spartacus's Slave Revolt, Late Republican Roman Consular Army and Sicilian Slave Revolt. Book page = printed page number.
Usage: python3 sp_build.py <outdir>   (then sh tools/sp_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import sp_data as D
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'spartacus')
REV = '13'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Pilum': 'Heavy Throwing Spear', 'Longbow': 'Long Bow', 'Javelins': 'Javelin', 'Two-handed Weapon': 'Double-handed Weapon'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)',
            'Open Order (if no heavy armour)': 'Open Order', 'Open Order (if not combined or mixed)': 'Open Order', 'Open Order (if not in Mixed Order)': 'Open Order', 'Open Order (when not in Mixed Order)': 'Open Order',
            'Medieval Phalanx (if not in Combined Formation)': 'Medieval Phalanx', 'Eastern Shock Cavalry (if heavy armour)': 'Eastern Shock Cavalry'}
def R(page, txt): return ('Spartacus ' + page, txt)
RULES = {
 'Spartacus Common Rules': R('pp.12-17', 'The minimum size of a unit is five models; there is no upper limit. One model in each unit may be upgraded to a Leader (+5 pts), Standard Bearer (+5 pts) and Musician (+5 pts) unless mentioned otherwise. Where a unit is armed with mixed weapons, the Mixed Weapons rule of the WAB rulebook applies (page 127); Improvised Weapons are on page 45. Percentages are by points. The Army Standard Bearer follows the Roman Army Standard rules (WAB rulebook page 119).'),
 'Hates Romans': R('p.12', 'Where this special rule is noted, the unit or character is subject to the Hatred rules sections 2 and 3 but not 1 (ie, re-roll misses in the first round of combat and must pursue towards the Roman units).'),
 'Looting': R('p.12', 'In the event of a Slave unit catching and destroying a fleeing Roman unit better equipped with shields and weapons than them, they may take the opportunity to loot the bodies and continue the battle using that equipment instead. Should the Slave unit subsequently flee for any reason, they lose this bonus equipment and revert to their original equipment options. The looting does not include armour.'),
 "I'm Spartacus!": R('p.13', 'If Spartacus is in a unit and should lose his final wound, then on a 4+ he is not really dead - he may be exchanged with another model in the unit and is left with one wound. If Spartacus is not in a unit and loses his final wound, or is killed/ran down due to pursuit, then on a roll of 6 he is not really dead but replaces the nearest friendly model and is left with one wound remaining.'),
 'All is lost!': R('p.13', 'If Spartacus is finally killed, then Spartacus\'s entire army has to carry out a Leadership test with -1 to their Ld.'),
 "We'll take care of the rear!": R('p.13', 'Units with this special rule must be deployed together as the last units (prior to any character placement) to the rear of the army.'),
 'Different Equipment': R('p.13', 'Unlike other units, separate Gladiator models may be armed and equipped differently within the unit, including the Toughness option (use a particularly large model). Gladiators may be deployed as a single unit of Light Infantry (at least five models, no Leader, Musician or Standard) or included in other units to a maximum of two per unit; if deployed in other units they are subject to that unit\'s Leadership and psychology and may not leave. If joined by Spartacus the unit is immune to panic, fear and terror and may use his Leadership even in skirmish order. Victory points are gained for each Gladiator killed.'),
 'Skirmishers (Spartacus)': R('p.14', 'Skirmishers: see the WAB rulebook (pages 54-56).'),
 'Bolt Thrower (Spartacus)': R('p.14', 'Bolt Thrower - see WAB rulebook: range 36", Strength 4/-1 per rank, no save, D3 wounds per hit. Crew of two or three men.'),
 'Fiery Rollers': R('p.14', 'Nominate one formed unit with the rollers at the start of the game and place two rollers or suitable markers along the unit\'s front facing; while it has the rollers it causes fear in its frontal facing. The unit can only move in open terrain. In its Shooting phase it may \'shoot\' one or both rollers at an enemy unit: 3D6" if on higher ground, 2D6" on level ground, over clear ground. A roller reaching the enemy causes D6 Strength 4 hits with no armour save; Drilled units and units in skirmish formation may take a test with -1 to their Ld to avoid each roller. If the unit is charged to its front or charges, each roller causes D6 S4 hits on the enemy unit. Wounds do not count towards combat resolution but may cause a Panic test if 25% casualties are caused. The rollers can only be used once.'),
 'Fasces': R('p.15', 'The Lictor carries the Fasces, which allows the Consul the following options once per Lictor during the game: (1) re-roll any Roman Leadership test once within 12" of the Consul, OR (2) add +1 to any Roman combat resolution once within 12" of the Consul. Lictors may be captured in the same way as a unit standard or killed in hand-to-hand combat; either way each is worth an additional 200 Victory points.'),
 'Reputation': R('p.16', 'At the start of the game Crassus may remove one legionary in ten (removed equally as possible across all legionary units, rounding to the nearest ten). This allows all Roman Legionary units to re-roll failed Panic tests and, should a legion break and be caught from combat, the slaves cannot loot its equipment. Once a re-rolled Panic test is also failed both benefits are lost. You may re-roll a failed test using the Lictor if it is that desperate.'),
 'Wealthy': R('p.16', 'At the start of the game Crassus may nominate and upgrade one Legionary unit to become Drilled and Stubborn at no additional points cost.'),
}
FIRSTCHAR = None
def comp_text(variants):
    out = ['ARMY COMPOSITIONS (pick one in the Army composition list):'] if len(variants) > 1 else ['ARMY COMPOSITION:']
    for vn, lim, txt in variants:
        out.append(f'[{vn.split(": ", 1)[-1]}]')
        for c, d in lim.items():
            out.append(f"  {c}: " + ', '.join(('at least' if k == 'min' else 'up to') + f' {v}%' for k, v in sorted(d.items())))
        out.append('  ' + txt)
    return '\n'.join(out)

def main():
    RB.PUB = SPUB; RB.SRC = 'Spartacus'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="Spartacus" shortName="SP" publisher="Warhammer Historical Wargames" publicationDate="2008"/>\n  </publications>', 1)
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
        first = units[0]
        first['models'][0]['rules'].append('Spartacus Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Spartacus army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'SP {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
