import turtle
from turtle import *
import colorsys

tracer(100)
h = 0.85
speed(25)
bgcolor("black")

for i in range(190):
    c = colorsys.hsv_to_rgb(h,1,1)
    fillcolor(c)
    h += 0.0015
    begin_fill()
    circle(190-i, 90)
    lt(75)
    lt(20)
    circle(190-i, 90)
    lt(18)
    end_fill()

done()    