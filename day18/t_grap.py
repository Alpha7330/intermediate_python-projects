from turtle import Turtle,Screen
ugway=Turtle()
ugway.shape("turtle")
ugway.color("green")
# def side(x):
#     ugway.forward(x)
#     ugway.right(90)

# def square(x):
#     for i in range(4):
#        side(x)
# square(200)    

# def dash_line(turtle,length,dash_length):
#     for i in range(length//dash_length):
#         turtle.forward(dash_length)
#         turtle.penup()
#         turtle.forward(dash_length)
#         turtle.pendown()
# dash_line(ugway,100,10)

def polygon(length,sides):
    for _ in range(sides):
        angle=360/sides
        ugway.forward(length)
        ugway.right(angle)
polygon(100,6)        











screen=Screen()
screen.exitonclick()

