from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("ping-pong")
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard=Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #bounce
        ball.bounce_y()
    #detect collision
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
    #ball-beyond R
    if ball.xcor()>380 :
        ball.reset_postion()
        scoreboard.l_point()
    #ball-beyond Y
    if ball.xcor()<-380:
        ball.reset_postion()


screen.exitonclick()