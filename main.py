import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
turtle.listen()
scoreboard = Scoreboard()
turtle.onkeypress(player.move, "Up")




game_is_on = True
while game_is_on:
    time.sleep(0.1)
    car_manager.generate_cars()
    car_manager.move()
    scoreboard.update_scoreboard()
    screen.update()

    for car in car_manager.cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.refresh_level()
        car_manager.increase_speed()



screen.exitonclick()