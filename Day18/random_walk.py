import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.pensize(10)

# Generate a random color using RGB
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color_tuple = (r, g, b)
    return color_tuple

# colors = ["crimson", "dark green", "wheat", "deep sky blue", "dark slate gray", "dark orchid", "magenta", "coral"]
directions = [0, 90, 180, 270]
# colors = random_color()

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = t.Screen()
screen.exitonclick()
