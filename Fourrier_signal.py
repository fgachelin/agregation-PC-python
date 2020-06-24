
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 15:07:51 2020

@autheur: Fançois Gachelin

p entier
créneau: 1/(2p+1)
triangle: 1/(2p+1)**2
sweep:
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

t=np.linspace(0,4,500)

fig=plt.figure()
fig.suptitle("Signal pur, signal complexe")

g1=fig.add_axes([0.1,0.6,0.8,0.2])
g1.set_ylim(-3,3)

w=2*np.pi
'''
l1,=g1.plot(0)
l2,=g1.plot(0)
l3,=g1.plot(0)
l4,=g1.plot(0)
l5,=g1.plot(0)
'''
l,=g1.plot(t,np.sin(w*t))

ax1=fig.add_axes([0.1,0.1,0.5,0.01])
ax2=fig.add_axes([0.1,0.2,0.5,0.01])
ax3=fig.add_axes([0.1,0.3,0.5,0.01])
ax4=fig.add_axes([0.1,0.4,0.5,0.01])
ax5=fig.add_axes([0.1,0.5,0.5,0.01])

s_a1=Slider(ax1,"$A_1$",-1,1,1)
s_a2=Slider(ax2,"$A_2$",-1,1,0)
s_a3=Slider(ax3,"$A_3$",-1,1,0)
s_a4=Slider(ax4,"$A_4$",-1,1,0)
s_a5=Slider(ax5,"$A_5$",-1,1,0)

def maj(x):#noter argument x même si on n'en fait rien
    global l
    global l1
    global l2
    global l3
    global l4
    global l5
    a1=s_a1.val
    a2=s_a2.val
    a3=s_a3.val
    a4=s_a4.val
    a5=s_a5.val

    w=2*np.pi
    def f(x):
        return a1*sin(w*x)+a2*sin(2*w*x)+a3*sin(3*w*x)+a4*sin(4*w*x)+a5*sin(5*w*x)
    
    y=[f(_) for _ in t]
    '''
    y1=[a1*sin(w*_) for _ in t]
    y2=[a2*sin(2*w*_) for _ in t]
    y3=[a3*sin(3*w*_) for _ in t]
    y4=[a2*sin(4*w*_) for _ in t]
    y5=[a3*sin(5*w*_) for _ in t]
    '''
    l.set_ydata(y)
    '''
    l1.set_ydata(y1)
    l2.set_ydata(y2)
    l3.set_ydata(y3)
    l4.set_ydata(y4)
    l5.set_ydata(y5)
    '''


s_a1.on_changed(maj)
s_a2.on_changed(maj)
s_a3.on_changed(maj)
s_a4.on_changed(maj)
s_a5.on_changed(maj)

plt.show()
