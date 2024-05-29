import turtle as t
ugway=t.Turtle()
ugway.speed(100)
def spiral():
    angle=0
    for i in range(200):
        ugway.circle(100)
        angle+=10
        ugway.setheading(angle)
        
spiral()        
t.done()