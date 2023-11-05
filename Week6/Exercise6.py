'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 30th, 2023
Version: Python 3.9.6

Exercise 6:
Write a function is_palindrome(num) that uses int_reverse() to check if a given integer is a palindrome. A number is palindromic if it remains the same when its digits are reversed (i.e. its reverse is the same as itself).
Example: 18381, 11, 474, 33 are all palindrome numbers.
is_palindrome(num) should return True if num is a palindrome and False if not.
'''

# Reversing a given number
def int_reverse(num):
    global number
    number = num
    global reversed_number
    reversed_number = 0
    while num > 0:
        # Getting the first digit
        remainder = num%10
        # Making the first digit into the last digit
        reversed_number = reversed_number * 10 + remainder
        # removing the first digit of the given number
        num = num // 10
    return reversed_number

int_reverse(18381)

# Checking if the number is palindrome
def is_palindrome():
    if reversed_number == number:
        print(True)
    else:
        print(False)
        
is_palindrome()