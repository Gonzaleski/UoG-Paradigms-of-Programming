'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6

Exercise 5
Write a program that prompts the user to enter alphanumeric characters separated by a space in one entry (the entry may contain duplicate characters),
then displays only the distinct characters entered (that is with any duplicates removed).
'''

# Getting the input as alphanumeric characters
list1 = list(input('Please enter your alphanumeric characters separated by a space: '))
print(set(list1))