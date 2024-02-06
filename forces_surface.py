"""Module for computing the forces on surfaces"""

import numpy as np;
from quadrature import midpoint as integrate;

def panel_midpoints(x, y):
	"""Calculates the midpoints of the panels 

	Inputs: numpy arrays x and y containing the coordinates of the panel nodes
	Output: 2 numpy arrays dfx, dfy that contain the x and y coordinates of the midpoints of each panel respectively
	"""
	xbar= np.zeros(x.shape[0]-1);
	ybar=np.zeros(x.shape[0]-1);
	for i in range(x.shape[0]-1):
		xbar[i]=(x[i+1]+x[i])/2;
		ybar[i]=(y[i+1]+y[i])/2;
	return xbar, ybar ;

def panel_midforces(x, y, press):
	"""Computes the differential forces at the midpoints of the segmentd x, y

	Inputs: numpy arrays x and y containing the coordinates of the panel nodes (the node coordinates x and y must be ordered in a counter-clockwise manner over the surface of the body), press is a numpy array containing the coefficient of pressure measured at each of the panel nodes.
	Output: numpy arrays dfx and dfy which are the differantial forces at the midpoints of the segments in the x and y direction respectively """
	dfx = np.zeros(x.shape[0]-1);
	dfy=np.zeros_like(dfx);
	for i in range(dfx.shape[0]):
		dfx[i]= -1* (y[i+1]-y[i])*.5*(press[i]+press[i+1]);
		dfy[i]=(x[i+1]-x[i])*.5*(press[i]+press[i+1]);
	return dfx, dfy;

def integrate_forces(dfx, dfy):
	"""computes the components of the forces in the x and y directions

	Inputs: dfx and dfy are 1d numpy arrays containing the x and y components of the forces on each panel respectively
	Output: fx and fy are Scalars describing the total force components in the x and y Directions respectively"""
	return integrate(dfx,1), integrate(dfy,1);

