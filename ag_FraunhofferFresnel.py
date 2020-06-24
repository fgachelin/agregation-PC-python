'''

Remarque
La diffraction de Fresnel aurait du montrer des interférences desctructructives pour certaines valeurs de z

'''


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
#from matplotlib.animation import FuncAnimation

points_source=601
points_ecran=2001

#paramètres
D=0.5
a=1e-3
largeur_écran=100*a*D
lamb=633e-9
#fin paramètres


list_x=np.linspace(-a/2,a/2,points_source)
list_X=np.linspace(-largeur_écran/2,largeur_écran/2,points_ecran)

def intensité(X,source,D):
    amplitude=0
    for x in source:
        distance=(D**2+(x-X)**2)**0.5
        amplitude=amplitude+np.exp(1j*2*np.pi*distance/lamb)/distance
    return (np.absolute(amplitude))**2

m=max(intensité(list_X,list_x,D))
g1=plt.subplot(111)
plt.subplots_adjust(bottom=0.15)#margin-bottom
F=(str(a*a/(4*D*lamb)))[0:4]
affichage=r"$F=\frac{a^2}{\lambda D}=$"+F+"\nD="+(str(D))[0:4]+"m\na=1,00mm"
txt=g1.text(list_X[0],0.8,affichage)
g1.set_xlabel(r"$d(m)$",fontsize=20, labelpad=0)
g1.set_ylabel(r"$\frac{I}{I_{max}}$",rotation=0,fontsize=20, labelpad=20)
ligne,=g1.plot(list_X,intensité(list_X,list_x,D)/m)#pour rafraichir le graphique
g1.set_title("Diffraction Fresnel- diffraction de Fraunhoffer",fontsize=20)


axD=plt.axes([0.2,0.01,0.6,0.02])
cD=Slider(axD,"$D$",-3,1)

def maj(_):
    D=5*10**cD.val
    largeur_écran=100*a*D
    list_X=np.linspace(-largeur_écran/2,largeur_écran/2,points_ecran)
    m=max(intensité(list_X,list_x,D))#pour normaliser y
    ligne.set_data(list_X,intensité(list_X,list_x,D)/m)
    g1.set_xlim(list_X[0],list_X[-1])#car pas de redimensionnement automatique avec set_data
    F=(str(a*a/(4*D*lamb)))[0:4]
    affichage=r"$F=\frac{a^2}{\lambda D}=$"+F+"\nD="+(str(D))[0:5]+"m\na=1,00mm"
    #g1.set_title(affichage)
    txt.set_position([0.9*list_X[0],0.8])
    txt.set_text(affichage)

cD.on_changed(maj)

plt.show()