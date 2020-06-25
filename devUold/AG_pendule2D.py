# -*- coding: utf-8 -*-
"""
Created on Tue Feb  4 18:17:52 2020

@author: click
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

k=2

x,xp=np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))
em=0.5*xp**2+(1-np.cos(x))+k*(abs(x)-1)**2

g=plt.subplot(121)
g=plt.contour(x,xp,em,[0.1,1,2,5,10])
plt.clabel(g)

x,xp=np.meshgrid(np.linspace(-5,5,100),np.linspace(-5,5,100))
em=0.5*xp**2+(1-np.cos(x))+k*(abs(x)-1)**2

h=plt.subplot(122, projection='3d')
h.plot_surface(x,xp,em)



plt.show()

