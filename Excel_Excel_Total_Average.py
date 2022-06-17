# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 13:19:22 2022

@author: Administrator
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x= pd.read_excel('sample.xlsx', 'New')

print(x)

c1 = x['Student Name']
c2 = x['Sub 1']
c3 = x['Sub 2']
c4 = x['Sub 3']

tx = np.linspace(0,4,5)

dx = pd.DataFrame({'Sl.No':tx,'Students Name':c1, 'Sub 1':c2,'Sub 2':c3, 'Sub 3':c4   })

total = c2 + c3 + c4
Average = (c2 + c3 + c4)/3

ty = np.linspace(0,4,5)

dy = pd.DataFrame({'Sl.No':ty,'Total':total, 'Average': np.around(Average,2)})

dx = dx.set_index('Sl.No')
dy = dy.set_index('Sl.No')

z = dx.join(dy,how='right')

print(z)
z.to_excel('Total.xlsx')


