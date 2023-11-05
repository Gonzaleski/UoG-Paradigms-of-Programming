'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6


Exercise 7
Copy/paste the list of the 10 employees that you created in exercise 6 and convert (cast) it to a set.
Hint: to cast a list into a set you can use the set()type function in a similar way you as
for casting different data types covered in week 2.
Create a second set of 3 employees (one of whom should be you plus two others who were
not in the original list) called award_winners.
Write a program to display the name(s) of every employee in the computer department who
has won a company award (hint: that’s you!).
Then display the names of those employees who have not won an award.
'''

# The list created in exercise 6
employees = ['Arad', 'Amir', 'Asal', 'Mamad', 'Mohsen', 'Akvile', 'Shabnam', 'Hamid', 'Reza', 'Ali']

# Converting it to a set
employees_set = set(employees)

# Displaying the set
print(employees_set)

# Creating a set called award_winners
award_winners = {'Arad', 'Jay', 'Chia'}

# A loop to check the similarities between the employees set and winners set
for index in employees:
    if index in award_winners:
        print(index)
        employees.remove(index)

# Displaying the names of those who have not won an award
print(employees)