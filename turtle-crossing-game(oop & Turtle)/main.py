import time
from turtle import Screen
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
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update() # update the screen at every 0.1 seconds

    car_manager.create_car() # create 1 car at every 0.1 seconds
    car_manager.move_car()


    #Detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()


    #Detect a successful crossing
    if player.ycor() > 280:
        player.go_at_start()
        car_manager.level_up()
        scoreboard.increase_level()






screen.exitonclick()

