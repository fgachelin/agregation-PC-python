# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 18:17:18 2020

@author: click
"""

from math import *
import matplotlib.pyplot as plt
import numpy as np


def serie(*a):
    retour=""
    for _ in a:
        retour=retour+'+'+_
    return retour

def parallele(*a):
    retour=""
    for _ in a:
        retour=retour+"+1/("+_+")"
    return "(1/("+retour+"))"

def l(valeur):
    return str(valeur)+"*w*1j"

def r(valeur):
    return str(valeur)

def c(valeur):
    return "1/("+str(valeur)+"*w*1j)"

def transfert(entree,sortie,frequence):
    s,e=sortie.replace("w",str(frequence)),entree.replace("w",str(frequence))
    return abs(eval(s+'/('+e+')'))


def trace():
    w=np.linspace(100,1e5,1000)
    #pre=[3e-11,1e-10,3e-10,1e-9,2e-9]
    pre=[0.1*_ for _ in range(1,9,2)]
    for _ in pre:
        R=1e6
        btn=serie(parallele(r((1-_)*R),c(1e-9)),parallele(r(_*R),c(1e-6)))
        s=parallele(btn,r(470e3))
        mic=serie(c(16e-9),l(8),r(15e3),c(6e-9))
        e=serie(s,mic)  
        h=[transfert(e,s,_) for _ in w]
        plt.plot(w/6.28,h,label=_)
        plt.yscale('log')
        plt.xscale('log')
        plt.legend()
        plt.show()
    
trace()
plt.hlines(0.71,0,1e4)
        
'''
ccl:
    C en serie entre 3 et 6n
    C en parallele avec entrée 0.01n et 1n
'''

'''
0820200091

dev73711

"1 euro deposé à la loge"
'''