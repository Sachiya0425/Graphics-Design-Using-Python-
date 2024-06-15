from turtle import*
import colorsys as cs
bgcolor('black')
tracer(20)
pensize(4)
h = 0
def draw(int,t):
    circle(5+t,90)
    left(int)
    circle(5+t,60)
goto(-10,0)
for i in range(400):
    c = cs.hsv_to_rgb(h,1,1)
    h +=0.005
    color(c)
    up()
    draw(90,i/50)
    draw(180,i/2)
    down()
    fillcolor('black')
    begin_fill()
    draw(1/2,0)
    draw(180,i/2)
    draw(90,i/2)
    end_fill()
    draw(60,i)
done()