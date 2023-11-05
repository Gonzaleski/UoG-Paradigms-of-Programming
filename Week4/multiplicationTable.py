'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Exercise 6
Write a program that prints out a multiplication table for numbers 1 through 10 as shown opposite.
'''

# For loop
for i in range(1, 11):

    # An array for saving results
    array = []

    # For loop for multiplication
    for j in range(1, 11):
      
      # Adding the results to the array
      array.append(i*j)

    # Displaying the array
    print(array)