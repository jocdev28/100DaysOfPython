from turtle import Screen, Turtle

# Screen set-up
screen = Screen()
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")
screen.tracer(0)

# Create the paddle for the player
paddle = Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.penup()
paddle.goto(350, 0)


# Functions to trigger on keypresses
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)

def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

# Get the screen to listen for keypresses
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()
