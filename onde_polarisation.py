#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

vecE(t)=vecE_x*cos(wt)+vecE_y*cos(wt-phi)
    cos(wt-phi) est en avance sur cos(wt)
    E_y est axe rapide,E_x est axe_lent
    

lame quart d'onde
    dephasage k*lamb/4=pi/2
    recitligne<->circulaire    
    
lame demi onde
    dephasage k*lamb/2=pi
    symétrique: gauche<->droit

gauche=sens trigo avec vecteur d'onde vers nous

cf illustration sur
http://olivier.granier.free.fr/cariboost_files/Tr-PC-pola-lumiere-1213.pdf
"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox


'''
représentation graphique 
'''

f=figure("Polarisation onde électromagnétique")
f.suptitle(r"$\vec{E}(t)=cos(2\pi ft)\vec{u}_x+cos(2\pi ft-\Phi)\vec{u}_y$",fontsize=28)
g1=subplot(111)
g1.set_xlim(-2,2)
g1.set_ylim(-2,2)
txt_phi=g1.text(0,1.6,"$\Phi=0$",fontsize=20)
txt_theta=g1.text(0,1.2,r"$(\vec{u}_x,\vec{E})=\pi /4$",fontsize=20)

t=linspace(0,20,1000)

phi,theta=0,pi/4

def onde(t):
    E_x=cos(theta)
    E_y=sin(theta)
    return E_x*cos(2*pi*t),E_y*cos(2*pi*t-phi)

l1,=g1.plot(t,t,"b-",label=r"$\vec{E}_x$ (axe lent)")
l2,=g1.plot(t,t,"g-",label=r"$\vec{E}_y$ (axe rapide)")
l3,=g1.plot(t,t,"r-",label=r"$\vec{E}$")
l4,=g1.plot([],[],"r-")


trace=[[],[]]

legend()
show()


'''
ajuster un paramètre par ui avec un curseur
'''

subplots_adjust(bottom=0.25)#réduit g1 pour laisser palce au slider

rect=f.add_axes([0.1,0.05,0.8,0.03])#emplacement du curseur
slider=Slider(rect,"$\Phi=$",-pi,2*pi,0)#paramètres du curseur

rect2=f.add_axes([0.1,0.1,0.8,0.03])#emplacement du curseur
slider2=Slider(rect2,r"$(\vec{u}_x,\vec{E})=$",0,pi,pi/4,)#paramètres du curseur

def maj(_):#met à jour l1 avec les valeurs du curseur
    global slider
    global phi
    global trace
    global theta
    phi=(slider.val//(pi/4))*pi/4
    theta=slider2.val
    txt_phi.set_text("$\Phi="+str(round(phi,2))+"rad$")
    txt_theta.set_text(r"$(\vec{u}_x,\vec{E})="+str(round(theta,2))+" rad$")
    l4.set_data([],[])
    trace=[[],[]]
slider.on_changed(maj)
slider2.on_changed(maj)


'''
animation de la représentation graphique (toujours en fin de code)
'''

for _ in t:
    
    x1,y1=[0,onde(_)[0]],[0,0]
    l1.set_data(x1,y1)
    
    x2,y2=[0,0],[0,onde(_)[1]]
    l2.set_data(x2,y2)
    
    x3,y3=[0,onde(_)[0]],[0,onde(_)[1]]
    l3.set_data(x3,y3)

    trace[0].append(onde(_)[0])
    trace[1].append(onde(_)[1])
    l4.set_data(trace[0],trace[1])
    
    pause(0.05)
    




