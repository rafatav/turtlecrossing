from turtle import Screen
from car_manager import Car
from player import Player
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.title("Turtle Crossing Game")
screen.bgcolor("purple")
screen.listen()
screen.tracer(0)

player = Player()
score = Scoreboard()
car = Car()

screen.onkeypress(fun=player.move, key="w")
screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.move_cars()

    for c in car.cars:
        if player.distance(c) < 27 and abs(player.ycor() - c.ycor()) < 20:
            score.game_over()
            game_is_on = False

    if player.ycor() > 280:
        score.update_score()
        player.reset_player()
        car.speed_up()
        car.create_cars()

screen.exitonclick()
