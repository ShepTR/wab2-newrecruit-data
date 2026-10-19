#!/usr/bin/env python3
"""Units that may mix spearmen and bowmen inside one unit (bowmen may not outnumber spearmen) get two model entries instead of a unit-wide bow checkbox:
  <unit> (spear)  -- min 5 in total (5 minus the bowmen), the original equipment
  <unit> (bow)    -- composite bow instead of thrusting spear and shield (price adjusted), at most as many as the spear model
Units: Polk, Smerd (Russian AoA2), Foot soldier (Carolingian AoA2).   Usage: python3 mix_models.py <outdir>   (idempotent)"""
import sys, os, re, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
SPEC = [('Russian_AoA2.cat', 'Polk'), ('Russian_AoA2.cat', 'Smerd'), ('Carolingian_AoA2.cat', 'Foot soldier')]
def rep(child, per=1):
    return (f'<repeat field="selections" scope="parent" value="{per}" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" repeats="1" roundUp="false"/>')
n = 0
for fn, uname in SPEC:
    path = os.path.join(OUT, fn); s = open(path, encoding='utf8').read()
    um = re.search(r'^    <selectionEntry id="([^"]*)" name="%s"[^>]*type="unit">\n.*?\n    </selectionEntry>\n' % re.escape(uname), s, re.S | re.M)
    U = um.group(0); uid = um.group(1)
    if '<!-- mix-split -->' in U: continue
    mm = re.search(r'^        <selectionEntry id="([^"]*)" name="%s"[^>]*type="model">\n.*?\n        </selectionEntry>\n' % re.escape(uname), U, re.S | re.M)
    M = mm.group(0); sid = mm.group(1)
    om = re.search(r'^        <selectionEntry id="([^"]*)" name="Composite bow"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n', U, re.S | re.M)
    O = om.group(0)
    delta = float(re.search(r'<modifier type="increment" field="points" value="(-?[0-9.]+)"', O).group(1))
    delta = int(delta) if delta == int(delta) else delta
    bid = hid(sid, 'bow-model')
    # ---- bow model: clone of the spear model
    B = M
    B = re.sub(r'(\bid=")([0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4})(")', lambda k: k.group(1) + hid(k.group(2), 'bow') + k.group(3), B)
    B = B.replace(f'id="{hid(sid, "bow")}"', f'id="{bid}"')                                  # (never matches; the entry id is set below)
    B = re.sub(r'^(        <selectionEntry id=")[^"]*(" name=")%s(")' % re.escape(uname), lambda k: k.group(1) + bid + k.group(2) + f'{uname} (bow)' + k.group(3), B, count=1, flags=re.M)
    B = re.sub(r'(<profile id="[^"]*" name=")%s(" [^>]*typeName="Model">)' % re.escape(uname), lambda k: k.group(1) + f'{uname} (bow)' + k.group(2), B, count=1)
    base = float(re.search(r'<cost name="pts" typeId="points" value="(-?[0-9.]+)"', B).group(1)); newp = base + delta
    B = re.sub(r'(<cost name="pts" typeId="points" value=")[^"]*(")', lambda k: k.group(1) + (str(int(newp)) if newp == int(newp) else str(newp)) + k.group(2), B, count=1)
    for lab in ('Thrusting Spear', 'Shield', 'Double-handed Weapon'):                       # no spear / shield / two-hander for bowmen
        B = re.sub(r' *<infoLink id="[^"]*" name="%s"[^>]*?(?:/>|>.*?</infoLink>)\n' % lab, '', B, flags=re.S)
    def bowlink(k):                                                                         # the bow profile is always shown on the bow model
        x = re.sub(r' hidden="true"', ' hidden="false"', k.group(0), count=1)
        return re.sub(r'\n *<modifiers>.*?</modifiers>\n( *)</infoLink>', r'\n\1</infoLink>', x, flags=re.S).replace('>\n' + ' ' * 12 + '</infoLink>', '/>') if False else re.sub(r'>\n *<modifiers>.*?</modifiers>\n *</infoLink>', '/>', x, flags=re.S)
    B = re.sub(r' *<infoLink id="[^"]*" name="Bow" hidden="true"[^>]*>.*?</infoLink>\n', lambda k: '            ' + bowlink(k).lstrip() + '\n', B, flags=re.S)
    B = re.sub(r'(<characteristic name="(?:Sv|Save)" typeId="[^"]*">)6\+(<)', r'\1-\2', B)       # no shield: no save from equipment
    B = B.replace('value="5+"', 'value="6+"')                                                  # light armour alone gives 6+
    B = B.replace('<constraints>\n', '<constraints>\n', 1)
    B = re.sub(r'<constraint field="selections" scope="parent" value="\d+"([^>]*?) id="([^"]*)" type="min"/>',
               lambda k: f'<constraint field="selections" scope="parent" value="0"{k.group(1)} id="{k.group(2)}" type="max"/>', B, count=1)
    bcid = re.search(r'<constraint [^>]*id="([^"]*)" type="max"/>', B).group(1)
    bmod = (f'          <!-- mix-split -->\n          <modifiers>\n            <modifier type="increment" field="{bcid}" value="1">\n              <repeats>\n                {rep(sid)}\n'
            f'              </repeats>\n            </modifier>\n          </modifiers>\n')
    B = B.replace('          </constraints>\n', '          </constraints>\n' + bmod, 1)
    # ---- spear model: renamed, min reduced by the bowmen
    S2 = re.sub(r'^(        <selectionEntry id="[^"]*" name=")%s(")' % re.escape(uname), lambda k: k.group(1) + f'{uname} (spear)' + k.group(2), M, count=1, flags=re.M)
    S2 = re.sub(r'(<profile id="[^"]*" name=")%s(" [^>]*typeName="Model">)' % re.escape(uname), lambda k: k.group(1) + f'{uname} (spear)' + k.group(2), S2, count=1)
    S2 = re.sub(r' *<infoLink id="[^"]*" name="Bow" hidden="true"[^>]*>.*?</infoLink>\n', '', S2, flags=re.S)   # bow now belongs to the bow model
    mcid = re.search(r'<constraint [^>]*id="([^"]*)" type="min"/>', S2).group(1)
    smod = (f'          <modifiers>\n            <modifier type="decrement" field="{mcid}" value="1">\n              <repeats>\n                {rep(bid)}\n'
            f'              </repeats>\n            </modifier>\n          </modifiers>\n')
    S2 = S2.replace('          </constraints>\n', '          </constraints>\n' + smod, 1)
    # ---- unit: drop the bow checkbox, add the bow model, per-model option costs also count the bowmen (except the two-hander)
    NU = U.replace(O, '', 1).replace(M, S2 + B, 1)
    def addrep(k):
        blk = k.group(0)
        if 'Double' in k.group(1) or f'childId="{sid}"' not in blk: return blk
        return blk.replace(rep(sid), rep(sid) + '\n                ' + rep(bid), 1)
    NU = re.sub(r'^        <selectionEntry id="[^"]*" name="([^"]*)"[^>]*type="upgrade">\n.*?\n        </selectionEntry>\n', addrep, NU, flags=re.S | re.M)
    s = s.replace(U, NU, 1); open(path, 'w', encoding='utf8').write(s); n += 1
print('mixed-weapon units split into spear and bow models:', n)
