#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

Mirage au-dessus du sol chaud
    grad(n) vers le haut (opposé à grad(T)) car n plus faible au sol cause air chaud 
    
Mirage au-dessus du sol froid
    grad(n) vers le bas

Fibre optique
    n_y=1.1-ay**2 ou 1.1-a.abs(y)
    toujours même période pour toute condition initiale

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider


'''
définit le gradiient vertical d'indice
'''
def n(y):
    return eval(n_y)
  

def trajectoire(i_0,y_0):
    '''
    résolution de 'léquation différentielle
    retourne x_data, y_data pour l'angle initial i_0 et l'ordonnée initiale y_0
    '''
    C=n(y_0)*cos(i_0) #invariant
    s=sign(i_0)
    
    dx=0.02#pas
    N=2000#nombre de points

    x_data=linspace(0,N*dx,N+1)
    y_data=[y_0]
    
    for _ in range(len(x_data)-1):
        K=(n(y_data[-1])/C)**2-1
        if K>0:
            dy_dx=sqrt(K)
        else:
            dy_dx=sqrt((n(y_data[-2])/C)**2-1)#on reprend dernière dérivée existante pour la réflexion
            s=-s#selon trajectoire monte ou descend
        y=y_data[-1]+s*dx*dy_dx
        y_data.append(y)
    return x_data, y_data



'''
représentation graphique 
'''

a=0.005

f=figure("Propagation dans un milieu d'indice variable")

n_y="1+a*y"
g1=subplot(131)
g1.set_title("$n(z)="+n_y+"$",fontsize=16)
x,y=trajectoire(-1,1)
g1.plot(x,y,"r-")
x,y=trajectoire(1,1)
g1.plot(x,y,"g-")

n_y="1-a*y"
g2=subplot(132)
g2.set_title("$n(z)="+n_y+"$",fontsize=16)
x,y=trajectoire(-1e-1,1)
g2.plot(x,y,"r-")
x,y=trajectoire(5e-2,1)
g2.plot(x,y,"g-")

#n_y="1.1-10*a*y**2"
n_y="1.1-30*a*y**2"
g3=subplot(133)
g3.set_title("$n(z)="+n_y+"$",fontsize=16)
x,y=trajectoire(-5e-2,0.1)
g3.plot(x,y,"r-")
x,y=trajectoire(5e-2,0.1)
g3.plot(x,y,"g-")
x,y=trajectoire(0.00001,0.05)
g3.plot(x,y,"y-")

show()

