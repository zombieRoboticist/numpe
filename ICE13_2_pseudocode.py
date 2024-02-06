# do you need to update your module docstring, or is what you wrote
# before sufficiently generic to include the new `trapazoidal` function?

import numpy as np

# cut and paste your `midpoint` function here

def trapezoidal(fvals, dx):
    # write a standard-conforming useful docstring for this function
    # based on the in-class exercise description and in your own words
    #    - explain what `fvals` is (this is different from midpoint!)
    #    - explain what `dx` is

    # Check that `dx` is positive; if it is not, raise a ValueError

    # implement the formula on Preliminaries page 14
    # Note that `fvals` is an array
    #   - with first element fvals[0]
    #   - and last element fvals[-1]
    # How can you write a slice of array `fvals` that includes
    # all of the points except the two end points?
    # Note that you can use np.sum on that slice.

    I =

    return I

# Cut and paste your `midpoint` testing here, except...
#    how does it need to change to test `trapazoidal`?
Submitty = False
if (not Submitty):
    for n in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]:
        x_lo = 0.0
        x_hi = 1.0
        dx   = (x_hi - x_lo) / (n-1)
        nodes = np.linspace(x_lo, x_hi, n)   # what does this do?
        fvals = np.exp(nodes)                # what does this do?
        integral = trapezoidal(fvals, dx)

        exact    = np.exp(1.0) - 1.0
        error    = integral - exact
        result_string  = "Error for " + '{:5d}'.format(n)
        result_string += " nodes = "  + '{:.10f}'.format(error)
        print(result_string)

# add a test that uses np.sin(2*pi*x)
# add a test that uses np.sqrt(x)
