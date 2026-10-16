import sys, glob, os, re, collections
import xml.etree.ElementTree as ET
d = sys.argv[1]
files = sorted(glob.glob(os.path.join(d,'*.gst'))+glob.glob(os.path.join(d,'*.cat')))
ids = collections.Counter(); targets = []; ok = True
allids = set()
trees = {}
for f in files:
    try: tr = ET.parse(f)
    except Exception as e: print('XML ERROR', f, e); ok = False; continue
    trees[f] = tr
    for el in tr.iter():
        i = el.get('id')
        if i: ids[i] += 1; allids.add(i)
        if el.tag.endswith('}infoLink') or el.tag.endswith('}categoryLink') or el.tag.endswith('}entryLink'):
            targets.append((os.path.basename(f), el.tag.split('}')[1], el.get('name'), el.get('targetId')))
dups = [i for i,c in ids.items() if c>1]
print('files:', len(files), '| elements with ids:', sum(ids.values()), '| duplicate ids:', len(dups))
bad = [t for t in targets if t[3] not in allids]
print('links:', len(targets), '| unresolved:', len(bad))
for b in bad[:20]: print('  UNRESOLVED', b)
ns = {'c':'http://www.battlescribe.net/schema/catalogueSchema'}
for f,tr in trees.items():
    if f.endswith('.cat'):
        r = tr.getroot()
        units = r.findall('.//c:selectionEntry[@type="unit"]', ns)
        models = r.findall('.//c:selectionEntry[@type="model"]', ns)
        opts = r.findall('.//c:selectionEntry[@type="upgrade"]', ns)
        print(f'{os.path.basename(f)}: {len(units)} units, {len(models)} model entries, {len(opts)} option entries')
print('PASS' if ok and not dups and not bad else 'FAIL')
