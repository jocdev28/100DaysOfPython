from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(x=0, y=280)
        self.display_score()

    def display_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="Game Over.", align=ALIGNMENT, font=FONT)
