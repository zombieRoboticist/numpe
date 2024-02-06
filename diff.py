# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:38:37 2022

@author: Niko
"""
"""Module to compute numerical derivatives"""

import numpy as np;
from math import factorial;

def finite_diff(y, h=1.0):
    """ approximates the values of the first derivative of a function from equidistant (h) points y.
    
    Input: y is a 1D NumPy array of function values at uniformly spaced x values, h is the uniform change in x that defaults to 1.0.
    Output: a 1d numpy array approximating the y' values"""
    
    if h <= 0:
        raise ValueError\
            ("h should be a positive number");
    yp = np.zeros_like(y);
    yp[0]= (y[1]-y[0])/h;
    yp[yp.shape[0]-1]=(y[y.shape[0]-1]-y[y.shape[0]-2])/h;
    for i in range(y.shape[0]-2):
        yp[i+1]= (y[i+2]-y[i])/(2*h);
    return yp;

#print(finite_diff(np.array([1,0,1,4,9])));
def fd_formula(x, deriv=1):
    """Computes the coefficients of the taylor series expansion from 0th order to qth order derivatives about x=x0.

    
    note: user must shift data to be about point you want to take the derivative at
    Input: x is a 1D NumPy array containing the x values, deriv indicates the order of the derivative (deriv=q)
    Output: a 1D Numpy array of coefficients of the taylor series expansion from 0th order to qth order derivatives"""
    if type(deriv) != int:
        raise TypeError \
            ("The order of a derivative must be an integer")
    if deriv < 0:        
        raise ValueError \
            ("must have an order of a derivative greater than or equal to 0")
    if deriv > x.size-1:
        raise ValueError\
            ("must have more points than the order of the derivative")
    m = np.zeros((x.shape[0],x.shape[0]));
    for i in range(x.shape[0]):
        for j in range(x.shape[0]):
            m[i][j] = x[j]**i;
    q= np.zeros(x.shape[0]);
    q[deriv]= factorial(deriv);
    return np.linalg.solve(m,q);


#print(fd_formula(np.array([-1., 0., 1.]), deriv=1))
#print(fd_formula(np.array([0., 1., 3.]), deriv=2))