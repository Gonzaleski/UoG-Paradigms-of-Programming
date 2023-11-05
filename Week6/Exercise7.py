'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Wednesday, November 1th, 2023
Version: Python 3.9.6

Exercise 7:
Write a function that take 2 integers, n and max_range, as arguments and displays the first n palindromic prime numbers up to max_range.
Use the function is_palindrome() you created in exercise 7 to find the palindromic numbers.
Display 10 numbers per line and align the numbers properly, as follows:
2 3 5 7 11 101 131 151 181 191
313 353 373 383 727 757 787 797 919 929
'''

# Getting input from the user
max_range = int(input('Please Enter your range: '))
n = int(input('Please the amount of numbers your want to be shown: '))

# Creating a function
def prime_palindrome(n, max_range):

    # Creating local lists for storing related data
    result = []
    prime_numbers = []

    # Cheking if the inputs are useful
    if max_range == 0 | max_range == 1:
        print('Range is too small')

    elif max_range == 2:
        print('1 is not a prime number')

    elif max_range > 2:
        numbers = range(1, max_range)
        reversed_numbers = []
        palindrome_numbers = []
        
        # Creating a for loop to access numbers elements
        for num in numbers:

            reversed_number = 0
            while num > 0:
                # Getting the first digit
                remainder = num%10
                # Making the first digit into the last digit
                reversed_number = reversed_number * 10 + remainder
                # removing the first digit of the given number
                num = num // 10
            reversed_numbers.append(reversed_number)

        # Checking if the number is palindrome
        for num in numbers:
            is_palindrome = False 
            if num == reversed_numbers[num-1]:
                is_palindrome = True
                palindrome_numbers.append(num)

            # Checking if the number is prime
            is_prime = True
            if num == 1:
                is_prime = False
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                prime_numbers.append(num)

            # Making the result list
            if is_prime & is_palindrome:  
                result.append(num)

        # Giving out put and check if n is more than the number of values in the list
        if len(result) < n:
            print('This list does not have', n, 'elements. But here is the maximum showable amount of numbers:')
            for i in range(len(result)):
                print(result[i], end = ' ')
                if i == 0:
                    pass
                elif i % 9 == 0:
                    print('')
        else:
            for i in range(n):
                print(result[i], end = ' ')
                if i == 0:
                    pass
                elif i % 9 == 0:
                    print('')

prime_palindrome(n, max_range)