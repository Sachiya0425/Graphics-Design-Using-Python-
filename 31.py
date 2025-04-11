import turtle
colors = ["red","yellow","green","blue","white","cyan"]
p = turtle.Pen()
turtle.bgcolor("black")

for i in range(500):
    p.pencolor(colors[i%4])
    p.width(i/100+2)
    p.forward(i)
    p.left(59)