from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")

paddle = Turtle("square")
paddle.penup()
paddle.color("white")
paddle.shapesize(5, 1)
paddle.goto(350, 0)

screen.exitonclick()
