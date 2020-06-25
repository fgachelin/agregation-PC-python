from matplotlib import pyplot as p
import numpy as np
from math import *

dt=0.25
t_min=0
t_max=20

m=1
k=1
tau=10
w=(k/m)**0.5


f_expression="cos(w*t)*e**(-t/tau)"

def f(t):
    return eval(f_expression) 

t=[i*dt for i in range(int((t_max-t_min)/dt))]
x=[f(i) for i in t]
dxdt=np.gradient(x,t)

p.figure()

p.clf()
p.show()

p1=p.subplot(311)
p1.set_xlim(0,t_max)
p1.set_ylim(-2,2)
p1.grid()

p2=p.subplot(313)
p2.set_xlim(-1,1)
p2.set_ylim(-1,1)
p2.grid()


p3=p.subplot(313,projection='polar')

p.legend()


for i in range(len(t)):
    p.subplot(311)
    p.plot(t[i],f(t[i]),linestyle = 'none', marker = 'o',color = 'blue',markersize='2',label="X(t)")

    p3.cla()
    p3.set_theta_zero_location("S")
    p3.set_rmax(2)
    p3.set_thetalim(-45,45)
    p3.scatter(x[i],1)
    
    p.subplot(312)
    p.plot(x[i],dxdt[i],linestyle = 'none', marker = 'o',color = 'green',markersize='2',label="Portait de phase")
    
    p.pause(0.002)

    



"""
#définitions des fonctions

tps=[i*dt for i in range(int((t_max-t_min)/dt))]

x=[f(t) for t in tps]

vitesse=np.gradient(x,tps)

Ec=[0.5*m*v**2 for v in vitesse]

Epp=[0.5*k*f(t)**2 for t in tps]

Em=[Ec[i]+Epp[i] for i in range(len(Ec)) ]

#représentations graphiques

#p.plot(tps,x,label=f_expression)

p.plot(tps,Ec,label="Ec")

p.plot(tps,Epp,label="Epp")

p.plot(tps,Em,label="Em")

#Annotations

p.xlabel("t(s)")

p.legend()

p.grid()

p.title("Youpi je sais dériver")

p.show()

"""