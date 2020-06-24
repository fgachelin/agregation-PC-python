#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox
from scipy.integrate import odeint
import scipy.fftpack

'''
résolution équation différentielle

[ddy,dy]=[-k*sin(y),dy+ddt*dt]

vérifier formule de Broda w=w_0(1-o**2/8)
Comparer avec l'expression donnée avec la méthode des perturbations (o(t)=o_1 sin(wt)+o_1**3/192*sin(3wt))
'''

omega=4*pi

def pendule(v,t):
    '''
    y est un tuple (position y, vitesse dy)
    retourne le tuple dérivé de y =(dy,ddy)
    '''
    y,dy=v
    return (dy,-(omega**2)*sin(y))


'''
représentation graphique 
'''

N=1000#nombre de points
t_max=50
dt=t_max/(N-1)#pas d'échantillonnage


t=linspace(0,t_max,N)

solution=odeint(pendule,[0,1],t)

tf_x = linspace(0,1/dt, N)
tf_y = scipy.fftpack.fft(solution[:, 0])
tf_y=abs(tf_y)/max(abs(tf_y))

f=figure("Pendule simple")
f.suptitle(r"$\ddot{\Theta}=-\omega_0^2 sin(\Theta)$")

g1=subplot(121,xlabel="$t_{(s)}$")
g1.set_ylabel("$\Theta(t)_{(rad)}$",fontsize=16)
g1.set_xlim(0,5)
g1.set_ylim(-4,4)
yticks((-pi,-pi/2,0,pi/2,pi),("$-\pi$",r"$-\frac{\pi}{2}$","$0$",r"$\frac{\pi}{2}$","$\pi$"),color="r")
g1.grid()

g2=subplot(222,xlabel="$fréquence_{(Hz)}$")
g2.set_title("Analyse spectrale")
g2.set_xlim(0,7)
g2.grid()

subplots_adjust(hspace=0.4)

g3=subplot(224)
g3.grid()
g3.set_title("Portrait de phase")
g3.set_xlim(-pi,pi)
g3.set_ylim(-0.5*omega**2,0.5*omega**2)#energie proportionnelle à omega**2
g3.set_xlabel(r"$\Theta$")
g3.set_ylabel(r"$\omega$")


l1,=g1.plot(t,solution[:, 0],label="$x(t)$")
l2,=g2.plot(tf_x,tf_y,label="$FFT(x(t))$")
l3,=g3.plot(solution[:, 0],solution[:, 1])

'''
ajustement de l'angle initial
'''

subplots_adjust(bottom=0.2)#réduit g1 pour laisser palce au slider
rect=f.add_axes([0.1,0.05,0.8,0.03])#emplacement du curseur
slider=Slider(rect,"$\Theta_0$",0.01,pi-0.001,1)#paramètres du curseur
def maj(theta_0):#met à jour l1 avec les valeurs du curseur
    solution=odeint(pendule,[theta_0,0],t)
    tf_y = scipy.fftpack.fft(solution[:, 0])
    tf_y=abs(tf_y)/max(abs(tf_y))
    l1.set_ydata(solution[:, 0])
    l2.set_ydata(abs(tf_y))
    l3.set_data(solution[:, 0],solution[:, 1])

slider.on_changed(maj)


'''
calcul des fréquences avec formule de Broda pour différents angles
'''
for o in [0.1,0.5,1,2,3]:
    print(omega*(1-(o**2)/16)/(2*pi))



"""
'''
Comparatif des valeurs de période T pour Broda et simulation numérique
'''

g=figure("Période du pendule simple")
g5=subplot(111)
T_data=[]
o_data=linspace(0.001,pi-0.00001,10)
for o in o_data:
    solution=odeint(pendule,[o,0],t)
    tf_y = scipy.fftpack.fft(solution[:, 0])
    tf_y=abs(tf_y)/max(tf_y)
    T_data.append((dt*tf_y.argmax())**(-1))

T_data=array(T_data)#tableau numpy permet la division

g5.plot(o_data,T_data/2,"r-",label="simulation numérique")
g5.plot(o_data,1+o_data**2/16,"b-",label=r"Formule de Broda $T=T_0(1+\frac{\Theta_0 ^2}{16})$")#+o_data**4/192
g5.set_ylim(0.8,2)
g5.grid()
legend()
show()

""" 
    
    

    