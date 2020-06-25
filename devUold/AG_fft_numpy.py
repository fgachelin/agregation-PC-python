# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 02:07:27 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np

'''
#modulation de fréquence

def fm(t,f):
    return np.sin(2*np.pi*(1.5+np.sin(2*np.pi*f*t))*t)

n=1

for mod in [0.0001,0.001,0.01]:
    t=np.linspace(-20,20,800)
    tf=np.fft.fft(fm(t,mod))
    fq=np.fft.fftfreq(800,0.05)
    g=plt.subplot(3,2,n)
    g.plot(t,fm(t,mod))
    h=plt.subplot(3,2,n+1)
    h.plot(fq,tf.real)    
    n=n+2
    
plt.suptitle("FFT modulation de fréquence")
plt.show()

'''
#paquet d'onde

f=1

def s(t,l):
    return np.sin(2*np.pi*f*t)*np.exp(-l*t**2)
    
n=1

for l in [1,0.1,0.01]:
    t = np.linspace(-25,25,500)
    sp = np.fft.fft(s(t,l))
    freq = np.fft.fftfreq(500,0.1)
    
    h=plt.subplot(3,2,n)
    h.plot(t,s(t,l),label=str(l))
    h.set_xlabel("fréquence (Hz)")
    h.legend()
    
    g=plt.subplot(3,2,n+1)
    g.plot(freq, sp.real/100,label="TF")
    g.legend()
    g.grid()
    g.set_xlabel("fréquence (Hz)")
    g.set_xlim([0,2])
    
    n=n+2
    
plt.suptitle("Transformée Fourrier paquet d'onde")
plt.show()

