import numpy as np
import matplotlib as plt
import math

def grav_accel(p1, p2, m):
    p1 = point mass element
    p2 = point of interested
    m  = mass
    returns a vector of the gravitational accleration
    G = 6.6743e-11
    
    m = 0
    rhat = np.array([(p2[0]-p1[0])/r,(p2[1]-p2[1])/r,(p2[2]-p1[2])/r])
    r = ([(p2[0]-p1[0])**2+(p2[1]-p1[1])**2+(p2[2]-p1[2])**2]**(1/2))
    return -1*G*m/r**2*rhat

def point_in_sphere(x,y,z, radius=None):
    if (
    return True

if __name__ == "__main__":
    km = 1000 #1 km = 1000 meters
    rho = 5514 #kg/m^3, density of Earth
    r_earth = 6378*km #radius of globe Earth
    h = 200.0*km #relatively coarse step size
    #set grid size same in x,y,z
    dx, dy, dz = h, h, h
    #x, y, z define boundaries of grid, here 7000 km
    x = np.arange(-7000*km, 7000*km, dx)
    len_x = x.shape[0]
    y = x.copy()
    z = y.copy()
    #define points on the north pole, south pole, and equator
    point_northpole = np.array([0, 0, 6378*km])
    point_equator   = np.array([0, 20037*km, 4750*km])
    point_southpole = np.array([0, 20037*km, 4750*km])
    ##Sample North Pole calc
    ##You might consider making this a function
    grav_vec_northpole = 0
    for idx, xx in enumerate(x):
        #this is a trick to tell how long it will take
        print(idx, " of ", len_x, "x steps.")
        for yy in y:
            for zz in z:
                if point_in_sphere(xx,yy,zz):#FIX THIS, MAKE THIS A VALID FUNCTION
                    m = 1 #FIX THIS, MAKE THIS A VALID MASS ELEMENT rho*dV
                    point = np.array([xx,yy,zz])
                    grav_vec_northpole += grav_accel(point, point_northpole, m)
    print("The gravity vector at the north pole is...", grav_vec_northpole)
    print("Should be something like [0,0,-9.8] m/s^2")

def point_in_disk(x, center_x, radius):
    if (x-centure_x)**2< radius**2:
        return true
    else:
        return False

