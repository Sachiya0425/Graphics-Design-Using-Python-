import turtle
import colorsys
screen = turtle.Screen()
screen.bgcolor('black')
spiral = turtle.Turtle()
spiral.speed(0)

for i in range(150):
    spiral.width(i/9)
    spiral.pencolor(colorsys.hsv_to_rgb(i/100,1.0,1.0))
    spiral.circle(i * 2)
    spiral.right(10)

    spiral.hideturtle()
turtle.done()