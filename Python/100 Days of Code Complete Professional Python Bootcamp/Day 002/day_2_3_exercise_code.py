# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 17:56:07 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Check : https://replit.com/@appbrewery/day-2-3-exercise?v=1
# Idea : https://waitbutwhy.com/2014/05/life-weeks.html


# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
years = 90 - int(age)
months = round(years * 12)
weeks = round(years * 52)
days = round(years * 365)

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
