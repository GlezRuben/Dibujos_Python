import turtle

t = turtle.Turtle()
t.pensize(4)
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

t.fillcolor("#f8fcfe")
go(141.16, -167.06)
t.begin_fill()
arco(106.99, 171.94, 136.73)
arco(243.72, 85.76, 90)
arco(334.16, 275.47, 51.67)
arco(25.84, 74.88, 81.15)
t.end_fill()

go(136.40, 63.04)
t.begin_fill()
arco(117.14, 175.35, 136.8)
arco(253.94, 79.28, 90.96)
arco(344.9, 410.23, 29.72)
arco(14.63, 91.88, 102.51)
t.end_fill()

t.fillcolor("red")
go(100.23, -58.65)
t.begin_fill()
arco(209.75, -91.88, 15.13)
arco(194.63, -410.23, 29.72)
arco(164.9, -79.28, 23.39)
arco(238.15, 39.84, 90)
arco(335.35, 298.14, 49.3)
arco(28.09, 27.57, 123.83)
t.end_fill()

go(66.38, -120.41)
t.begin_fill()
arco(197.67, -298.14, 9.06)
arco(290.94, -176.02, 30.75)
arco(260.19, 20.55, 65.56)
arco(344.96, 42.64, 57.5)
arco(42.46, 50.75, 56.51)
arco(98.96, 167.2, 25.69)
t.end_fill()

t.fillcolor("black")
go(-13.53, -169.16)
t.begin_fill()
t.circle(34.79/2)
t.end_fill()
go(-13.53, -226.31)
t.begin_fill()
t.circle(34.79/2)
t.end_fill()

t.pencolor("LightPink")
t.fillcolor("LightPink")
go(95.59, -12.09)
t.begin_fill()
t.circle(45.84/2)
t.end_fill()
go(-100.19, -12.09)
t.begin_fill()
t.circle(45.84/2)
t.end_fill()

t.pencolor("black")
t.fillcolor("black")
go(-6.39, -5.39)
arco(256.11, -20.71, 152.23)
go(76.32, 13.81)
t.begin_fill()
t.circle(68.6/2)
t.end_fill()
go(-59.8, 13.81)
t.begin_fill()
t.circle(67.22/2)
t.end_fill()

t.pencolor("white")
t.fillcolor("white")
go(-69.38, 20.21)
t.begin_fill()
t.circle(29.1/2)
t.end_fill()
go(-99.05, -2.74)
t.begin_fill()
t.circle(12.87/2)
t.end_fill()
go(47.87, 20.21)
t.begin_fill()
t.circle(27.98/2)
t.end_fill()
go(60.85, -2.74)
t.begin_fill()
t.circle(11.89/2)
t.end_fill()

t.pencolor("black")
t.fillcolor("white")
go(227.43, 159.97)
t.begin_fill()
arco(6.7, 33.11, 138.77)
arco(121.09, 43.83, 270)
t.end_fill()


t.fillcolor("red")
go(136.4, 63.04)
t.begin_fill()
arco(47.24, 93.65, 75.03)
arco(18.07, 76.02, 33.3)
arco(133.71, 250.71, 74.91)
arco(208.62, 165, 87.21)
arco(73.94, -175.35, 136.8)
t.end_fill()
go(146.83, 176.63)
arco(112.27, 134.48, 22.7)

t.fillcolor("white")
go(146.52, 21.12)
t.begin_fill()
arco(22.31, 58.49, 128.41)
arco(123.02, 133.25, 74.99)
arco(163.19, 165.39, 64.54)
arco(194.47, 68.73, 131.75)
arco(85.99, -92.66, 50.18)
arco(8.45, 172.89, 31.14)
arco(354.18, 115.31, 30.8)
arco(8.56, -95.7, 29.89)
arco(334.95, 109.69, 31.57)
arco(319.39, -134.57, 44.22)
t.end_fill()

t.hideturtle()
turtle.done()