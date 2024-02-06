"""Module for calculating random numbers in ranges""";

import numpy as np;

def dirac(r):
	"""probability distribution function for a constant

	Input: constant sccalar r
	Output: consttant scalar r"""
	return r;

def uniform(low, high):
	"""calculates a random number from a uniform distribution with a given range

	Inputs: `low` and `high`, scalar values for the low and high values of the range respectively
	Output: a uniformly distributed random number in the provided range"""
	return low + (high-low) * np.random.random();

def normal(mu, sigma, low, high):
	"""calculates a random number from a normal distribution with mean `mu` and standard deviation `sigma`,in the range [`low`, `high`]

	Inputs: scalars mu, sigma, low, high which describe the mean, standard deviation, low and high values of the range respectively
	Output: a normaly distributed random number within the provided range"""
	r= np.random.normal(loc=mu, scale=sigma);
	while( (low> r or high< r)):
		r= np.random.normal(loc=mu, scale=sigma);		
	return r;

	"""Module for calculating the physics of a tennis serve under constant accerleration"""
import numpy as np;
from math import sqrt;
def displacement(u, a, t):
	"""Calculates the displacement of an object under constant acceleration at time t

	Inputs: u is a numpy array describing the initial velocity vector, a is numpy array describing the acceleration vector, t is a scalar instance of time
	Output: a numpy arrat describing the vector of displacement at the given time"""
	if (u.shape[0]!= a.shape[0]):
		raise ValueError("u and a must be same size");
	s = np.zeros_like(u);
	for i in range(s.shape[0]):
		s[i]=u[i]*t+.5*a[i]*t*t;
	return s;

def time_to_land(dz, uz, az):
	""" calculates the time it takes for an obect to have displacement dz under constant acceleration a

	Inputs: scalars dz (displacement between two time instances), uz ( initial velocity component), az (the acceleration component)
	Output: a scalar time for delta displacement component"""

	v = sqrt(((2*abs(az)*abs(dz)))+(uz**(2)));
	# print(dz);
	print("uz", uz)
	# print("az",az);
	# print('v',v)
	return abs((v-uz)/az);

def acceleration_from_spin(q, v, rpm):
	"""Function for calculating acceleration due to spin

	Inputs: numpy arrays q (the spin axis unit vector), v (the velocity vector), and scalar rpm (the spin speed)
	Output: a numpy array describing the spin acceleration vector"""

	if (not ( 3==v.shape[0])):
		raise ValueError ("v must have length of 3");
	if (not ( 3==q.shape[0])):
		raise ValueError ("v must have length of 3");
	out = np.cross(q,v);
	# for i in range (out.shape[0]):
	# 	out[i]*=(1.2E-4)*rpm;
	# print(q);
	# print(v);
	return out*(1.2E-4)*rpm;

def impact_position(p, u, a, q, rpm, zval):
	"""Function for calculating impact position

	Inputs: 1d numpy arrays of length 3: p (the initial position vector), u (the initial velocity vector), a (the acceleration vector), q (the spin axis unit vector) and scalars rpm (the spin velocity) and zval (the change in z value)
	Output: a 1d numpy arrray describing the position vector at given zval"""
	t= time_to_land((p[2]-zval),abs(u[2]),abs(a[2]));
	return (p+displacement(u,a,t));