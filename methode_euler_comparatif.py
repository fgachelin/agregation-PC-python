#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 19:08:29 2020

@author: maison
"""

from numpy import *
from matplotlib.pyplot import *

g=-9.8
x,y=[0],[0]#conditions initiales

vx0,vy0=5,3

duree=1

v_x,v_y=[vx0],[vy0]
dt=0.001#pas d'intégration
for t in linspace(0,duree,int(duree/dt)):
    x.append(x[-1]+dt*v_x[-1])
    y.append(y[-1]+dt*v_y[-1])
    v_x.append(v_x[-1])
    v_y.append(v_y[-1]+g*dt)
    
plot(x,y,"g-",label="explicite 1000 pas")
axis('equal')


x,y=[0],[0]#conditions initiales
v_x,v_y=[vx0],[vy0]
dt=0.2#pas d'intégration
for t in linspace(0,duree,int(duree/dt)):
    v_x.append(v_x[-1])
    v_y.append(v_y[-1]+g*dt)
    x.append(x[-1]+dt*v_x[-1])
    y.append(y[-1]+dt*v_y[-1])
    
plot(x,y,"b-", label="implicite 5 pas")#vitesse à t+dt
    
x,y=[0],[0]#conditions initiales
v_x,v_y=[vx0],[vy0]
dt=0.2#pas d'intégration
for t in linspace(0,duree,int(duree/dt)):
    x.append(x[-1]+dt*v_x[-1])
    y.append(y[-1]+dt*v_y[-1])
    v_x.append(v_x[-1])
    v_y.append(v_y[-1]+g*dt)
    
plot(x,y,"m-",label="explicite 5 pas")#vitesse à t



x,y=[0],[0]#conditions initiales
v_x,v_y=[vx0],[vy0]
dt=0.02#pas d'intégration
for t in linspace(0,duree,int(duree/dt)):
    v_x.append(v_x[-1])
    v_y.append(v_y[-1]+g*dt)
    x.append(x[-1]+dt*0.5*(v_x[-1]+v_x[-2]))
    y.append(y[-1]+dt*0.5*(v_y[-1]+v_y[-2]))
    
    
plot(x,y,"y-",label="semi-implicite 50 pas")#moyenne de la vitesse actuelle et de la suivante


x=linspace(0,5,200)

def parabole(x):
    return 0.5*g*(x/vx0)**2+x*(vy0/vx0)

plot(x,parabole(x),"r-",label="Solution exacte")

legend()

show()
      
