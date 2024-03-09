# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 17:21:23 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Check : https://replit.com/@appbrewery/day-3-2-exercise?v=1

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

bmi = round(weight / height ** 2)
if bmi < 18.5:
    print(f'Your BMI is {bmi}, You are underweight.')
elif bmi < 25:
    print(f'Your BMI is {bmi}, You have a normal weight.')
elif bmi < 30:
    print(f'Your BMI is {bmi}, You are slightly overweight.')
elif bmi < 35:
    print(f'Your BMI is {bmi}, You are obese.')
else:
    print(f'Your BMI is {bmi}, You are clinically obese.')
