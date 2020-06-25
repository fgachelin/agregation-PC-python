# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 18:13:56 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np


def potentiel(x,y):
    return (x**2+y**2)**-0.5

def grad(x,y):
    return np.gradient(potentiel(x,y))

valx = np.linspace(-10,10,10)
valy = np.linspace(-10,10,10)
x,y = np.meshgrid(valx,valy)

g1=plt.subplot(121)
equipotentielles=[0.1,0.2,0.4,0.8]
g1=plt.contour(x,y,potentiel(x,y),equipotentielles)
plt.clabel(g1)

valx = np.linspace(-10,10,10)
valy = np.linspace(-10,10,10)
x,y = np.meshgrid(valx,valy)

g2=plt.subplot(122)
g2=plt.quiver(x,y,potentiel(x,y)[0],potentiel(x,y)[1])


