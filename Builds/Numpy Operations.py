# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 08:56:47 2020

@author: m87450 - Ed Saiedi 
"""

# Python code to perform arithmetic 
# operations on NumPy array 

# Derived from here: https://www.geeksforgeeks.org/python-operations-on-numpy-arrays/  
  
import numpy as np  
  
  
# Initializing the array 
arr1 = np.arange(4, dtype = np.float_).reshape(2, 2)  
  
print('First array:')  
print(arr1) 
  
print('\nSecond array:')  
arr2 = np.array([12, 12])  
print(arr2) 
  
print('\nAdding the two arrays:')  
print(np.add(arr1, arr2)) 
  
print('\nSubtracting the two arrays:')  
print(np.subtract(arr1, arr2)) 
  
print('\nMultiplying the two arrays:') 
print(np.multiply(arr1, arr2)) 
  
print('\nDividing the two arrays:') 
print(np.divide(arr1, arr2)) 

# Add example 2

# Python code to perform reciprocal operation 
# on NumPy array 
import numpy as np  
arr = np.array([25, 1.33, 1, 1, 100])  
  
print('Our array is:') 
print(arr) 
  
print('\nAfter applying reciprocal function:')  
print(np.reciprocal(arr)) 
  
arr2 = np.array([25], dtype = int) 
print('\nThe second array is:') 
print(arr2) 
  
print('\nAfter applying reciprocal function:')  
print(np.reciprocal(arr2)) 

# Adding example 3 on this cool page:

import numpy as np  
  
  
arr = np.array([5, 15, 20])  
arr1 = np.array([2, 5, 9])  
  
print('First array:')  
print(arr)  
  
print('\nSecond array:')  
print(arr1) 
  
print('\nApplying mod() function:')  
print(np.mod(arr, arr1)) 
  
print('\nApplying remainder() function:')  
print(np.remainder(arr, arr1))
