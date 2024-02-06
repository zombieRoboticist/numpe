"""modual to plot parachute information"""

import numpy as np;
import matplotlib.pyplot as plt;
from math import pi;
import time;
import parachute as par;
import euler as eu;

plot = True;

tf=25; #s the final time
numSteps = 25;
t1 = np.linspace(0, par.t0, numSteps+1);
t2 = np.linspace(par.t0, tf,numSteps+1);
t = np.append(t1,t2[1:numSteps+1]);
vAnalytical = par.velocity_analytical(t);
# print(v)
y0 = 0;
vForward = np.zeros_like(t);
vBackward = np.zeros_like(t);
vForward[0:numSteps+1] = eu.forward_euler(par.parachute_model1, [0,par.t0], y0,numSteps)[1];
vBackward[0:numSteps+1] = eu.backward_euler(par.parachute_model1, [0,par.t0], y0, numSteps)[1];
vForward[numSteps:t.size+0] = eu.forward_euler(par.parachute_model2, [par.t0, tf], vForward[numSteps], numSteps)[1];
vBackward[numSteps:t.size+0] = eu.backward_euler(par.parachute_model2, [par.t0, tf], vBackward[numSteps], numSteps)[1];
N = np.array([40, 80, 100, 120]);
errorForward = np.zeros(N.size);
errorBackward = np.zeros(N.size);
tError = 30 #s final time for error
ref = par.velocity_analytical(np.array([tError]))[0];
compTimeForward = 0;
compTimeBackward = 0;

for i in range(N.size):
    startTime = time.perf_counter();
    euf30 = eu.forward_euler(par.parachute_model2, [par.t0, tError], vAnalytical[numSteps], N[i])[1][-1];
    endTime = time.perf_counter();
    errorForward[i] = abs(ref - euf30);
    compTimeForward = endTime-startTime;
    startTime2 = time.perf_counter();
    eub30 = eu.backward_euler(par.parachute_model2, [par.t0, tError], vAnalytical[numSteps], N[i])[1][-1];
    endTime2 = time.perf_counter();
    errorBackward[i] = abs(ref - eub30);
    compTimeBackward = endTime2-startTime2;

if plot:
    fig1, ax1 = plt.subplots(figsize=(8, 6));
    ax1.plot(t, vAnalytical, color="blue", label="Analytical solution");
    ax1.plot(t, vBackward, ".", color="red", label="Backward Euler solution");
    ax1.plot(t, vForward, ".", color="purple", label="Forward Euler solution");
    ax1.set_title("Velocity Profile of the Parachute Model (Hamiln)");
    ax1.set_xlabel("Time(s)");
    ax1.set_ylabel("Velocity (m/s)");
    ax1.legend(loc="lower right", title="25 steps");
    ax1.grid(1);
    fig2, ax2 = plt.subplots(figsize=(8, 6));
    ax2.plot(N, errorBackward, ".", linestyle="solid", color="red", label="Backward Euler, in " + "{:.4f}".format(compTimeBackward) + " seconds");
    ax2.plot(N, errorForward, ".", linestyle="solid", color="purple", label="Forward Euler, in " + "{:.4f}".format(compTimeForward) + " seconds");
    ax2.set_xscale("log");
    ax2.set_yscale("log");
    ax2.set_title("Accuracy of numerical solution at 30s (Hamiln)");
    ax2.set_ylabel("Absolute Error");
    ax2.set_xlabel("Number of Steps");
    ax2.legend(loc="lower left", title="For 120 steps");
    ax2.grid(1);
    fig1.savefig("hw09_velocityProfile.png");
    fig2.savefig("hw09_eulerError.png");
    plt.show();