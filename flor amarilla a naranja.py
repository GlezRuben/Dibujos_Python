from turtle import *
import colorsys

speed(0)
pensize(2)
h = 0.18
bgcolor("black")

for i in range(200):
    c = colorsys.hsv_to_rgb(h,1,1)
    color(c)
    h -= 0.0012
    circle(200-i, 100)
    lt(100)
    circle(200-i, 100)
    rt(100)
    
    for j in range(3):
        rt(20)
        
done()