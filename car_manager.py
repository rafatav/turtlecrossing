from turtle import Turtle
import random
COLORS = ["medium violet red", "medium orchid", "violet", "plum", "medium purple", "blue violet"]


class Car:

    def __init__(self):
        self.car_speed = 5
        self.cars = []
        self.create_cars()

    def create_cars(self):
        for pos in range(25):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choices(COLORS))
            x_random = random.randint(-400, 400)
            y_random = random.randint(-230, 230)
            self.cars.append(car)
            self.cars[pos].goto(x_random, y_random)

    def move_cars(self):
        for car in self.cars:
            car.backward(self.car_speed)
            if car.xcor() < -400:
                car.goto(400, car.ycor())

    def speed_up(self):
        self.car_speed += 1
