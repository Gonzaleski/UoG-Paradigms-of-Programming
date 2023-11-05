'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 9th, 2023
Version: Python 3.9.6

Magic Kingdom Park
Checking if customers can use a specific ride name based on their age and height.
'''
print('''
Ride name           code
Carnival Carousel    1
Dodgems              2
Pandemonium          3
Phantom Ghost Zone   4
Scenic River Cruise  5
      ''')

code = int(input('Please enter your preferred ride code: '))
age = int(input('Please enter your age: '))
height = float(input('Please enter your height(in meter): '))

if code == 1:
    if age >= 5:
        print('You can use Carnival Carousel')
    
    else:
        print('You cannot use Carnial Carousel')

elif code == 2:
    if age >= 12 and height >= 1.3:
        print('Your can use Dodgems')

    else:
        print('You cannot use Dodgems')

elif code == 3:
    if 16 <= age <=70 and 1.4 <= height <= 2:
        print('You can use Pandemonium ')
    
    else:
        print('You cannot use Pandemonium')

elif code == 4:
    if age >= 8:
        print('You can use Phantom Ghost Zone')
    
    else:
        print('You cannot use Phantom Ghost Zone')

elif code == 5:
    print('You can use Scenic River Cruise')

else:
    print('Entered code is not valid! Please try again.')