import colorgram
import random
import turtle as t

ugway = t.Turtle()
screen=t.Screen()
screen.bgcolor("light gray")
ugway.speed("fastest")
ugway.penup()
ugway.ht()
rgb_colors = []
colors = colorgram.extract('spots.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)
t.colormode(255)
ugway.setheading(225)
ugway.forward(300)
ugway.setheading(0)
number_of_dots = 100
for n_dots in range(1, number_of_dots+1):
    ugway.dot(20, random.choice(rgb_colors))
    ugway.forward(50)
    if n_dots % 10 == 0:
        ugway.setheading(90)
        ugway.forward(50)
        ugway.setheading(180)
        ugway.forward(500)
        ugway.setheading(0)

t.done()
