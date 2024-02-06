# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 15:03:25 2022

@author: Niko
"""

import numpy as np;
import linsolve;

def bar_conductance(kb):
    """Returns the bar conductance matrix given by the relation [𝑘] = 𝑘𝑏 [1,−1;−1,1]
    
    kb is the input for the function which contains 𝑘𝑏
    [𝑘] is the output, the conductance matrix as a NumPy array """
    return np.array([[kb,-1*kb],[-1*kb,kb]]);
def assemble_conductance(kmat, K, connect_bar):
    """Assembles the bar’s conductance matrix into the structure conductance matrix

    input: kmat is the bar’s conductance matrix, K is the structure’s conductance matrix, and connect_bar is a numpy integer array containing the node number for the bar.
    output: there is no output, function modifies input K
    """
    low= min(connect_bar[0]-1,connect_bar[1]-1);
    high = max(connect_bar[0]-1,connect_bar[1]-1);
    K[low][low]+= kmat[0][0];
    K[high][low]+= kmat[1][0];
    K[low][high]+= kmat[0][1];
    K[high][high]+= kmat[1][1];

def solve_truss_temperature(conduct, connect, Q):
    """Returns the solved temperature vector for a given truss problem
    
    Inputs: conduct is an array of bar conductance (𝑘𝑏) for each bar, connect is a numpy matrix containing the node connections for each bar, Q is an array containing the external heat fluxes at every node. 
    output: temperature array T containing the solved temperature at every node"""
    k = np.zeros((len(Q),len(Q)),float);
    
    for i in range(len(connect)):
        assemble_conductance(bar_conductance(conduct[i]), k, connect[i]);
    T=np.zeros(len(Q));
    c=1;
    #print(k);
    for j in linsolve.solve(k[1:len(Q),1:len(Q)],Q[1:len(Q)]):
        T[c]=j;
        c+=1;
    return T;


#conduct=np.load("conduct.npy");
#conduct =np.array([1.,2,3,4,5,6,7]);
#connect=np.array([[1,2],[1,3],[2,3],[3,4],[2,4],[4,5],[3,5]]);
#Q=np.array([0.,0,0,0,20]);

conduct = np.array([bar_conductance(10) for _ in range(4)])
connect = np.array([[1,2],[2,3],[3,4],[4,5]])
Q = np.array([0,2500,0,-200,0])

T_truss=solve_truss_temperature(conduct, connect, Q);
print(T_truss);
