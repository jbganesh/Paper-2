# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 13:00:39 2022

@author: Administrator
"""
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

x = np.arange(0, 0.8, 0.01)

y = ((1-x) ** (-1)) - 1

z = - (np.log(1-x))



print(x)



plt.plot(y ,x,'r-', label = 'Function value 1')
plt.plot(z ,x,'b--', label = 'Function value 2')

plt.ylabel('Alpha')
plt.xlabel('Time in Days')
plt.legend(loc='best')

plt.show()
