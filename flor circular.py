from turtle import *
import colorsys

tracer(100)
bgcolor("black")
pensize(20)
h = 0.6
up()
goto(-100, -60)
down()

for i in range(580):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 0.001
    color(c)
    up()
    circle(i, 20)
    down()
    circle(65, 145)
    lt(141)
    
done()