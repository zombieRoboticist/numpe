# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:06:22 2022

@author: Niko
"""

"""Module for calculating the viscosity of a fluid at a given temperature"""

C1=1.458E-6;
S=110.4;

def calc_viscosity(T):
    """ computes the viscosity of the fluid at a given temperature

        Input: Temperature (in Kelvin)
        Output: the viscosity of the fluid
        """
    return ((C1*(T**(1.5)))/(S+T));


if __name__ == "__main__":   # if run from command prompt
    # get temperature, `T`, from command line and compute
    import sys
    T = float(sys.argv[1])   # convert string to float
    mu = calc_viscosity(T)   # compute viscosity
    print(mu)                # output value to screen
