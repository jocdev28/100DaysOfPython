from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

snake = []

snake_length = 3

for index in range(snake_length):
    snake.append(tim)
    tim.shape("square")
    tim.color("white")
    tim.penup()



screen.exitonclick()
