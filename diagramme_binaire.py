#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

Loi de Raoult: P_i=x_i^l*P_totale (pour un mélange idéal)
Loi de Dalton: P_i=x_i^v*P_totale (loi des pressions partielles)
P_2^sat > P_1^sat :  2 est plus volatil que 1, T_2^éb < T_1^éb

Commenter changement d'état du mélange à x_2 fixée
Commenter les étapes d'un distillation fractionnée en déplaçant x_2=x_2^v à chaque étape. D'autant plus rapide que 
"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider


'''
représentation graphique diagramme isotherme
'''

P=1#pression totale
x2=0.4#fraction molaire x2
P1,P2=1,4#Pressions de vapeur saturante. P1<P2 obligatoire

x=linspace(0,1,400)
ebullition=[_*(P2-P1)+P1 for _ in x]
rosee=[-P1*P2/(_*(P2-P1)-P2) for _ in x]


f=figure("Diagramme binaire")
g1=subplot(111)
y_max=P2+0.5

text=g1.text(0.1,y_max-1,"",fontsize=20)
text_v=g1.text(-10,0,"$x_2^v$",fontsize=14,color="blue")
text_l=g1.text(-10,0,"$x_2^l$",fontsize=14,color="green")

g1.text(-0.1,P1,"$P_1^{sat}$",fontsize=20)
g1.text(1.05,P2,"$P_2^{sat}$",fontsize=20)



g1.plot(x,ebullition,"g-", label="Courbe d'ébullition")
g1.plot(x,rosee,"b-", label="Courbe de rosée")
g1.set_xmargin(0)
lx,=g1.plot([x2,x2],[0,P],"--")
lpoint,=g1.plot([x2],[1],"ro")
lx2eb,=g1.plot([0],[0],"go")
lx2ro,=g1.plot([0],[0],"bo")
lecture_x2v,=g1.plot([],[],"b--")
lecture_x2l,=g1.plot([],[],"g--")
lvp,=g1.plot([],[],"r--")
g1.set_ylim(0,y_max)
g1.legend()
g1.grid()

show()


'''
ajuster un paramètre par ui avec un curseur
'''
   

subplots_adjust(bottom=0.2)

rect=f.add_axes([0.1,0.05,0.8,0.03])
slider=Slider(rect,"$x_2$",0,1,0.5,valfmt='%1.3f')

rect2=f.add_axes([0.1,0.10,0.8,0.03])
slider2=Slider(rect2,"$P$",0,y_max,1)

def maj(_):#met à jour l1 avec les valeurs du curseur
    global x2
    global x1
    global P
    x2=slider.val
    P=slider2.val
    lx.set_data([x2,x2],[0,P])
    lpoint.set_data([x2],[P])
    
    x1=1-x2
    x2l=(P-P1)/(P2-P1)
    x2v=(P-P1)/(P2-P1)*P2/P
    x1l=1-x2l
    x1v=1-x2v
    if x2l<x2 and x2<x2v:
        lx2eb.set_data([x2l],[P])
        lx2ro.set_data([x2v],[P])
        lvp.set_data([x2l,x2v],[P,P])
        lecture_x2v.set_data([x2v,x2v],[0,P])
        lecture_x2l.set_data([x2l,x2l],[0,P])
        text.set_text("$x_2^v=$"+str(round(x2v,3))+"\n$x_2^l=$"+str(round(x2l,3)))
        text_v.set_position([x2v,-0.2])
        text_l.set_position([x2l,-0.2])
    else:
        lx2eb.set_data([],[])
        lx2ro.set_data([],[])
        lvp.set_data([],[])
        lecture_x2v.set_data([],[])
        lecture_x2l.set_data([],[])
        text_v.set_position([-10,0])
        text_l.set_position([-10,0])
    if x2l>x2:
        text.set_text("$x_2^l=$"+str(round(x2,3))+"\n$x_1^l=$"+str(round(x1,3)))
    if x2>x2v:
        text.set_text("$x_2^v=$"+str(round(x2,3))+"\n$x_1^v=$"+str(round(x1,3)))
    
    
    
slider.on_changed(maj)
slider2.on_changed(maj)


