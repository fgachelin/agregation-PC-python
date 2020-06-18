#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 01:58:45 2020

@author: François Gachelin
"""

from numpy import *
from matplotlib.pyplot import *


w=linspace(1-dw,1+dw,10)

def paquet_ondes(dw,t):
    w=linspace(1-dw,1+dw,100)
    a=0
    for _ in w:
       a=a+sin(_*t)*exp(-t**2/10000)
    return a
    
t=linspace(-300,300,1000)


f=figure()
f.suptitle("Paquets d'onde gaussiens $\omega=1$")

g1=subplot(311)
g1.plot(t,paquet_ondes(0.5,t),"r-")
g1.text(-100,50,"$d\omega=0.5$")

g2=subplot(312)
g2.plot(t,paquet_ondes(0.05,t),"g-")
g2.text(-100,50,"$d\omega=0.05$")

g3=subplot(313)
g3.plot(t,paquet_ondes(0.005,t),"g-")
g3.text(-100,50,"$d\omega=0.005$")

show()

