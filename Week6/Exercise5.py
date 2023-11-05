'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 30th, 2023
Version: Python 3.9.6

Exercise 5:
Write a function int_reverse(num) that will return a given integer in reverse.
Example: int_reverse(384) should return 483.
'''

# Reversing a given number
def int_reverse(num):
    reversed_number = 0
    while num > 0:
        # Getting the first digit
        remainder = num%10
        # Making the first digit into the last digit
        reversed_number = reversed_number * 10 + remainder
        # removing the first digit of the given number
        num = num // 10
    print(reversed_number)

int_reverse(384)