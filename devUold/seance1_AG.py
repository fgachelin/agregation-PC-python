#Séance AG ext  10/10/2019

from random import * 
import numpy as np
import matplotlib.pyplot as p



#p.hist(serie_aleatoire)
#p.show()


def f(x):
    return 1+np.sin(5*x)


def extremum_fonction(f,a,b):
    minis=[]
    maxis=[]
    pas=1000
    dx=(b-a)/pas
    
    x=[_/pas for _ in range(pas*a,pas*b)]
    dfdx=[f(i+dx)-f(i) for i in x[1:-1]]
    y=[f(i) for i in x]
    
    for i in range(len(dfdx[:-1])):
        if dfdx[i]*dfdx[i+1]<0:
            if dfdx[i]<0:
                minis.append(x[i])
            else:
                maxis.append(x[i])
    (minis,maxis)
    
    #pprint.plot(x[1:-1],dfdx,label="dfdx")
    p.plot(x,y)
    p.show()
    
extremum(f,0,5)
    
    