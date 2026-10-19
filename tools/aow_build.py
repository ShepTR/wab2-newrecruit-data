#!/usr/bin/env python3
"""Add The Art of War (Warhammer Historical, 2006) army lists. Book page = printed page number.
Usage: python3 aow_build.py <outdir>   (then sh tools/aow_all.sh <outdir>)."""
import sys, os, re, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import rb_build as RB
import cw_build as CW
import aow_data as D
import aow_rules as AR
B = RB.B
hid = B.hid
OUT = RB.OUT
SPUB = hid('pub', 'artofwar')
REV = '17'
CW.DROP_WEAPONS.update({'Horse', 'Warhorse'})
CW.WEAPON_MAP.update({'Javelins': 'Javelin', 'Compound Bow': 'Bow', 'Repeat Crossbow': 'Repeating Crossbow', 'Barding': 'Full Metal Barding', 'Rocks': 'Rocks'})
RULE_MAP = {'Army General': 'Army General (Chariot Wars)'}
def R(page, txt): return ('The Art of War ' + page, txt)

RULES = dict(AR.RULES)
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
    RB.PUB = SPUB; RB.SRC = 'The Art of War'
    gst = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
    s = open(gst, encoding='utf8').read()
    if f'id="{SPUB}"' not in s:
        s = s.replace('  </publications>', f'    <publication id="{SPUB}" name="The Art of War" shortName="AW" publisher="Warhammer Historical Wargames" publicationDate="2006"/>\n  </publications>', 1)
    s = re.sub(r'gameSystemRevision="\d+"', f'gameSystemRevision="{REV}"', s, count=1) if 'gameSystemRevision' in s else s
    s = re.sub(r'(<gameSystem [^>]*?)revision="\d+"', lambda m: m.group(1) + f'revision="{REV}"', s, count=1)
    # new shared weapon / armour profiles used by the Art of War
    PROFS = [
     ('Noble Sword', 'p.6', '89ad-db9d-72f5-90d2', [('fa7e-7b3b-c328-7b67', 'Nobles and other notables may have a specially forged sword, usually of extraordinary length and beauty. It confers a +1 Strength bonus on all hits.')]),
     ('Repeating Crossbow', 'p.6', '5de1-764d-a40b-f6b5', [('6962-86a7-af53-83bb', '24"'), ('e237-5c6b-65a3-8bf7', '3'), ('b819-8576-7e60-dba3', '-'), ('6282-7884-5061-ecf1', 'A crossbow with a feed magazine on top for the bolts. Fires twice per turn with a -1 To Hit roll. May be used as a Last Ditch Weapon (stand & fire charge reaction even if the charging unit is within half distance; the unit may use no other close combat weapon except hand weapons after firing). Strength is not printed in the book; treated as 3.')]),
     ('Rocks', 'p.110', '5de1-764d-a40b-f6b5', [('6962-86a7-af53-83bb', '4"'), ('e237-5c6b-65a3-8bf7', '3'), ('b819-8576-7e60-dba3', '-'), ('6282-7884-5061-ecf1', 'Thrown rocks and farm implements (Peasants, Tribespeople).')]),
     ('Lamellar Armour', 'p.6', '96b5-bd5f-9a95-1bd7', [('80cf-4b2c-fa74-7e4d', '5 or 6'), ('227d-844c-2992-a59b', '4, 5 or 6'), ('85c2-9874-4f90-9229', 'Generals and other notable leaders may have increased protection, considered to be lamellar armour, which provides the wearer with a 5+ armour save but counts as light armour for the purposes of movement penalties.')]),
    ]
    TN = {'89ad-db9d-72f5-90d2': 'Hand-to-Hand Weapon', '5de1-764d-a40b-f6b5': 'Missile Weapon', '96b5-bd5f-9a95-1bd7': 'Armour'}
    CN = {'fa7e-7b3b-c328-7b67': 'Effects', '6962-86a7-af53-83bb': 'Range', 'e237-5c6b-65a3-8bf7': 'Strength', 'b819-8576-7e60-dba3': 'Save Modifier', '6282-7884-5061-ecf1': 'Notes', '80cf-4b2c-fa74-7e4d': 'Infantry Save', '227d-844c-2992-a59b': 'Cavalry Save', '85c2-9874-4f90-9229': 'Notes'}
    add = ''
    for pn, pg, ty, chs in PROFS:
        if f'id="{hid("prof", pn)}"' in s: continue
        add += f'    <profile id="{hid("prof", pn)}" name="{pn}" publicationId="{SPUB}" page="{pg}" hidden="false" typeId="{ty}" typeName="{TN[ty]}">\n      <characteristics>\n'
        add += ''.join(f'        <characteristic name="{CN[c]}" typeId="{c}">{RB.t(v)}</characteristic>\n' for c, v in chs)
        add += '      </characteristics>\n    </profile>\n\n'
    if add: s = s.replace('  </sharedProfiles>', add + '  </sharedProfiles>', 1)
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
        first['models'][0]['rules'].append('The Art of War Common Rules')
        x = RB.build_cat(name, units, notes + '\n\n' + comp_text(vs), None)
        x = x.replace('gameSystemRevision="1"', f'gameSystemRevision="{REV}"').replace('from the Warhammer Ancient Battles 2nd Edition rulebook army list.', 'from the Art of War army list book (Warhammer Historical).')
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(x)
        variants[fn] = [{'name': vn, 'limits': lim} for vn, lim, txt in vs]
        print('wrote', fn, len(units), 'units,', len(vs), 'compositions')
    json.dump(variants, open(cache, 'w', encoding='utf8'), indent=1)
    RB.patch_gst(gst, [(f'AW {n}', u, {}) for k, n, fn, u, v, nt in D.LISTS], dict(RULES))

if __name__ == '__main__':
    main()
