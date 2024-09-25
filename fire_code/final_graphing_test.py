#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 17:46:23 2023

@author: williamluik
"""

import numpy as np
import matplotlib.pyplot as plt

time_on_fire= np.linspace(0, 50, 51)
print(time_on_fire)

function= (-6*10**-7 * time_on_fire**6)+ (1*10**-4 * time_on_fire**5) + (0.1399 * time_on_fire**3) -1.225 *time_on_fire**2 + (3.822 *time_on_fire)+9.041


# for t in time_on_fire:
#     print ((-6*10**-7 * t**6)+ (1*10**-4 * t**5) + (0.1399 * t**3) -1.225 *t**2 + (3.822 *t)+9.041)
    
    
#     print((1.117*(10**-8) *t**6) + (-3.8*(10**-6) * t**5)+ (0.0005 * t**4)+ (-0.032 *t**3) + (1.003 *t**2) + -12.52* t + (54.65) )
    
    
    
    
    
def f(t):
    return (-6*10**-7 * t**6)+ (1*10**-4 * t**5) + (-0.0058 * t**4)+ (0.1399 * t**3) -1.225 *t**2 + (3.822 *t)+9.041
t = np.linspace ( start = 0.    # lower limit
                , stop = 50      # upper limit
                , num = 51      # generate 51 points between 0 and 3
                )
y = f(t)    # This is already vectorized, that is, y will be a vector!
plt.plot(t, y)
plt.show()    


t=35
print( (-6*10**-7 * t**6)+ (1*10**-4 * t**5) + (-0.0058 * t**4)+ (0.1399 * t**3) -1.225 *t**2 + (3.822 *t)+9.041)
