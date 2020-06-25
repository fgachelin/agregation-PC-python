from matplotlib import pyplot as p
import numpy as np
from math import *

m=1
k=1
tau=10

w=(k/m)**0.5

t=[0.1*i for i in range(200)]

def f(x):
    return cos(w*x)*e**(-x/tau)


x=[f(i) for i in t]

p.figure()

p.polar(1,1)

p.show()


'''
p.subplot(211)
p.plot(t,x, color='tab:blue')
#p.plot(t2, f(t2), color='black')

p.subplot(212)
p.plot(x, np.gradient(x,t), color='tab:orange')
p.show()
'''