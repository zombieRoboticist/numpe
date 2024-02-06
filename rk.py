"""Module for computing IVP solutions"""

import numpy as np;



def explicit_midpoint(func, tspan, y0, num_steps):
    """solves ivps using the explicit forward midpoint method

    Inputs:func is a function representing F(y, t),  tspan is a 1D two-element array of [t0,tf], y0 is the scalar initial condition, num_steps is an integer value of the number of time steps
    Output: t and y, two 1D NumPy arrays of length N+1 holding time and y values respectively"""

    if(num_steps<=0):
        raise ValueError("num_steps must e a positive integer");
    if (tspan[0]>= tspan[1]):
        raise ValueError("t0 must be < than tf");

    t= np.linspace(tspan[0],tspan[1], num_steps+1);
    y= np.zeros_like(t);
    y[0]=y0;
    for i in range(1,num_steps+1):
        y[i] = y[i-1] + func(func(y[i-1],t[i-1])*(t[i]-t[i-1])/2+y[i-1],t[i-1]+(t[i]-t[i-1])/2)*(t[i]-t[i-1]);
    return t, y;

def runge_kutta_4th(func, tspan, y0, num_steps):
    """solves ivps using the clasic runge-kutta method

    Inputs:func is a function representing F(y, t),  tspan is a 1D two-element array of [t0,tf], y0 is the scalar initial condition, num_steps is an integer value of the number of time steps
    Output: t and y, two 1D NumPy arrays of length N+1 holding time and y values respectively"""

    if(num_steps<=0):
        raise ValueError("num_steps must e a positive integer");
    if (tspan[0]>= tspan[1]):
        raise ValueError("t0 must be < than tf");

    t= np.linspace(tspan[0],tspan[1], num_steps+1);
    y= np.zeros_like(t);
    y[0]=y0;
    for i in range(1,num_steps+1):
        k1 = (t[i]-t[i-1])*func(y[i-1],t[i-1]);
        k2= (t[i]-t[i-1])*func(y[i-1]+.5*k1,t[i-1]+.5*((t[i]-t[i-1])));
        k3= (t[i]-t[i-1])*func(y[i-1]+.5*k2,t[i-1]+.5*((t[i]-t[i-1])));
        k4=(t[i]-t[i-1])*func(y[i-1]+k3,t[i-1]+(t[i]-t[i-1]));
        y[i] = y[i-1] +1/6*(k1+2*k2+2*k3+k4);
    return t, y;