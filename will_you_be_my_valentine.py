import turtle

t = turtle.Turtle()
t.pensize(5)
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
    
t.fillcolor("white")
go(-186.78, -8.13) 
t.begin_fill()
linea(270, 267.92)
linea(0, 467.72)
linea(90, 267.92)
linea(180, 467.72)
t.end_fill()
t.begin_fill()
linea(39.37, 268.77)
arco(39.37, -41.11, 78.73)
linea(320.63, 268.77)
linea(180, 467.72)
t.end_fill()

t.fillcolor("Silver")
t.begin_fill()
linea(337.55, 221.41)
arco(337.55, 76.55, 44.91)
linea(22.45, 221.41)
linea(180, 467.72)
t.end_fill()

t.fillcolor("Black")
go(-14.61, -153.89) 
t.begin_fill()
arco(90, 64.84, 360)
t.end_fill()
go(239.54, -155.77) 
t.begin_fill()
arco(90, 63.91, 360)
t.end_fill()

t.pensize(1)
t.fillcolor("Pink")
t.pencolor("Pink")
go(-108.02, -232.42) 
t.begin_fill()
arco(90, 31.52, 360)
t.end_fill()
go(271.49, -229.91) 
t.begin_fill()
arco(90, 30.95, 360)
t.end_fill()

t.fillcolor("White")
t.pencolor("White")
go(-66.09, -136.21) 
t.begin_fill()
arco(90, 26.94, 360)
t.end_fill()
go(188.23, -139.16) 
t.begin_fill()
arco(90, 26.95, 360)
t.end_fill()
go(-48.14, -182.03) 
t.begin_fill()
arco(90, 12.77, 360)
t.end_fill()
go(205.76, -184.78) 
t.begin_fill()
arco(90, 12.41, 360)
t.end_fill()

t.pensize(8)
t.pencolor("Black")
go(80.05, -181.18)
arco(219.25, -71.6, 65.45)
go(81.89, -210.84)
arco(232.2, -24.96, 70.62)

t.pensize(5)
t.fillcolor("Wheat")
go(-114.49, -38) 
t.begin_fill()
linea(337.55, 143.19)
arco(337.55, 76.55, 44.91)
linea(22.45, 138.66)
linea(90, 129.48)
linea(180, 318.96)
linea(270, 129.48)
t.end_fill()

go(130, 30)
t.write("Will you be", False,
        "right", ("arial", 25))
go(70, -10)
t.write("my", False,
        "right", ("arial", 25))
t.color("red")
go(150, -60)
t.write("valentine?", False,
        "right", ("arial", 30, "bold"))

t.fillcolor("Red")
t.pencolor("Black")
go(-152.96, 83.47) 
t.begin_fill()
arco(69.88, -286.51, 5.74)
arco(64.14, 149.59, 18.81)
arco(82.94, 50.57, 45.28)
arco(128.23, 39.43, 148.4)
arco(148, 45.33, 28.96)
arco(176.96, 34.04, 97.51)
arco(274.46, 55.53, 76.12)
arco(350.58, 237.37, 16.14)
t.end_fill()

go(158.67, 146.56) 
t.begin_fill()
arco(16.32, -487.58, 5.43)
arco(10.9, 76.98, 23.98)
arco(34.88, 32.51, 73.83)
arco(108.71, 30.29, 116.87)
arco(78.83, 22.46, 57.98)
arco(136.81, 30.96, 100.17)
arco(236.99, 45.87, 39.56)
arco(276.55, 105.7, 34.01)
t.end_fill()

t.pensize(9)
t.pencolor("White")
go(177.46, 215.19)
arco(85.42, 24.28, 60.67)
go(-153.02, 166.3)
arco(95.23, 30.25, 73.55)

t.hideturtle()
turtle.done()