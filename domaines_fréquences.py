#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:28:09 2020

@author: Francois Gachelin
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatch

x_data=[0,np.log10(20),np.log10(20000),np.log10(1000000)]
x_tick=[0,20,20000,1e6]

f=plt.figure()
f.suptitle("Domaines sonores",fontsize="xx-large")
g=f.add_subplot(111)
g.barh(1.05,np.log10(2e5)-np.log10(100),left=np.log10(100),label="dauphin")
g.barh(2.05,np.log10(1e4)-np.log10(15),left=np.log10(15),label="éléphant")
g.barh(3.05,np.log10(6e4)-np.log10(50),left=np.log10(50),label="chien")
#plt.text(r"$f(Hz)$")
plt.yticks([])
plt.xticks(x_data,x_tick)
plt.ylim(-0.5,4)
plt.xlim(0,6)
plt.text(1,3,r"$50Hz$")
plt.text(3,3,r"chien")
plt.text(5,3,r"$60000Hz$")
plt.text(0.5,2,r"$15Hz$")
plt.text(2.5,2,r"éléphant")
plt.text(4.3,2,r"$10000Hz$")
plt.text(1,1,r"$100Hz$")
plt.text(3.5,1,r"dauphin")
plt.text(5.4,1,r"$200000Hz$")
x=[0,np.log10(20),np.log10(20000),np.log10(1e6)]
for i in range(3):
    g.barh(0.05,x[i+1]-x[i],left=x[i])
plt.text(0.3,0,"infrason")
plt.text(2,-0.05,"son = domaine audible\n  de l'oreille humaine")
plt.text(4.7,0,"ultrason")
plt.text(6,-1,r"$f(Hz)$")
plt.show()

