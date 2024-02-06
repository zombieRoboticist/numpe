# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 12:42:55 2022

@author: Niko
"""
import numpy as np;

def back_sub (lu_fac, b):
    """ solves the equation LuX=b for X given the upper triangle matrix lu (lu_fac) and the solution vector b (b)
    
    input: a 2d numpy array desctibing an upper triangle matrix (lu_fac) and a 1d numpy arry describing the knows (b)
    output: a 1d numpy array describing the state varriables
    """
    assert lu_fac.ndim ==2, "lu_fac must be a 2D matrix";
    assert b.ndim ==1, "b must be a 1D vector";
    assert lu_fac.shape[0] == lu_fac.shape[1], "lu_fac must be a square (nxn) Matrix";
    assert b.shape[0]==lu_fac.shape[0], "b must have the same number of rows as lu_fac";
    
    lu=lu_fac.copy();
    x = np.zeros(b.shape[0]);
    for i in range(lu.shape[0]):
    
        n = x.shape[0]
        x[n-1-i]+=b[n-1-i]
        #print(n-1-i)
        for j in range(1,i+1):
            p=lu.shape[1]
            x[n-i-1]-= x[n-1-i+j]* lu[n-1-i][p-1-i+j];
            #print(p-1-i+j)
            #print(n-1-i+j)
            #print(p-1-i)
        assert lu[n-1-i][n-i-1] >1.0e-15, "divide by zero error"
        x[n-1-i]/=lu[n-1-i][n-i-1]
    return x;