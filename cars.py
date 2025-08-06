import random
from turtle import Turtle

colors = ["chartreuse2","cyan1","coral2","DeepPink2","burlywood4","DarkOrchid3","DarkGoldenrod2","cornsilk4"]
steps = [5,10,15,20,40]
speed = [0,1,6]

class Cars(Turtle):
    """Create cars"""
    def __init__(self): # accept a coordinate as parameter
        super().__init__()
        self.shape("square")
        self.color(random.choice(colors))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=random.randint(280, 640), y=random.randint(-250, 260))
        self.setheading(180)

    def move(self):
        self.speed(random.choice(speed))
        new_x = self.xcor() - random.choice(steps)
        y = self.ycor()
        self.goto(new_x,y)

