"""Code to run ice24_integrate"""

"""
SOME SAMPLE PYTHON RESULTS

Number of intervals 10
Integral = 1.1463117522843178
Elapsed time [s] =  0.00030790000005254115

Number of intervals 100
Integral = 1.1464971928483056
Elapsed time [s] =  0.17978330000005371

Number of intervals 1000
Integral = 1.1464990537313209
Elapsed time [s] =  189.46685580000008

How do your results compare to how the C++ code performed?
"""

from ice24 import ice24_integral

N = 50
I = ice24_integral(N, output=True)
