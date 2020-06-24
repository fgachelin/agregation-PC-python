#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

gain_dB=20log(gain) en puissance
gain_dB=10log(gain) en tension
"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider
import scipy.fftpack


FS=20#fontsize
'''
représentation graphique 
variable réduite x=w/w_0, w_0=1
'''

x=logspace(-1,1,2001)

pb1="1/(1+1j*x)"
ph1="x/(1+1j*x)"

r=0.1#proportionnelle à la résistance totale du circuit, faire calcul avec variables réduites

pb21="r*x/(1+2j*r*x-x**2)"
pb22="1/(1+2j*r*x-x**2)"#type RLC


filtre=pb22

def h(x):
    return eval(filtre)

gain=[abs(h(_)) for _ in x]
gain_dB=[20*log10(_) for _ in gain]
argument=[angle(h(_)) for _ in x]

'''
Représentation graphique
'''

f=figure("Fonction de transfert")
f.suptitle("H(x)="+filtre, fontsize=FS)
#f.suptitle(r"$H(x)=\frac{x}{1+jx}$", fontsize=FS)

g1=subplot(211)
g1.set_title("Gain en puissance "+r"$H(x)$", fontsize=FS)
g1.set_ylabel(r"$G(dB)$",rotation=0, fontsize=FS)
g1.set_xlabel(r"$x=\frac{\omega}{\omega_0}$", fontsize=FS)
xscale("log")
g1.grid()
g1.plot(x,gain_dB)

subplots_adjust(hspace=0.4)

g2=subplot(212)
g2.set_title("Déphasage "+r"$\phi(x)$", fontsize=FS)
xscale("log")
g2.grid()
yticks((0,-pi/4,-pi/2, -3*pi/4,-pi),(r"$0$",r"$-\frac{\pi}{4}$",r"$-\frac{\pi}{2}$",r"$-\frac{3\pi}{4}$",r"$-\pi$"),fontsize=FS)
g2.plot(x,argument)


show()
