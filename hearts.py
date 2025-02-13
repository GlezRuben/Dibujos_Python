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
    
x = [78.71, -28.25, -96.17, -31.18, 76.9]
y = [55.28, 91.94, 1.53, -90.99, -57.77]
angle = [326, 38, 110, 182, 254]
t.fillcolor("Pink")
for i in range(5):
    go(x[i], y[i])
    t.begin_fill()
    linea(angle[i], 92.97)
    arco(angle[i], 98.45, 41.46)
    arco(angle[i]+41.45, 65.99, 58.91)
    arco(angle[i]+100.36, 59.51, 98.77)
    arco(angle[i]+85.51, 59.51, 98.77)
    arco(angle[i]-175.13, 65.99, 58.91)
    arco(angle[i]-116.94, 98.45, 41.46)
    linea(angle[i]-75.24, 92.97)
    t.end_fill()
    
x = [-61.89, -188.06, -54.33, 154.48, 149.81]
y = [177.63, -3.97, -180.09, -107.32, 113.75]
angle = [29.6, 101.6, 173.6, 245.6, 317.6]
t.fillcolor("DeepPink")
for i in range(5):
    go(x[i], y[i])
    t.begin_fill()
    arco(angle[i], 263.13, 9.56)
    arco(angle[i]+9.57, 24.6, 131.78)
    arco(angle[i]+141.34, 22.27, 54.38)
    arco(angle[i]+95.49, 22.27, 54.38)
    arco(angle[i]+149.86, 24.6, 131.78)
    arco(angle[i]+281.64, 263.13, 9.56)
    t.end_fill()
    
x = [59.74, -57.28, -95.14, -1.51, 94.2]
y = [79.64, 81.42, -29.32, -99.54, -32.2]
angle = [31.85, 103.85, 175.85, 247.85, 319.85]
t.fillcolor("Red")
for i in range(5):
    go(x[i], y[i])
    t.begin_fill()
    arco(angle[i], 251.38, 19.33)
    arco(angle[i]+19.33, 47.45, 38.59)
    arco(angle[i]+57.92, 38.43, 156.78)
    arco(angle[i]+81.6, 38.43, 156.78)
    arco(angle[i]+238.38, 47.45, 38.59)
    arco(angle[i]+276.97, 251.38, 19.33)
    t.end_fill()
    
x = [127.9, -169.63, -232.74, 25.79, 248.68]
y = [219.92, 189.6, -102.74, -253.1, -53.68]
angle = [348.54, 72, 144, 216, 288]
t.fillcolor("MediumVioletRed")
for i in range(5):
    go(x[i], y[i])
    t.begin_fill()
    arco(angle[i], 40.4, 47.5)
    arco(angle[i]+47.5, 13.4, 161.89)
    arco(angle[i]-252.41, 13.4, 161.89)
    arco(angle[i]-90.52, 40.4, 47.5)
    t.end_fill()

t.hideturtle()
turtle.done()