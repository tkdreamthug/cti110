import turtle

# Create a turtle object
t = turtle.Turtle()

# Set the pen color and size
t.pencolor('blue')
t.pensize(5)


t.penup()
t.goto(-100, 0)
t.pendown()

# Draw the first initial
t.penup()
t.forward(120)
t.right(90)
t.pendown()
t.forward(100)
t.backward(100)
t.left(90)
t.forward(40)
t.backward(80)

# Move to the right and lower the pen to draw the second initial
t.penup()
t.goto(150, 0)
t.pendown()

# Draw the second initial

t.backward(45)
t.left(90)
t.backward(45)
t.left(90)
t.backward(45)
t.right(90)
t.backward(45)
t.right(90)
t.backward(45)

# Hide the turtle cursor
t.hideturtle()

# Wait for the user to close the window
turtle.done()
