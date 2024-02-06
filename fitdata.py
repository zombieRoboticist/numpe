# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 11:58:06 2022

@author: Niko
"""
import numpy as np;

"""Module for calculating the line of best fit for a data set using qr factorization and back substitution"""

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
        x[n-1-i]/=lu[n-1-i][n-i-1]
    return x;

def calc_fit(xdata, ydata, degree=1):
    """finds the coefficients for a line of best fit which is a polinomial of degree degree for the data set (xdata,ydata)
    
    Inputs: 1d numpy arrays xdata and ydata which describe the x and y vallues of the data set respectively and dergree which determines the highest power of x in the line of best fit
    Output: a 1d numpy array which describes the coeeficient matrix from least to greatest power of x.
    """
    assert xdata.ndim ==1, "xdata must be a 1D vector";
    assert ydata.ndim ==1, "ydata must be a 1D vector";
    assert xdata.shape[0] == ydata.shape[0], "xdata must have the same number of rows as ydata";
    assert degree>=0, "degree must be larger than or equal to 0";
    assert type(degree) == int, "degree must be an interger"
    
    A = np.ones((len(xdata),degree+1));
    for i in range(degree+1):
        for j in range(len(xdata)):
            A[j][i]*= xdata[j]**i;
    q, r = np.linalg.qr(A.copy()) ;
    return back_sub(r, np.dot(np.transpose(q), ydata));

def eval_fit(coeff, xdata):
    """evaluates the polinomial described by the coeff at the points xdata
    
    Input: 1d numpy arrays coeff and xdata which describe the coefficients of the terms in the polinomial and the x vallues to evaluate the polinomial at respectively
    output: a 1d numpy array describing the y vallues of the polinomial described by coeff evaluated at the x vallues xdata
    """
    assert xdata.ndim ==1, "xdata must be a 1D vector";
    assert coeff.ndim ==1, "coeff must be a 1D vector";
    
    y=np.zeros(len(xdata));
    for i in range(len(xdata)):
        for j in range(len(coeff)):
            y[i]+= coeff[j]*xdata[i]**j;
    return y;


# tdata,sdata = np.loadtxt('sea-level-data.txt',     skiprows=50, usecols=(2,8), unpack=True)
# print(calc_fit(tdata,sdata,3))
# sdata = np.loadtxt(name,     max_rows=1, delimiter = ',',dtype=str, unpack=True)