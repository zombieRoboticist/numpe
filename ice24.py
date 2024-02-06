"""Module for inegration"""

import numpy as np;
from timeit import default_timer as timer;

def ice24_integral(N, output=False):
	"""Computes integral of function

	Inputs: N  an integer describing the number of integral steps, output is a boolean that determins if the code prints things out
	Outut: the vallue of the integral """
	start = timer();
	if not (type(N) == int ):
		raise TypeError ("N must be an integer");
	if N<=0:
		raise ValueError ("N must be positive");

	dx = 1.0/N;
	integral = 0.0;
	for i in range(N):
		x = (i+0.5)*dx;
		for j in range(N):
			y = (j+0.5)*dx;
			for  k in range(N) :
				z = (k+0.5)*dx;
				integral += np.exp(x*y*z) * dx*dx*dx;
	end = timer();
	if output:
		print("Number of intervals", N);
		print("Integral =", integral);
		print("Elapsed time [s] = ", end-start);
	return integral;