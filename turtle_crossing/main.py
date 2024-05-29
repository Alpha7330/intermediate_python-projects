import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard



screen= Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(player.go_up,"Up")
game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars()
    #collision
    for car in car_manager.all_cars:
       if  car.distance(player)<20:
           game_on=False
           scoreboard.game_over()
    #success crossing
    if player.is_finishl():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increasel()





screen.exitonclick()