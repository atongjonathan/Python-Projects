from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.x_position = 0
        self.y_position = 0
        self.speed = 10


    def generate_position(self):
        self.x_position = random.randint(-250, 250)
        self.y_position = random.randint(-250, 250)
        position = self.x_position, self.y_position
        return position

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            random_y = random.randint(-250, 250)
            new_car.goto(300, random_y)
            self.cars.append(new_car)

    def move(self):
        for car in self.cars:
            car.back(self.speed)

    def speed_up(self):
        self.speed *= 2




