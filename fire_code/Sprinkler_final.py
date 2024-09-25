#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:09:59 2023

@author: williamluik
"""
import math
import numpy as np
import Projectile_final
import droplet_iter
import sys
from random import randrange
import Ising_fire_spread
import bar_plot
import matplotlib.pyplot as plt


#spatial demensions of array
#floor demensions
floor_width= 10 #width of room in meters
floor_length = 10 
#step size
dx= 1 
dy= 1
#actual demensions of array
Nx= int(floor_width/dx) 
Ny = int(floor_length/dy)




ising_floor= np.zeros((Nx,Ny)) #fire=-1 and not_fire=1
   

#set floor temperature all to the same number
for i in range(Nx):
    for j in range(Ny):
        ising_floor[i,j]= 1  #start all positions not on fire
        
#sprinkler position --> need to find center of array
x_center = (Nx+1)/2 -1 #subtract by one because arrays start at position zero
y_center =(Nx+1)/2 -1


#kinnematics-->add drag and variable velocity
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
#time_fall = math.sqrt(2*height/g) --> this id there was no drag
#projectile_d= vx* time_fall #how far the water droplet can shoot -->this if there is no drag

#Find the maximum distance that the water droplet can travel with linear drag in 2d
#I am importing code from Projectile_final to solve projectile motion with linear drag in the x and z directions
max_drop_distance, max_drop_time= Projectile_final.Projectile(k,m,height,vx).x_distance_time()
print("max distance", max_drop_distance)

#location of fire
fire_width = 2
fire_length= 2
#array dimensions
fire_Nx = int(fire_width/dx) 
fire_Ny = int(fire_length/dy)

x_fire_position = 5
y_fire_position= 5
fire_pos_list=[]
for i in range(x_fire_position - int(fire_Nx/2),x_fire_position + int(fire_Nx/2) ):
    for j in range(y_fire_position - int(fire_Ny/2), y_fire_position + int(fire_Ny/2)):
        fire_pos_list.append((i,j))
        ising_floor[i,j]=-1





#use Ising model to randomize the spread of the fire in the array

J= 1.0 #coupling coefficent of Ising model
J_diag= J/2  #coupling constant on the neighbors to the diagonal 
T=60  #temperature of Ising model. This will vary the entropy of the system
num_steps=300   #step iterated through the ising model. I will increment through a small # of steps, then look at what is on fire, then repeat

#ising_floor = Ising_fire_spread.Fire(ising_floor, Nx, Ny, J, J_diag, T, num_steps).ising_model()

time_step= 1
final_time= 300
t =np.linspace(0, final_time, int(final_time/time_step + 1))
print(t)


floor_time= np.zeros((Nx, Ny)) #create floor array for time
floor_hrr=np.zeros((Nx, Ny))
floor_water= np.zeros((Nx,Ny))

for time in t:  
    bar_floor= bar_plot.Bar(floor_hrr, Nx, Ny).heatmap()
    ising_floor = Ising_fire_spread.Fire(ising_floor, Nx, Ny, J, J_diag, T, num_steps).ising_model() #spread the fire a little bit for what would be one second
    floor_water+=droplet_iter.Droplet(Nx, Ny, max_drop_distance, x_center, y_center, dx, dy).droplets()
    for i in range(Nx):
        for j in range(Ny): #look through all the positions for new fire so that we can start the HRR polynomial
            if (ising_floor[i,j]== -1) and ((i,j) not in fire_pos_list):  # if there is a NEW fire in this location 
                fire_pos_list.append((i,j))  #postions of all arrays on fire
                floor_time[i,j]= time  #this will state the start time of the fire
                time_on_fire= time- floor_time[i,j]
            elif (ising_floor[i,j]==-1):  #if there is just a fire in this location that has already been here
                time_on_fire= time -floor_time[i,j]
            else: #if position is not on fire
                time_on_fire=0
                
            if ising_floor[i,j]==-1: #find HRR which is in kilo Wats (multiply by Nx and Ny to get ride of meters squared)
                if time <= 35:
                    floor_hrr[i,j]= dx * dy* ((-6*10**-7 * time_on_fire**6)+ (1*10**-4 * time_on_fire**5) + (-0.0058 * time_on_fire**4)+ (0.1399 * time_on_fire**3) -1.225 *time_on_fire**2 + (3.822 *time_on_fire)+9.041)   
                else: 
                    floor_hrr[i,j]=86 - 0.2*(time_on_fire-50)
                    
                floor_hrr[i,j]-= floor_water[i,j]
                if floor_hrr[i,j]<=0:
                    floor_hrr[i,j]=0
                
                


bar_floor= bar_plot.Bar(floor_hrr, Nx, Ny).plot_bar()
water_graph= bar_plot.Bar(floor_water, Nx, Ny).plot_bar()


print(fire_pos_list)
print(ising_floor)
print (floor_hrr)  #in kilo jouls
print(floor_time)
print(floor_water)


plt.imshow(ising_floor, cmap='RdYlGn')  #note: black is -1 while white is 1
plt.show()








