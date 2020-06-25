# -*- coding: utf-8 -*-
"""
Created on Tue Oct 22 23:22:35 2019

@author: click
"""

from math import *
import matplotlib.pyplot as p
from matplotlib.widgets import Slider
import numpy as np


r=1
R=100

def H(w):
    return ((r/(R+r))+w*1j)/(1+w*1j)  #RL
    #return 1/(1+w*1j)   #circuit RC passe-bas
    
x=[i/100 for i in range(1,10000)]

gain=[20*np.log(np.abs(H(w))) for w in x] 
dephasage=[np.angle(H(w)) for w in x] 
 
p.subplot(211)
p.plot(x,gain,label="G_dB")
p.xscale('log')
p.legend()
p.grid()


p.subplot(212)
p.plot(x,dephasage,label="Déphasage_radians")
p.xscale('log')
p.legend()
p.grid()

p.show()

