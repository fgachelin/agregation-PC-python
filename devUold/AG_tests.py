# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 01:12:01 2019

@author: click
"""

from math import *
import matplotlib.pyplot as p
import numpy as np

w=2*pi/86400
g=9.81



def z(t):
    return 158-0.5*g*t**2

def x(t):
    return g*w*np.sin(pi/4)*t**3/3

t=np.linspace(0,7,100)

p.title("Force de Coriolis, déviation vers l'Est (ordre 1)\n")
p.plot(x(t),z(t),marker="+",color="red")
p.ylim(0,160)
p.xlim(-0.05,0.05)
p.legend()
p.show()

'''
Expérience historique faite avec une chute de 158m, déviation mesurée de 28mm
'''