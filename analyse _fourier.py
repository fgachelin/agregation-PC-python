#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

"""

from numpy import *
from matplotlib.pyplot import *
import scipy.fftpack

f= figure("DFT")

'''
fonctions usuelles
'''

def gaussienne(x):
    return exp(-(x**2)/0.3)

def porte(x):
    if abs(x)<5:
        return 1
    else:
        return 0
    
def creneaux(x):
    T=0.5#peride d'un creneau
    if x%T>T/2:
        return 1
    else:
        return 0

def paquet_ondes(x):
    df=0.01
    f=arange(0.1-df,0.1+df,0.0001)
    a=0
    for _ in f:
       a=a+sin(2*pi*_*x)
    return a
       
def sinc(x):
    return sin(x)/x

def porte_positive(x):
    if x>0:
        return 0
    else:
        return 1

def triangle(x):
    T=50
    if x%T>T/2:
        return x%T-0.75*T
    else:
        return -x%T-0.75*T
    
def rampe(x):
    T=300
    return x%T   

def triangle_simple(x):
    T=50
    if x<-T/2:
        return 0
    elif x>T/2:
        return 0
    else:
        return T/2-abs(x)
    
def f(x):
    return (cos(0.1*2*pi*x))**2

'''
Paramètres de discrétisation

Ici x de -x_max à x_max
Pour x de 0 à x_max, redéfinir dx=x_max/N
'''
x_max=100
N=10000#nombre de points
dx=2*x_max/N#pas d'échantillonnage

'''
signal f(x)
'''

x = linspace(-x_max, x_max, N)
y=[f(_) for _ in x]

g1=subplot(121)
g1.set_title("Nom de la fonction",fontsize=16)
g1.plot(x,y)

'''
FFT(s(t))
Le graphique n'affiche que les valeurs positives de la TF, d'où l'allure des sincs pour FFT porte par exemple.
'''


xf = linspace(0, 1/dx, N)[:N//2]
tf_f = scipy.fftpack.fft(y)[:N//2]     
tf_f=abs(tf_f.real/max(abs(tf_f.real)))#normalise yf

g2=subplot(122)
g2.plot(xf, tf_f,"b-")
g2.set_title("$DFT$",fontsize=16)
g2.set_xlim(0.01,1)


show()




