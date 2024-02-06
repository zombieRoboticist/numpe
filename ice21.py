# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:59:25 2022

@author: Niko
"""

import numpy as np;

u = np.array([0.5, (-.6),1.3]);
mag2 = 0;
#compute dot product
for i in range(len(u)):
    mag2+= (u[i]*u[i]);
#compute magnitude
mag2 **= .5;
#normalize vector
for i in range(len(u)):
    u[i]/=mag2;
print(u);
