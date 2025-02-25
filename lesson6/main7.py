import turtle
# Set up the screen
screen = turtle.Screen()  # Corrected indentation
screen.bgcolor("lightblue")  # Set the background color
# Create a turtle to draw the triangle
tri = turtle.Turtle()
# Set the fill color
tri.fillcolor("green")
# Begin the fill process
tri.begin_fill()
# Draw an equilateral triangle
for _ in range(3):
    tri.forward(100)  # Side length of 100 units
    tri.left(120)  # Turn left by 120 degrees to form an equilateral triangle
# End the fill process
tri.end_fill()
# Hide the turtle after drawing
tri.hideturtle()
# Close the turtle graphics window when clicked
screen.exitonclick()

import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightyellow")  # Set the background color

# Create a turtle to draw the rectangle
rect = turtle.Turtle()

# Set the fill color
rect.fillcolor("blue")

# Begin the fill process
rect.begin_fill()

# Draw a rectangle
for _ in range(2):
    rect.forward(150)  # Length of the rectangle
    rect.left(90)
    rect.forward(100)  # Width of the rectangle
    rect.left(90)

# End the fill process
rect.end_fill()

# Hide the turtle after drawing
rect.hideturtle()


import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightcoral")  # Set the background color

# Create a turtle to draw the hexagon
hex = turtle.Turtle()

# Set the fill color
hex.fillcolor("yellow")

# Begin the fill process
hex.begin_fill()

# Draw a hexagon
for _ in range(6):
    hex.forward(100)  # Side length of 100 units
    hex.left(60)  # Turn left by 60 degrees to form a hexagon

# End the fill process
hex.end_fill()

# Hide the turtle after drawing
hex.hideturtle()

# Close the turtle graphics window when clicked
screen.exitonclick()
