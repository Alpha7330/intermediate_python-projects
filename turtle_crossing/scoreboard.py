from turtle import Turtle
FONT=("courier",24,"normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.goto(-280, 260)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"level:{self.level}", align="left", font=FONT)

    def increasel(self):
        self.level+=1
        self.update_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=FONT)