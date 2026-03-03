from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []

    def create_snake(self):
        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            snake_body = Turtle("square")
            snake_body.penup()
            snake_body.color("white")
            snake_body.goto(position)
            self.snake.append(snake_body)

    def move_snake(self):
        for body in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[body - 1].xcor()
            new_y = self.snake[body - 1].ycor()
            self.snake[body].goto(new_x, new_y)
        self.snake[0].forward(20)
