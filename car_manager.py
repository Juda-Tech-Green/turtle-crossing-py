from turtle import Turtle
from random import randint,choice
import time
MOVE_INCREMENT = 1
STARTING_MOVE_DISTANCE = 5

class CarManager():
    def __init__(self):
        self.cars_list = []
        self.MOVE_DISTANCE = 5
    def get_car(self):
        if randint(1,6)==6:
            new_car = Turtle('square')
            new_car.up()
            new_car.color(self.change_color())
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            random_y = randint(-240, 240)
            new_car.goto(300, random_y)
            self.cars_list.append(new_car)

    def change_color(self):
        R = randint(1, 255)
        G = randint(1, 255)
        B = randint(1, 255)
        return (R, G, B)

    def move_cars(self):
        for car in self.cars_list:
            car.goto(car.xcor()-self.MOVE_DISTANCE,car.ycor())


    def upgrade_speed(self):
        self.MOVE_DISTANCE += MOVE_INCREMENT