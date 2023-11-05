'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6

Exercise 4
Write a program that creates a tuple containing the seven days of the week and displays it.
Prompt the user to enter one of the days shown and then display the index number of that
element in the tuple.
Finally, ask the user to enter a number within the tuple size range and display the day of the
week that corresponds to that index number in the tuple.
'''

# Creating the tuple
weekdays = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', )

# Displaying the tuple
print(weekdays)

# Getting the inputs as an element
name = input('Please enter your preferred day: ')

# Displaying the index number of an element
print(weekdays.index(name))

# Getting the inputs as an index
index = int(input('Please enter your preferred index in the range of 0 to 6: '))

# Displaying the element of an index number
print(weekdays[index])