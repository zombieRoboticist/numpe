# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 12:13:18 2022

@author: Niko
"""
import numpy as np;


def dot_product(a,b):
    """ Takes a dot product of 2 vectors

        Input: vectors a and b of equal size
        Output: scalar vallue of the dot product of the input vector 
    """
    temp = 0;
    if (len(a)==len(b)):
        for i in range(len(a)):
            temp+=a[i]*b[i];
        return temp;
    return None

def cross_product(a,b):
    """ takes the cross product of 2 3 domentional vectors

        Input: 2 3d vectors a and b
        Output: 1 3d vector that is the cross producto of those vectors
    """
    c=np.zeros(3);
    c[0]= a[1]*b[2]-b[1]*a[2];
    c[1]= a[2]*b[0]-b[2]*a[0];
    c[2]= a[0]*b[1]-b[0]*a[1];
    return c;

def moment_about_point(force,vP,vO):
    """"finds the moment of a force acting about point O

        Input: 3 3d vectors (force vector force, position vector of point P vP, position vector of point O vO)
        Output: 1 3d vector describing the moment about point o
    """
    r = np.zeros(len(vP));
    for i in range(len(vP)):
        r[i]=vP[i]-vO[i]; 
    return cross_product(r, force);

def moment_about_axis(force, r, u):
    """ finds the scalar product that describes the moment aboutan axis

        Input 3 3d vectors (the force vector (force), the position vector descring the radius of rotation(r), and the vector describing the direction of the axis (u))
        Output: the scalar product of the 3 vectors
    """
    temp = cross_product(r,force);
    uh=unit(u);
    return dot_product(temp,uh);
def unit(v):
    """finds unit vector of given vector
    
    
    """
    mag = dot_product(v,v)**.5;
    for i in range(len(v)):
        v[i]/=mag;
    return v;

uF = [[0.70014, -0.70014, -0.14003], [0.57735, -0.80829, -0.11547], [-0.37139, 0.928477, 0], [-0.28735, 0.957826, 0], [-0.0995, 0.995037, 0],[0, 1, 0]];

F = np.array([20000, 20000, 15000, 15000, 15000, 15000]);


vF=np.zeros((len(uF),len(uF[0])));
for i in range(len(F)):
    for j in range(len(uF[i])):
        vF[i][j]=F[i]*uF[i][j];    
#print(vF);

P = np.array([[95, -2.6, -25],[90, -3.2, -20],[-75, -30, 2.5],[-80, -30, 2.5],[-85, -30, 2.5],[-90, -30, 2.5]]);
#print(P)
O = np.zeros(3);
U = [1.0,0.02,0.11];

T_u=0;
M_O= np.zeros(3)
for i in range(len(vF)):
    T_u+= moment_about_axis(vF[i],P[i],U);
    temp = moment_about_point(vF[i],P[i],O);
   # print(temp);
    for j in range(len(M_O)):
        M_O[j]+=temp[j];
print(T_u);
print(M_O);