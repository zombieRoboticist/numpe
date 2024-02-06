# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 14:18:14 2022

@author: Niko
"""

import numpy as np;
A = np.load("matrix.npy")
x = np.load("vector.npy")
#A = np.array([[1,2,3],[4,5,6],[7,8,9]]);
#x= np.array([6,4,7]);
y = np.zeros(A.shape[0]);
for i in range(A.shape[0]):
    for j in range(A.shape[1]):
        y[i] += A[i][j]*x[j];
np.save("result.npy", y);