from turtle import *
color("red")
bgcolor("black")
speed(30)
right(45)
for i in range(155):
    if 7 < i < 62:
        left(5)
    if 80 < i <133:
        right(5)
    circle(50)
    if i < 80:
        forward(10)
    else:
        forward(5)