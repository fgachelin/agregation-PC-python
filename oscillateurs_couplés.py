#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

Oscillateurs couplés sans amortissement
-ressort-masse1(x)-ressort_couplage-masse2(y-ressort-

Deux modes propres  
Battements avec situation initiale quelconque       

Vérifier période des battements avec valeur théorique
"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox

'''
résolution équation différentielle (méthode d'Euler)
'''

'''
paramètres physiques
'''
mx,my=1,1
k,k_couplage=1,0.2

dt=0.2#pas d'intégration
t=arange(0,200,dt)

def acceleration(x,y):
    ax=(-k*x+k_couplage*(y-x))/mx
    ay=(-k*y+k_couplage*(x-y))/my
    return ax,ay

def resolution(x0,y0,vx0,vy0):
    '''
    conditions initiales position et vitesse
    retourne x(t) et y(t)
    '''
    ax0,ay0=acceleration(x0,y0)
    x,y,vx,vy,ax,ay=[x0],[y0],[vx0],[vy0],[ax0],[ay0]
    for _ in t:
        ax_t,ay_t=acceleration(x[-1],y[-1]) 
        vx.append(vx[-1]+dt*ax_t)
        vy.append(vy[-1]+dt*ay_t)
        x.append(x[-1]+dt*vx[-1])
        y.append(y[-1]+dt*vy[-1])
    return x[:-1],y[:-1]


'''
représentation graphique 
'''

f=figure()
f.suptitle("Oscillateurs couplés",fontsize=16)
g1=subplot(311)
g1.set_xlabel('abscisse (m)')
g2=subplot(312)
g2.set_ylabel('Amplitude $(m)$')
g3=subplot(313)
g3.set_ylabel('Amplitude $(m)$')
g3.set_xlabel('temps $(s)$')

#g1.text(-9,1.2,"Note",fontsize=14)#plus pratique que les titres mal placés
x,y=resolution(0.5,0,0,0)

lx,=g1.plot([0],[0],"ro")
ly,=g1.plot([0],[0],"bo")
g1.set_xlim(-2.2,2.2)
lx2,=g2.plot(t,x,"r-")
ly2,=g3.plot(t,y,"b-")


show()


'''
animation g1
'''

n=0
for _ in t:
    lx.set_xdata([-1+x[n]])
    ly.set_xdata([1+y[n]])
    lx2.set_data(t[:n],x[:n])
    ly2.set_data(t[:n],y[:n])
    n=n+1
    pause(0.05)

