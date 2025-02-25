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
