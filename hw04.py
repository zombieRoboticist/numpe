# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:09:28 2022

@author: Niko
"""

import matplotlib.pyplot as plt;
import numpy as np;
import fitdata;


#files = ["300MR1.dat","300MR0.33.dat","300MR0.2.dat","300MR0.05.dat"];
files = [];
colors = [['og','-g'],['oc','-c'],['oy','-y'],['ob','-b']];
ratios=["R=1:P2","R=0.33:P2","R=0.2:P2","R=0.05:P2"]
#filename = ["300MR1.png","300MR0_33.png","300MR0_2.png","300MR0_05.png"]
filename='300M.png';
for f in range(len(files)):
    xdat,  ydata = np.loadtxt(files[f], skiprows=3, delimiter=',', unpack=True);
    #print(xdata,ydata);
    xdata=np.zeros(len(xdat));
    for i in range(len(xdat)):
        xdata[i] = np.log10(xdat[i]);
    evalx=np.zeros(len(np.linspace(np.amin(xdata), np.amax(xdata), 100)));
    c=0;
    for k in np.linspace(np.amin(xdata), np.amax(xdata), 100):
         evalx[c]=10**k;
         c+=1;
    coeff = fitdata.calc_fit(xdata, ydata,2);
    calced = fitdata.eval_fit(coeff, np.linspace(np.amin(xdata), np.amax(xdata), 100));
    plt.figure(1, figsize=(10, 6));
    plt.plot(xdat, ydata,colors[f][0] )      
    plt.plot(evalx, calced,colors[f][1],label=ratios[f] )   
    plt.title( "Fatigue life for 300M alloy for different stress ratios" , fontsize=14)
    plt.xlabel(" Fatigue life (cycles)"        , fontsize=12)
    plt.ylabel("Stress (MPa)", fontsize=12)
    plt.legend();
plt.show();
#plt.savefig(filename, dpi=300, edgecolor='none')
x= np.array([0,1,2,3,2,1,0,-1,-2,-3,-2,-1,0]);
y=np.array([-4,-3.771,-2.981, 0,2.981,3.771,4,3.771,2.981,0,-2.981,-3.771,-4]);
coeff = fitdata.calc_fit(x, y,2);
#calced = fitdata.eval_fit(coeff, np.linspace(np.amin(x), np.amax(x), 100));
print(coeff)
#print(sqrt())