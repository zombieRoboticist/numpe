# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 12:28:49 2022

@author: Niko
"""

"""Module for solving a linear system of equations"""

import numpy as np;

def forward_sub (lu_fac, b):
    """ solves the equation LuX=b for X given the lower triangle matrix lu (lu_fac) and the solution vector b (b)
    
    input: a 2d numpy array desctibing a lower triangle matrix (lu_fac) and a 1d numpy arry describing the knows (b)
    output: a 1d numpy array describing the state varriables
    """
    lu=lu_fac.copy();
    #print(lu)
    x = np.zeros(b.shape[0]);
    for i in range(lu.shape[0]):
        x[i]+=b[i]
        for j in range(i):
            x[i]-= lu[i][j]*x[j];
    return x;


"""
    xi = bn-i/lun-i,n-j-1 - sum (from x n-j=n/lu n-i,n-j-2 to xn-j=i/lun-i,n-j=i )
    or 
    for all xi
        xi= bi/lui,n
        for all n>j>i
            xi = xi -xj*lui,j
"""
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

def lu_factor(A, tol=1E-15):
    """ Takes in a nxn 2d array A and factors A into L and U such that A =LU
    
        input: a 2d numpy nxn array 
        output: none
    """
    U = A;
    L = A;
    #for 0<=j<= n-2
    for j in range(A.shape[0]-1):
        #for j+1<=i<n
        for i in range(j+1,A.shape[1]):
            #Lij = Uij/jj
            if (abs(U[j][j])<=tol):
                return False;
            L[i][j] = float(U[i][j])/ float(U[j][j]);
        # for j<i<n
        for i in range(j+1,A.shape[0]): 
            #for j<k<n
            for k in range(j+1,A.shape[0]):
                #Uik -= LijUlk
               U[i][k]-=L[i][j]*U[j][k];
    return True;
               
def solve(A,b):
    """ takes in an nxn 2d numpy array A and a 1d numpy array b ans solves the system of equations Ax=b for x

        input: a 2d numpy array describing the coeficient matrix and a 1d numpy array describing the solution vector
        output: a 1d numpy array describing the state varriables
    """
    a=A.copy()
    #print(A)
    if lu_factor(a):
        temp = forward_sub(a, b);
        out = back_sub(a, temp)
        # print(out)
        
        # print(a)
        return out;
    return False;



#n = np.array([[1,0,0],[2,1,0],[3,2,1]]);
#m =np.array([[5,4,3,2,1],[10,4,3,2,1],[10,7,3,2,1],[98,10,30,2,1],[5,70,1,4,12]],float);
#c= np.array([1,4,6,2,7]);
#print(forward_sub(n,c));
#print(back_sub(m, c));
#print(solve(m,c));