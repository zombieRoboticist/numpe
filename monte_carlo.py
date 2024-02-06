"""Module for doing Monty Carlo Integration"""

import random;

def estimate_area(func, xlo, xhi, ylo, yhi, n=100):
    """estimates the area under a 2D curve using the monty carlo method
    
    Inputs:  func(x,y) a function that returns the value math function being integrated, xlo, xhi, ylo, and yhi the bounds of the rectangle surounding the area to integrate, n = the numper of points to estimate the area with.    Use Monte Carlo Simulation (MCS) with n samples.
    Output: the estimated area"""
    if(n <= 0):
        raise ValueError ("n must be >0");
    if(type(n)!= int):
        raise ValueError ("n must be an integer");
    if(xhi < xlo):
        raise ValueError ("xhi must be > xlo");
    if(yhi < ylo):
        raise ValueError ("yhi must be > ylo");

    randp = lambda hi , lo : (hi-lo)*random.random() +lo;
    count = 0;
    for i in range (n):
        if(func(randp(xhi,xlo),randp(yhi,ylo))<0.0):
            count+=1;   
    return count/n*(xhi-xlo)*(yhi-ylo);


def mc_integral(func, a, b, n):
    """estimates the integral and error of a function using the monty carlo simulation

    Input: func the math formula to be integrated, a the min x value, b the max x value, n the number of points to estimate with
    Output: the integral and its uncertainty"""
    if(n <= 0):
        raise ValueError ("n must be >0");
    if(type(n)!= int):
        raise ValueError ("n must be an integer");
    if(b <= a):
        raise ValueError ("b must be > a");
    randp = lambda hi , lo : (hi-lo)*random.random() +lo;
    fsum = 0.;
    f2sum=0.;
    for i in range (n):
        temp =   func((a-b)*random.random() +b);
        fsum+= temp;
        f2sum+= temp**2;
    return ((b-a)*fsum/n),((b-a)*(((1/n*f2sum)-(1/n*fsum)**2)/n)**(1/2));