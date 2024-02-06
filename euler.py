"""Module for computing differential equations"""
import numpy as np;
import scipy;

def forward_euler(func, tspan, y0, num_steps):
	"""computes the forward euler approximation of y

	Inputs: y0 is the scalar initial condition, num_steps is integer N, the number of time steps, func is a function representing F(y, t) and takes in the arguments y and t in	that order, tspan is a 1D two-element array with tspan[0] = t0 and tspan[1] = tf
	Output: t and y, two 1D NumPy arrays of length N+1 holding t and y vallues respectively"""

	if(num_steps<=0):
		raise ValueError("num_steps must e a positive integer");
	if (tspan[0]>= tspan[1]):
		raise ValueError("t0 must be < than tf");
	t= np.linspace(tspan[0],tspan[1], num_steps+1);
	y= np.zeros_like(t);
	y[0]=y0;
	for i in range(1,num_steps+1):
		y[i] = y[i-1] + (t[i]-t[i-1])*func(y[i-1],t[i-1]);
	return t, y;

def backward_euler(func, tspan, y0, num_steps):
	"""computes the backward euler approximation of y

	Inputs: y0 is the scalar initial condition, num_steps is integer N, the number of time steps, func is a function representing F(y, t) and takes in the arguments y and t in	that order, tspan is a 1D two-element array with tspan[0] = t0 and tspan[1] = tf
	Output: t and y, two 1D NumPy arrays of length N+1 holding t and y vallues respectively"""

	if(num_steps<=0):
		raise ValueError("num_steps must e a positive integer");
	if (tspan[0]>= tspan[1]):
		raise ValueError("t0 must be < than tf");
	t= np.linspace(tspan[0],tspan[1], num_steps+1);
	y= np.zeros_like(t);
	y[0]=y0;
	for i in range(1,num_steps+1):
		g= lambda x: x-y[i-1]-func(x,t[i])*(t[i]-t[i-1]);
		y[i] = scipy.optimize.root_scalar(g, x0=y[i-1], x1=y[i-1] + (t[i]-t[i-1])*func(y[i-1], t[i-1]), method='secant').root
	return t, y;
