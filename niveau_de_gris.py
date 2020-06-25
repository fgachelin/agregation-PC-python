'''
Author: Francois Gachelin

Page démo matplotlib

* Utiliser add_axes pour positionner précisément les graphiques
* sub_plot ne permet pas facilement le positionnement
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

ddm=3
t_data=np.linspace(0,10,500)
y_data=[1+(np.cos(2*t)) for t in t_data]
img_data=[[np.sin(k*x*y) for x in np.linspace(-10,10,200)]for y in np.linspace(-10,10,200)]





a=[[3+np.cos(t) for _ in range(100)]for t in np.linspace(-10,10,500)]
b=[[3+np.cos(t) for _ in range(100)]for t in np.linspace(-10,10,500)]

f=plt.figure()

g=f.add_axes([0,0.2,0.5,0.6])
g.set_title("gauche")
g.yaxis.set_visible(False)
g.xaxis.set_visible(False)
g.imshow(a,cmap="gray",vmin=0,vmax=20)

h=f.add_axes([0.5,0.2,0.5,0.6])
h.set_title("droite")
h.yaxis.set_visible(False)
h.xaxis.set_visible(False)
h.imshow(b,cmap="gray_r",vmin=0,vmax=10)

'''

f=plt.figure()
f.suptitle("chouette alors!")

g1=f.add_axes([0.2,0.2,0.6,0.68])
a,=g1.plot(t_data,y_data,"r-",label=r"$1+cos(2\delta)$")
b,=g1.plot(t_data,x_data,"b-",label="$cos(SM_1)+cos(SM_2)$")
plt.legend()


'''

'''
f,a=plt.subplots()
f.suptitle(r"$E=\frac{1}{2}mv^2$",fontsize=20)

g0=plt.subplot(131,label="g0")
g0.set_title("g0",fontsize=18)
g0.set_xlabel("$t$",fontsize=16)
g0.set_ylabel(r"$\lambda$",rotation=0,fontsize=16)
gx,=g0.plot(t_data,x_data,"r-+")
gy,=g0.plot(t_data,y_data,"g-+")
plt.subplots_adjust(top=0.9)#margin-bottom ou top, toujours en hauteur relative partant du bas

g1=plt.subplot(132)
g1.set_title("g1",fontsize=16)
g1.plot(x_data,y_data)

g2=plt.subplot(133)
g2.set_title("PsyTime")
g2.imshow(img_data,cmap="rainbow")

#curseur pour valeur de k dans img_data
ax_k=plt.axes([0.2,0.01,0.6,0.02])
s_k=Slider(ax_k,"k",0.1,50)
def maj(val):
    k=val
    img_data=[[np.sin(k*x*y)*np.exp(-x**2/10)*x**2 for x in np.linspace(-10,10,200)]for y in np.linspace(-10,10,200)]
    g2.imshow(img_data,cmap="rainbow")
s_k.on_changed(maj)

#redéfinit line2D gy
gy.set_ydata(z_data)

plt.legend()
plt.show()
'''
