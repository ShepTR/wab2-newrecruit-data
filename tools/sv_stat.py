#!/usr/bin/env python3
"""Copies the armour save into the Model stat line as 'Sv' (after Ld).
The value and its equipment modifiers are copied from the model's Armour Save profile (equip_save.py); models without one get '-'.
Usage: python3 sv_stat.py <outdir>   (idempotent; run after equip_save.py / mount_profiles.py)"""
import sys, os, re, glob, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
MODEL_T = 'a802-40b5-d980-cabc'; LD = 'b6d1-0987-3a4d-d6a9'
SV = hid('ctype', 'Sv'); PT = hid('ptype', 'Armour Save'); SAVE = hid('ctype', 'Save')
GST = os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst')
g = open(GST, encoding='utf8').read()
if f'id="{SV}"' not in g:
    g = g.replace(f'        <characteristicType id="{LD}" name="Ld"/>\n', f'        <characteristicType id="{LD}" name="Ld"/>\n        <characteristicType id="{SV}" name="Sv"/>\n', 1)
    open(GST, 'w', encoding='utf8').write(g)
LDRX = re.compile(r'( *)(<characteristic name="Ld" typeId="' + LD + r'">[^<]*</characteristic>\n)')
PRX = re.compile(r'( *<profile id="[^"]*" name="[^"]*"[^>]*typeId="' + MODEL_T + r'"[^>]*>\n)(.*?)( *</profile>\n)', re.S)
def add_sv(prof_m, value, mods):
    head, inner, tail = prof_m.group(1), prof_m.group(2), prof_m.group(3)
    if f'name="Sv"' in inner: return prof_m.group(0)
    inner = LDRX.sub(lambda k: k.group(1) + k.group(2) + f'{k.group(1)}<characteristic name="Sv" typeId="{SV}">{value}</characteristic>\n', inner, count=1)
    if mods:
        mx = '                <!-- sv-stat -->\n' + mods
        if '<modifiers>\n' in inner:
            inner = re.sub(r'( *<modifiers>\n)', lambda k: k.group(1) + mx, inner, count=1)
        else:
            inner += '              <modifiers>\n' + mx + '              </modifiers>\n'
    return head + inner + tail
n_save = n_dash = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); orig = s
    def do_model(mm):
        global n_save
        blk = mm.group(0)
        ap = re.search(r' *<profile id="[^"]*" name="Armour Save"[^>]*typeId="' + PT + r'"[^>]*>.*?</profile>\n', blk, re.S)
        if not ap: return blk
        val = re.search(r'<characteristic name="Save" typeId="' + SAVE + r'">([^<]*)</characteristic>', ap.group(0)).group(1)
        mods = ''.join(re.sub(r'field="' + SAVE + '"', f'field="{SV}"', m.group(0)) + '\n' for m in re.finditer(r' *<modifier type="set" field="' + SAVE + r'" value="[^"]*">\n.*?</modifier>', ap.group(0), re.S))
        pm = PRX.search(blk)
        if not pm or 'name="Sv"' in pm.group(0): return blk
        n_save += 1
        return blk.replace(pm.group(0), add_sv(pm, val, mods), 1)
    s = re.sub(r'^        <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="model">\n.*?\n        </selectionEntry>\n', do_model, s, flags=re.S | re.M)
    def rest(pm):
        global n_dash
        if 'name="Sv"' in pm.group(0): return pm.group(0)
        n_dash += 1
        return add_sv(pm, '-', '')
    s = PRX.sub(rest, s)
    if s != orig: open(path, 'w', encoding='utf8').write(s)
print('Sv added: %d models with a save, %d without' % (n_save, n_dash))
