from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

# Function to move forward
def move_forward():
    timmy.forward(10)

# Function to turn left
def turn_left():
    timmy.setheading(90)

# Get the Screen to listen for events
screen.listen()
screen.onkey(key="space", fun=move_forward)
screen.onkey(key="l", fun=turn_left)
screen.exitonclick()
