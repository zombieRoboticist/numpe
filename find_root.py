# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:08:54 2022

@author: Niko
"""

"""Module for finding the roots of a function"""


def bisection(func, x_lo, x_hi, xtol=1.0e-15, ftol=1.0e-11, maxiter=100):
    """Finds the zero of a given function that is in the given range of x values.
    
    inputs: a function that takes a single numeric input and gives a single numeric output describing the function the root is being analised, x_lo is a number that describes the lower bound of the reigion to work in, x_hi is a number that describes the upper bound of the reigion to work in, xtol describes the smallest range in x values to look for, ftol describes how close to 0 is defined as 0, maxiter describe the maximum number of itterations the loop can use
    output: the zero of the function in the bounds given.
    """
    #print(func(x_lo));
    #print(func(x_hi));
    assert (func(x_lo)*func(x_hi)) <= 0.0, "bounds dont contain a singlular zero";
    assert abs(func(x_lo))>= ftol, "x_lo must not be a zero";
    assert abs(func(x_hi))>= ftol, "x_hi must not be a zero";
    assert x_hi>x_lo, "x_hi must be greater than x_lo";
    assert type(maxiter) == int, "maxiter must be an integer";
    assert maxiter >0, "maxiter must be >0";
    assert maxiter<1000, "maxiter must be < 1000";
    i=0;
    found = False;
    ans=0.;
    xlo=x_lo;
    xhi=x_hi;
    while i<maxiter:
        if abs(func(xlo))<=ftol:
            found =True;
            ans=xlo;
            return xlo;
            break;
        elif( abs(func(xhi))<=ftol):
            found =True;
            ans=xhi;
            return xhi;
            break;
        elif (abs(func((xhi+xlo)/2))<= ftol):
             found =True;
             ans=(xlo+xhi)/2
             return (xlo+xhi)/2;
             #print(ans);
             break;
        elif abs((xhi-xlo)/2)< xtol:
             #print("break 2");
             break;
        elif (func((xhi+xlo)/2)*func(xlo))<0.0:
            xhi=(xhi+xlo)/2;
            #print(xhi)
        else:
            xlo=(xhi+xlo)/2;
            #print(xlo);
        #print(i);
        i+=1;
        ans=(xlo+xhi)/2;
    #print(ans)
    #assert found, "Zero not found in bounds";
    return ans;

def newton(funcdf, x0, ftol=1e-12, xtola=1e-7, maxiter=100):
    """ computes the zero of a function funcdf near a guess x0
    
        Input: funcdf is a Python function that takes in x and returns f(x) and df(x) in that order, x0 is an initial guess for the root, ftol is f's tolerance for what is zero, xtola is change in x's tolerance for what is zero
        Output: r a float describing the root and n a scalar describing the number of itterations that were run.
    """
    assert type(x0)==int or type(x0)==float, "x0 must be a number";
    
    f, df = funcdf(x0);
    #print(f,df);
    r=x0;
    n=0;
    while (abs(0-f)>= ftol) and (n<= maxiter):
        f, df = funcdf(r);
        n+=1;
        try:
            if(abs(f/df)<= xtola):
                break;
            r-=f/df;
        except ZeroDivisionError:
            n*=-1;
            break;
        except:
            n=-404;
            r=404;
            break;
    return r, n;
    """
    
def functs(x):
    return (x-1)*(x+1), ((x+1)+(x-1));

print(newton(functs,0));"""