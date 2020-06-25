# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 02:30:11 2020

@author: click
"""

from math import *
import matplotlib.pyplot as plt
from numpy import *



x=linspace(0,10)

plt.plot(cos(x),label="cos(x)")
plt.plot(cos(x+0.1),label="cos(x+0.1)")
plt.plot(cos(x-0.1),label="cos(x-0.1)")
plt.legend()
plt.show()