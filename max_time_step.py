import numpy as np;

tstep = lambda lam: -4*lam[0]/(2*((lam[0]**(2))+(lam[1]**(2))));

lam1 = np.array([-.01,0]);
A1= max(tstep(lam1),0.0);

lam2 = np.array([-36/.2,0]);
A2= max(tstep(lam2),0.0);

lam3 = np.array([-.75,1.2]);
A3= max(tstep(lam3),0.0);

lam4 = np.array([0, -2*(2**(.5))]);
A4= max(tstep(lam4),0.0);
print(A1,A2,A3,A4);