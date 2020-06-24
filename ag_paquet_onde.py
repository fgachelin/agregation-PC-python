
from numpy import *
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#from matplotlib.animation import FuncAnimation

w,dw=3,3.05
k,dk=1,0.05

def signal(x,t,ddw,ddk):
    return cos((w+ddw)*t-x*(k+ddk))+cos((w-ddw)*t-x*(k-ddk)) 


x_data=linspace(0,200,500)
t_data=linspace(0,20,500)

dx=0.04

f=plt.figure()
f.suptitle("Modèle simplifié d'un paquet d'ondes")

g1=f.add_subplot(311)
#g1.set_title(r"Pas de dispersion$\frac{dv}{dw}=0$")
y1,=g1.plot(x_data,signal(x_data,0,0,0),"b-")
y11,=g1.plot(0,signal(0,0,0,0),"r+")

g2=f.add_subplot(312)
#g2.set_title(r"Dispersion $\frac{dv}{dw}>0$")
y2,=g2.plot(x_data,signal(x_data,0,dw,dk),"b-")
y22,=g2.plot(0,signal(0,0,dw,dk),"r+")

g3=f.add_subplot(313)
#g3.set_title(r"Dispersion $\frac{dv}{dw}<0$")
y3,=g3.plot(x_data,signal(x_data,0,dw,-dk),"b-")
y33,=g3.plot(0,signal(0,0,dw,dk),"r+")

plt.show()


x_1,x_2,x_3=100,100,100

for t in t_data:
    y1.set_data(x_data,signal(x_data,t,0,0))
    y2.set_data(x_data,signal(x_data,t,dw,dk))
    y3.set_data(x_data,signal(x_data,t,dw,-dk))
    
    '''
    x_1=x_1+w/k*dx
    y11.set_data(x_1,signal(x_1,t,0,0))
    x_2=x_2+(w+dw)/(k+dk)*dx
    y22.set_data(x_2,signal(x_2,t,dw,dk))
    x_3=x_3+(w-dw)/(k-dk)*dx
    y33.set_data(x_3,signal(x_3,t,dw,-dk))
    '''
    
    plt.pause(0.01)

