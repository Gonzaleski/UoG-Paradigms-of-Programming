'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Exercise 4
Write a program that asks for a name until the user enters END.
Display the name each time. When END is entered, display "All done!"
'''

# While loop
while True:

    # Asking for the name
    name = input('Please enter a name: ')

    # Checking if it is END
    if name == 'END':
        print('All done!')
        break

    # Displaying the name
    else:
        print(name)