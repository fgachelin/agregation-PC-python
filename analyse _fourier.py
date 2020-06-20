#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

TF réciproques
    porte - sinc
    gaussienne - gaussienne (donc paquets d'onde)
    


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

def paquet_ondes(x):#spectre plat de largeur 2df autour de f avec N ondes monochromatiques
    f=0.5
    df=0.05
    N=1
    f=linspace(f-df,f+df,N)
    a=0
    for _ in f:
       a=a+sin(2*pi*_*x)
    return a
       
def sinc(x):
    return sin(2*pi*0.4*x)/x

def triangle(x):
    T=10
    if x%T>T/2:
        return x%T-0.75*T
    else:
        return -x%T-0.75*T
    
def rampe(x):
    T=10
    return x%T   

def triangle_simple(x):
    T=50
    if x<-T/2:
        return 0
    elif x>T/2:
        return 0
    else:
        return T/2-abs(x)
    
def cos_carré(x):
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

nom_fonction="paquet_ondes"#nom de la fonction sans ()
x = linspace(-x_max, x_max, N)
y=[eval(nom_fonction+"(_)") for _ in x]

g1=subplot(121)
g1.set_title(nom_fonction.replace("_"," "),fontsize=16)
g1.plot(x,y)
g1.set_xlabel("temps $(s)$")
g1.set_ylabel("Amplitude", rotation=0)

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
g2.set_xlabel("fréquence $(Hz)$")
g2.set_ylabel("Amplitude normalisée")


show()




