import time
from turtle import  Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkeypress(player.go_up, 'Up') 
screen.onkeypress(player.go_down, 'Down')

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # collusion with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()

    # Successful crossing
    if player.finishing():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()





screen.exitonclick()