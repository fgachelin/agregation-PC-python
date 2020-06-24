#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

Oscillateur forcé avec amortissement
    RLC avec GBF
    électron élastiquement lié
    masse-ressort et forçage
    
Mesurer Q (A_max/2**0.5) et le comparer avec w*tau=w/gamma=1/gamma
    
A comparer avec resolution numérique oscillateur_forcé.py
"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider


'''
représentation graphique 
'''

f=figure("Résonance")
f.suptitle(r"A(x)=$\frac{1}{(1-x^2)+j\frac{x}{Q}}$",fontsize=30)
g1=subplot(111)
g1.set_xlabel(r"$x=\frac{\omega}{\omega_0}$",fontsize=26)
g1.set_ylabel(r"$Amplitude$",fontsize=26,rotation=0,color="red")
g1.set_ylim(-30,30)
g1.grid()

y_droite=g1.twinx()
y_droite.set_ylim(-4,4)
y_droite.set_ylabel(r"$déphasage(rad)$",rotation=0,fontsize=26,color="blue")

texte=g1.text(0,g1.get_ylim()[0]/2,r"$Q=\frac{\omega_0}{\Gamma}=\frac{1}{\Gamma}$",fontsize=26)

w=linspace(0,2,500)


gamma=1
def signal(w):
    return 1/((1-w**2)+1j*(gamma*w))

l1,=g1.plot(w,signal(w).real,"y-",label="Partie réelle")
l2,=g1.plot(w,signal(w).imag,"g-",label="Partie imaginaire")
l3,=g1.plot(w,abs(signal(w)),"r-",label="Amplitude")
l4,=g1.plot(w,angle(signal(w)),"b-",label="Phase")
g1.legend()
show()


'''
ajuster un paramètre par ui avec un curseur
'''

subplots_adjust(bottom=0.2)#réduit g1 pour laisser palce au slider
rect=f.add_axes([0.1,0.05,0.8,0.03])#emplacement du curseur
slider=Slider(rect,"$\Gamma$",0.01,2,1)#paramètres du curseur
def maj(_):#met à jour l1 avec les valeurs du curseur
    global gamma
    gamma=slider.val
    l1.set_ydata(signal(w).real) 
    l2.set_ydata(signal(w).imag) 
    l3.set_ydata(abs(signal(w))) 
    l4.set_ydata(angle(signal(w))*30/4) 
    Q=1/gamma
    texte.set_text(r"$Q=\frac{\omega_0}{\Gamma}="+str(round(Q,2))+"$")
    
slider.on_changed(maj)

