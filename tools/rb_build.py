#!/usr/bin/env python3
"""Add the WAB2 rulebook Roman and Barbarian army lists to an existing output folder.
Usage: python3 rb_build.py <outdir>   (run after build_wab2.py; patches the .gst and writes two .cat files)"""
import sys, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = sys.argv[1]
sys.argv = ['build_wab2.py', 'unused.docx', OUT]
import build_wab2 as B
import rb_data as RD
hid, q, t, PT, STATS = B.hid, B.q, B.t, B.PT, B.STATS
PUB = B.PUB_RB
SRC = 'rulebook'

def model_xml(uid, m, notes_txt, notes_rule, first):
    mid = hid(uid, m['key'])
    nm = m['name']
    x = f'        <selectionEntry id="{mid}" name={q(nm)} hidden="false" collective="false" import="true" type="model">\n          <constraints>\n'
    x += f'            {B.constraint("selections","parent",m["mn"],"min",hid(mid,"min"))}\n'
    if m['mx'] is not None:
        x += f'            {B.constraint("selections","parent",m["mx"],"max",hid(mid,"max"))}\n'
    x += '          </constraints>\n          <profiles>\n'
    st = [(s if s != '-' else '-') for s in m['stats']]
    x += B.profile_xml(hid(mid, 'prof'), nm, PT['Model'], 'Model', list(zip(STATS, st)), PUB, None, '            ')
    if first and notes_txt:
        x += B.profile_xml(hid(mid, 'notes'), 'Equipment and options (as printed in WAB2 army list)', PT['Equipment and Notes'],
                           'Equipment and Notes', [('Text', notes_txt)], PUB, None, '            ')
    x += '          </profiles>\n'
    links = [f'<infoLink id="{hid(mid,"r",rn)}" name={q(rn)} hidden="false" targetId="{hid("rule",rn)}" type="rule"/>' for rn in m['rules']]
    links += [f'<infoLink id="{hid(mid,"w",wn)}" name={q(wn)} hidden="false" targetId="{hid("prof",wn)}" type="profile"/>' for wn in m['weapons']]
    if first and notes_rule:
        links.append(f'<infoLink id="{hid(mid,"nl")}" name={q(notes_rule[1])} hidden="false" targetId="{notes_rule[0]}" type="rule"/>')
    if links:
        x += '          <infoLinks>\n' + ''.join('            ' + l + '\n' for l in links) + '          </infoLinks>\n'
    if m['options']:
        x += '          <selectionEntries>\n'
        for k, (lab, cost) in enumerate(m['options']):
            oid = hid(mid, 'opt', k, lab)
            x += (f'            <selectionEntry id="{oid}" name={q(lab)} hidden="false" collective="true" import="true" type="upgrade">\n'
                  f'              <constraints>\n                {B.constraint("selections","parent",1,"max",hid(oid,"max"))}\n'
                  f'                {B.constraint("selections","parent",0,"min",hid(oid,"min"))}\n              </constraints>\n'
                  f'              <costs>\n                <cost name="pts" typeId="points" value="{cost}"/>\n              </costs>\n            </selectionEntry>\n')
        x += '          </selectionEntries>\n'
    x += f'          <costs>\n            <cost name="pts" typeId="points" value="{m["pts"]}"/>\n          </costs>\n        </selectionEntry>\n'
    return x

def build_cat(name, units, notes_text, limits):
    cid = hid('catalogue', name)
    nrid = hid('rule', cid, 'notes'); nrname = f'{name} - List Notes'
    x = ['<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n',
         f'<catalogue id="{cid}" name={q(name)} revision="1" battleScribeVersion="2.03" authorName={q(B.AUTHOR)} library="false" '
         f'gameSystemId="{B.GS_ID}" gameSystemRevision="1" xmlns="http://www.battlescribe.net/schema/catalogueSchema" type="catalogue">\n',
         f'  <readme>{t(name)}: units and points from the Warhammer Ancient Battles 2nd Edition rulebook army list.</readme>\n  <selectionEntries>\n']
    for u in units:
        uid = hid(cid, u['name'], 'unit')
        x.append(f'    <selectionEntry id="{uid}" name={q(u["name"])} hidden="false" collective="false" import="true" type="unit">\n')
        if u['mx']:
            x.append(f'      <constraints>\n        {B.constraint("selections","roster",u["mx"],"max",hid(uid,"max"),shared=True)}\n      </constraints>\n')
        x.append(f'      <categoryLinks>\n        <categoryLink id="{hid(uid,"cat")}" name={q(u["cat"])} hidden="false" targetId="{hid("cat",u["cat"])}" primary="true"/>\n      </categoryLinks>\n      <selectionEntries>\n')
        for i, m in enumerate(u['models']):
            first = (i == 0)
            x.append(model_xml(uid, m, u['notes'] + (f' ({SRC} p.{u["page"]})' if u['page'] else ''),
                               (nrid, nrname) if u['cat'] == 'Characters' else None, first))
        x.append('      </selectionEntries>\n    </selectionEntry>\n')
    x.append('  </selectionEntries>\n  <sharedRules>\n')
    x.append(f'    <rule id="{nrid}" name={q(nrname)} publicationId="{PUB}" hidden="false">\n      <description>{t(notes_text)}</description>\n    </rule>\n')
    x.append('  </sharedRules>\n</catalogue>\n')
    return ''.join(x)

def patch_gst(path, forces, rules):
    s = open(path, encoding='utf8').read()
    cats = sorted({u['cat'] for _, us, _ in forces for u in us})
    add_c = ''
    for c in cats:
        if f'id="{hid("cat",c)}"' not in s:
            add_c += f'    <categoryEntry id="{hid("cat",c)}" name={q(c)} hidden="false"/>\n'
    s = s.replace('  </categoryEntries>', add_c + '  </categoryEntries>', 1)
    add_f = ''
    for fname, us, limits in forces:
        fid = hid('force', fname)
        if f'id="{fid}"' in s: continue
        add_f += f'    <forceEntry id="{fid}" name={q(fname)} hidden="false">\n      <categoryLinks>\n'
        for cn in sorted({u['cat'] for u in us}):
            add_f += f'        <categoryLink id="{hid("flink",fid,cn)}" name={q(cn)} hidden="false" targetId="{hid("cat",cn)}" primary="false"'
            lim = limits.get(cn)
            if lim:
                add_f += f'>\n          <constraints>\n            {B.constraint("limit::points","roster",lim[1],lim[0],hid("lc",fid,cn),pct=True,inc_child=True)}\n          </constraints>\n        </categoryLink>\n'
            else:
                add_f += '/>\n'
        add_f += '      </categoryLinks>\n    </forceEntry>\n'
    s = s.replace('  </forceEntries>', add_f + '  </forceEntries>', 1)
    add_r = ''
    for n, (src, tx) in rules.items():
        if f'id="{hid("rule",n)}"' in s: continue
        add_r += f'    <rule id="{hid("rule",n)}" name={q(n)} publicationId="{PUB}" hidden="false">\n      <description>{t(tx)}</description>\n    </rule>\n'
    s = s.replace('  </sharedRules>', add_r + '  </sharedRules>', 1)
    open(path, 'w', encoding='utf8').write(s)

def main():
    lists = [('Roman Army List', RD.ROMAN, RD.ROMAN_NOTES, RD.ROMAN_LIMITS, 'Roman_Army_List.cat'),
             ('Barbarian Army List', RD.BARB, RD.BARB_NOTES, RD.BARB_LIMITS, 'Barbarian_Army_List.cat')]
    forces = []
    for name, units, notes, limits, fn in lists:
        open(os.path.join(OUT, fn), 'w', encoding='utf8').write(build_cat(name, units, notes, limits))
        forces.append((name, units, limits))
        print('wrote', fn, len(units), 'units')
    patch_gst(os.path.join(OUT, 'Warhammer_Ancient_Battles_2.gst'), forces, RD.RULES)
    print('patched gst')

if __name__ == '__main__':
    main()
