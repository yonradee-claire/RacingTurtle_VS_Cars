import random
from random import randint
from turtle import Turtle, Screen
from little_turtle import LittleTurtle
from level import Level
from cars import Cars
import time

screen = Screen ()
screen.setup(600,600)
screen.bgcolor("white")
screen.title("Turtle Crossing Road")
screen.tracer(0)

turtle = LittleTurtle()

screen.listen()
screen.onkey(turtle.go_up, "Up")

level = Level()
car_list = []
def create_cars():
    for _ in range(randint(0, 1)):
        new_car = Cars()
        car_list.append(new_car)
    for cars in car_list:
        cars.move()

create_cars()

game_is_on = True
while game_is_on:
    create_cars()
    time.sleep(0.1)
    screen.update()
    level.update_level()

    # When turtle is at the opposite side send him back to where it starts
    if turtle.ycor() > 280:
        turtle.reset_position()
        level.level_up()

    # When turtle is bumped by a car, then game over
    for car in car_list:
        if turtle.distance(car) < 20:
            game_is_on = False
            level.game_over()

screen.exitonclick()