import math
import turtle

t = turtle.Turtle()
turtle.speed(2000)
turtle.bgcolor("black")

def corazon(k):
    return 15*math.sin(k)**3

def corazon1(k):
    return 12*math.cos(k)-5*\
           math.cos(2*k)-2*\
           math.cos(3*k)-\
           math.cos(4*k)

t.color("gold")
t.penup()
t.goto(115,-40)
t.pendown()
t.write("I Love You", True,
      "right", ("indie flower", 30, "bold"))

for i in range(600):
    t.goto(corazon(i)*18, corazon1(i)*18)
    for j in range(5):
        t.color("red")

t.hideturtle()
turtle.done()