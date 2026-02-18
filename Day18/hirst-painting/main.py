import turtle as t
import random

screen = t.Screen()
screen.setup(768, 720)
screen.colormode(255)

timmy = t.Turtle()
timmy.penup()
timmy.speed(0)

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

def move_to_start():
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)

color_list = [(231, 206, 85), (218, 229, 219), (231, 222, 226), (224, 150, 89), (215, 224, 230), (120, 166, 185), (159, 14, 21), (34, 110, 157), (232, 82, 46), (124, 176, 144), (8, 97, 38), (171, 21, 16), (199, 65, 28), (185, 186, 27), (31, 128, 47), (12, 41, 74), (15, 63, 40), (242, 202, 5), (138, 82, 95), (85, 15, 22), (51, 166, 77), (44, 26, 22), (6, 65, 137), (173, 135, 149), (232, 170, 160), (48, 150, 195), (219, 66, 71), (74, 135, 186), (169, 206, 175)]

rows = 10

while rows > 0:
    for _ in range(10):
        timmy.dot(20, random.choice(color_list))
        timmy.forward(50)

    move_to_start()
    rows -= 1

timmy.hideturtle()
screen.exitonclick()
