#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:58:45 2020

@author: François Gachelin
"""

from numpy import *
from matplotlib.pyplot import *

w=0

def paquet_ondes(dw,t):
    global w
    w=arange(1-dw,1+dw,0.001)#pas de linspace pour garder même écart entre deux fréquences
    #w=linspace(1-dw,1+dw,10)
    a=0
    for _ in w:
       a=a+sin(_*t)
       #*exp(-t**2/10000)
    return a
   
t=linspace(-1000,1000,4000)


f=figure()
f.suptitle("Paquets d'onde gaussiens $\omega=1$")

g1=subplot(311)
g1.plot(t,paquet_ondes(0.5,t),"r-")
g1.text(-100,0,"$d\omega=0.5$")
g1.set_ylabel("amplitude",rotation=0)

g2=subplot(312)
g2.plot(t,paquet_ondes(0.1,t),"g-")
g2.text(-100,0,"$d\omega=0.05$")

g3=subplot(313)
g3.plot(t,paquet_ondes(0.01,t),"g-")
g3.text(-100,0,"$d\omega=0.005$")
g3.set_xlabel("temps")


show()

