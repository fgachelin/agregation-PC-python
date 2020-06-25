# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 01:07:24 2020

@author: click
"""

import matplotlib.pyplot as plt
import numpy as np


def norme(vec,p):
    s=0
    for x in vec:
        s=s+x**p
    return s**(1/p)

v1=[1,1,1]

v2=[2,2,2]

vi=[1,5,3]


p=[_ for _ in range(1,20)]
n=[]

for i in p:
    n.append(norme(vi,i))
    
plt.scatter(p,n)
plt.show()
        