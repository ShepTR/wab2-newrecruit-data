"""Ratio rules as validation: "A may be taken once per N units of B"  ==  the army needs at least N*count(A) units of B.
Implemented as ONE min constraint on B (modifiers add N per unit of each A that depends on B), so B shows a validation error instead of A
showing a misleading 0-1 maximum.  Rules with several B's, extra conditions, or 'unless none' keep the old max-on-A form.
Also: size_limit(cat, A, B): a unit of A may not have more models than the models in B units (exact with one B unit, lenient with several)."""
import sys, os, re, hashlib
BIG = 1000
def hid(*p):
    h = hashlib.md5('|'.join(str(x) for x in p).encode('utf8')).hexdigest()
    return '-'.join(h[i:i + 4] for i in range(0, 16, 4))
def mod(kind, field, value, conds=(), repeat=None):
    x = f'<modifier type="{kind}" field="{field}" value="{value}">\n'
    if repeat:
        child, per, incl = repeat
        x += (f'  <repeats>\n    <repeat field="selections" scope="force" value="{per}" percentValue="false" shared="true" includeChildSelections="{incl}" '
              f'includeChildForces="false" childId="{child}" repeats="1" roundUp="false"/>\n  </repeats>\n')
    if conds: x += '  <conditions>\n' + ''.join(f'    {c}\n' for c in conds) + '  </conditions>\n'
    return x + '</modifier>\n'
def cond(child, op):
    return (f'<condition field="selections" scope="force" value="1" percentValue="false" shared="true" includeChildSelections="true" '
            f'includeChildForces="false" childId="{child}" type="{op}"/>')

def strip_old(cat, A, tag):
    """remove a max-on-A ratio rule built earlier under this tag (constraint, comment and its modifiers)"""
    uid = cat.unit(A)[0]; cid = hid(uid, tag)
    if f'<!-- {tag} -->' not in cat.s or cid not in cat.s: return
    s = cat.s
    s = re.sub(r'^ *<constraint [^\n]*id="%s" type="max"/>\n' % re.escape(cid), '', s, flags=re.M)
    s = re.sub(r'^ *<!-- %s -->\n(?: *<modifier type="[a-z]+" field="%s" value="[^"]*">\n.*?</modifier>\n)+' % (re.escape(tag), re.escape(cid)), '', s, flags=re.M | re.S)
    cat.s = s; cat.changed = True

def ratio(cat, A, Bs, per=1, extra=(), tag=None, unless_none=False):
    tag = tag or f'limit-{A}-per-{"-".join(Bs)}'
    ids = [cat.unit(b)[0] for b in Bs]
    if len(Bs) == 1 and not extra and not unless_none:
        strip_old(cat, A, tag)
        b = Bs[0]; buid = cat.unit(b)[0]; aid = cat.unit(A)[0]
        if '<!-- need -->' not in cat.unit(b)[2].group(0):
            cat.add_unit_limit(b, 'need', 'min', 0, lambda cid: [])
        mk = f'<!-- need:{A} -->'
        m = cat.unit(b)[2].group(0)
        if mk in m: return
        cid = hid(buid, 'need')
        x = mod('increment', cid, per, repeat=(aid, 1, 'false'))
        x = f'        {mk}\n' + ''.join(('        ' + l if l.strip() else l) for l in x.splitlines(True))
        nb = m.replace('        <!-- need -->\n', '        <!-- need -->\n' + x, 1)
        cat.s = cat.s.replace(m, nb, 1); cat.changed = True
        return
    def mods(cid):
        out = [mod('increment', cid, 1, conds=[*extra], repeat=(b, per, 'false')) for b in ids]
        if unless_none: out.append(mod('set', cid, BIG, conds=[cond(b, 'lessThan') for b in ids] + list(extra)))
        return out
    cat.add_unit_limit(A, tag, 'max', 0, mods)

def size_limit(cat, A, B, tag=None):
    """models of one A unit <= total models in the B unit(s) (0 with none); B = unit name or list of names"""
    Bs = [B] if isinstance(B, str) else list(B)
    tag = tag or f'size-{A}-vs-{"-".join(Bs)}'
    mids = [cat.unit(b)[1] for b in Bs]
    cat.add_model_limit(A, tag, 'parent', 0, lambda cid: [mod('increment', cid, 1, repeat=(m, 1, 'true')) for m in mids])
