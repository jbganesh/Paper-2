# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 18:25:16 2022

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline
from sklearn.metrics import r2_score 

# Read the data from the experiment files
x= pd.read_excel('Raw_data.xlsx', 'Exp_data')

# Reading the experimental alpha and Time (Day) values
c1 = x['Act wt % value']            # alpha value
c2 = x['Act Time(Days) value']      # Time in days   

# Calculation of modified alpha value (In terms of % change)
ini_weight = c1[0]
no_of_values = len(c1)
i = 0
a = []

for i in range (no_of_values):
    c1_mod = (ini_weight - c1[i]) / ini_weight    
    a.append(c1_mod)     # This is the modified alpha value (C1 modified)
    
# Calcuation test value for the alpha value 0.5
interpolate_a = 0.5

#From the alpha 0.5 -> Corresponding experimental Time calculated by interpolation
y_interp = CubicSpline(a, c2)
y_test_half = y_interp(interpolate_a)


# Converted experimental time value i.e Y_test value
i = 0
b = []
for i in range (no_of_values):
    c2_mod = c2[i] / y_test_half
    b.append(c2_mod)  # This is the modified time value (C2 Modified)


# Calculation of G(a) function
    # First taking the alpha value from the exp data
array_len = len(a)

# Calculation of G(a) function values
i =0
G_a= []
y_fit = []
a_half = 0.5    # Half the alpha value
G_a_half = (1-(1-(a_half))**(0.5))**(2)        ####!!!! Update Here (1/2)
print(G_a_half)


# Calcuation y_fit value for the alpha value 0.5
for i in range (array_len):   
    G = (1-(1-a[i])**(0.5))**(2)           ####!!!! Update Here (2/2)
    G_a.append(G)
    y= G_a[i] / G_a_half
    y_fit.append(y)

# Writing the fit values to Excel
z = pd.DataFrame({'Act wt % value':c1, 'Act Time(Days) value':c2, 'Alpha Value':a,'Function(G(a))':G_a, 'Y Fit':y_fit,'Y Test':b})
z.to_excel('Function31_act.xlsx')
print(z)

# Calculating the R Square value

R_square = r2_score(b, y_fit) 
print('Coefficient of Determination {:.2f}'.format(R_square))


