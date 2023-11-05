'''
Name: Arad Soutehkeshan
Student ID: 001347318
Date: Monday, October 16th, 2023
Version: Python 3.9.6

Exercise 8:
Modify the code such that it produces a design similar to figure 8.2.
'''

# Draws a design using repeated circles using Python's turtle module.
import turtle

# Program constants
MAX_NUM_CIRCLES = 24 # Number of circles to draw
ANGLE = 15           # Angle to turn
ANIMATION_SPEED = 0  # Animation speed

# Program variables
radius = 100         # Radius of each circle

# Set the animation speed.
turtle.speed(ANIMATION_SPEED)

# Draw 24 circles, with the turtle tilted by 15 degrees after each circle is drawn.
for x in range(MAX_NUM_CIRCLES):
    turtle.circle(radius)
    turtle.left(ANGLE)

for x in range(MAX_NUM_CIRCLES):
    turtle.circle(50)
    turtle.left(ANGLE)

for x in range(MAX_NUM_CIRCLES):
    turtle.circle(25)
    turtle.left(ANGLE)
    
turtle.exitonclick()  # waits until you click on the turtle window to close it.