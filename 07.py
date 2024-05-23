import turtle as t
import colorsys
t.bgcolor('black')
t.tracer(100)
def draw():
    h = 0
    n = 78
    t.up()
    t.goto(0,0)
    t.down()
    t.pensize(1)
    for i in range(100):
        c = colorsys.hsv_to_rgb(h,1,1)
        h +=1/n
        t.color(c)
        t.fd(20)
        t.circle(i,5,3)
        for k in range(i):
            t.fd(25)
            t.rt(36)
            t.bk(9)
            t.circle(k,5,3)
            t.rt(90.2)
draw()
for p in range(50):
    draw()
t.done()