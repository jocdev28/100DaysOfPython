from turtle import Turtle, Screen
# import heroes
# import villains


timmy = Turtle()
timmy.shape("turtle")
timmy.color("purple")

# Make a square
# for index in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# Draw dotted lines
timmy.pensize(2)
square = 4
while square > 0:
    for _ in range(5):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)
    timmy.left(90)
    square -= 1



screen = Screen()
screen.exitonclick()

# print(heroes.gen())
# print(villains.gen())

