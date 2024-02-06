

import numpy as np



def dot_product(r, force):
    """Returns scalar dot product of two equal size input vectors
    
    INPUT: position vector, force vector
    OUTPUT: scalar moment value
    """
    dp = 0
    for i in range(len(r)):
        dp += (r[i]*force[i])
    return dp


#print(dot_product(r, force))

def cross_product(r, force):
    """Returns vector that is cross product of two input vectors
    
    Input: position vector, force vector
    Output: moment vector
    """
    i = r[1]*force[2] - r[2]*force[1]
    j = r[0]*force[2] - r[2]*force[0]
    k = r[0]*force[1] - r[1]*force[0]
    return np.array([i, -j, k])

#print(cross_product(r, force))


def subtract(v1, v2):
    """Input: two vectors
    Output: difference between vectors
    
    Subtracts one vector from another in each vector element
    """
    ret_vec = np.zeros(v1.shape)
    rows = v1.shape[0]
    for row in range(rows):
        ret_vec[row] = v1[row] - v2[row]

    return ret_vec
# print(subtract(r, force))

def moment_about_point(force, vP, vO):
    """Returns moment caused by input force F applied at point P about a point O
    
    INPUT: Force vector, position vector of point force is applied, position vector of point about which moment is needed
    OUTPUT: Moment vector about point O"""
    r = subtract(vP, vO)
    return cross_product(r, force)
    
    
def moment_about_axis(force, r, u):
    """Returns scalar caused by force F applied at point P about any axis u
    
    INPUT: Force vector, vector r from any point along the axis to any point on the line of action of the force, vector u denoting the axis
    OUTPUT: Scalar Moment about that axis"""
    x = cross_product(r, force)
    u_norm = np.linalg.norm(u)
    for row in range(u.shape[0]):
        u[row] /= u_norm

    return dot_product(u, x)
    
def multiply(v,c): #modifies original Force unit vector (multiplies force unit vector by the force magnitude)
    """Input: force unit vector, force magnitude
    Output: Force vector
    
    Modifies the force unit vector and returns true force vector
    """
    for row in range(v.shape[0]):
        v[row] *= c


def make_data(fx, fy, fz, fm, px, py, pz):
    """Input: force unit vector, force magnitude, position vector
    Output: array of force and position coordinates
    
    Allows input of data
    """
    v = np.array([fx, fy, fz])
    multiply(v, fm)
    
    return [v, np.array([px, py, pz])]
data = [
    make_data(.70014, -.70014, -.14003, 20000, 95, -2.6, -25),
    make_data(0.57735, -.80829, -.11547, 20000, 90, -3.2, -20),
    make_data(-.37139, 0.928477, 0, 15000, -75, -30, 2.5),
    make_data(-.28735, 0.957826, 0, 15000, -80, -30, 2.5),
    make_data(-0.0995, 0.995037, 0, 15000, -85, -30, 2.5),
    make_data(0, 1, 0, 15000, -90, -30, 2.5)
            
        
    ]

u = np.array([1.0, 0.02, 0.11])

#print(u)
O = np.zeros(3)

M_O = np.zeros(3)
T_u = 0;


for (f, p) in data:
  #  print(f, p ,O
    m_p = moment_about_axis(f, p, u)
    m_z = moment_about_point(f, p, O)
    M_O += moment_about_point(f, p, O)
    print(m_p)
    print(m_z)
    T_u =+ m_p
    # print(f, p, O, u)
    #print(M_O)
    #print(T_u)
    # print(m_z)
    
