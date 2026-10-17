#!/usr/bin/env python3
"""Adds a 'Warhorse' Model profile (M8 WS3 BS0 S3 T- W- I3 A1 Ld-; Hannibal p.7, rulebook p.175) to every Warhorse option, so the mount's
profile shows only when the Warhorse is chosen. An ordinary horse has no profile of its own: it only raises the rider's M to 8
(handled in equip_save.py). Usage: python3 mount_profiles.py <outdir>   (idempotent)"""
import sys, os, re, glob, hashlib
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
PT = 'a802-40b5-d980-cabc'
CH = [('M', '35a2-714d-db3e-3738', '8'), ('WS', 'bb04-2b70-ae79-3559', '3'), ('BS', 'ffff-54f0-d131-b6a9', '0'), ('S', '9e7c-6fc0-c50c-ee53', '3'),
      ('T', 'd226-f704-80f9-6e23', '-'), ('W', 'ce59-af10-7f37-4238', '-'), ('I', '8ec4-e9a6-0b8a-08aa', '3'), ('A', 'ee87-e286-4768-82be', '1'),
      ('Ld', 'b6d1-0987-3a4d-d6a9', '-')]
RX = re.compile(r'^( *)<selectionEntry id="([^"]*)" name="((?:Warhorse|Ride a warhorse|Mounted on a warhorse)[^"]*)"[^>]*type="upgrade">\n(.*?\n)( *)</selectionEntry>', re.M | re.S | re.I)
tot = 0
for path in sorted(glob.glob(os.path.join(OUT, '*.cat'))):
    s = open(path, encoding='utf8').read(); n = 0
    def f(m):
        global tot
        nonlocal_n[0] += 1
        body = m.group(4)
        if 'mount-profile' in body: return m.group(0)
        prof = (f'          <!-- mount-profile -->\n          <profiles>\n            <profile id="{hid(m.group(2), "mount")}" name="Warhorse" hidden="false" typeId="{PT}" typeName="Model">\n              <characteristics>\n' +
                ''.join(f'                <characteristic name="{n}" typeId="{t}">{v}</characteristic>\n' for n, t, v in CH) +
                '              </characteristics>\n            </profile>\n          </profiles>\n')
        key = '          <!-- def-link -->\n'
        if key not in body: raise SystemExit('no def-link in ' + m.group(3))
        tot += 1
        return m.group(0).replace(key, prof + key, 1)
    nonlocal_n = [0]
    s2 = RX.sub(f, s)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('warhorse profile added to', tot, 'options')
