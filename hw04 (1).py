# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 14:09:28 2022

@author: Niko
"""

import matplotlib.pyplot as plt;
import numpy as np;
import fitdata;


files = ["300MR1.dat","300MR0.33.dat","300MR0.2.dat","300MR0.05.dat"];
colors = [['og','-g'],['or','-r'],['oy','-y'],['ob','-b']];
ratios=["R=1:P3","R=0.33:P3","R=0.2:P3","R=0.05:P3"]
filename = ["300MR1.png","300MR0_33.png","300MR0_2.png","300MR0_05.png"]
for f in range(len(files)):
    xdat,  ydata = np.loadtxt(files[f], skiprows=3, delimiter=',', unpack=True);
    #print(xdata,ydata);
    xdata=np.zeros(len(xdat));
    for i in range(len(xdat)):
        xdata[i] = np.log10(xdat[i]);
    coeff = fitdata.calc_fit(xdata, ydata,3);
    calced = fitdata.eval_fit(coeff, xdata);
    
    plt.figure(1, figsize=(6, 4));
    plt.plot(xdata, ydata,colors[f][0] )      
    plt.plot(xdata, calced,colors[f][1],label=ratios[f] )   
    plt.title( "Fatigue life for 300M alloy for different stress ratios" , fontsize=14)
    plt.xlabel(" Fatigue life (log 10 (cycles))"        , fontsize=12)
    plt.ylabel("Stress (MPa)", fontsize=12)
    plt.legend();
    plt.show();
    plt.savefig(filename[f], dpi=300, edgecolor='none')