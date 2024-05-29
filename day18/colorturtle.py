import  turtle as t
import random
ugway=t.Turtle()
t.colormode(255)
dir=[0,90,180,270]
ugway.pensize(7)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    return (r,g,b)
for i in range(200):
    random_color()
    ugway.color(random_color())
    ugway.forward(25)
    ugway.setheading(random.choice(dir))

t.done()


    