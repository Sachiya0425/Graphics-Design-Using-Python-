import turtle
h = 1
t = turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)

while True:
    t.forward(h)
    t.color('yellow')
    t.left(120*3)
    t.left(1)
    h += 1
    t.forward(h)
    t.color('green yellow')
    t.right(350)
    t.radians()
    t.color('orange')
    t.right(30)
turtle.done()