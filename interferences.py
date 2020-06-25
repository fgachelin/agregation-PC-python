import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

#paramètres
ddm=0#différence de marche
lamb=5#longueur d'onde
amp_s1=0.5#amplitude source 1
amp_s2=5#amplitude source 2
#fin paramètres

k=2*np.pi/lamb

f=plt.figure()
f.suptitle("Interférences de deux ondes synchrones")

g1=f.add_axes([0.3,0.2,0.3,0.68])
g1.xaxis.set_visible(False)
g1.set_aspect('equal', adjustable='box')#repère orthonormé
g1.set_xlim(0,d)
g1.set_ylim(-X_max,X_max)
#g1.yaxis.tick_right()#graduations à droite
s1,=g1.plot(0,s1y,"r+")
s2,=g1.plot(0,s2y,"b+")


#g2=plt.subplot(122)
g2=f.add_axes([0.5,0.2,0.2,0.68])
g2.yaxis.set_visible(False)
g2.xaxis.set_visible(False)

x_data=np.linspace(0,1.5*d,500)
y_data=[np.sin(k*x)+s1y for x in x_data]
v_data=[np.sin(k*x)+s2y for x in x_data]

c1,=g1.plot(x_data,y_data,"r-")
c2,=g1.plot(x_data,v_data,"b-")


def rota(x,y,angle,decalage_vertical):
    c, s = np.cos(angle), np.sin(angle)
    R = np.array(((c, -s), (s, c)))
    rx,ry=[],[]
    for i in range(len(x)):
        rx.append(c*x[i]-s*y[i])
        ry.append(s*x[i]+c*y[i]+decalage_vertical)
    return rx,ry

def intensité(x,s1y,s2y):
    
    MS_1=((x-s1y)**2+d**2)**0.5
    MS_2=((x-s2y)**2+d**2)**0.5
    delta=((x-s1y)**2+d**2)**0.5-((x-s2y)**2+d**2)**0.5#différence de marche
    return (amp_s1)**2+(amp_s2)**2+(2*amp_s1*amp_s2)*np.cos(2*np.pi*delta/lamb)

img_data=[[intensité(x,s1y,s2y) for _ in range(10)] for x in np.linspace(-X_max,X_max,500)]
img=g2.imshow(img_data,cmap="gray",vmin=0,vmax=amp_s1**2+amp_s2**2+2*amp_s1*amp_s2) 

def frame(i):
    s1x,s1y,s2x,s2y=0,a/2,0,-a/2
    k=2*np.pi/lamb
    angle1,angle2=np.arctan((X-s1y)/d),np.arctan((X-s2y)/d)
    
    y_data=[amp_s1*np.sin(k*x-i) for x in x_data]
    rx,ry=rota(x_data,y_data,angle1,s1y)
    c1.set_data(rx,ry)
    
    v_data=[amp_s2*np.sin(k*x-i) for x in x_data]
    ru,rv=rota(x_data,v_data,angle2,s2y)
    c2.set_data(ru,rv)
    
    s1.set_ydata(s1y)
    s2.set_ydata(s2y)    
    #return c1, c2... est inutile

animation=FuncAnimation(f,frame,frames=np.linspace(0,2*np.pi,10),interval=100)


axX=plt.axes([0.2,0.01,0.6,0.02])
sX=Slider(axX,"$X$",-X_max,X_max)
axlamb=plt.axes([0.2,0.04,0.6,0.02])
slamb=Slider(axlamb,r"$\lambda$",2,10)
axa=plt.axes([0.2,0.07,0.6,0.02])
sa=Slider(axa,r"$a$",0,30)

def maj(_):
    global X
    global lamb
    global a
    global img
    X,lamb,a=sX.val,slamb.val,sa.val

    img_data=[[intensité(XX,a/2,-a/2) for _ in range(2)] for XX in np.linspace(-X_max,X_max,200)]
    img.set_data(img_data)

sX.on_changed(maj)
slamb.on_changed(maj)
sa.on_changed(maj)


plt.show()



#animation.save('interferencesConstructives.gif', dpi=80, writer='imagemagick')