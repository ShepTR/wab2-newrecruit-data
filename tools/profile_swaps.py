#!/usr/bin/env python3
"""When a unit-level equipment option is ticked, show/hide the matching weapon, armour and shield profile lines on the model:
'(replaces x)' / 'Exchange x for y' hide x's profile; the new item's profile is shown. Options with no matching shared profile are skipped.
Usage: python3 profile_swaps.py <outdir>   (idempotent)."""
import sys, os, re, glob, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
g = open(os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst'), encoding='utf8').read()
PROFILES = set(re.findall(r'<profile id="[^"]*" name="([^"]*)"', re.search(r'<sharedProfiles>(.*?)</sharedProfiles>', g, re.S).group(1)))
MAP = {'javelins': 'Javelin', 'javelin': 'Javelin', 'light armour': 'Light Armour', 'light': 'Light Armour', 'heavy armour': 'Heavy Armour',
       'shield': 'Shield', 'large shield': 'Large Shield', 'buckler': 'Buckler', 'thrusting spear': 'Thrusting Spear',
       'throwing spear': 'Throwing Spear', 'heavy throwing spear': 'Heavy Throwing Spear', 'pilum': 'Heavy Throwing Spear',
       'sling': 'Sling', 'composite bow': 'Bow', 'bow': 'Bow', 'cataphract armour': 'Cataphract Armour',
       'full plate armour': 'Full Plate Armour', 'kontos': 'Kontos', 'halberd': 'Halberd', 'double handed weapon': 'Double-handed Weapon',
       'light crossbow': 'Light Crossbow', 'hand-and-a half sword': 'Halberd'}
def norm(t):
    t = t.strip().lower()
    return MAP.get(t)
def parse(label):
    l = label.lower().replace('&amp;', '&')
    add, rem = [], []
    m = re.match(r'exchange (.+?) for (?:a |an )?(.+)$', l)
    if m:
        for t in re.split(r' and ', m.group(1)): rem.append(norm(t))
        add.append(norm(re.sub(r'\s*\(.*', '', m.group(2))))
    else:
        r = re.search(r'replaces ([a-z ]+?)[;)]', l)
        if r: rem.append(norm(r.group(1)))
        head = re.sub(r'\s*\(.*', '', l)
        for t in re.split(r' and ', head): add.append(norm(t))
    return [a for a in add if a and a in PROFILES], [x for x in rem if x and x in PROFILES]
def cond(uid, oid):
    return (f'<condition field="selections" scope="{uid}" value="1" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{oid}" type="atLeast"/>')
done = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read()
    def do_unit(m):
        global done
        blk = m.group(0)
        if 'profile-swap' in blk or 'name="Characters"' in blk.split('<selectionEntries>')[0]: return blk
        uid = re.match(r'    <selectionEntry id="([^"]*)"', blk).group(1)
        opts = re.findall(r'^        <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="upgrade"', blk, re.M)
        models = [mm.group(0) for mm in re.finditer(r'        <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="model">\n.*?\n        </selectionEntry>\n', blk, flags=re.S)]
        if not models: return blk
        newblk = blk
        for mblk in models:
            mid = re.match(r'        <selectionEntry id="([^"]*)"', mblk).group(1)
            m2 = mblk
            adds = ''
            for oid, oname in opts:
                add, rem = parse(oname)
                if not add and not rem: continue
                # an option that repeats on a specific model belongs to that model only
                ob = re.search(r'<selectionEntry id="' + oid + r'".*?\n        </selectionEntry>\n', blk, re.S).group(0)
                rep = re.search(r'childId="([^"]*)" repeats', ob)
                if rep and rep.group(1) != mid: continue
                for rname in rem:
                    pat = re.compile(r'(            <infoLink id="[^"]*" name="' + re.escape(rname) + r'" hidden="false" targetId="[^"]*" type="profile")/>\n')
                    mod = (f'>\n              <modifiers>\n                <!-- profile-swap -->\n                <modifier type="set" field="hidden" value="true">\n                  <conditions>\n                    {cond(uid, oid)}\n'
                           f'                  </conditions>\n                </modifier>\n              </modifiers>\n            </infoLink>\n')
                    m2, n = pat.subn(lambda x: x.group(1) + mod, m2, count=1)
                for aname in add:
                    if re.search(r'name="' + re.escape(aname) + r'" hidden="(false|true)" targetId', m2): continue
                    adds += (f'            <infoLink id="{hid(mid, "swap", oid, aname)}" name="{aname}" hidden="true" targetId="{hid("prof", aname)}" type="profile">\n'
                             f'              <modifiers>\n                <!-- profile-swap -->\n                <modifier type="set" field="hidden" value="false">\n                  <conditions>\n                    {cond(uid, oid)}\n'
                             f'                  </conditions>\n                </modifier>\n              </modifiers>\n            </infoLink>\n')
            if adds:
                if '          </infoLinks>\n' in m2: m2 = m2.replace('          </infoLinks>\n', adds + '          </infoLinks>\n', 1)
                else: m2 = m2.replace('          <costs>', '          <infoLinks>\n' + adds + '          </infoLinks>\n          <costs>', 1)
            if m2 != mblk:
                newblk = newblk.replace(mblk, m2, 1); done += 1
        return newblk
    s2 = re.sub(r'    <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', do_unit, s, flags=re.S)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda m: f' revision="{int(m.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('profile swaps added to', done, 'model entries')
