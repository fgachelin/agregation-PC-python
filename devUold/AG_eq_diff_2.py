# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 18:31:48 2019

@author: François Gachelin
"""
from math import *
import matplotlib.pyplot as plt
import numpy as np

def ea(x,xp):#exacte amortie
    return -sin(x)-xp/Q

def ena(x,xp):#exacte non amortie
    return -sin(x)

def ana(x,xp):#approchee amortie
    return -x

def aa(x,xp):#approchee non amortie
    return -x-xp/Q


def signe(a):
    if a>=0:
        return 1
    else:
        return 0

k=0.5
def bifurc(x,xp):
    return -np.sin(x)-k*np.sign(x)*(abs(x)-1)-xp/Q


h=0.01  #pas d'integration

def champ(x,xp):
    return xp,bifurc(x,xp)


def resolution():
    nb_de_points=(t_final-t_initial)/h
    t=np.linspace(t_initial,t_final,int(nb_de_points))
    #liste des solutions numeriques
    x_t=[x_0]
    xn_t=[1]   #grandeur normalisée
    xp_t=[xp_0]    
    xpp_t=[acceleration(x_t[0],xp_t[0])]
    
    n=0
    while n<nb_de_points-1:
        '''
        algorithme plus stable que celui d'Euler
        d'après https://femto-physique.fr/omp/euler.php#Roussel:2015
        '''
        #algorithme de résolution
        x=x_t[-1]+h*xp_t[-1]+0.5*h**2*xpp_t[-1]
        xp=xp_t[-1]+0.5*h*(xpp_t[-1]+acceleration(x,xp_t[-1]))
        xpp=acceleration(x,xp)
        x_t.append(x)
        xn_t.append(x/x_0)
        xp_t.append(xp)
        xpp_t.append(xpp)
        n=n+1
        
    return np.array(t),np.array(x_t),np.array(xp_t),np.array(xpp_t),np.array(xn_t)

def ec(xp_t):
    return np.array([0.5*xp_t[i]**2 for i in range(len(xp_t))])

def ep(x_t):
    return np.array([1-cos(x_t[i]) for i in range(len(x_t))])


#Paramètres de l'éq diff
acceleration=bifurc  
Q=9.5
x_0=radians(90)
xp_0=1
t_initial=0
t_final=200


#Portraits de phases pour différentes vitesses initiales
acceleration=bifurc
#poser conditions initiales très proches et faire varier Q pour avoir bifurcation
param="x_0"
liste=[0.507,0.508]
g=plt.subplot(121)
for valeur in liste:
    exec(param+"="+str(valeur))
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) )
plt.title("Bifurcation")


h=plt.subplot(122)

x,y=np.meshgrid(np.linspace(-1,1,10),np.linspace(-1,1,10))
u,v=champ(x,y)
h.quiver(x,y,u,v,pivot='mid',headwidth=0)


'''
#paramètre qui varie
param="xp_0"
liste=[1,2,3]
for valeur in liste:
    exec(param+"="+str(valeur))
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(t,ec(xp_t),label='Ec' ) 
'''    



'''
#parametres de la representation graphique
plt.title("Oscillateur harmonique\n")
plt.xlabel("t")
plt.ylabel("Energie")
#plt.xlim(-5,15)
#plt.ylim(-1,7)

plt.legend()
plt.grid()
plt.show()    
'''  

'''
#Energies en fonction du temps pour différentes vitesses initiales
acceleration=ea
param="xp_0"
liste=[3]
for valeur in liste:
    exec(param+"="+str(valeur))
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(t,ec(xp_t),label='Ec' ) 
    plt.plot(t,ep(x_t),label='Ep' ) 
    plt.plot(t,ep(x_t)+ec(xp_t),label='Em' ) 
'''





'''
#Portraits de phases pour différentes vitesses initiales
acceleration=ea
param="xp_0"
liste=[2.2,2.3,3]
for valeur in liste:
    exec(param+"="+str(valeur))
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) ) 
'''



'''
#Angle(t) pour différentes vitesses initiales
acceleration=ea
param="xp_0"
liste=np.linspace(0,2*pi,8)

for valeur in liste:
    exec(param+"="+str(valeur))
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(t,x_t,label=param+'='+str(valeur) ) 
'''



'''
#portrait de phase
for valeur in liste:
    
    exec(param+"="+str(valeur))
    
    x_0=-4*pi
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) )  
  
    
    x_0=2*pi
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) )  
    
    x_0=0.0001
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) )  
    
    x_0=-2*pi
    t,x_t,xp_t,xpp_t,xn_t=resolution()
    plt.plot(x_t,xp_t,label=param+'='+str(valeur) )  
'''
