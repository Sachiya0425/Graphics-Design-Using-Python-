from turtle import*
import colorsys

bgcolor('black')
shape('turtle')
speed(0)
h = 0
size = 5
for i in range(180):
    color(colorsys.hsv_to_rgb(h,1,1))
    h +=0.005
    stamp()
    size +=1
    forward(size)
    right(30)
done()
