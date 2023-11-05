'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 9th, 2023
Version: Python 3.9.6

Checking if forming a triangle is possible or not.
'''
line_lenght1 = int(input('Enter the first length: '))
line_lenght2 = int(input('Enter the second length: '))
line_lenght3 = int(input('Enter the third length: '))

if line_lenght1+line_lenght2 <= line_lenght3 or line_lenght1+line_lenght3 <= line_lenght2 or line_lenght3+line_lenght2 <= line_lenght1:
    print('Triangle cannot be formed')

else:
    print('Triangle can be formed')