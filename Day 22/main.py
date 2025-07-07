import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
score = Scoreboard()
car_manager = CarManager()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            score.over()

    if player.finish():
        player.start_again()
        score.update()
        car_manager.speed_up()

screen.exitonclick()
