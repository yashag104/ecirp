from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def generate_car(self):
        chance = randint(1, 6)
        if chance == 2 or chance == 4:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            y = randint(-250, 250)
            new_car.goto(300, y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
