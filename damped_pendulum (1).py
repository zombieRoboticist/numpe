"""damped pendulum ODE model to test IVP solvers"""

import odesys
import numpy as np

# =============================================================================
# OUTPUT CONTROL
# =============================================================================
print_table = True
show_plot   = False

# =============================================================================
# PENDULUM MODEL CONSTANTS
# =============================================================================
g = 9.80665   # gravity acceleration [m/s2]
L = 0.1       # pendulum length [m]
c = 0.0       # damping coefficient [kg/s]
m = 1.0       # pendulum mass [kg]

def func(u, t):
    """non-linear damped pendulum model.
    
    INPUT:  u - u0 = angular position, theta [rad]
                u1 = angular velocity, omega [rad/s]
            t - time [s]
    OUTPUT: F - F0 = d(u0) / dt
                F1 = d(u1) / dt
    Constants must be available as module variables:
        g = earth gravity acceleration, 9.80665 m/s2
        L = pendulum length [m]
        c = damping coefficient [kg/s]
        m = pendulum mass [kg] 
    """
    F = np.array( [ u[1], -(g/L)*np.sin(u[0]) - (c/m)*u[1] ] )
    return F

def jac(u, t):
    """Returns the Jacobian of the non-linear damped pendulum model.
        
    INPUT:  u - u0 = angular position, theta [rad]
                u1 = angular velocity, omega [rad/s]
            t - time [s]
    OUTPUT: dFdu = [ [dF0/du0, dF0/du1], [dF1/du0, dF1/du1] ]
    Constants must be available as module variables:
        g = earth gravity acceleration, 9.80665 m/s2
        L = pendulum length [m]
        c = damping coefficient [kg/s]
        m = pendulum mass [kg] 
    """
    dFdu = np.array( [ [0.0, 1.0], [-(g/L)*np.cos(u[0]), -(c/m)] ] )
    return dFdu

# Matrix for Linearized Damped Pendulum Model
A = np.array( [ [0.0, 1.0], [-(g/L), -(c/m)] ] )

# =============================================================================
# SOLUTION SPECIFICATIONS
# =============================================================================
num_steps = 15
t_0 = 0.0
t_N = 4*np.pi/np.sqrt(g/L)

theta_0 = 20.0 * np.pi/180.0
omega_0 = 0.0

tspan = np.array([t_0, t_N])
u0 = np.array([theta_0, omega_0])

# =============================================================================
# SELECT SOLUTION METHOD
# =============================================================================

# fourth order explicit classical RK4
# t, u = odesys.runge_kutta_4th(func, tspan, u0, num_steps)

# second order implicit trapezoidal for linear systems
#t, u = odesys.trapezoidal(A, tspan, u0, num_steps)

# first order implicit backeard Euler for non-linear systems
t, u = odesys.backward_euler(func, jac, tspan, u0, num_steps)

# =============================================================================
# OUTPUT
# =============================================================================

if (print_table):
    print("Damped Pendulum (sketch u0 for angles < 90 deg.)")
    print("    t        u0       u1     ")
    print("--------- --------- ---------")
    for i in range(num_steps+1):
        string  = "{:8.3f} ".format(t[i])
        string += "{:8.3f} ".format(u[0,i])
        string += "{:8.3f} ".format(u[1,i])
        factor = 20 - int(6*(np.pi/2-u[0,i]))
        # quick and easy ASCII art like it's the 1980s
        if (factor > 0 and factor < 20):
            string += factor * " " + "*"
        else:
            string += "(~)"
        print(string)

if (show_plot):
    import matplotlib.pyplot as plt
    plt.plot(t,u[0,:],label="u[0]: angular position")
    plt.plot(t,u[1,:],label="u[1]: angular velocity")
    plt.plot([0.0, 1.02*t_N],[0.0, 0.0],'k-.',linewidth=0.5)
    plt.xlim([0.0, 1.02*t_N])
    plt.ylim([-5.5, 4.0])
    plt.legend(loc=4)
    string  = "damped pendulum ["
    string += "c = " + "{:.2f}".format(c) + " kg/s , "
    string += "N = " + "{:d}".format(num_steps) + " steps"
    string += "]"
    plt.title(string)
    plt.xlabel('time [s]')
    plt.ylabel('angular position [rad] and velocity [rad/s]')