# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:22:31 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

'''
def traj(angle,x):
    return -5*(x/np.cos(angle))**2+(np.tan(angle))*x

x=np.linspace(0,0.1,100)

plt.subplot(111)
plt.grid(True)
plt.axis('equal')
plt.ylim(0,0.1)
plt.xlim(0,0.1)

for a in np.linspace(0.1,0.49*np.pi,10):
    plt.plot(x,traj(a,x),label=round(a,2))
    plt.legend()

plt.show()
'''

'''
def psi(x,y):
    return (x**2+y**2)*np.exp(-(x**2+y**2)/np.pi)
'''

def ldc(x,y):
    return 10*(((x-1)**2+y**2)**-1-((x+1)**2+y**2)**-1)
  
    
def potentiel(x,y):
    #return 100*(x/y)/(y**2+x**2)
    return 10*(((x-1)**2+y**2)**-0.5-((x+1)**2+y**2)**-0.5)
    
g1=plt.subplot(111,projection='3d')
l=5
valx = np.linspace(-l,l,100)
valy = np.linspace(-l,l,100)
x,y = np.meshgrid(valx,valy)
g1.plot_surface(x,y,potentiel(x,y))
cset = g1.contourf(x,y,potentiel(x,y), zdir='z', offset=-150, cmap=cm.coolwarm)
cset = g1.contourf(x,y,potentiel(x,y), zdir='x', offset=-5, cmap=cm.coolwarm)
cset = g1.contourf(x,y,potentiel(x,y), zdir='y', offset=5, cmap=cm.coolwarm)




plt.show()


