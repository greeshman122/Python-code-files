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