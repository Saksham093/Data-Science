# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 11:06:13 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Check : https://replit.com/@appbrewery/day-1-3-exercise?v=1

# Write your code below this line 👇

# Using len()...
print(len(input('Name : ')))

# Using sys.getsizeof()
from sys import getsizeof

print(getsizeof(input('Name : ')))  # gives 54(Memory Size) 'Hello' input


# data['name of column'].str.len() 
print(len('йцы'.encode().decode('utf8')))
