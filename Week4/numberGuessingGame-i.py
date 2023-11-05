'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Asking the user to enter integers until the number entered matches the number generated
in the program or the user terminates the guessing process by entering 0.
'''

from random import randint

# Generating a random number
random_number = randint(1, 10)

# While loop
while True:

    # User guess
    user_guess = int(input('Please guess a number between 1 to 9: '))
    
    if user_guess == random_number or user_guess == 0:
        break