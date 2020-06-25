import matplotlib.pyplot as pp


#divers outils...
def cherche_maximums(liste_x,liste_y):
    '''
    Retourne les abscisses x des maximums locaux de y
    '''
    resultats=[]
    ecarts=[liste_y[i+1]-liste_y[i] for i in range(len(liste_x)-1)]
    for i in range(len(ecarts)-1):
        if ecarts[i]*ecarts[i+1]<0 and ecarts[i]>0:
            resultats.append(liste_x[i])
    return resultats

def période(liste_max):
    '''
    retourne la moyenne des écarts entre les maximums locaux
    '''
    périodes=[liste_max[i+1]-liste_max[i] for i in range(len(liste_max)-1)]
    somme=0
    for i in périodes:
        somme=somme+i
    return somme/len(périodes)
        
        
#équations différentielles
# tout est normalisé: l=1, m=1, g=1 pour un pendule par exemple


Q=1  #fateur de qualité
angle_initial=30   #en degrés


def exact_amorti(x,xp):
    '''
    Solution non linéaire de l'oscillateur amorti avec amortissement en 'dérivée première'
    '''
    return -sin(x)-xp/Q
    #k=0.87 return -sin(x)-k*(xp)**2

def exact_non_amorti(x,xp):
    return -sin(x)

def approché_non_amorti(x,xp):
    return -x

def resolution(acceleration,commentaire):
    t=[0]
    o=radians(angle_initial)
    x_t=[o]
    xn_t=[1]   #angle normalisé
    xp_t=[0]
    xpp_t=[acceleration(x_t[0],xp_t[0])]
    h=0.02
    n=0
    while n<1000:
        '''
        algorithme plus stable que celui d'Euler
        d'après https://femto-physique.fr/omp/euler.php#Roussel:2015
        '''
        x=x_t[-1]+h*xp_t[-1]+0.5*h**2*xpp_t[-1]
        xp=xp_t[-1]+0.5*h*(xpp_t[-1]+acceleration(x,xp_t[-1]))
        xpp=acceleration(x,xp)
        x_t.append(x)
        xn_t.append(x/o)
        xp_t.append(xp)
        xpp_t.append(xpp)
        n=n+1
        t.append(n*h)
        
    return t,xn_t

    '''Pour tracer vitesse(t)
    pp.plot(t,xn_t,label=commentaire)
    pp.legend()
    pp.show()
    '''
    '''
    #Poir tracer les portraits de phases
    pp.plot(x_t,xp_t,label=commentaire)
    pp.legend()
    pp.show()
    
    '''
    '''
    #Pour tracer les énergies
    E_caracteristique=1-cos(x_t[0])
    Ec=[(0.5*v**2)/E_caracteristique for v in xp_t]
    Ep=[(1-cos(o))/E_caracteristique for o in x_t]
    Em=[Ec[i]+Ep[i] for i in range(len(Ec))]
    pp.plot(t,Ec,color='green',label="Ec")
    pp.plot(t,Ep,color='blue',label="Ep")
    pp.plot(t,Em,color='red',label="Em")
    pp.ylabel("Energie")
    pp.xlabel("temps")
    pp.legend()
    pp.show()
    '''

'''facteur de qualité Q pour oscillateur amorti
for Q in [0.3, 0.71, 1, 2, 10]:
    resolution(exact_amorti,"Q = "+str(Q))
'''


# valeur de référence de la période=2pi
T_0=2*pi

for angle in [1,5,10,20,30,50,70,90]:
    angle_initial=angle
    xt, xp_exacte=resolution(exact_non_amorti,"sin(o) "+str(angle))
    xt, xp_approchée=resolution(approché_non_amorti,"(o) "+str(angle))
    
    
    #trace la période en fonction de l'angle
    T=période(cherche_maximums(xt,xp_exacte))
    dT=T-T_0
    pp.plot(angle,dT,marker='+',label=str(angle)+'°')
    pp.title("Influence de l'angle initial sur la valeur de la période, \neffet de la non-linéarité")
    pp.xlabel('angle(°)')
    pp.ylabel('T-T_réf')
    pp.legend()
    pp.show()
    
    '''
    #trace log(dT=T-T0)=f(log(o))
    T=période(cherche_maximums(xt,xp_exacte))
    pp.plot(log(angle),log(T-T_0),marker='+',label=str(angle)+'°')
    pp.plot(angle,T-T_0,marker='+',label=str(angle)+'°')
    pp.legend()
    pp.show()
    '''
    
    '''
    ecarts=[xp_approchée[_]-xp_exacte[_] for _ in range(len(xt))]
    pp.plot(xt,ecarts,label=str(angle))
    pp.title("Ecart entre solution linéaire et non linéaire pour différents angles initiaux")
    pp.legend()
    pp.show()
    '''
    
    '''
    #ne donne rien de bien ici...trop peu de périodes
    analsye_spectrale = np.fft.fft(ecarts)
    pp.plot(analsye_spectrale,label=str(angle))
    pp.xlim(990,1010)
    pp.legend()
    pp.show()
    '''
    
    #on visualise aussi l'isochronimse des petites oscillations
    #puis l'augmentation de la période avec l'angle initial
    

    
