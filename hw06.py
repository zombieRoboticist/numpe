# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 10:25:34 2022

@author: Niko
"""
import numpy as np;
import diff6 as dif;
import fitdata;
import matplotlib.pyplot as plt;

def mad(x, y):
    """computes the mean absolute differance between two sets of data
    
    Inputs: x and y are 1d numpy arrays of the same size
    Output: a float that is the mean absolute difference between the 2 data sets"""
    assert x.shape[0]==y.shape[0],"arrays must be of same size";
    add=0.0
    for i in range(x.shape[0]):
        add+= abs(x[i]-y[i]);
    add/= x.shape[0];
    return add;

def rmsd(x, y):
    """computes the root mean square difference between two sets of data
    
    Inputs: x and y are 1d numpy arrays of the same size
    Output: a float that is the root mean square difference between the 2 data sets"""
    assert x.shape[0]==y.shape[0],"arrays must be of same size";
    add=0.0
    for i in range(x.shape[0]):
        add+= (x[i]-y[i])**2;
    add/= x.shape[0];
    add= add**.5;
    return add;

rate1 =1/5.;
rate2 = 3/5.;
deg =4;
xdat,  ydat = np.loadtxt('hw6.dat', delimiter=',', unpack=True);
xdata = np.array(xdat);
ydata = np.array(ydat);
vdata = dif.finite_diff(xdata, ydata);

y= fitdata.calc_fit(xdata, ydata, degree=8);
v =np.zeros(xdata.shape[0]);
for i in range(v.shape[0]):
    v[i] =dif.polynomial_derivative(y, xdata[i]);
    

plt.figure(1, figsize=(6, 4));
fig, ax1 = plt.subplots();
ax1.set_xlabel('time (s)');
ax1.set_ylabel('Altitude (m)', color="red");
plt.plot(xdata,ydata, "-",color = 'red', label = "altitude"  );
ax1.tick_params(axis='y', labelcolor="red");

ax2 = ax1.twinx();

color = 'tab:blue';
ax2.set_ylabel('Veleocity (m/s)', color=color);
plt.plot(xdata, v,"-g", label = "Polynomial fit velocity");
plt.plot(xdata, vdata,"-", color = 'blue', label = "finite dif velocity " );
ax2.tick_params(axis='y', labelcolor=color);

#plt.axis([-2, 1.25, -2, 3])
text = "Comparrison of Numeric Finite Derivative Techniques:\nMAD: "+ str(('{:6.3f}'.format(mad(v,vdata)))) + ", RMSD: "+ str(('{:6.3f}'.format(rmsd(v,vdata))));
#print(text)
fig.legend(loc = 'lower center', bbox_to_anchor=(.5,.125));
plt.title( text , fontsize=14)
plt.savefig('hw06_plot.png', dpi=300, edgecolor='none')
plt.show();