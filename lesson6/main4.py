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