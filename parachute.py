"""Module for Parachute kinetic equations and variables"""

import numpy as np;
from math import nan;
import euler;
import time;


test_N = np.array([40,80,100,120]);
num_steps = 30; #number of steps
g = 9.81; #m/s^2 gravity
rho = 1.204; #kg/m^3 air density
h = 1.778; #m human height
m = 97.2; #kg human mass
l = 8.96; #m equipment height
b0 = 0.5; #m^2 wind cross section free fall
b1 = 0.1; #m^2 wind cross section vertical
t0 = 10; #s rip cord pulled
# t1 = 10.5; #s snatch force occurs
# t2 = 11.5; #s parachute opens
# t3 = 13.2; #s steady state 
tf = 30; #s length of plot
a0 = ((1.95*b0)+0.35*b1*(1-h))/1.33; #m^2 area coefficient
a1 = 43.8; #m^2 cross section of parachute
beta = np.log(a1/a0); #unitless time coeficient
tspan = np.linspace(0,tf,num_steps+1); #create an array of times
# Ae = np.zeros_like(tspan);  #m^2 initializes Area of equipment
k = np.array([0.5 * rho * (1.95 * b0),0.5 * rho * (0.35 * b1 * h + 1.33 * a1) ]); #initialize drag coefficients



def velocity_analytical(t):
    """calculates the velocity profile
    
    Input: 1d numpy array t, the time to calculate velocity at
    Output: 1d numpy array describing velocity """
    if t.any() <= 0:
        raise ValueError("All time values must be positive");
    v = np.zeros(t.size);
    for i in range(t.size):
        if 0 <= t[i] and t[i] < t0:
            v[i] = ((m*g)/k[0] )*((np.exp(-(k[0] *t[i]/m)))-1);
        elif t[i] >= t0:
             v[i] = (((m*g/k[1] )*(np.exp(-k[1] *(t[i] - t0)/m)-1) + (m*g/k[0] )*(np.exp(-k[1] *(t[i]-t0)/m))*((np.exp(-k[0] *t0/m)-1))));
    return v ;
    

def parachute_model1(v,t):
    """Returns the right hand side of the function dv/dt = F(v,t), a first order differential equation considering that
    t is between 0 and t1

    Input: 1d numpy array v describing the velocity and 1d numpy array t describing the time
    Output:: 1d numpy array describing the acceleration of the system"""


    if t >= 0.0:
        return -g-((k[0] *v)/m);
    return nan;

def parachute_model2(v,t):
    """Returns the right hand side of the function dv/dt = F(v,t), a first order differential equation considering that t is
    greater than t1

    Input: 1d numpy array v describing the velocity and 1d numpy array t describing the time
    Output:: 1d numpy array describing the acceleration of the system"""

    if t >= 0.:
        return -g-((k[1] *v)/m);
    return  nan;

    