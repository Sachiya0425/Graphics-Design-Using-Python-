from turtle import*
import colorsys
tracer(3)
h = 0.7
bgcolor('black')
pensize(2)

for i in range(190):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h +=0.004
    circle(190-i, 90)
    lt(90)
    lt(20)
    circle(190-i, 90)
    lt(20)
done()