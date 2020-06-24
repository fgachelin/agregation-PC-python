#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox


'''
représentation graphique 
'''

def angle(o,t):
    '''
    retourne la valeur de l'angle à l'instant t pour l'angle maximal o
    '''
    w=1-o**2/16
    return o*sin(w*t)+(o**3)/192*sin(3*w*t)
    
t=linspace(0,30,1000)

f=figure()
titre=r"$\Theta (t)=\Theta _0 sin(\omega t)+\frac{\Theta ^3}{192}sin(3\omega t)~avec~\omega=$"
f.suptitle(titre,fontsize=16)
g1=subplot(111)

for o in [0.1,0.5,1,2,3.13]:
    g1.plot(t,angle(o,t))#l1 utile seulement si animation


show()



