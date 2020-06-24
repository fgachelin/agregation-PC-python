#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Créé le Thu Jun 18 09:56:12 2020

@auteur: François Gachelin

Van der Pol: amortissement en x**2-1

Pour toutes les conditions initiales il existe un attracteur
    vérifier avec des conditions initiales presque nulles ou "extremes"

pour x faible, x**2-1>0:
    gain des oscillations
    
pour x élevé, x**2-1<0:
    amortissement des oscillations
    
amortissement faible: oscillateur presque harmonique
amortissement fort: oscillateur à relaxation


"""

from numpy import *
from matplotlib.pyplot import *
from matplotlib.widgets import Slider, TextBox
from scipy.integrate import odeint
import scipy.fftpack

'''
résolution équation différentielle
'''

tau=0.5#amortissement

def vdp_asym(x):
    '''
    coefficient d'amortissement asymétrique pour avoir des signaux asymétriques
    '''
    if x>0:
        return 0.01*x**2-1
    else:
        return 0.1*x**2-1
    
def vdp(beta,x):
    return beta*x**2-1
    
        
def oscillateur(data,t):
    x,dx=data
    return [dx,-x-dx/tau*(vdp_asym(x))]

t=linspace(0,50,2000)

solution=odeint(oscillateur,[0,0.1],t)
     
'''
représentation graphique 
'''

f=figure("Oscillateur amorti")
g1=subplot(121)
g2=subplot(122)

x=solution[:,0]
dx=solution[:,1]


g1.plot(t,x,"b-")
g1.set_title("$x(t)$")
g1.set_xlabel("t")

g2.plot(x,dx,"b-")
g2.set_title("Portrait de phase")
g2.set_xlabel(r"$x(t)$")
g2.set_ylabel(r"$\frac{dx(t)}{dt}$")

l1,=g1.plot([0],[0],"ro")
l2,=g2.plot([0],[0],"ro")
   
show()


'''
animation de la représentation graphique 
'''

for i in range(len(t)):
    l1.set_data(t[i],x[i])
    l2.set_data(x[i],dx[i])
    #l31.set_data(t[i],Ec[i])
    #l32.set_data(t[i],Ep[i])
    pause(0.01)



"""
'''
Oscillateur libre amorti, rprésentation des énergies
'''
g3=subplot(222)

Ec=[0.5*_**2 for _ in dx]
Ep=[0.5*_**2 for _ in x]
Em=[Ec[_]+Ep[_] for _ in range(len(Ec))]

g3.plot(t,Ec,"b-", label="énergie cinétique "+r"$\frac{1}{2}(\frac{dx}{dt})^2$")
g3.plot(t,Ep,"g-",label="énergie potentielle "+r"$\frac{x^2}{2}$")
g3.plot(t,Em,"r-",label="énergie mécanique")
g3.set_xlabel("t")
g3.legend()

l31,=g3.plot([0],[0],"ro")
l32,=g3.plot([0],[0],"ro")
"""

