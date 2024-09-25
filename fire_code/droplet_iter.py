#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 16:48:05 2023

@author: williamluik
"""

import matplotlib.pyplot as plt
import numpy as np
import math
from random import randrange

class Droplet:
    def __init__(self, Nx, Ny, max_drop_distance, x_center, y_center,dx,dy ):
        self.Nx= Nx
        self.Ny=Ny
        self.max_drop_distance= max_drop_distance
        self.x_center=x_center
        self.y_center= y_center
        self.dx=dx
        self.dy=dy
        
        
    def drop_energy(self):
        #use the specific heat formula to find the energy from each water droplet
        m= 0.00005 # mass of a water droplet in kg
        c=4.186 # specific heat of water
        temp0= 15 #inital temp of water when it is released from sprinkler
        temp_final= 100 #boiling point of water
        delt_temp= temp_final-temp0
        heat_energy= m*c*delt_temp/1000 #divide by 1000 so that it is in kilo jouls
        return heat_energy
        
    def droplets(self):
        #collect all of the water droplets into each position on the array
        floor_water= np.zeros((self.Nx,self.Ny))
        
        for droplet in range(500):  #should be 33333 iterations but instead I am assuming that the drop has a value of 100 drops so that the iteration is quicker.
            #find the position of a random droplet
            drop_distance= randrange(1,int(self.max_drop_distance))  #this will be a random distance up to three decimal places
            projection_angle= randrange(0,360)  #angle zero is directly to the right --> later wil convert to radians
            xdrop_distance= math.cos(projection_angle * (math.pi/ 180)) *drop_distance
            ydrop_distance= math.sin(projection_angle * (math.pi/ 180)) *drop_distance

            #position of the random water droplet
            xdrop_position= int(self.x_center + (xdrop_distance)/self.dx)
            ydrop_position= int(self.y_center + (ydrop_distance)/self.dy)
        
            #energy of the droplet that landed in that position 'bucket'
            floor_water[xdrop_position,ydrop_position] += self.drop_energy() *100 #multiply by 100 to account for the reduction in iteration. itterating less but assuming that the random droplet has the energy of 100 droplets

        return floor_water
        
        
        
        
        
        
        
        