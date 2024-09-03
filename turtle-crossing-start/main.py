import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("silver")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()  # focus on TurtleScreen in order to collect key-events
screen.onkeypress(player.go_up, "Up")

game_is_on = True
game_loop = 1

while game_is_on:

    if game_loop % 5 == 0:
        car_manager.generate_car()

    if car_manager.cars:
        car_manager.move()  # move one step for each car
        for car in car_manager.cars:
            if player.collide_with(car):
                game_is_on = False
                scoreboard.display_game_over()

    if player.cross_finish_line():
        player.reset_position()
        car_manager.increase_speed()
        scoreboard.increase_level()

    game_loop += 1
    time.sleep(0.1)
    screen.update()  # Perform a TurtleScreen update every 0.016 seconds (refresh)

screen.exitonclick()
