def prime_palindrome(n, max_range):
    result = []
    prime_numbers = []
    if max_range == 0 | max_range == 1:
        print('Range is too small')

    elif max_range == 2:
        print('1 is not a prime number')

    elif max_range > 2:
        
        numbers = range(1, max_range)
        reversed_numbers = []
        palindrome_numbers = []
        
        
        
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

        
        count = 0
        for num in numbers:
            is_palindrome = False 
            if num == reversed_numbers[count]:
                is_palindrome = True
                palindrome_numbers.append(num)

            count += 1
                
            is_prime = True
            if num == 1:
                is_prime = False
            for i in range(2, num):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime == True:
                prime_numbers.append(num)


            if is_prime & is_palindrome:
                
                result.append(num)
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

def is_palindrome():
    if reversed_number == number:
        print(True)
    else:
        print(False)