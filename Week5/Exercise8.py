'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6


Exercise 8
Copy/paste the list of the 10 employees that you created in exercise 6 and convert it to a dictionary that adds the salary for each employee as entered by the user.
Write a program that prompts the user to enter a name that exists in the dictionary and then displays their salary.
'''

# The list created in exercise 6
employees = ['Arad', 'Amir', 'Asal', 'Mamad', 'Mohsen', 'Akvile', 'Shabnam', 'Hamid', 'Reza', 'Ali']

# Creating an empty dictionary for employees and thier salaries given by the user
employees_dic = {}

# Creating a loop to add keys and values to the dictionary
for index in employees:
    salary = int(input('Please enter the salary: '))
    employees_dic[index] = salary

# Displaying the dictionary
print(employees_dic)