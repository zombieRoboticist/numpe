import numpy as np;
import matplotlib.pyplot as plt;
import forces_surface as fs;
from math import sin, cos, pi;

x,y,r,press = np.loadtxt("tire_contact_pressure.dat",skiprows=1, delimiter=',', unpack=True);
dfx , dfy = fs.panel_midforces(x,y,press);
xbar,ybar = fs.panel_midpoints(x,y);
fx, fy = fs.integrate_forces(dfx,dfy);
text = "Net Contact Force Vector:\n(" + '{:6.4e}'.format(fx)+ ", "+ '{:6.4e}'.format(fy)+ ")";
xx = -150.; 
ytxt = 100.;

xp = np.zeros(100);
yp = np.zeros(100);
theta = np.linspace(0, (2*pi), 100);
c=0;
for i in theta:
    xp[c]= 300*cos(i);
    yp[c]=300*sin(i);
    c+=1;

fig,ax= plt.subplots(1,1,figsize=(6,6));
plt.plot(xp, yp,"--g", label = "undeformed tire");
plt.text(xx, ytxt, text);
plt.plot(x,y,"-k", label = "deformed tire");
q = ax.quiver(xbar,ybar,dfx,dfy, color='r',units='xy', scale=25.0);
ax.quiverkey(q, X=.7, Y=.0175, U=2000., label="Pressure Force", labelpos ='E');
plt.title(" Contact pressure in tire (hamiln)");
plt.xlabel("X Position (mm)"        , fontsize=12);
plt.ylabel("Y Position (mm)", fontsize=12);
plt.legend();
ax.axis('equal') ;
plt.axis([-350, 375, -350, 375])
# print(dfx, dfy);
#plt.savefig('hw07_plot.png', dpi=300, edgecolor='none')
plt.show()