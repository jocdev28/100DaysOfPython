from turtle import Turtle, Screen

tim = Turtle()

colors = ["crimson", "dark green", "wheat", "deep sky blue", "dark slate gray", "dark orchid", "magenta", "coral"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for index in range(3, 11):
    tim.pencolor(colors[index-3])
    draw_shape(index)


screen = Screen()
screen.exitonclick()
