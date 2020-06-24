#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:16:56 2020

@author: François Gachelin

odeint fonctionne moyennement car le pas a intérêt à être variable, ce qui ne semble pas être le cas
"""

#Remarque: plt.contour ne prend pas de fonction mais une variable définie à partir des coordonnées

from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

q1_x,q2_x=-0.5,0.5
q1_y,q2_y=0,0
q1,q2=1,-1

f=figure()

f.suptitle(r"Dipôle électrostatique",fontsize=20)

g=subplot(111)

g.axis('equal')

x=linspace(-10,10,200)

X,Y=meshgrid(x,x)

V=q1/(((X-q1_x)**2+Y**2)**0.5)+q2/(((X-q2_x)**2+Y**2)**0.5)

v=[1,0.3,0.1,0.03,0.01,0.001]

V_valeurs=[]
for i in v:
    V_valeurs.append(-i)
v.sort()
V_valeurs=V_valeurs+v

c=contour(X,Y,V,V_valeurs,colors='k')
g.clabel(c)
g.plot(0.5,0,"ro")
g.plot(-0.5,0,"go")

text(4,4,"Lignes équipotentielles",fontsize=16)

show()


def E(data,t):
    '''
    retourne les coordonnées du champ électrique au point de coordonnées (x,y), un booleen pour stopper les itérations, d_min pour ajuster le pas d'intégration
    '''
    x,y=data
    d1=((x-q1_x)**2+y**2)**0.5
    d2=((x-q2_x)**2+y**2)**0.5
    E_1=q1/d1**2
    E_2=q2/d2**2
    E_1y=E_1*y/d1
    E_1x=E_1*(x-q1_x)/d1
    E_2y=E_2*y/d2
    E_2x=E_2*(x-q2_x)/d2
    E_x=E_1x+E_2x
    E_y=E_1y+E_2y
    if d2<0.1:
        return [0,0]
    else:
        return [E_x,E_y]
    

t=linspace(0,30000,10000)    

data=odeint(E,[-0.5,0.11],t)
g.plot(data[:, 0],data[:, 1])

for x_depart in [-0.75,-0.7,-0.6,-0.5]:
    data=odeint(E,[x_depart,0.11],t)
    g.plot(data[:, 0],data[:, 1])
    data=odeint(E,[x_depart,-0.11],t)
    g.plot(data[:, 0],data[:, 1])
    
    
text(4,-4,"Ligne de champ",fontsize=16,color="red")
