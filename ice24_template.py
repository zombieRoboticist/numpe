# write a useful module docstring

def ice24_integral(N, output=False):
    # Compute three dimensional integral of e^(xyz) in [0, 1]**3
    # etc., etc., etc....

    from timeit import default_timer as timer
    # Test the input:
    #    raise TypeError with useful error message if N is not an integer
    #    raise ValueError with useful error message if N is not positive

    # start the stopwatch
    start = timer()

    # compute the integral
    integral = 0.0  # this dummy code executes until you write your own

    # stop the stopwatch
    end = timer()

    if output:
        print("Number of intervals", N)
        print("Integral =", integral)
        print("Elapsed time [s] = ", end-start)

    return integral

