# -*- coding: utf-8 -*-
"""
Created on Fri Jun 17 11:47:40 2022

@author: Administrator
"""

from sklearn.metrics import r2_score 
import numpy


#actual = [1,2,3,4,5]
#predict = [1.1,2.2,3.3,4.4,5.5]
 
#corr_matrix = numpy.corrcoef(actual, predict)
#corr = corr_matrix[0,1]
#R_sq = corr**2
 
#print("{:.2f}".format(R_sq))



a =[1, 2, 3, 4, 5] 
b =[1.1,2.2,3.3,4.4,5.5] 
R_square = r2_score(a, b) 
print('Coefficient of Determination', R_square) 