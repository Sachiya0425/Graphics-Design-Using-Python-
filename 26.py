from turtle import*
from colorsys import*
bgcolor('black')
tracer(100)
pensize(3)
h = 0 

def draw(th, n):
    circle(5+n,69)
    left(th)
    circle(5+2*n, 60)

goto(0,0)

for i in range(500):
     c = hsv_to_rgb(h,1,1)
     h+= 0.005
     color(c)
     up()
     draw(90,i)
     draw(180, i)
     down()
     draw(1/2, i-i)
     draw(180, i-2)
     draw(120, i-i)
