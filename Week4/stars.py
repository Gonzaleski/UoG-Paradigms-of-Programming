'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Exercise 9:
Modify the code so that it draws 15 random-sized stars at random positions in the window.
'''

import turtle
import random

# Program constants
ANIMATION_SPEED = 10     # Animation speed (speed is a value from 0..10, where
                         # 0 is fastest; 10 is fast; 6 is normal; 3 is; 1 is slowest
ANGLE = 144              # Angle to turn

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 15 five corner stars in random sizes and positions
for i in range(15):
    DISTANCE = random.randint(1, 200)     # Distance to move (will determine star size)
    for i in range(1, 6):
        turtle.left(ANGLE)                # left(ANGLE) changes current direction counter-clockwise or anti-clockwise by "ANGLE" degrees.
        turtle.forward(DISTANCE)          # forward(DISTANCE) moves turtle "DISTANCE" number of steps (pixels) in current direction.
                                          # If the pen is down (pendown()) a line will be drawn as the turtle moves forward.
                                          # If "distance" is a negative number, the turtle will move backwards "distance" number of pixels.

    # Move to a random position in window
    turtle.penup()                        # raise drawing pen so that no line is drawn when moving
    turtle.goto(random.randint(-300, 300), random.randint(-300, 300))    # move to a position with random x, y coordinates
    turtle.pendown()                      # lower drawing pen again so a line is drawn when moving

turtle.exitonclick()  # waits until you click on the turtle window to close it.