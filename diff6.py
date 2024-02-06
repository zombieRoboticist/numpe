# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 11:58:10 2022

@author: Niko
"""
import numpy as np;

"""Module for computing numeric derivatives"""

np.seterr(all='raise');

def finite_diff(t,y):
    """ approximates the values of the first derivative of a function from points t, y.
    
    Input: y is a 1D NumPy array of function values at t values, t is a 1D NumPy array of x values the function is evaluated at.
    Output: a 1d numpy array approximating the y' values"""
    
    if y.shape[0] != t.shape[0]:
        raise ValueError\
            ("t and y must be same size");
    yp = np.zeros_like(y);
    try:
        yp[0]= (y[1]-y[0])/(t[1]-t[0]);
        yp[yp.shape[0]-1]=(y[y.shape[0]-1]-y[y.shape[0]-2])/(t[t.shape[0]-1]-t[t.shape[0]-2]);
        #for i in range(y.shape[0]-2):
        #    yp[i+1]= (y[i+2]-y[i+1])*(t[i+1]-t[i])/(t[i+2]-t[i])/(t[i+2]-t[i+1])+(y[i+1]-y[i])*(t[i+2]-t[i+1])/(t[i+2]-t[1])/(t[i+1]-t[i]);
        for i in range(1, y.size - 1):
            yp[i] = ((t[i] - t[i-1])/(t[i+1] - t[i-1]) * (y[i+1] - y[i])/(t[i+1]-t[i])) + ((t[i+1] - t[i])/(t[i+1] - t[i-1]) * (y[i] - y[i-1])/(t[i] - t[i-1]))
    except FloatingPointError:
        print("t values must be unique");
        raise;
    except:
        raise RuntimeError ("An error has occured")
    return yp;

def polynomial_derivative(coef, t):
        """calculates the numeric derivative of a function described by coef at the x value t.
        
        Inputs: a 1d numpy array coef which contains the coeficients of the polonomial function and t a float that is the x value to calculate the derivative at
        Outputs: a float that describes the derivative of the function at t"""
        yp =0.0;
        if(coef.shape[0]==0):
            raise RuntimeError ("coef must not have size 0");
        elif( coef.shape[0]>1):
            yp += coef[coef.shape[0]-1]*((coef.shape[0]-1));
            for i in range(coef.shape[0]-2, 0 ,-1):
                #print(coef, i)
                yp= (i*coef[i]+t*yp);
            if yp == 0:
                raise ValueError ("First derivative is zero");
            #yp+= coef[0];
        return yp;