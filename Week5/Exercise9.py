'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6


Exercise 9
Using the dictionary of the 10 employees and their salaries that you created in exercise 8, write a program that creates two lists from that dictionary: one of the employee names and the other of their salaries, then displays both lists.
The names of the employees should be converted to upper-case (or lower-case if your original list was in upper-case). The salaries should each have £1,000 added to them because everyone got a bonus, then displays the converted lists.
'''

# The list created in exercise 6
employees = ['Arad', 'Amir', 'Asal', 'Mamad', 'Mohsen', 'Akvile', 'Shabnam', 'Hamid', 'Reza', 'Ali']

# Remaking the dictionary in exercise 8
dic_employees = {}
for index in employees:
    salary = int(input('Please enter the salary: '))
    dic_employees[index] = salary

# The list for the names in the dictionary
names = list(dic_employees.keys())

# The list for the salaries in the dictionary
salaries = list(dic_employees.values())

# Displaying names and salaries lists
print(names)
print(salaries)

# Making the names uppercase and desplaying them
names = list(map(lambda x: x.upper(), names))
print(names)

# Adding 1000 to the salaries and desplaying them
salaries = list(map(lambda x: x+1000, salaries))
print(salaries)