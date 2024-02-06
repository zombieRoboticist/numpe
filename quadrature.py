# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 12:35:10 2022

@author: Niko
"""
"""module for computing the numeric intgrals of functions"""

import numpy as np;

def midpoint(fvals, dx):
    """calculates the numeric integral of a function using the midpoint method
    
    inputs: fval is a 1d numpy array describing the function values, and dx a float describing the distance between each x vallue
    output: a float that describes the numeric intergral over the bounds xi to xf"""
    if dx<=0:
        raise ValueError ("dx must be grater than 0");
    out =0.0;
    for i in range(fvals.shape[0]):
        out+= fvals[i]*dx;
    return out;

def trapezoidal(fvals, dx):
    """calculates the numeric integral of a function using the trapexoidal method
    
    inputs: fval is a 1d numpy array describing the function values, and dx a float describing the distance between each x vallue
    output: a float that describes the numeric intergral over the bounds xi to xf"""
    if dx<=0:
        raise ValueError ("dx must be grater than 0");
    out =0.0;
    for i in range(fvals.shape[0]-1):
        out+= (fvals[i]+fvals[i+1])/2*dx;
    return out;

def gauss_quad(func, numpts, a=-1, b=1):
    """calculates the numeric integral of a function using the Gauss-Legendre Quadrature method
    
    Inputs: func is a Python function that describes a math function, numpts is a scalar that describes the number of nodes to evaluate the integral at 0<numpts<4, a and b define the lower and upper integration limits respectively
    Output: a float that describes the numeric intergral over the bounds a to b"""
    if not (numpts ==1 or numpts ==2 or numpts==3):
        raise ValueError ("numpts must be an integer in the range 0 < numpts < 4");
    elif (a>= b):
        raise ValueError("a must be less than b");
    else:
        x= lambda x0: (b-a)/2*x0+(b+a)/2;
        coef= [[2],[1,1],[8/9.,5/9.,5/9.]];
        xs=[[0],[-1/(3.**.5),1/(3.**.5)],[0, -(3/5.)**.5, (3/5.)**.5]];
        temp=0.0;
        for i in range(numpts):
            temp+= coef[numpts-1][i]*func(x(xs[numpts-1][i]));
        temp*= (b-a)/2.
        return temp;

