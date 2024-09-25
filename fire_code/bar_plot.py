#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:29:10 2023

@author: williamluik
"""

"""
Making an 3D bar chart
"""

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns # for data visualization

class Bar:
    def __init__(self,floor_hrr , Nx, Ny):
        self.floor_hrr = floor_hrr
        self.Nx= Nx
        self.Ny=Ny
    
    def heatmap(self):
        plt.imshow(self.floor_hrr, cmap='coolwarm')
        plt.colorbar()
        plt.title( "Heat Map of HRR on Floor (Meters)" )
        #plt.savefig("heatmap_video.png")
    

        #test_array = np.arange(self.Nx * self.Ny).reshape(self.Nx, self.Ny)
        return plt.show()
        
    def plot_bar(self):
        fig = plt.figure()
        ax = plt.axes(projection = "3d")

        numOfCols= self.Nx
        numOfRows= self.Ny

        xpos = np.arange(0, numOfCols, 1)
        ypos = np.arange(0, numOfRows, 1)
        xpos, ypos = np.meshgrid(xpos + 0.5, ypos + 0.5)
 
        xpos = xpos.flatten()
        ypos = ypos.flatten()
        zpos = np.zeros(numOfCols * numOfRows)
 
        dx = np.ones(numOfRows * numOfCols) * 0.5
        dy = np.ones(numOfCols * numOfRows) * 0.5
        dz = self.floor_hrr.flatten()
 
        ax.bar3d(xpos, ypos, zpos, dx, dy, dz)
        ax.set_xticklabels(list(range(self.Nx)))
        ax.set_yticklabels(list(range(self.Ny)))
    
        ax.set_xlabel('Depth of room (meters)')
        ax.set_ylabel('Width of room (meters)')
        ax.set_zlabel('HRR (kilo Jouls)')
        #plt.savefig("bar_plot.png")
        
        return plt.show()


        
        
    
    
    
    
    
    
    
    
    