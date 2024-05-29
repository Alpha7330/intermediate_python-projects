import turtle
from turtle import Turtle,Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
game_on=False
bet=screen.textinput(title="make your bet",prompt="which turtle you bet on").lower()
print(bet)
all_turtles=[]
colors=("red","orange","yellow","green","blue","purple")
y_list=(-60,-30,0,30,60,90)
for t_index in range(0,6):
    tim=Turtle()
    tim.shape("turtle")
    tim.color(colors[t_index])
    tim.penup()
    tim.goto(x=-240,y=y_list[t_index])
    all_turtles.append(tim)

if bet:
    game_on=True
while game_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            game_on=False
            wincolor=turtle.pencolor()
            if wincolor==bet:
                print(f"you won {wincolor} has won the race")
            else:
                print(f"you lose {wincolor} has won the race")

        rand_distance=random.randint(1,10)
        turtle.forward(rand_distance)
















screen.exitonclick()