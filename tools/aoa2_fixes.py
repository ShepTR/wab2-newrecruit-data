"""Corrections layer for the generated AoA2 data (survives regeneration).
apply(LISTS) is called at the end of tools/aoa2_data.py."""

def _find(LISTS, title):
    for l in LISTS:
        if l[1] == title + ' (AoA2)':
            return l
    raise KeyError(title)

def recat(L, old, new, names=None):
    for u in L[3]:
        if u['cat'] == old and (names is None or u['name'] in names):
            u['cat'] = new

def rename(L, cat, old, new):
    for u in L[3]:
        if u['cat'] == cat and u['name'] == old:
            u['name'] = new
            for m in u['models']:
                if m['name'] == old:
                    m['name'] = new

def limit(L, cat, **kw):
    """Add/replace a limit on every composition variant of the army."""
    for v in L[4]:
        v[1][cat] = dict(kw)

def apply(LISTS):
    L = _find(LISTS, 'Late Imperial Roman')
    recat(L, 'Stone Thrower', 'Artillery'); recat(L, 'Bolt Thrower', 'Artillery')
    limit(L, 'Artillery', max=20)

    L = _find(LISTS, 'Later Achaemenid Persian')
    recat(L, 'Cavalry', 'Levies')

    L = _find(LISTS, 'Thematic Byzantine')
    recat(L, 'Varangian Guards', 'Infantry and Skirmishers')

    L = _find(LISTS, 'Later Byzantine')
    recat(L, 'Varangian Guards', 'Infantry')

    L = _find(LISTS, 'Persians and Medes')
    recat(L, 'Corps of Immortals', 'Infantry')
    rename(L, 'Cavalry', 'Heavy', 'Heavy Cavalry')
    rename(L, 'Cavalry', 'Light', 'Light Cavalry')
    rename(L, 'Cavalry', 'Skirmish', 'Skirmish Cavalry')
    rename(L, 'Cavalry', 'Heavy (Levy Cavalry)', 'Heavy Levy Cavalry')
    rename(L, 'Cavalry', 'Skirmish (Levy Cavalry)', 'Skirmish Levy Cavalry')
