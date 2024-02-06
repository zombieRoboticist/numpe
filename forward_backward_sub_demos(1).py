
import numpy as np
#import linsolve
from linsolve import forward_sub

L = np.array([[1., 0., 0.], [2., 1., 0.], [3., 4., 1.]])
b = np.array([1.0, 2.0, 3.0])
y = forward_sub(L, b)
#y = np.array([1.0, 0.0, 0.0])

# check that answer is actually a solution
print( L @ y == b )

