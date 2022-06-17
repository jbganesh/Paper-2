# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 17:49:23 2022

@author: Administrator
"""

from scipy.interpolate import interp1d
from scipy.interpolate import BarycentricInterpolator
from scipy.interpolate import KroghInterpolator
from scipy.interpolate import PchipInterpolator
from scipy.interpolate import CubicSpline

import numpy as np

#x = [2,4,8,10,12,14]
#y = np.power(x,3)

x = [0.00000,0.12510,0.25692,0.28086,0.36076,0.42678,0.53621,0.56016,0.61073]
y = [0.15098,10.1346,20.11821,30.10183,40.61555,50.06906,60.58278,69.94794,79.93156]



interpolate_x = 0.5

#y_interp = interp1d(x, y)
#y_interp = BarycentricInterpolator(x,y)
#y_interp = PchipInterpolator(x, y)
#y_interp = KroghInterpolator(x, y)
y_interp = CubicSpline(x, y)

print("Value of Y at x = {} is {:.2f}".format((interpolate_x), y_interp(interpolate_x)))
