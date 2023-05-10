import turtle

# Create a turtle object
t = turtle.Turtle()

# Draw a square
side_length = 100
angle = 90
count = 0
while count < 4:
    t.forward(side_length)
    t.right(angle)
    count += 1

# Move the turtle to a new location for the triangle
t.penup()
t.goto(150, 0)
t.pendown()

# Draw a triangle
side_length = 100
angle = 120
count = 0
while count < 3:
    t.forward(side_length)
    t.left(angle)
    count += 1

# Hide the turtle cursor
t.hideturtle()

# Wait for the user to close the window
turtle.done()
