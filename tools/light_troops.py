#!/usr/bin/env python3
"""Link the 'Light Troops' special rule (rulebook p.108: light infantry and light cavalry fight as skirmishers or open order) to every unit of the
official lists whose army-list text says Light Infantry / Light Cavalry (and the units named Light Cavalry). Usage: python3 light_troops.py <outdir> (idempotent)"""
import sys, os, re, glob, hashlib, html
OUT = sys.argv[1]
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
RID = '5be5-5832-c8fb-3a19'
OFFICIAL = ['Barbarian_Army_List', 'Roman_Army_List', 'Carthaginian_Hannibal', 'Republican_Roman_Hannibal', 'Spanish_Hannibal', 'Numidian_Hannibal', 'Ligurian_Hannibal', 'Gallic_Hannibal',
            'Sumerian_Akkadian_Chariot_Wars', 'Egyptian_New_Kingdom_Chariot_Wars', 'Hammurabic_Babylonian_Chariot_Wars', 'Hittite_Chariot_Wars', 'Trojan_War_Chariot_Wars', 'Israelite_Chariot_Wars', 'Assyrian_Chariot_Wars',
            'Late_Roman_Fall_of_the_West', 'Late_Barbarian_Fall_of_the_West', 'Warlord_Fall_of_the_West',
            'Sumerian_Armies_of_Antiquity', 'Egyptian_Armies_of_Antiquity', 'Hittite_Armies_of_Antiquity', 'Trojan_War_Armies_of_Antiquity', 'Assyrian_Armies_of_Antiquity', 'Persian_Armies_of_Antiquity', 'Greek_Armies_of_Antiquity', 'Rise_of_Macedon_Alexander', 'Alexandrian_Imperial_Alexander', 'Greek_Mercenaries_Alexander', 'Thracians_Alexander', 'Illyrians_Alexander', 'End_of_Persia_Alexander', 'Slave_Revolt_Spartacus', 'Late_Republican_Roman_Spartacus', 'Sicilian_Slave_Revolt_Spartacus', 'Early_Byzantines_Byzantium', 'Sassanid_Persians_Byzantium', 'Germanic_Kingdoms_Byzantium', 'Steppe_Nomads_Byzantium', 'Bulgars_and_Slavs_Byzantium', 'Early_Caliphates_Byzantium', 'Thematic_Byzantines_Byzantium', 'Rus_Byzantium', 'Late_Byzantines_Byzantium', 'Kingdom_of_Hungary_Vlad', 'Moldavia_and_Walachia_Vlad', 'Ottomans_Vlad', 'Serbia_Vlad', 'Return_of_the_Bulgars_Vlad', 'Albania_Vlad', 'Byzantine_Empire_Vlad', 'Achaian_Franks_Vlad', 'Catalan_Company_Vlad', 'Frontier_Horsemen_Alexander', 'Indian_Alexander', 'Alexander_Successors_Armies_of_Antiquity', 'Indian_Armies_of_Antiquity', 'Republican_Roman_Armies_of_Antiquity', 'Carthaginian_Armies_of_Antiquity', 'Late_Roman_Armies_of_Antiquity', 'Cataphract_Armies_of_Antiquity', 'Nomadic_Hordes_Armies_of_Antiquity', 'Byzantine_Armies_of_Antiquity', 'Arabs_and_Saracens_Armies_of_Antiquity', 'Saxon_Armies_of_Antiquity', 'Viking_Armies_of_Antiquity', 'Normans_Armies_of_Antiquity', 'Crusaders_Armies_of_Antiquity', 'Ancient_Chinese_Armies_of_Antiquity', 'Samurai_Armies_of_Antiquity', 'Northmen_Shieldwall', 'English_Shieldwall', 'Caledonians_Shieldwall', 'Welsh_Shieldwall', 'Hibernians_Shieldwall', 'Western_Franks_Shieldwall', 'Christian_Spain_El_Cid', 'Al_Andalus_El_Cid', 'African_Invaders_El_Cid', 'Romano_British_Civitates_Arthur', 'Romano_British_Vortigern_Arthur', 'British_Welsh_Kingdoms_Arthur', 'Saxon_Sea_Raiders_Arthur', 'Saxon_Early_Anglo_Saxon_Arthur', 'Saxon_Kingdoms_Heptarchy_Arthur', 'Saxon_Anglian_Kingdoms_Arthur', 'Franks_Early_Merovingian_Arthur', 'Picts_Arthur', 'Scots_Irish_Arthur']
SKIP = {'Numidian Elephant'}        # "escorts (Light Infantry)" refers to the escorts, not the elephant
total = 0
for fn in OFFICIAL:
    path = os.path.join(OUT, fn + '.cat')
    if not os.path.exists(path): continue
    s = open(path, encoding='utf8').read(); n = 0
    def f(m):
        global total
        nonlocal_n[0] += 0
        blk = m.group(0); name = html.unescape(m.group(2))
        if name in SKIP or RID in blk: return blk
        notes = ' '.join(html.unescape(x) for x in re.findall(r'name="Equipment and options[^"]*"[^>]*>.*?<characteristic[^>]*>(.*?)</characteristic>', blk, re.S))
        if not (re.search(r'Light (Cavalry|Infantry)\b', notes) or re.fullmatch(r'Light Cavalry', name)): return blk
        link = f'        <infoLink id="{hid(m.group(1), "light-troops")}" name="Light Troops" hidden="false" targetId="{RID}" type="rule"/>\n'
        mm = re.search(r'^      <infoLinks>\n', blk, re.M)
        total += 1; nonlocal_n[0] += 1
        if mm: return blk[:mm.end()] + link + blk[mm.end():]
        cl = re.search(r'^      <categoryLinks>\n', blk, re.M)       # unit without any unit-level link: add the block before the category links
        return blk[:cl.start()] + '      <infoLinks>\n' + link + '      </infoLinks>\n' + blk[cl.start():]
    nonlocal_n = [0]
    s2 = re.sub(r'    <selectionEntry id="([^"]*)" name="([^"]*)"[^>]*type="unit">\n.*?\n    </selectionEntry>\n', f, s, flags=re.S)
    if s2 != s:
        s2 = re.sub(r' revision="(\d+)" battleScribeVersion', lambda mm: f' revision="{int(mm.group(1)) + 1}" battleScribeVersion', s2, count=1)
        open(path, 'w', encoding='utf8').write(s2)
print('Light Troops linked to', total, 'units')
