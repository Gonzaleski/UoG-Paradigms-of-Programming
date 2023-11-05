'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6


Exercise 7
Write a program that calculates the factorial of positive integers entered by the user.
Write two versions of the factorial function, one using a Python while loop and the other using a for loop.
First version using while:
'''

# Asking for input
num = int(input('Please enter your number: '))

# Setting a constant for storing data
factorial = 1

# while loop
while num != 0:
    factorial *= num
    num -= 1

# Displayin the factorial
print('The factorial of your number is', factorial)