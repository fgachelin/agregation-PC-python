# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:26:25 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np



'''angle=[_*0.1 for _ in range(1000)]
rayon=[a**2*np.exp(-0.5*a) for a in angle]

ax = plt.subplot(111, projection='polar')

ax.plot(angle,rayon)

plt.show()
'''

def p2c(rayon,angle):
    return rayon*np.cos(angle),rayon*np.sin(angle)

def champ(rayon,angle):
    return -rayon*np.sin(angle)**2,rayon*np.cos(angle)**2

x,y,u,v=[],[],[],[]

rayons=np.linspace(5,20,5)
angles=np.linspace(-np.pi,np.pi,17)

for er in rayons:
    for ea in angles:
        xx,yy=p2c(er,ea)
        uu,vv=champ(er,ea)
        x.append(xx)
        y.append(yy)
        u.append(uu)
        v.append(vv)



g = plt.subplot(111)
g.quiver(x,y,u,v)
plt.show()