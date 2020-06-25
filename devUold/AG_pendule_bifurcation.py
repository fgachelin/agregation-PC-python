# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:13:26 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm



D=-0.1

def energie(angle):
    return 1-np.cos(angle)+(((1+D)*np.cos(angle))**0.5-1)**2

angle=np.linspace(-3,3,368)

g=plt.subplot(111)
g.plot(angle,energie(angle))

plt.legend()
plt.show()