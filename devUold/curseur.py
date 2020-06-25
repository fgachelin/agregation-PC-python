# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:22:56 2020

@author: click
"""

import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from numpy import *
import math

f,tau=1,1

x=linspace(0,10,1000)

courbe=plt.axes([0.1,0.18,0.8,0.78])

curseur_f=plt.axes([0.1,0.01,0.8,0.03])
curseur_tau=plt.axes([0.1,0.06,0.8,0.03])

def maj(r):
    f=sf.val
    tau=stau.val
    courbe.clear()
    courbe.set_ylim(-1.1,1.1)
    courbe.set_xlabel("temps")
    courbe.set_ylabel("Amplitude")
    courbe.plot(x,sin(2*pi*f*x)*exp(-x/tau))


stau=Slider(curseur_tau,r"$\tau$",0.1,10,valinit=1)
stau.on_changed(maj)

sf=Slider(curseur_f,"$f$",0.1,10,valinit=1)
sf.on_changed(maj)

   



#courbe.legend()
    
plt.show()
    
    

