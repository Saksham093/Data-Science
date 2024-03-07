# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 15:03:56 2024

@author: M.SAKSHAM
GitHub: Saksham093
"""

# Day: 02
# Data Types, Numbers, Operations, Type Conversion, f-Strings

# Data Types
print(type(234))  # Use type(), check the dType of prompt.


# Subscript
print('Hello'[1])

# Integers
print(123 + 456)
print(123_456_789)

# Float
print(34.234242)

# Boolean
print(True, False)

# TypeError
num_char = len(input('Your Name : '))
new_num_char = str(num_char)  # Type Conversion
print('Your Name has ' + num_char + " character.")  # TypeError: can only concatenate str (not "int") to str

print(70 + float('100.5'))

print(str(70) + str(100))

# Mathematical Oparations
6 + 6
3 - 1
3 * 3  # int as output
8 / 2  # float as output
2 ** 3

# Rules for Priority
# PEMDAS : () ** * / + -

print(3 * 3 + 3 / 3 - 3)
print(3 * (3 + 3) / 3 - 3)

# Number Manipulation
print(round(8 / 3, 3))

print(8//3)  # floor divison

score = 0
score += 1  # increase by one
print(score)

# F-String
score = 0
height = 1.78
isWinning = True

# using f
print(f'Your score is {score}, Your height is {height}, You are winning is {isWinning}')

# Using format()
print('Your score is {}, Your height is {}, You are winning is {}'.format(score, height, isWinning))
