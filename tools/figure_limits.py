#!/usr/bin/env python3
"""Total-figure rules that were notes only:
 - Illyrians (Alexander): Slave Warriors units <= Illyrian Warriors units (one Slave unit per warrior unit); Slave Warrior figures <= Illyrian Warrior figures;
   an Illyrian Skirmisher unit may not outnumber the Warriors (exact with one Warrior unit, total of figures otherwise)
 - Germanic Kingdoms (Byzantium): Unfree figures <= Warrior Elite figures (foot + mounted)
 - Kingdom of Hungary (Vlad): Tartar Cavalry figures <= Szekeler Cavalry figures
Usage: python3 figure_limits.py <outdir>   (idempotent)"""
import sys
from limlib import *
from ratiolib import ratio, size_limit
def figs(cat, A, B, tag, scope):
    bm = cat.unit(B)[1]
    cat.add_model_limit(A, tag, scope, 0, lambda cid: [mod('increment', cid, 1, repeat=(bm, 1, 'true'))])
I = Cat('Illyrians_Alexander.cat')
ratio(I, 'Slave Warriors', ['Illyrian Warriors'])
figs(I, 'Slave Warriors', 'Illyrian Warriors', 'figures-vs-warriors', 'force')
size_limit(I, 'Illyrian Skirmishers', 'Illyrian Warriors')
I.save()
H = Cat('Kingdom_of_Hungary_Vlad.cat')
figs(H, 'Tartar Cavalry', 'Szekeler Cavalry', 'figures-vs-szekelers', 'force')
H.save()
G = Cat('Germanic_Kingdoms_Byzantium.cat')
wm = [G.unit(n)[1] for n in ('Warrior Elite (On Foot)', 'Warrior Elite (Mounted)')]
G.add_model_limit('Unfree', 'figures-vs-warrior-elite', 'force', 0, lambda cid: [mod('increment', cid, 1, repeat=(m, 1, 'true')) for m in wm])
G.save()
print('figure limits added')
