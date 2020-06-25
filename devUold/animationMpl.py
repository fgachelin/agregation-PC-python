# -*- coding: utf-8 -*-
"""
Created on Sun May 24 01:30:24 2020

@author: Francois Gachelin
"""

import numpy as np
import matplotlib.pyplot as plt
#from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation


f,g1=plt.subplots()
g1.set_xlim(0,6*np.pi)
g1.set_ylim(-2,10)


x_data=np.linspace(0,6*np.pi,100)
y_data=[np.sin(x) for x in x_data]
u_data=np.linspace(0,6*np.pi,100)
v_data=[np.sin(x) for x in x_data]

c1,=g1.plot(x_data,y_data,"r-")
c2,=g1.plot(u_data,v_data,"b-")

def rota(x,y,angle):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array(((c, -s), (s, c)))
    rx,ry=[],[]
    for i in range(len(x)):
        rx.append(c*x[i]-s*y[i])
        ry.append(s*x[i]+c*y[i])
    return rx,ry
    

def frame(i):
    y_data=[np.sin(i-x) for x in x_data]
    rx,ry=rota(x_data,y_data,np.pi/3)
    c1.set_data(rx,ry)
    v_data=[np.sin(i-x) for x in x_data]
    c2.set_data(u_data,v_data)
    return c1, c2

animation=FuncAnimation(f,frame,frames=np.linspace(0,6*np.pi,100),interval=50)

plt.show()


