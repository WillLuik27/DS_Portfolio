#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 20:52:30 2023

@author: williamluik
"""

import matplotlib.pyplot as plt
import numpy as np

class Fire:
    def __init__(self, ising_floor, Nx, Ny, J, J_diag, T, num_steps ):
        self.ising_floor=ising_floor
        self.Nx= Nx
        self.Ny= Ny
        self.J=J
        self.J_diag= J_diag
        self.T=T
        self.num_steps=num_steps
        
    def ising_model(self):
        # floor is given through as a parameter of the function

        # Calculate the initial energy and magnetization
        E = -self.J * np.sum(self.ising_floor * np.roll(self.ising_floor, -1, axis=0) +
                       self.ising_floor * np.roll(self.ising_floor, -1, axis=1))
        M = np.sum(self.ising_floor)


        # Perform the Monte Carlo simulation
        for i in range(self.num_steps):
            # Choose a random spin to flip
            row = np.random.randint(self.Nx)
            col = np.random.randint(self.Ny)

            # Calculate the energy change if the spin is flipped
            delta_E = 2 * self.J * self.ising_floor[row, col] * (
                self.ising_floor[row, (col+1)%self.Ny] + self.ising_floor[row, (col-1)%self.Ny] +
                self.ising_floor[(row+1)%self.Nx, col] + self.ising_floor[(row-1)%self.Nx, col]) + 2*self.J_diag*self.ising_floor[row,col]*(
                self.ising_floor[(row+1)%self.Nx, (col+1)%self.Ny] + self.ising_floor[(row-1)%self.Nx, (col+1)%self.Ny] + 
                self.ising_floor[(row-1)%self.Nx, (col-1)%self.Ny] + self.ising_floor[(row+1)%self.Nx, (col-1)%self.Ny] )

        # Accept or reject the spin flip based on the Metropolis algorithm
        if (delta_E < 0 or np.exp(-delta_E / self.T) > np.random.rand()) and  self.ising_floor[row,col]!=-1:  #no spin flip is there is already a fire
            self.ising_floor[row, col] *= -1
            E += delta_E
            M += 2 * self.ising_floor[row, col]
           
        # Plot the floor
        #plt.imshow(self.ising_floor, cmap='RdYlGn')  #note: black is -1 while white is 1
        #plt.show()
        return self.ising_floor








