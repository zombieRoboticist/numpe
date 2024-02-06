# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:11:07 2022

@author: Niko
"""
"""Module for calculating the solutions to a overdetermined linear system of equations"""


import numpy as np;
import linsolve;

def solve_ls(A,b):
    """ Solve an overdetermined linear system of equations for X
    
        Inputs: a 2d numpy array A that describes the coeficient matrix and a 1d numpy array b that sdescribes the solution vector
        Output: a 1d numpy array that describes the vector X
    """
    q, r = np.linalg.qr(A.copy()) ;
    #print(q);
    #print(r);
    #print(np.transpose(q))
    return linsolve.back_sub(r, np.dot(np.transpose(q), b));
#solve_ls(np.array([[1,2],[2,7],[5,2]]),np.array([3,4,6]));