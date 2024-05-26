import turtle
import colorsys as cs
turtle.setup(1000.1000)
turtle.tracer(10)
turtle.width(4)
turtle.bgcolor('black')

def square(x):
    for i in range(3):
        turtle.forward(x)
        turtle.left(90)
    turtle.forward(x)
for j in range(20):
    for i in range(10):
        turtle.color(cs.hsv_to_rgb(i/10,1-j/20,1))
        turtle.right(135)
        square(200-j*4)
        turtle.right(135)
        turtle.circle(20,36)
turtle.hideturtle()
turtle.done()