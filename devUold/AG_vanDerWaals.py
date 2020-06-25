# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 12:13:26 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def vdw(v,t,vb,a):
    return t/(v-vb)-a/v**2

v=np.linspace(0.001,5,100)

g=plt.subplot(111)
for t in [0.1,0.2,0.5,0.7,0.8,0.9,1,2]:
    g.plot(v,vdw(v,t,0.1,0.3),label=t)
plt.ylim(-1,2)
plt.legend()
plt.show()