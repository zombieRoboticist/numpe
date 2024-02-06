# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:17:23 2022

@author: Niko
"""
import numpy as np;

data_array = np.load("data.npy");
bins = np.zeros(5);

for i in range(len(data_array)):
    temp =data_array[i];
    if (temp<185.0):
        bins[0]+=1;
    elif( (temp<195.0)and(temp>= 185.0)):
        bins[1]+=1;
    elif( (temp<205.0)and(temp>= 195.0)):
        bins[2]+=1;
    elif( (temp<215.0)and(temp>= 205.0)):
        bins[3]+=1;
    else:
        bins[4]+=1
        
for i in range(len(bins)):
    print( int(bins[i]));
        