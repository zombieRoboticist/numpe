
import numpy as np;
from scipy.optimize import root;

fun = lambda x: np.array([x[0]**4+100*x[1]**4-1,x[0]**3+x[1]-.5]);
jac= lambda x:np.array([[4*x[0]**3, 400*x[1]**3],[3*x[0]**2,1]]);
x0 = np.array([0.5, 0.3]);
sol =root(fun,x0,method='lm', jac=jac)
if (not sol.success):
    raise RuntimeError("scipy.optimize.root failed to find root");
root_array=sol.x;