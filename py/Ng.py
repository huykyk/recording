# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:32:16 2017

@author: Administrator
"""

import numpy as np
#a = np.random.randn(5)
#
#print (a)
#print (a.shape)
#print(a.T)
#print(np.dot(a,a.T))
#a = np.random.randn(5,1)
#print(a)
#print(a.T)
#print(np.dot(a,a.T))
A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)
print(B.shape)