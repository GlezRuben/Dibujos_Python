import turtle
import math
turtle.bgcolor("black")
t = turtle.Turtle()
t.pensize(3)

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def petalo1(angulo_eje):
    t.seth(angulo_eje - 38.79)
    t.circle(212.08, 77.58)
    t.seth(angulo_eje - 32.42 + 180)
    t.circle(247.82, 64.48)
    
def petalo2(angulo_eje):
    t.seth(angulo_eje - 45)
    t.circle(154.24, 90)
    t.seth(angulo_eje - 45 + 180)
    t.circle(154.24, 90)
    
def petalo3(angulo_eje):
    t.seth(angulo_eje - 45)
    t.circle(126.27, 90)
    t.seth(angulo_eje - 45 + 180)
    t.circle(126.27, 90)
    
def petalo4(angulo_eje):
    t.seth(angulo_eje - 18.58)
    t.circle(158.94, 37.16)
    t.seth(angulo_eje - 17.32 + 180)
    t.circle(170.11, 34.63)

t.pencolor("#a72545")
t.fillcolor("#fd2157")

petalos_capa1 = [65.2, 168.29, 250.8, 327.29]
for angulo in petalos_capa1:
    go(0,0)
    t.begin_fill()
    petalo1(angulo)
    t.end_fill()


t.pencolor("#df347d")
t.fillcolor("#ff80b6")

petalos_capa2 = [12.51, 119.16, 216.07, 293.71]
for angulo in petalos_capa2:
    go(0,0)
    t.begin_fill()
    petalo1(angulo)
    t.end_fill()
    
petalos_capa3 = [350.43, 78.47, 137.49, 193.74,
                 264.44, 41.44, 112.74, 168.29,
                 236.28, 307.56]
for angulo in petalos_capa3:
    go(0,0)
    t.begin_fill()
    petalo2(angulo)
    t.end_fill()
    
    
petalos_capa4 = [3.29, 59.45, 125.24, 176.54,
                 247.16, 312.27, 24.57, 93.79,
                 152.34, 214.16, 276.63, 340.03]
for angulo in petalos_capa4:
    go(0,0)
    t.begin_fill()
    petalo3(angulo)
    t.end_fill()

t.pencolor("#ffc414")
t.fillcolor("#e5e619")

petalos_capa4 = [17.45, 53.49, 79.61, 102.65,
                 129.66, 168.29, 199.65, 234.34,
                 258.19, 296.7, 310.05, 345.98]
for angulo in petalos_capa4:
    go(0,0)
    t.begin_fill()
    petalo4(angulo)
    t.end_fill()

turtle.speed(0)
phi = 137.508 * (math.pi / 180.0)
for i in range (200):
    r = 4 * math.sqrt(i)
    x = r * math.cos(i * phi)
    y = r * math.sin(i * phi)
    t.penup()
    t.goto(x, y)
    t.setheading(i * 137.508)
    t.pendown()
    t.stamp()

t.hideturtle()