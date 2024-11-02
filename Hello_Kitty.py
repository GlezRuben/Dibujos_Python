import math
import turtle as t

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

def polyline(t1, n, long, ang):
    for index in range(n):
        t1.fd(long)
        t1.lt(ang)
        
def flower(n):
    for x in range(n):
        t.forward(0.5)
        if x < 80:
            t.left(1)
        elif x < 120:
            t.left(2.3)
        else:
            t.left(1)
            
t.bgcolor("white")
t.pensize(8)
t.speed(100)

go(-130,170)
t.setheading(220)
for x in range(580):
    t.forward(1)
    if x < 250:
        t.left(0.5)
    elif x < 350:
        t.left(0.1)
    else:
        t.left(0.5)
        
t.setheading(70)
for y in range(150):
    t.forward(1)
    if y < 80:
        t.left(0.2)
    elif y < 90:
        t.left(10)
    else:
        t.left(0.2)
t.setheading(160)
for y1 in range(140):
    t.forward(1)
    t.left(0.15)
t.setheading(140)
for y2 in range(157):
    t.forward(1)
    if y2 < 65:
        t.left(0.2)
    elif y2 < 75:
        t.left(8)
    else:
        t.left(0.5)
        
t.pensize(5)
go(-100,60)
t.setheading(350)
t.fillcolor("black")
t.begin_fill()
step = 0.3
for i in range(2):
    for j in range(60):
        if j < 30:
            step += 0.02
        else:
            step -= 0.02
        t.forward(step)
        t.left(3)
t.end_fill()

go(50, 40)
t.setheading(350)
t.fillcolor("black")
t.begin_fill()
step = 0.3
for i in range(2):
    for j in range(60):
        if j < 30:
            step += 0.02
        else:
            step -= 0.02
        t.forward(step)
        t.left(3)
t.end_fill()

go(-40, 30)
t. setheading(260)
t.fillcolor("#EBC70E")
t.begin_fill()
step = 0.3
for i in range(2):
    for j in range(60):
        if j < 30:
            step += 0.02
        else:
            step -= 0.02
        t.forward(step)
        t.left(3)
t.end_fill()

go(20, 180)
t.fillcolor("#DD4A76")
t.begin_fill()
t.setheading(175)
flower(200)
t.setheading(250)
flower(200)
t.setheading(325)
flower(200)
t.setheading(40)
flower(200)
t.setheading(115)
flower(200)
t.end_fill()

go(30, 180)
t.setheading(270)
t.fillcolor("#E7BE04")
t.begin_fill()
t.circle(10)
t.end_fill()

go(-150, 65)
t.setheading(170)
t.pensize(6)
for y in range(40):
    t.forward(1)
    t.left(0.3)
    
go(-150, 85)
t.setheading(160)
for y in range(50):
    t.forward(1)
    t.left(0.3)
        
go(-150, 45)
t.setheading(180)
for y in range(55):
    t.forward(1)
    t.left(0.3)

go(110, 10)
t.setheading(340)
for y in range(40):
    t.forward(1)
    t.left(0.3)
    
go(120, 30)
t.setheading(350)
for y in range(30):
    t.forward(1)
    t.right(0.3)
    
go(115, 50)
t.setheading(360)
for y in range(50):
    t.forward(1)
    t.right(0.3)
    
t.pensize(8)
go(-100, -30)
t.setheading(230)
t.fillcolor("#EFA9C1")
t.begin_fill()
for z in range(140):
    t.forward(1)
    t.left(0.2)
    
t.setheading(340)
for z in range(200):
    t.forward(1)
    t.left(0.1)
    
t.setheading(85)
for z in range(140):
    t.forward(1)
    t.left(0.1)
t.end_fill()

go(-73, -33)
t.setheading(250)
t.fillcolor("#DA4B76")
t.begin_fill()
t.circle(40, 205)
t.setheading(170)
t.pensize(6)
t.forward(75)
t.end_fill()

t.pensize(8)
go(-120, -17)
t.setheading(230)
t.fillcolor("#D64B75")
t.begin_fill()
t.forward(50)
t.setheading(320)
for k in range(27):
    t.forward(1)
    t.left(1)
t.setheading(75)
for k in range(50):
    t.forward(1)
    t.right(1)
t.end_fill()

go(-125, -15)
t.setheading(140)
t.fillcolor("white")
t.begin_fill()
t.forward(8)
t.setheading(50)
t.circle(10, 190)
t.setheading(150)
for j in range(80):
    t.forward(1)
    t.left(2.2)
t.forward(24)
t.end_fill()

go(27, -45)
t.fillcolor("#DB4E79")
t.setheading(350)
t.begin_fill()
for x in range(50):
    t.forward(1)
    t.right(1)
t.setheading(220)
t.forward(40)
t.setheading(100)
for x in range(50):
    t.forward(1)
    t.left(0.2)
t.end_fill()

go(70, -75)
t.setheading(300)
t.forward(8)
t.setheading(30)
for x in range(40):
    t.forward(1)
    t.right(5)
t.setheading(280)
for x in range(70):
    t.forward(1)
    t.right(2)

go(-70, -180)
t.setheading(250)
for x in range(30):
    t.forward(1)
    t.left(0.3)
for x in range(160):
    t.forward(1)
    if x < 30:
        t.left(3)
    elif x < 65:
        t.left(0.1)
    else:
        t.left(1)
        
go(-150, -210)
t.setheading(340)
t.fillcolor("white")
t.begin_fill()
step = 1.5
for i in range(2):
    for j in range(60):
        if j < 30:
            step += 0.1
        else:
            step -= 0.1
        t.forward(step)
        t.left(3)
t.end_fill()

t.hideturtle()