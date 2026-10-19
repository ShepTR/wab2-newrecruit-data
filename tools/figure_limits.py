#!/usr/bin/env python3
"""Total-figure rules that were notes only:
 - Illyrians (Alexander): Slave Warriors units <= Illyrian Warriors units (one Slave unit per warrior unit); Slave Warrior figures <= Illyrian Warrior figures;
   an Illyrian Skirmisher unit may not outnumber the Warriors (exact with one Warrior unit, total of figures otherwise)
 - Germanic Kingdoms (Byzantium): Unfree figures <= Warrior Elite figures (foot + mounted)
 - Kingdom of Hungary (Vlad): Tartar Cavalry figures <= Szekeler Cavalry figures
Usage: python3 figure_limits.py <outdir>   (idempotent)"""
import sys
from limlib import *
from ratiolib import ratio, size_limit, fig_cap
def figs(cat, A, B, tag, scope): fig_cap(cat, A, B, tag, scope)
I = Cat('Illyrians_Alexander.cat')
ratio(I, 'Slave Warriors', ['Illyrian Warriors'])
figs(I, 'Slave Warriors', 'Illyrian Warriors', 'figures-vs-warriors', 'force')
size_limit(I, 'Illyrian Skirmishers', 'Illyrian Warriors')
I.save()
H = Cat('Kingdom_of_Hungary_Vlad.cat')
figs(H, 'Tartar Cavalry', 'Szekeler Cavalry', 'figures-vs-szekelers', 'force')
H.save()
G = Cat('Germanic_Kingdoms_Byzantium.cat')
fig_cap(G, 'Unfree', ['Warrior Elite (On Foot)', 'Warrior Elite (Mounted)'], 'figures-vs-warrior-elite', 'force')
G.save()
print('figure limits added')
