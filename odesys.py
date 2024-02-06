"""Module for computing ode systems"""
import numpy as np;
from scipy.optimize import root;

def runge_kutta_4th(func, tspan, u0, num_steps):
    """solves systems of ivps using the clasic runge-kutta method

    Inputs:func is a function representing F(u, t),  tspan is a 1D two-element array of [t0,tf], u0 is a 1d numpy array of the initial conditions, num_steps is an integer value of the number of time steps
    Output: t and y, a 1D NumPy arrays of length N+1 and a 2d numpy array of shape u0.length, N+1 holding time and u values respectively"""

    if(num_steps<=0):
        raise ValueError("num_steps must e a positive integer");
    if (tspan[0]>= tspan[1]):
        raise ValueError("t0 must be < than tf");

    t= np.linspace(tspan[0],tspan[1], num_steps+1);
    u= np.zeros((u0.shape[0],t.shape[0]));
    u[:,0]=u0;
    for i in range(1,num_steps+1):
        k1 = (t[i]-t[i-1])*func(u[:,i-1],t[i-1]);
        k2= (t[i]-t[i-1])*func(u[:,i-1]+.5*k1,t[i-1]+.5*((t[i]-t[i-1])));
        k3= (t[i]-t[i-1])*func(u[:,i-1]+.5*k2,t[i-1]+.5*((t[i]-t[i-1])));
        k4=(t[i]-t[i-1])*func(u[:,i-1]+k3,t[i-1]+(t[i]-t[i-1]));
        u[:,i] = u[:,i-1] +1/6*(k1+2*k2+2*k3+k4);

    # print(u);
    # print(u0);

    return t, u;

def trapezoidal(A, tspan, u0, num_steps):
    """solves systems of odes using the trapezoindal area method

    Inputs: A is a square 2D NumPy array representing the coefficients,  tspan is a 1D two-element array of [t0,tf], u0 is a 1d numpy array of the initial conditions, num_steps is an integer value of the number of time steps
    Output: t and y, a 1D NumPy arrays of length N+1 and a 2d numpy array of shape u0.length, N+1 holding time and u values respectively"""

    if(num_steps<=0):
        raise ValueError("num_steps must e a positive integer");
    if (tspan[0]>= tspan[1]):
        raise ValueError("t0 must be < than tf");

    t= np.linspace(tspan[0],tspan[1], num_steps+1);
    u= np.zeros((u0.shape[0],t.shape[0]));
    u[:,0]=u0;
    I = np.zeros_like(A);
    for i in range(I.shape[0]):
        I[i,i] = 1;
    for i in range(1,t.shape[0]):
        # print(np.linalg.inv(I-.5*(t[i]-t[i-1])*A))
        # print((I+.5*(t[i]-t[i-1])*A))
        # print(u[:,i-1])
        u[:,i] = np.matmul(np.linalg.inv(I-.5*(t[i]-t[i-1])*A), (I+.5*(t[i]-t[i-1])*A)@u[:,i-1]);
    return t,u;

def backward_euler(func, jac, tspan, u0, num_steps):
    """solves systems of ivps using the the backward euler method

    Inputs:func is a function representing F(u, t), jac is a function returning 2D NumPy array MF/Mu for arguments u and t, tspan is a 1D two-element array of [t0,tf], u0 is a 1d numpy array of the initial conditions, num_steps is an integer value of the number of time steps
    Output: t and y, a 1D NumPy arrays of length N+1 and a 2d numpy array of shape u0.length, N+1 holding time and u values respectively"""

    if(num_steps<=0):
        raise ValueError("num_steps must e a positive integer");
    if (tspan[0]>= tspan[1]):
        raise ValueError("t0 must be < than tf");

    t= np.linspace(tspan[0],tspan[1], num_steps+1);
    u= np.zeros((u0.shape[0],t.shape[0]));
    u[:,0]=u0;
    for i in range(1,num_steps+1):
        fx = lambda X: X- u[:,i-1]-func(X, t[i])*(t[i]-t[i-1]);
        ja = lambda X :np.identity(u.shape[0])-jac(u[:,i],t[i])*(t[i]-t[i-1]);
        u[:,i] = root(fx, x0=u[:,i-1],jac=ja,method='hybr' ).x

    # print(u);
    # print(u0);

    return t, u;