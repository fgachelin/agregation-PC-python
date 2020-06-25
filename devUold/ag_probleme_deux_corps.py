# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:05:20 2019

@author: click
"""

import matplotlib.pyplot as pp
import numpy as np

L=0.5

def e(r,L):
    a=-r**-1+(L**2)/(2*r**2)
    if a>0:
        return 0
    else: 
        return a
    

#liste abscisses=rayon
r=np.arange(0.01,5,0.001)

#Ep_effective=f(rayon)
'''
for L in [0.3,0.5,0.8,1,2]:
    #pp.plot(r,-r**-1,label='E_gravitation')
    #pp.plot(r,L**2/(2*r**2),label='E_centrifuge')
    pp.title("Energie potentielle effective\n Problème à deux corps\n")
    pp.plot(r,e(r,L),label='L='+str(L))
    pp.ylim(-6,5)
    pp.xlim(0,2)
    pp.xlabel('Rayon normalisé')
    pp.legend()
    pp.grid()
    pp.annotate("R_équilibre\n L=0.5",xy=(0.25,-2),xytext=(0.5,0.5),arrowprops=dict(arrowstyle="->"))
    pp.show()
'''    

#représentation 2d de Ep_effective
largeur=600    #largeur
img=[]
for l in range(largeur):
    img.append([])
    for c in range(largeur):
        r=((l-0.50001*largeur)**2+(c-0.50001*largeur)**2)**0.5
        img[l].append(e(r/largeur,L))
   
pp.imshow(img)
pp.set_cmap("gray")
pp.show()
    


