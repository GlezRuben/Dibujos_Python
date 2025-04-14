import turtle

t = turtle.Turtle()
turtle.bgcolor("black")
cafe1 = "#6D4C41"
cafe2 = "#5D4037"
cafe3 = "#4E342E"
cafe4 = "#3E2723"
verde1 = "#00FF00"
verde2 = "#229954"
verde3 = "#006600"
blanco = "white"
amarillo1 = "#FFEB3B"
amarillo2 = "#FFCA28"
amarillo3 = "#FFA000"
rojo1 = "#FF0000"
rojo2 = "#E53935"
rojo3 = "#B71C1C"

def cuadrado(color):
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    t.seth(0)
    t.forward(30)
    t.seth(90)
    t.forward(30)
    t.seth(180)
    t.forward(30)
    t.seth(270)
    t.forward(30)
    t.end_fill()
    
def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def maceta(x, y):
    go(x, y)
    cuadrado(cafe1) 
    go(x+30, y)
    cuadrado(cafe2) 
    go(x+60, y)
    cuadrado(cafe3)
    go(x+90, y)
    cuadrado(cafe3)
    go(x+120, y)
    cuadrado(cafe3)
    go(x+150, y)
    cuadrado(cafe4)
    
    go(x, y+30)
    cuadrado(cafe1) 
    go(x+30, y+30)
    cuadrado(cafe1) 
    go(x+60, y+30)
    cuadrado(cafe2)
    go(x+90, y+30)
    cuadrado(cafe1)
    go(x+120, y+30)
    cuadrado(cafe3)
    go(x+150, y+30)
    cuadrado(cafe4)
    
    go(x, y+60)
    cuadrado(cafe1) 
    go(x+30, y+60)
    cuadrado(cafe1) 
    go(x+60, y+60)
    cuadrado(cafe1)
    go(x+90, y+60)
    cuadrado(cafe2)
    go(x+120, y+60)
    cuadrado(cafe3)
    go(x+150, y+60)
    cuadrado(cafe4)
    
    go(x, y+90)
    cuadrado(cafe1) 
    go(x+30, y+90)
    cuadrado(cafe1) 
    go(x+60, y+90)
    cuadrado(cafe2)
    go(x+90, y+90)
    cuadrado(cafe3)
    go(x+120, y+90)
    cuadrado(cafe2)
    go(x+150, y+90)
    cuadrado(cafe4)
    
    go(x, y+120)
    cuadrado(cafe1) 
    go(x+30, y+120)
    cuadrado(cafe2) 
    go(x+60, y+120)
    cuadrado(cafe1)
    go(x+90, y+120)
    cuadrado(cafe1)
    go(x+120, y+120)
    cuadrado(cafe3)
    go(x+150, y+120)
    cuadrado(cafe2)
    
    go(x, y+150)
    cuadrado(cafe1) 
    go(x+30, y+150)
    cuadrado(cafe1) 
    go(x+60, y+150)
    cuadrado(cafe1)
    go(x+90, y+150)
    cuadrado(cafe2)
    go(x+120, y+150)
    cuadrado(cafe1)
    go(x+150, y+150)
    cuadrado(cafe2)
    
maceta(-210, -300)

go(-150, -120)
cuadrado(verde1)
go(-150, -90)
cuadrado(verde1)
go(-120, -90)
cuadrado(verde2)
go(-150, -60)
cuadrado(verde1)
go(-120, -60)
cuadrado(verde2)
go(-180, -30)
cuadrado(verde2)
go(-150, -30)
cuadrado(verde1)
go(-120, -30)
cuadrado(verde2)
go(-90, -30)
cuadrado(verde2)
go(-210, 0)
cuadrado(verde2)
go(-180, 0)
cuadrado(verde1)
go(-150, 0)
cuadrado(verde1)
go(-150, 30)
cuadrado(verde1)
go(-150, 60)
cuadrado(verde1)
go(-120, 60)
cuadrado(verde2)

go(-180, 90)
cuadrado(blanco)
go(-150, 90)
cuadrado(blanco)
go(-120, 90)
cuadrado(blanco)
go(-210, 120)
cuadrado(blanco)
go(-180, 120)
cuadrado(blanco)
go(-150, 120)
cuadrado(blanco)
go(-120, 120)
cuadrado(blanco)
go(-90, 120)
cuadrado(blanco)
go(-240, 150)
cuadrado(blanco)
go(-210, 150)
cuadrado(blanco)
go(-180, 150)
cuadrado(amarillo2)
go(-150, 150)
cuadrado(amarillo1)
go(-120, 150)
cuadrado(amarillo3)
go(-90, 150)
cuadrado(blanco)
go(-60, 150)
cuadrado(blanco)
go(-240, 180)
cuadrado(blanco)
go(-210, 180)
cuadrado(blanco)
go(-180, 180)
cuadrado(amarillo1)
go(-150, 180)
cuadrado(amarillo1)
go(-120, 180)
cuadrado(amarillo2)
go(-90, 180)
cuadrado(blanco)
go(-60, 180)
cuadrado(blanco)
go(-240, 210)
cuadrado(blanco)
go(-210, 210)
cuadrado(blanco)
go(-180, 210)
cuadrado(amarillo2)
go(-150, 210)
cuadrado(amarillo1)
go(-120, 210)
cuadrado(amarillo1)
go(-90, 210)
cuadrado(blanco)
go(-60, 210)
cuadrado(blanco)
go(-210, 240)
cuadrado(blanco)
go(-180, 240)
cuadrado(blanco)
go(-150, 240)
cuadrado(blanco)
go(-120, 240)
cuadrado(blanco)
go(-90, 240)
cuadrado(blanco)
go(-180, 270)
cuadrado(blanco)
go(-150, 270)
cuadrado(blanco)
go(-120, 270)
cuadrado(blanco)

maceta(90, -300)

go(150, -120)
cuadrado(verde3)
go(180, -120)
cuadrado(verde3)
go(90, -90)
cuadrado(verde3)
go(120, -90)
cuadrado(verde3)
go(150, -90)
cuadrado(verde3)
go(180, -90)
cuadrado(verde3)
go(60, -60)
cuadrado(verde3)
go(90, -60)
cuadrado(verde3)
go(150, -60)
cuadrado(verde1)
go(180, -60)
cuadrado(verde3)
go(210, -60)
cuadrado(verde3)
go(240, -60)
cuadrado(verde3)
go(150, -30)
cuadrado(verde1)
go(150, 0)
cuadrado(verde1)
go(150, 30)
cuadrado(verde1)
go(90, 60)
cuadrado(rojo1)
go(120, 60)
cuadrado(verde3)
go(150, 60)
cuadrado(verde3)
go(60, 90)
cuadrado(rojo1)
go(90, 90)
cuadrado(rojo1)
go(120, 90)
cuadrado(rojo1)
go(150, 90)
cuadrado(rojo1)
go(180, 90)
cuadrado(rojo3)
go(60, 120)
cuadrado(rojo1)
go(90, 120)
cuadrado(rojo2)
go(120, 120)
cuadrado(rojo3)
go(150, 120)
cuadrado(rojo2)
go(180, 120)
cuadrado(rojo1)
go(210, 120)
cuadrado(rojo3)
go(90, 150)
cuadrado(rojo1)
go(120, 150)
cuadrado(rojo2)
go(150, 150)
cuadrado(rojo3)
go(180, 150)
cuadrado(rojo1)
go(210, 150)
cuadrado(rojo2)
go(150, 180)
cuadrado(rojo3)
go(180, 180)
cuadrado(rojo3)

t.hideturtle()
turtle.done()
