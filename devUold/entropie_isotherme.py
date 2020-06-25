from math import *
import matplotlib.pyplot as p
import numpy as np


def s(vi,vf):
    return 8.314*(log(vf/vi)-(vi-vf)/vf)


vi=1
vf=5

x=[0.1*_ for _ in range(1,10*vf)]
y=[s(vi,v) for v in x]

dv=0.1
y_palier=[s(vi,0.0001)]
'''
for i in range(1,50):
    v=
    y_palier.append(s(y_palier[i-1]))
'''

p.plot(x,y,color='red')
p.plot(x,y_palier,color='green')
p.xlim(0,5)
p.ylim(0,20)
p.grid()
p.show()