# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 12:15:40 2019

@author: click
"""

'''
A finir!!!

'''

from matplotlib.pyplot import *
import numpy as np
from math import *

angles=[30,60,90]
la=[log(radians(_)) for _ in angles]
periodes=[2.103,2.16,2.24]
ldt=[log(periodes[i]/2.064) for i in range(3)]


pente=(ldt[2]-ldt[0])/(la[2]-la[0])
print("pente",pente)

title("Ecart à l'isochronisme des petites oscillations\n")
xlabel("log(angle)")
ylabel("log(T/T_0)")
plot(la,ldt)
show()