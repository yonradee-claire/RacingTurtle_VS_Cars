from turtle import Turtle

class LittleTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(x=0, y=-280)
        self.setheading(90)

    def go_up(self):
        new_y = self.ycor() + 15
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(x=0, y=-280)