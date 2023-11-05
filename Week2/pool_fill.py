'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 2nd,2023
Version: Python 3.9.6

This code represents the time it takes for a pool to be filled with two hoses (green and red) at the same time; while the green and the red
hoses themselves fill the pool in 1.5 and 1.2 hours, respectively.
'''
green_filling_rate = 1/1.5
red_filling_rate = 1/1.2
estimated_time = (1/(green_filling_rate + red_filling_rate))*60
print('Both hoses will fill the pool in', estimated_time ,'minutes')