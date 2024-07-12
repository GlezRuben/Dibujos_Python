import turtle as t
import colorsys as cs

t.bgcolor("black")
c = 0
t.tracer(2,1)

for i in range(80):
     c += 0.15
     color = cs.hsv_to_rgb(c,1,1)
     t.pencolor(color)
     x = 2
     for j in range(1, 90):
         x += 2
         t.circle(x, j, steps=5)
         t.rt(60)
         t.right(j)
     t.reset()
     
t.exitonclick