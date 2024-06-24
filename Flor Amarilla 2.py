from turtle import *
import turtle,

tracer(2)
h = 0
bgcolor('black')
pensize(2)
color('yellow')

for i in range(195):
    h += 0.006
    lt(179)
    backward(i*0.1)
    circle(i*0.3, 120)
    rt(14)
    forward(i*0.1)
    circle(i*0.3, 120)
    
turtle.shape('turtle')
turtle.pencolor('orangered')
turtle.fillcolor('orange')
phi = 137.508 * (math.pi / 180.0)
for i in range(300):
    r = 4 * math.sqrt(i)
    theta = i * phi
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(i * 137.508)
    turtle.pendown()
    turtle.stamp()
    
done()