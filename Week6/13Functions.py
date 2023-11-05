'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 30th, 2023
Version: Python 3.9.6

Exercise 3:
seconds_since_midnight() should return the number of seconds since midnight.
Pass 3 integers to the function representing the current time of day (i.e. the current time represented by the current hour, minute, and seconds)
Assume that hour is an integer from 0 (midnight) to 23 (23pm), and assume minutes and seconds are integer from 0 to 59.
Test your function with actual time. For example, if the current time is 15:40:25, you will pass 15, 40 and 25 to the seconds_since_midnight() function.
'''

# Getting the inputs as hour, minute, second
def seconds_since_midnight(hour, minute, second):
    # Calculating seconds based on the number of given hours
    hour_in_secs = 3600 * hour
    # Calculating seconds based on the number of given minutes
    minute_in_secs = 60 * minute
    # Summing the seconds
    return hour_in_secs + minute_in_secs + second

# Giving some example inputs
time = seconds_since_midnight(15, 40, 25)
# printing our function results
print(time)