# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:29:24 2020

@author: click
"""

from math import *
import matplotlib.pyplot as plt
from numpy import *
import sys
sys.setrecursionlimit(10000)


def div_fact(a,b):
    if a>b:
        return a*div_fact(a-1,b)
    else:
        return 1
    
def C(N,n):
    num=div_fact(N,max(n,N-n))
    den=div_fact(min(n,N-n),1)
    print(num)
    print(den)
    return num/den


def nombres_etats(n1,n):
    '''
    Retourne le nombre de possibilités pour avoir n1 particules dans moitié 1
    pour n partiules
    '''
    return C(n,n1)

'''
for n_particules in [100,300,1000,3000]:
    x=[_ for _ in range(n_particules)]
    effectifs=[nombres_etats(_,n_particules) for _ in x]
    m=max(effectifs)
    plt.plot([_/n_particules for _ in x],[nombres_etats(_,n_particules)/m for _ in x],label="N="+str(n_particules))
    plt.legend()


plt.show()
'''

    