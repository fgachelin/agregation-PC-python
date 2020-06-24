#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

solution numérique à comparer avec l'expression theorique resonance.py

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox

'''
résolution équation différentielle
'''

'''
    paramètres physiques
'''
m,gamma,k,w_forcage=1,0.05,1,1

dt=0.02#pas d'intégration
t=arange(0,200,dt)

def acceleration(x,dx,t):
    return -k*x-gamma*dx+sin(w_forcage*t)
    

def resolution(x0,dx0):
    '''
    conditions initiales position et vitesse
    retourne x(t) et y(t)
    '''
    x,dx=[x0],[dx0]
    for _ in t:
        dx.append(dx[-1]+dt*acceleration(x[-1],dx[-1],_) )
        x.append(x[-1]+dt*dx[-1])
    return x[:-1],dx[:-1]

'''
représentation graphique 
'''

f=figure("Oscillateur harmonique forcé")

g1=subplot(111)
g1.set_xlabel("temps (s)")

ls,=g1.plot(t,resolution(0,0)[0],"r-",label="Amplitude du système")
lf,=g1.plot(t,sin(w_forcage*t),"g-",label="Force excitatrice")
legend()
show()


'''
ajuster la pulsation de l'exi=ciateur par ui avec un curseur
'''

subplots_adjust(bottom=0.2)#réduit g1 pour laisser palce au slider
rect=f.add_axes([0.1,0.05,0.8,0.03])#emplacement du curseur
slider=Slider(rect,r"$\frac{\omega_{forçage}}{\omega _0}$",0.01,2,1)#paramètres du curseur
slider.label.set_size(40)
def maj(_):#met à jour l1 avec les valeurs du curseur
    global w_forcage
    w_forcage=slider.val
    ls.set_ydata(resolution(0,0)[0]) 
    lf.set_ydata(sin(w_forcage*t)) 
slider.on_changed(maj)
