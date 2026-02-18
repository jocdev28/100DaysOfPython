import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed(0)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple

def draw_spirograph(size_of_gap):
    gap_stop = int(360 / size_of_gap)
    for _ in range(gap_stop):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()
