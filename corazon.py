import math
import turtle

def xt(t):
    return 16*math.sin(t)**3

def yt(t):
    return 13*math.cos(t)-5*\
           math.cos(2*t)-2*\
           math.cos(3*t)-\
           math.cos(4*t)

t = turtle.Turtle()
t.speed(500)
turtle.bgcolor('black')

for i in range (2550):
    t.goto((xt(i)*20, yt(i)*20))
    t.pencolor('red')
    t.goto(0, 0)