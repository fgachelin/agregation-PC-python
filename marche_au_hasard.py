#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider
from random import *
from scipy.integrate import odeint


'''
représentation graphique 
'''



f=figure()
f.suptitle("Marche aléatoire",fontsize=16)
g1=subplot(111)


a=50
g1.set_xlim(-a,a)
g1.set_ylim(-a,a)

t=linspace(0,1,100)

l,=g1.plot([0],[0],"b-")

def marche_aleatoire(N):
    x,y=[0],[0]
    for _ in range(N):
        x.append(x[-1]+cos(2*pi*random())+cos(0.1*_))
        y.append(y[-1]+sin(2*pi*random())+cos(0.1*_))
        l.set_data(x,y)
        pause(0.05)
        g1.set_title(_)
    return int((x[-1]**2+y[-1]**2)**0.5)

show()

marche_aleatoire(1000)

"""

'''
distribution des distances pour différentes pour N pas
'''
N=[30,100,300,1000]

distribution_distance=[0 for _ in range(100)]

for n in N:
    for _ in range(3000):
        l=marche_aleatoire(n)
        distribution_distance[l]=distribution_distance[l]+1
    g1.plot(distribution_distance[:30],label=n)
    g1.legend()
    '''
    Modèle théorique
    x=range(n)
    y=[n*_*exp(-_**2/n) for _ in x]
    g1.plot(x,y,label="th")
    g1.legend()
    '''
    
"""