# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:34:18 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np

t=np.linspace(0,50,10000)

f1,f2=2,2.1
a1,a2=1,1.2

def x(t):
    return (a1*np.cos(2*np.pi*f1*t)+a2*np.cos(2*np.pi*f2*t))*np.exp(-0.1*t)

tf=np.fft.rfft(x(t))
fq=np.fft.rfftfreq(10000,0.005)

g=plt.subplot(211)
g.plot(t,x(t))
h=plt.subplot(212)
h.plot(fq,tf)
h.set_xlim(1,3)
plt.show()









'''

import numpy as np

#matrice à diagonaliser
m=np.array([[1,3],[1,2]])

#valeurs propres
valp=np.linalg.eig(m)[0]

#vecteurs propres normalisés
p=np.linalg.eig(m)[1]

#inversier de vecp
pi=np.linalg.inv(p)

'''
