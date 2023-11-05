'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Exercise 5
Write a program that calculates and displays the average of 10 integers entered by the user.
'''
# Setting a constant for the sum
sum = 0

# While loop
for i in range(10):

    # Asking for inetegers
    integer = int(input('Please enter your number: '))

    # Adding the integers to the sum
    sum += integer

print('The average of your numbers is', sum/10)