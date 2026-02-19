from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# Function to move forward
def move_forward():
    timmy.forward(10)

# Function to move backward
def move_backward():
    timmy.backward(10)

# Function to move counter clock-wise
def counter_clockwise():
    timmy.left(10)
# Function to move clockwise
def clockwise():
    timmy.right(10)

# Function to clear screen
def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)

screen.exitonclick()
