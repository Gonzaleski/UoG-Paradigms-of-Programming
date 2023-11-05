'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 23th, 2023
Version: Python 3.9.6

Modifying the code
'''
list1 = [0.3, 0.0, 0.4]
list2 = [0.2, 0.5, 0.6]

sum = 0.0

# Replaced XXXX with range(0, ,3)
for index in range(0, 3):
    # Replaced XXXX with list1[index] and list2[index]
    difference = list1[index]-list2[index]
    sum += difference**2

print(sum)