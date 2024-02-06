# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 12:27:43 2022

@author: Niko
"""
import numpy as np;

def interpolate(xdata, ydata, xeval):
    """ interpolates the function defined by the points xdata, ydata at the points xeval using lagrange interplation.
    
    Input: xdata and ydata are 1d numpy arrays containing the x and y values to interpolate from, xeval is a NumPy 1d array of x values to evaluate the function.
    Output: a 1d numpy array containing the interpolated values of the function
"""

    assert xdata.ndim == 1, "xdata must be a 1d numpy array";
    assert ydata.ndim == 1, "ydata must be a 1d numpy array";
    assert xeval.ndim == 1, "Xeval must be a 1d numpy array";
    if xdata.shape[0]!=ydata.shape[0]:
        raise ValueError  \
            ("xdata and ydata should have the same length");
    yeval=np.zeros(xeval.shape[0]);
    for i in range(xeval.shape[0]):
        #ls = np.ones(xdata.shape[0]);
        for j in range(xdata.shape[0]):
            l=1;
            for k in range(xdata.shape[0]):
                if k!= j:
                    if xdata[k]==xdata[j]:
                        raise ZeroDivisionError \
                            ("cannot have 2 same x values in xdata");
                    l*= (xeval[i]-xdata[k])/(xdata[j]-xdata[k]);
            yeval[i]+= ydata[j]*l;
    return yeval;