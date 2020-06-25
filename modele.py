#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

manque champs de vecteur(quiver) et lignes de niveau (contour)

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox
from scipy.integrate import odeint
import scipy.fftpack

'''
représentation graphique 
'''

f=figure()
f.suptitle("Titre $latex$",fontsize=16)
g1=subplot(111)
#g1.text(-9,1.2,"Note",fontsize=14)#plus pratique que les titres mal placés

x=linspace(-10,10,1000)


l1,=g1.plot(x...,,0),"r-")#l1 utile seulement si animation


show()




"""
'''
ajuster un paramètre par ui avec un curseur
'''

subplots_adjust(bottom=0.2)#réduit g1 pour laisser palce au slider
rect_lamb=f.add_axes([0.1,0.05,0.8,0.03])#emplacement du curseur
slider_lamb=Slider(rect_lamb,"$\omega$",0.1,2,1)#paramètres du curseur
def maj(_):#met à jour l1 avec les valeurs du curseur
    global lamb
    lamb=slider_lamb.val
    print(lamb)
    l1.set_ydata(signal(lamb,x,_)) 
slider_lamb.on_changed(maj)
"""




"""
'''
animation de la représentation graphique (toujours en fin de code)
'''

t=linspace(0,20*pi,1000)#définit le temps

for _ in t:
    l1.set_ydata(signal(lamb,x,_))
    pause(0.1)
"""



"""
'''
définir fonction par entree texte (incompatible avec animation por l'instant)...pas indispensable
'''

rect_entree = plt.axes([0.1, 0.1, 0.8, 0.03])
text_box = TextBox(rect_entree, '$f(x)=$', initial="sin(2*pi*x/lamb)")
def entree(text):
    ydata = eval(text)
    l1.set_ydata(ydata)
    draw()
text_box.on_submit(entree)

"""


"""

'''
représentation graphique DFT et odeint
'''

def derivée(data,t):
    '''
    y est un tuple (position y, vitesse dy)
    retourne le tuple dérivé de y =(dy,ddy)
    '''
    y,dy=data
    return (dy,-(omega**2)*sin(y))


N=1000#nombre de points
t_max=50
dt=t_max/(N-1)#pas d'échantillonnage


t=linspace(0,t_max,N)

solution=odeint(pendule,[0,1],t)

tf_x = linspace(0,1/dt, N)
tf_y = scipy.fftpack.fft(solution[:, 0])
tf_y=abs(tf_y)/max(abs(tf_y))

"""
