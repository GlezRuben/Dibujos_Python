import turtle

t = turtle.Turtle()
t.pensize(3)
t.shape("turtle")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def arco(direc, radio, ang):
    t.seth(direc)
    t.circle(radio, ang)

def linea(direc, longitud):
    t.seth(direc)
    t.forward(longitud)
    
t.fillcolor("LimeGreen")
go(52.29, 104.26)
t.begin_fill()
arco(206.44, -26.96, 26.44)
arco(281.55, -460.92, 33.98)
arco(247.57, 175.21, 38.2)
arco(285.77, 6.92, 180)
arco(103.48, -182.9, 35.42)
arco(68.06, 460.63, 34.33)
t.end_fill()

t.fillcolor("Gold")
go(82.67, 105.89)
ang = 334.09
t.begin_fill()
for i in range(6):
    arco(ang, 242.88, 10.31)
    arco(ang+10.31, 115.26, 41.29)
    arco(ang+51.6, 41, 40.58)
    arco(ang+92.18, 10.04, 84.73)
    arco(ang+176.91, 100.83, 9.63)
    arco(ang+45.45, 60.81, 14.09)
    arco(ang+59.53, 11.72, 83.9)
    arco(ang+143.43, 40.17, 43.69)
    arco(ang+187.12, 108.31, 46.5)
    arco(ang+233.62, 462.65, 4.51)
    ang += 60
t.end_fill()

t.fillcolor("#D2691E")
go(82.24, 130.4)
t.begin_fill()
arco(90, 41.96, 360)
t.end_fill()

t.fillcolor("Green")
go(13.18, -256.53)
t.begin_fill()
arco(68.04, 57.26, 82.02)
arco(150.06, 130.63, 48.22)
arco(281.62, 178.19, 14.31)
arco(295.93, 96.09, 57.53)
arco(353.47, 51.19, 49.84)
t.end_fill()
t.pencolor("DarkGreen")
arco(132.51, 265.41, 28.11)

t.pencolor("Black")
t.fillcolor("Green")
go(25.87, -163.07)
t.begin_fill()
arco(302.06, 58.79, 64.32)
arco(6.38, 160.35, 57.18)
arco(63.56, 331.87, 9.82)
arco(163.06, 230.85, 35.56)
arco(198.62, 94.76, 84.61)
t.end_fill()
t.pencolor("DarkGreen")
arco(45.23, -387.9, 28.66)

t.hideturtle()
turtle.done()