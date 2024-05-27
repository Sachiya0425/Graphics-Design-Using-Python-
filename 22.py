import turtle
turtle.pensize(3)
turtle.speed(50)
turtle.bgcolor('black')

colors=['red','yellow','green','blue','grey']

def circle(s):
    for i in range(10):
        turtle.circle(s)
        s=s-4
        turtle.circle(s)
        turtle.color(colors[i%5])

def draw(s,repeat):
    for i in range(repeat):
        circle(s)
        turtle.right(360/repeat)
draw(100,10)
turtle.done()