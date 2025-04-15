import turtle as l
l.bgcolor("black")
l.pencolor("red")
l.speed(100)
l.penup()
l.goto(0,300)
l.pendown()
x=0
y=0

while True:
    l.forward(x)
    l.right(y)
    x+=3
    y+=1

    if y == 210:
        break
    l.hideturtle()
l.done()
