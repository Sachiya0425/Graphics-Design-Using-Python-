import turtle
import colorsys
turtle.bgcolor('black')
turtle.tracer(100)
turtle.pensize(2)
h = 0
for i in range(350):
    c=colorsys.hsv_to_rgb(h,1,1)
    turtle.pencolor(c)
    h+=0.006
    turtle.right(119)
    turtle.circle(-i*0.3,120)
    turtle.circle(i*0.3,120)
    turtle.circle(-i*0.3,120)
turtle.done()
