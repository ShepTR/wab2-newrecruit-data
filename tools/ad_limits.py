#!/usr/bin/env python3
"""Alexander the Great: availability limits and per-composition changes (helpers in limlib.py).
 - AVAIL / UNAV: a unit is only available (or not available) in the listed army compositions (picker conditions)
 - OPTAV: an option is hidden unless one of the listed compositions is chosen;  OPTRULE: an option links a rule that shows when it is chosen
 - COSTV / STATV / OPTSTAT: points cost or a characteristic changes in a composition / when an option is chosen
 - RATIOS, PAIRS (0-1 across units), HIRDMEN_LE_BONDIR (no more units of Hirdmen than Bondir), OPT_ONCE (an option once per army)
Usage: python3 el_limits.py <outdir>   (run after the post-processing scripts; idempotent)"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from limlib import *
import ad_data as D

GST = open(os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst'), encoding='utf8').read()
def rule_id(name):
    m = re.search(r'<rule id="([^"]*)" name="%s"' % re.escape(name.replace('&', '&amp;')), GST)
    if not m: raise SystemExit('no rule ' + name)
    return m.group(1)
CT = {'M': '35a2-714d-db3e-3738', 'WS': 'bb04-2b70-ae79-3559', 'BS': 'ffff-54f0-d131-b6a9', 'S': '9e7c-6fc0-c50c-ee53', 'T': 'd226-f704-80f9-6e23',
      'W': 'ce59-af10-7f37-4238', 'I': '8ec4-e9a6-0b8a-08aa', 'A': 'ee87-e286-4768-82be', 'Ld': 'b6d1-0987-3a4d-d6a9'}
def pids(cat, key, names): return [cat.vid(D.VAR[key][n]) for n in names]
def cond_sel(scope, child):
    return (f'<condition field="selections" scope="{scope}" value="1" percentValue="false" shared="true" includeChildSelections="false" '
            f'includeChildForces="false" childId="{child}" type="atLeast"/>')

def opt_block(cat, unit, label):
    uid, mid, m = cat.unit(unit)
    mm = re.search(r'^( *)<selectionEntry id="([^"]*)" name="%s"[^>]*type="upgrade">\n.*?\n\1</selectionEntry>\n' % re.escape(label.replace('&', '&amp;')), m.group(0), re.S | re.M)
    if not mm: raise SystemExit(f'{cat.fn}: no option "{label}" in {unit}')
    return uid, mm
def replace_opt(cat, old, new):
    cat.s = cat.s.replace(old, new, 1); cat.changed = True
def add_opt_modifier(blk, modxml):
    if re.search(r'^ *<modifiers>\n', blk, re.M):
        return re.sub(r'^( *<modifiers>\n)', lambda k: k.group(1) + modxml, blk, count=1, flags=re.M)
    return re.sub(r'^( *)(<!-- def-link -->|<rules>|<infoLinks>|<costs>)', lambda k: k.group(1) + '<modifiers>\n' + modxml + k.group(1) + '</modifiers>\n' + k.group(1) + k.group(2), blk, count=1, flags=re.M)

def opt_avail(cat, key, unit, label, variants):
    uid, mm = opt_block(cat, unit, label); blk = mm.group(0)
    if '<!-- sw-avail -->' in blk: return
    nb = blk.replace(' hidden="false"', ' hidden="true"', 1)
    mods = '<!-- sw-avail -->\n' + ''.join(f'<modifier type="set" field="hidden" value="false">\n<conditions>\n{cond(p, "atLeast")}\n</conditions>\n</modifier>\n' for p in pids(cat, key, variants))
    replace_opt(cat, blk, add_opt_modifier(nb, mods))

def opt_rule(cat, unit, label, rule):
    uid, mm = opt_block(cat, unit, label); blk = mm.group(0); oid = mm.group(2)
    if f'<!-- sw-rule-{rule} -->' in blk or f'targetId="{rule_id(rule)}"' in blk: return
    ind = mm.group(1) + '  '
    link = f'{ind}  <infoLink id="{hid(oid, "rule", rule)}" name="{rule}" hidden="false" targetId="{rule_id(rule)}" type="rule"/>\n'
    if re.search(r'^ *<infoLinks>\n', blk, re.M):
        nb = re.sub(r'^( *<infoLinks>\n)', lambda k: k.group(1) + link, blk, count=1, flags=re.M)
    else:
        nb = re.sub(r'^( *)(<rules>|<costs>)', lambda k: f'{ind}<infoLinks>\n{link}{ind}</infoLinks>\n' + k.group(1) + k.group(2), blk, count=1, flags=re.M)
    nb = nb.replace(f'{ind}<infoLinks>', f'{ind}<!-- sw-rule-{rule} -->\n{ind}<infoLinks>', 1) if '<!-- sw-rule' not in nb else nb
    replace_opt(cat, blk, nb)

def option_once(cat, pairs, tag):
    for unit, label in pairs:
        uid, mm = opt_block(cat, unit, label); blk, oid = mm.group(0), mm.group(2)
        cid = hid(oid, tag)
        if cid in blk: continue
        con = (f'<constraint field="selections" scope="roster" value="1" percentValue="false" shared="true" includeChildSelections="false" '
               f'includeChildForces="false" id="{cid}" type="max"/>\n')
        if '<constraints>\n' not in blk: raise SystemExit(f'{cat.fn}: no constraints in option {oid}')
        replace_opt(cat, blk, blk.replace('<constraints>\n', '<constraints>\n' + con, 1))

def model_block(cat, unit, model=None):
    uid, mid, m = cat.unit(unit)
    mm = re.search(r'^        <selectionEntry id="[^"]*" name="[^"]*"[^>]*type="model">\n.*?\n        </selectionEntry>\n', m.group(0), re.S | re.M)
    return uid, mm

def cost_variant(cat, key, unit, table, tag='swcost'):
    uid, mm = model_block(cat, unit); blk = mm.group(0)
    if f'<!-- {tag} -->' in blk: return
    mods = f'          <!-- {tag} -->\n' + ''.join(f'          <modifier type="set" field="points" value="{v}">\n            <conditions>\n              {cond(cat.vid(D.VAR[key][n]), "atLeast")}\n            </conditions>\n          </modifier>\n' for n, v in table.items())
    if re.search(r'^          <modifiers>\n', blk.split('<profiles>')[0], re.M):
        nb = blk.replace('          <modifiers>\n', '          <modifiers>\n' + mods, 1)
    else:
        nb = blk.replace('          </constraints>\n', '          </constraints>\n          <modifiers>\n' + mods + '          </modifiers>\n', 1)
    if nb == blk: raise SystemExit('could not add cost modifier to ' + unit)
    replace_opt(cat, blk, nb)

def stat_mod(cat, unit, stat, value, conds, tag):
    uid, mm = model_block(cat, unit); blk = mm.group(0)
    if f'<!-- {tag} -->' in blk: return
    pm = re.search(r'(            <profile id="[^"]*" name="[^"]*"[^>]*typeId="a802-40b5-d980-cabc"[^>]*>.*?)(            </profile>\n)', blk, re.S)
    mod_x = f'                <!-- {tag} -->\n                <modifier type="set" field="{CT[stat]}" value="{value}">\n                  <conditions>\n                    {conds}\n                  </conditions>\n                </modifier>\n'
    inner = pm.group(1)
    if '<modifiers>\n' in inner: inner = inner.replace('              <modifiers>\n', '              <modifiers>\n' + mod_x, 1)
    else: inner += '              <modifiers>\n' + mod_x + '              </modifiers>\n'
    replace_opt(cat, blk, blk.replace(pm.group(0), inner + pm.group(2), 1))

cats = {}
def C(key):
    fn = next(f for k, n, f, *_ in D.LISTS if k == key)
    if fn not in cats: cats[fn] = Cat(fn)
    return cats[fn]

for key, unit, vs in D.AVAIL:
    c = C(key); ps = pids(c, key, vs)
    c.add_unit_limit(unit, 'avail-sw', 'max', 0, lambda cid, ps=ps: [mod('set', cid, BIG, conds=[cond(p, 'atLeast')]) for p in ps])
for key, unit, vs in D.UNAV:
    c = C(key); ps = pids(c, key, vs)
    c.add_unit_limit(unit, 'unav-sw', 'max', BIG, lambda cid, ps=ps: [mod('set', cid, 0, conds=[cond(p, 'atLeast')]) for p in ps])
for key, names, tag in D.PAIRS: pair(C(key), names, tag)
for key, a, bs, per in D.RATIOS: ratio(C(key), a, bs, per)
for key, a, b, vs in D.HIRDMEN_LE_BONDIR:
    c = C(key); ps = pids(c, key, vs); ub = c.unit(b)[0]
    def mods(cid, ps=ps, ub=ub):
        return [mod('set', cid, 0, conds=[cond(p, 'atLeast')]) for p in ps] + [mod('increment', cid, 1, conds=[cond(p, 'atLeast')], repeat=(ub, 1, 'false')) for p in ps]
    c.add_unit_limit(a, 'hirdmen-le-bondir', 'max', BIG, mods)
for key, unit, label, vs in D.OPTAV: opt_avail(C(key), key, unit, label, vs)
for key, unit, label, rule in D.OPTRULE: opt_rule(C(key), unit, label, rule)
for key, pairs in D.OPT_ONCE: option_once(C(key), pairs, 'once-sw')
for key, unit, table in D.COSTV: cost_variant(C(key), key, unit, table)
for key, unit, stat, table in D.STATV:
    c = C(key)
    for n, v in table.items(): stat_mod(c, unit, stat, v, cond(c.vid(D.VAR[key][n]), 'atLeast'), f'swstat-{stat}-{n}')
for key, unit, label, stat, v in D.OPTSTAT:
    c = C(key); uid, mm = opt_block(c, unit, label)
    stat_mod(c, unit, stat, v, cond_sel(uid, mm.group(2)), f'swstat-{stat}-opt')
for key, unit, n, vs in D.UNIT_MAX_IN:
    c = C(key); ps = pids(c, key, vs)
    c.add_unit_limit(unit, 'ad-max-in', 'max', BIG, lambda cid, ps=ps, n=n: [mod('set', cid, n, conds=[cond(p, 'atLeast')]) for p in ps])
def opt_mods(cat, unit, label, tag, conds_list):
    uid, mm = opt_block(cat, unit, label); blk, oid = mm.group(0), mm.group(2)
    if f'<!-- {tag} -->' in blk: return
    cid = hid(oid, 'once-sw')
    mods = f'<!-- {tag} -->\n' + ''.join(f'<modifier type="set" field="{cid}" value="0">\n<conditions>\n{cd}\n</conditions>\n</modifier>\n' for cd in conds_list)
    replace_opt(cat, blk, add_opt_modifier(blk, mods))
for key, (inherent, opts) in D.GEN.items():
    c = C(key); oids = [(u, l, opt_block(c, u, l)[1].group(2)) for u, l in opts]; iids = [c.unit(n)[0] for n in inherent]
    for u, l, oid in oids:
        others = [o for _, _, o in oids if o != oid]
        opt_mods(c, u, l, 'ad-gen', [cond(x, 'atLeast') for x in others + iids])
    for n in inherent:
        c.add_unit_limit(n, 'ad-gen', 'max', BIG, lambda cid: [mod('set', cid, 0, conds=[cond(o, 'atLeast')]) for _, _, o in oids])
for key, unit, other, label in D.EXCL:
    c = C(key); oid = opt_block(c, other, label)[1].group(2); uid = c.unit(unit)[0]
    c.add_unit_limit(unit, 'ad-excl', 'max', BIG, lambda cid, oid=oid: [mod('set', cid, 0, conds=[cond(oid, 'atLeast')])])
    opt_mods(c, other, label, 'ad-excl', [cond(uid, 'atLeast')])
for c in cats.values(): c.save()
print('limits added')

