# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:08:25 2020

@author: click
"""

from math import *
import matplotlib.pyplot as plt


passe_haut=[0,0,1,10,-10,0,0]
passe_bas=[0,0,-1,1,3,1,-1,0,0,0,0]
passe_bande=[0,0,0,-1,1,3,1,-1,0,0,0]
coupe_bande=[0,0,-1,-3,-1,0]
retard=[1,0,0.3,0,0,0.1,0,0,0]


#entree=[cos(0.5*_) for _ in range(100)]

entree=[ceil(cos(0.02*_)) for _ in range(1000)]


def convolution(entree,ri):
    sortie=[0 for _ in range(len(ri)+len(entree))]
    coeff=1/sum(ri)
    for t in range(len(entree)):
        for T in range(len(ri)):
            sortie[t+T]=sortie[t+T]+entree[t]*ri[T]*coeff
    return sortie

sortie=convolution(entree,passe_bas)
       

plt.plot(entree,label="entree") 
plt.plot(sortie,label="sortie")
plt.xlim(0,len(entree))
plt.legend()
plt.show()