# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 13:33:38 2020

@author: click
"""

from random import *
import re
import matplotlib as plt
import numpy

bases="abcdefghijklmnopqrstu"
#bases="AGCU"


def sequence(l):
    s=''
    for _ in range(l):
        s=s+bases[randint(0,3)]
    return s


def coincidences(n):
    '''retourne le nombre de sequences communes à n bases parmi 30000'''
    covid=sequence(10000)
    recherche=sequence(n)
    return len(re.findall(recherche,covid))

def produireDonnees():
    print("Longueur de sequence cherchée -> nombre d'occurences sur 30000")
    for n in range(1,6):
        valeurs=[]
        for _ in range(10):
            valeurs.append(coincidences(n))
        print(n,' -> ',numpy.nanmean(valeurs),' écart-type=',numpy.nanstd(valeurs))
    
produireDonnees()


'''

Longueur de sequence cherchée -> nombre d'occurences sur 30000
2  ->  1791.76  écart-type= 160.86951979787844
3  ->  458.65  écart-type= 32.30274756115956
4  ->  115.23  écart-type= 12.385358291143618
5  ->  29.33  écart-type= 4.9518784314641655
6  ->  7.53  écart-type= 2.651244990565753
7  ->  1.73  écart-type= 1.3553966209195005
8  ->  0.26  écart-type= 0.482078831727758
9  ->  0.13  écart-type= 0.364828726939094
10  ->  0.02  écart-type= 0.13999999999999999
11  ->  0.0  écart-type= 0.0
12  ->  0.0  écart-type= 0.0
13  ->  0.0  écart-type= 0.0
14  ->  0.0  écart-type= 0.0

'''