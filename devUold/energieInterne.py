# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 23:22:34 2019

@author: click
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np

#système isolé = deux sous sytèmes: Vg, T, n moles et Vd, T, 1 mole 
#équilibre thermique, hors équilibre mécanique initial
'''
def U(n,vol):
    return -np.log(1-vol)-n*np.log(vol)


v=np.linspace(0.1,1.9,1000)
plt.title("Energie interne totale")
u=[U(2,x) for x in v]
plt.plot(v,u,label="n_g=2 moles")
u=[U(1,x) for x in v]
plt.plot(v,u,label="n_g=1 mole")
u=[U(0.5,x) for x in v]
plt.plot(v,u,label="n_g=0.5 mole")
plt.legend()
plt.xlabel("Volume réduit")
plt.ylabel("Energie interne réduite")
plt.ylim(0,4)
plt.show()
'''
#système isolé = deux sous sytèmes hors équilibre thermique avec n_g=n mole et n_d=1 mole

Tc,Tf=5,35

def U(n,T):
    return T*(n-1)+0.5*(Tc+Tf)

Tfn=20
def G(n,T):
    return (1+n)*(T*np.log(T)-T)

temp=np.linspace(0.1,40,500)
plt.title("Energie interne totale\n Nécessité de la notion d'entropie")
u=[U(1,x) for x in temp]
s=[S(1,x) for x in temp]

plt.plot(temp,u, label="énergie interne")
plt.plot(temp,s, label="Entropie")
plt.grid()
plt.show()

