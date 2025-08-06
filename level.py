from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 0
        self.color("black")
        self.penup()
        self.hideturtle()

    def update_level(self):
        self.goto(-240, 250)
        self.write(f"Level: {self.current_level}", align="center", font=("Courier", 16, "bold"))

    def level_up(self):
        self.current_level += 1
        self.clear()
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("Game Over!", align="center", font=("Courier", 32, "bold"))


