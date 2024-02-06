# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 23:51:08 2022

@author: Niko
"""
from math import pi, sin, cos, atan, tan;
from find_root import bisection;
import matplotlib.pyplot as plt;
import numpy as np;
def kepler_residual(E, M, e):
    """computes the residual function of M = E-esin(E)

    Inputs: float 𝐸 the eccentric anomaly (radians), float 𝑀 the mean anomaly (radians), and float 𝑒 the eccentricity
    Outputs: a float describing the residual of the kepler function"""
    return (M-E+e*sin(E));

a = 1.325313;
e = 0.25571;
T = 1.525;
wave = 2*pi/T;
t0=0;
tn = 1.5;
M = lambda t: wave*t;
itter = 100;
ti=t0;
r=0;
theta=0;
if tn> 1:
    x= np.zeros(itter+1);
    y= np.zeros(itter+1);
else:
    x= np.zeros(itter);
    y= np.zeros(itter);
c=0;
while ti<=tn:
    Elo= M(ti)-1/2;
    Ehi= M(ti)+1/2;
    E = bisection(lambda E: kepler_residual(E, M(ti), e), Elo,Ehi);
    theta = 2*atan((((1+e)/(1-e))**(1/2)*tan((E/2))));
    r=a*(1-e*e)/(1+e*cos(theta));
    x[c]=r*cos(theta)
    y[c]=r*sin(theta)
    c+=1;
    ti+= (tn-t0)/itter;
if False:
    plt.figure(1, figsize=(6, 4));
    text = "r = "+ str(r)+ " AU \ntheta = "+ str(theta) + " rad";
    v=plt.plot(x,y,color = 'brown', label = text  );
    plt.axis([-2, 1.25, -2, 3])
    plt.plot(0,0,"oy", ms= 14, label = "Sun");
    plt.plot(r*cos(theta), r*sin(theta),"or", label = "Roadster" );
    plt.legend(loc = 'upper right');
    plt.title( "Position of Tesla Roadster (hamiln)" , fontsize=14)
    plt.xlabel("X (AU)"        , fontsize=12)
    plt.ylabel("Y (AU)", fontsize=12)
    plt.savefig('hw05_plot.png', dpi=300, edgecolor='none')
    plt.show();
    