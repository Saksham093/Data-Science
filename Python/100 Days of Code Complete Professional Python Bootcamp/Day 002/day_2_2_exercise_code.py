# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:34:52 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Check : https://replit.com/@appbrewery/day-2-2-exercise?v=1

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Using the exponent operator **
bmi_1 = weight / height ** 2

# or using multiplication and PEMDAS
bmi_2 = weight / (height * height)

print(int(bmi_1))
