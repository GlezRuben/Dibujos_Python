import turtle

t = turtle.Turtle()
t.pensize(7)
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
    
t.fillcolor("LightSeaGreen")
go(127.05, -59.49)
t.begin_fill()
arco(56.91, 203.4, 59.35)
arco(116.26, 127.7, 35.89)
arco(152.16, 176.08, 80.14)
arco(232.3, 161.45, 23.71)
arco(256.02, 234.54, 40.92)
arco(209.66, 84.85, 36.55)
arco(163.02, 23.09, 107.57)
arco(270, 22.84, 63.27)
arco(255.38, 17.83, 159.74)
arco(333.16, 37.74, 26.42)
arco(266.26, 137.63, 24.01)
arco(197.64, 58.35, 17.95)
arco(217.17, 22.71, 90)
arco(324.82, 32.23, 59.65)
arco(285.74, 23.45, 62.69)
arco(348.43, 50.4, 42.29)
arco(325.71, 47.62, 71.33)
arco(37.04, 39.53, 47.57)
arco(95.65, 8.34, 81.08)
arco(51.14, -11.96, 90)
arco(228.19, 24.49, 113.53)
arco(333.53, 30.18, 70.75)
arco(317.48, 38.01, 90)
arco(331.82, 42.56, 46.68)
arco(18.5, 26.25, 136.9)
arco(71.61, 77.7, 36.77)
arco(316.05, 28.65, 42.91)
arco(358.96, 15.44, 83.36)
arco(26.09, 25.94, 126.83)
arco(103.9, 133.51, 36.48)
t.end_fill()

go(-152.07, -173.37)
arco(359.16, 24.17, 140.13)
go(136.17, -181.99)
arco(226.44, -18.51, 199.53)

t.fillcolor("DeepSkyBlue")
go(148.24, -16.72)
t.begin_fill()
arco(305.26, 25.62, 91.22)
arco(36.48, 62.63, 91.15)
arco(127.63, 28.26, 70.7)
arco(198.33, 20.94, 20.28)
arco(275.79, -203.49, 25.41)
t.end_fill()

go(159.81, 41.75)
linea(357.23, 24.61)
go(155.25, 7.66)
arco(15.33, -27.33, 55.59)

go(-169.46, 75.63)
t.begin_fill()
arco(135, 13.01, 83.87)
arco(218.87, 69.96, 79.03)
arco(297.9, 58.22, 31.83)
arco(329.72, 13.96, 83.3)
arco(105.74, -234.54, 26.06)
t.end_fill()

go(-173.23, 36.38)
linea(180, 21.98)
go(-170.98, 1.09)
linea(187.97, 21.86)

go(106.95, 182.66)
t.begin_fill()
arco(94.04, -40.53, 39.74)
arco(54.31, 26.03, 77.68)
arco(131.99, 42.55, 54.05)
arco(88.93, 34.97, 94.3)
arco(183.23, 74.32, 87.98)
arco(10.61, -176.08, 38.45)
arco(332.16, -127.7, 12.36)
t.end_fill()

t.fillcolor("Black")
go(74.71, 218.1)
t.begin_fill()
linea(36.59, 20.42)
arco(121.37, 13.58, 52.19)
arco(206.21, 13.89, 90)
t.end_fill()

go(26.53, 234.84)
t.begin_fill()
linea(49.14, 24.81)
arco(127.41, 17.23, 52.59)
arco(241.76, 33.46, 45.09)
t.end_fill()

t.fillcolor("White")
go(-15.5, 56.49)
t.begin_fill()
arco(90, 59.54, 360)
t.end_fill()

go(135.59, 59.91)
t.begin_fill()
arco(90, 62.66, 360)
t.end_fill()

t.fillcolor("Black")
go(-37.34, 48.85)
t.begin_fill()
arco(90, 12.36, 360)
t.end_fill()

go(63.48, 48.85)
t.begin_fill()
arco(90, 11.9, 360)
t.end_fill()

t.fillcolor("LightPink")
go(141.97, -38.01)
t.begin_fill()
arco(166.07, 584.79, 29.28)
arco(195.35, 14.07, 157.53)
arco(352.88, 1147.19, 14.62)
arco(7.5, 15.4, 158.57)
t.end_fill()

go(-143.38, -58.54)
arco(19.61, -118.32, 39.76)
arco(339.85, 159.09, 38.44)
arco(18.29, -171.55, 31.45)

go(-99.03, -110.71)
arco(287.26, 18.08, 131.29)
go(-29.6, -112.24)
arco(299.56, 21.3, 112.67)
go(40.25, -112.24)
arco(289.75, 16.93, 134.03)
go(-68.06, -160.7)
arco(294.63, 21.22, 114.49)
go(8.64, -164.3)
arco(304.94, 26.12, 90)

t.hideturtle()
turtle.done()