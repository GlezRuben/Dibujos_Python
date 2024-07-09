from turtle import *
from colorsys import *

bgcolor("black")
pu()
setpos(190, -60)
pd()
width(5)
speed(15)

R = 1
G = 1
B = 0

for i in range(150):
    begin_fill()
    color((R, G, B))
    circle(150-i, 50)
    lt(80)
    circle(150-i, 50)
    rt(150)
    R -= 0.0065
    G -= 0.0065
    end_fill()
    
done()