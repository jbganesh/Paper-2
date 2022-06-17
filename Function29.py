# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 16:22:35 2022

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


a = np.arange(0, 0.8, 0.01)


G_a = ((1-a)** (-1)) - 1


a_half = 0.5
G_a_half = ((1-(a_half))** (-1)) - 1
y_fit = G_a / G_a_half


z = pd.DataFrame({'Alpha Value':a,'Function':G_a, 'Y Fit':y_fit})

print (z)
z.to_excel('Function29.xlsx')



