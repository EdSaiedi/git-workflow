# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 10:57:00 2020

@author: m87450 - Ed Saiedi 
"""

import pandas as pd
import numpy as np

# Implement example A of this df exercise: https://www.geeksforgeeks.org/python-pandas-dataframe-pow/

df1 = pd.DataFrame({"A":[14, 4, 5, 4, 1], 
                    "B":[5, 2, 54, 3, 2], 
                    "C":[20, 20, 7, 3, 8], 
                    "D":[14, 3, 6, 2, 6]}) 

sr = pd.Series([2, 3, 4, 2], index =["A", "B", "C", "D"]) 

print(sr)
print(df1)
df1_to_power_of_sr = df1.pow(sr, axis=1)
print(df1_to_power_of_sr)

# Implement example B of this df exercise: https://www.geeksforgeeks.org/python-pandas-dataframe-pow/:

df2 = pd.DataFrame({"A":[1, 5, 3, 4, 2], 
                    "B":[3, 2, 4, 3, 4], 
                    "C":[2, 2, 7, 3, 4], 
                    "D":[4, 3, 6, 12, 7]}) 
# using pow() function to raise each element 
# in df1 to the power of corresponding element in df2 
df1.pow(df2) 