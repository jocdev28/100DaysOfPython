from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place a bet", prompt="Which turtle will win the race? Enter a color: ").lower()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

turtle_speed = ['fastest', 'fast', 'normal', 'slow', 'slowest']

# Function to create turtle
def create_turtle(color, step_x, step_y):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()

    new_turtle.goto(x=step_x, y=step_y)
    return new_turtle

turtles = []

start_x = -230
start_y = -100

for index in range(6):
    turtles.append(create_turtle(colors[index], start_x, start_y))
    start_y += 40

is_race_on = True

while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(10, 20)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lose. The {winning_color} turtle is the winner!")
            break

        # turtle.speed(random.choice(turtle_speed))

screen.exitonclick()
