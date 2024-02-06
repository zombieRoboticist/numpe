# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 18:24:00 2022

@author: 17163
Module file for calculating where the ball will land given by a set of variables that affects
where the ball lands
"""
import numpy as np
from math import sqrt
Make_Plot = True
Dim = 3 #number of dimensions to work with, use when looping through vectors and creating vectors
g = 386.088583 #in/s
balldiameter = 1.3 #in
netheight = 42 #in
#SAMPLING FUNCTIONS-------------------------------------------------------------
def dirac(r):
    """Function to “sample” constant rates"""
    return r
# print(dirac(r))
def normal(mu,sigma,low,high):
    """Function to sample normally distributed rates

    Input:
        low: lowest allowable value
        high: highest allowable value
    Output:
        r: normal distribution of sample with excess values cut
    """
    r = 0.
    while r < low or r > high:
        r = np.random.normal(loc=mu,scale=sigma)
    return r
#print(normal(mu, sigma, low, high))

def uniform(low,high):
    """Function to sample uniformly distributed rates
    
    Input:
        low: lowest allowable value
        high: highest allowable value
    Output:
        r: normal distribution of sample with excess values cut
    """
    r = 0.
    while r < low or r > high:
        r = low+(high-low)*np.random.random() #number between 0 and 1
    return r

# u = np.array([.5,.6,.7]) #TESTVAR
# a = np.array([1,0.5,2]) #TESTVAR
# t = 10 #TESTVAR
def displacement(u,a,t):
    """Function to compute displacement given {u}, {a} and t
    
    Input:
        u: initial velocity vector
        a: acceleration vector
        t: time (scalar constant)
    Output:
        s: a vector of displacement in the given time
    """
    
    s = np.zeros(Dim)
    for i in range(Dim):
        s[i] = u[i]*t+0.5*a[i]*(t**2) #displacement equation (WORKING)
    return s
# print("displacement of ball: ",displacement(u, a, t))

# dz = 0.1 #TESTVAR
# uz = 0.023 #TESTVAR
# az = 0.31 #TESTVAR
def time_to_land(dz,uz,az):
    """Function to compute time to land given displacement, u and t
    Input:
        dz: delta z between two time instances
        uz: initial velocity component
        az: acceleration component
    Output:
        t: scalar time for delta displacement component
    """
    vz = 0.
    vz = sqrt(2*az*dz+(uz**2))
    # print(dz);
    t = (vz-uz)/az
    # print("zval=",zval)
    return t
# print("time to land=",time_to_land(dz, uz, az))

# q = np.array([1.023,2.21,3.972]) #TESTVAR
# v = np.array([4.1284,5.12,6.1821]) #TESTVAR
# rpm = 1500 #TESTVAR
def acceleration_from_spin(q,v,rpm):
    """Function to compute acceleration due to spin
    Inputs:
        q: spin axis unit vector
        v: velocity vector
        rpm: spin rpm
    Outputs:
        as: vector with acceleration contribution due to spin
    """
    cs = 1.2E-4 #coefficient of spin, given in assignment
    a_s = np.zeros(Dim)
    
    a_s = cs*rpm*np.cross(q,v)

    return a_s
# print(acceleration_from_spin(q,v,rpm))




# print("zval = ",zval,"inches from the ground")
# p = np.array([0,0,0]) #TESTVAR
def impact_position(p,u,a,q,rpm,zval):
    """Function to impact position given all inputs
    Input:
        p: initial position vector
        u: initial velocity vector
        a: acceleration vector
        q: spin axis unit vector
        rpm: spin rpm
        zval: intended z value (can be used for landing or hitting the net)
    Output:
        r: Position vector at given zval
    """

    z = abs(zval-p[2])
    time = time_to_land(z,abs(u[2]),abs(a[2]))
    d = displacement(u,a,time)
    r = np.zeros(Dim)
    for i in range(Dim):
        r[i] = p[i] + d[i]
    return r
# print("final impact position:",impact_position(p,u,a,q,rpm,zval))







#SERVE UNTIL YOU DIE (10,000)---------------------------------------------------
nsamples = 10000
position = np.zeros([nsamples,2])
tot_fails = 0 #if a ball does not clear the net and/or does not land in the bbox
fill_net = 0
fail = 0
fill_sl = 0
fill_sb = 0
for i in range(nsamples):
    c = np.zeros(Dim)
    c[0] = normal(15.,4.2,6.,22.)
    c[1] = -6.
    rx = np.random.normal(0.5,3.2)
    ry = np.random.normal(6.,2.2)
    rz = np.random.normal(98.,0.5)
    umag = np.random.normal(130.,5.4) #mph
    
    u_num = np.array([-0.012,0.95,-0.04])
    u_num[0] = np.random.normal(-0.012,1.0E-2) #inches
    u_num[1] = np.random.normal(0.95,1.2E-2) #inches
    u_num[2] = np.random.normal(-0.04,1.25E-2) #inches
    
    u = u_num/u_num.dot(u_num)    #unit vector lol
    u*= umag * 63360/3600 #from mph to in/s #real vector lol
    
    
    rpm = normal(1500,60,1200,1600)
    q_num = np.array([-0.65,-0.25,0.35])
    q_num[0] = np.random.normal(-0.65,0.01) #in.
    q_num[1] = np.random.normal(-0.25,0.01) #in.
    q_num[2] = np.random.normal(0.35,0.01) #in.


    q = q_num/q_num.dot(q_num)

    d = np.array([rx,ry,rz])
    p = c+d


    
    a_s = acceleration_from_spin(q, u, rpm)
    a_g = np.array([0.,0.,-g]) #in/s^2
    a_d = np.array([0.,1.,0.])
    a_d *= -6.0E-4 * (umag*(63360/3600))**2
    a = a_s + a_g + a_d
    
    r = impact_position(p, u, a, q, rpm, balldiameter) #clears net (nice)
    
    znet = balldiameter+netheight
    rnet = impact_position(p, u, a, q, rpm, znet) #hits net (fail)
    
    net_d = 39*12
    
    #tally up all the stuff

    if rnet[1]<net_d: #checks for failures
        fill_net+= 1
        fail = 1
        
    position[i,0] = r[0]
    position[i,1] = r[1]
    

    if r[0] > 0.: #checks for failures (is inside box?)
        fill_sb+=1
        fail = 1
        
    diss_sl = (21+21+18)*12 

    if r[1] > diss_sl: #checks for failures (is over the net?)
        fill_sl+=1
        fail = 1
    
    tot_fails += fail
    fail = 0 #if none of the if statements are true, fail = 0
    fail_sb = fill_sb
    fail_sl = fill_sl
    
success_rate = ((nsamples-tot_fails)/nsamples)*100 #convert to percentage   
 
#trajectory calculator
disp = abs(balldiameter-d[2])
tfinal = time_to_land(disp, abs(u[2]), abs(a[2]))
times = np.linspace(0,tfinal,100)
trajectory = np.zeros([times.size,Dim])
for i in range(times.size):
    trajectory[i,:] = p+displacement(u, a, times[i])
    
    
#PLOT ALL THE THINGS -----------------------------------------------------------
if(Make_Plot):    #Make the plot
    import matplotlib.pyplot as plt
    # ax = plt.subplots()
    fig = plt.figure(1,figsize=[5.5,8])

    

    
    rx,ry = position[0],position[1]
    plt.plot(position[:,0],position[:,1],'o',color='red',markersize = 0.25)
    
    target = np.loadtxt("bbox.dat")
    plt.plot(target[:,0],target[:,1],'-',color='purple',linewidth=4,zorder=2)
    
    plt.plot(trajectory[:,0],trajectory[:,1],'-',color='yellow',linewidth=3)
    
    court = np.loadtxt("court.dat")
    plt.plot(court[:,0],court[:,1],'-',color='blue',linewidth = 3,zorder=1)
    
    text_string = "Success Percentage ="
    text_string += str(success_rate)+"\n"
    text_string += "Total Fails ="
    text_string += str(tot_fails)+"\n"
    text_string += "Fails Service Box ="
    text_string += str(fail_sb)+"\n"
    text_string += "Fails Service Line ="
    text_string += str(fail_sl)+"\n"
    xx = -150.
    ytxt = 800.
    plt.text(xx,ytxt,text_string,fontsize=8)
    
    title_string = "Serve statistics (roberm10)"
    plt.title(title_string)
    plt.xlabel('x [inches]')
    plt.ylabel('y [inches]')
    fig.legend(['Simulated Landings','Target','Nominal Trajectory'],fontsize=10,loc=[0.175,0.16])
    plt.show()