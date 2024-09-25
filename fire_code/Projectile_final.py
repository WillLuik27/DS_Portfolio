#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 15:04:35 2023

@author: williamluik
"""


import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

g=9.8
height= 3  # in meters... 9.84 feet
g=9.
vx= 7
vy=0
c = 0.47   #drag coeffient of a sphere
r = .001   #radius of water droplet is 1mm
A = np.pi * r**2  #area of water droplet
m = 0.05  #mass of the water droplet
# Air density (kg.m-3), acceleration due to gravity (m.s-2).
rho_air = 1.28  #air coeffient
k = 0.5 * c * rho_air * A


class Projectile:
    def __init__(self,k,m,height,v0):
        self.k=k
        self.m=m
        self.height=height
        self.v0=v0
        
    def k_value(self, c,rho_air,r ):
        A = np.pi * self.r**2
        k = 0.5 * self.c * self.rho_air * A
        return k

    def x_distance_time(self):
        def deriv(t, u):
            x, xdot, z, zdot = u
            speed = np.hypot(xdot, zdot)
            xdotdot = -self.k/self.m * speed * xdot
            zdotdot = -self.k/self.m * speed * zdot - g
            return xdot, xdotdot, zdot, zdotdot

        # Initial conditions: x0, v0_x, z0, v0_z.
        u0 = 0, self.v0 , self.height, 0
        # Integrate up to tf unless we hit the target sooner.
        t0, tf = 0, 50

        def hit_target(t, u):
            # We've hit the target if the z-coordinate is 0.
            return u[2]
        # Stop the integration when we hit the target.
        hit_target.terminal = True
        # We must be moving downwards (don't stop before we begin moving upwards!)
        hit_target.direction = -1

        def max_height(t, u):
            # The maximum height is obtained when the z-velocity is zero.
            return u[3]

        soln = solve_ivp(deriv, (t0, tf), u0, dense_output=True,
                         events=(hit_target, max_height))

        # A fine grid of time points from 0 until impact time.
        t = np.linspace(0, soln.t_events[0][0], 100)
        sol = soln.sol(t)
        x = sol[0]
        #final value
        xmax = x[-1]
        tmax= soln.t_events[0][0]
        return xmax, soln.t_events[0][0]

    
def methods():
    print("projectile")


    





