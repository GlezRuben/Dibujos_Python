import turtle
t = turtle.Turtle()
t.pensize(5)

turtle.bgcolor("black")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.pencolor("#663333")
t.fillcolor("#663333")

go(-40, -210)

t.begin_fill()
t.seth(270)
t.goto(-40,-270)
t.circle(10,90)
t.goto(30,-280)
t.circle(10,90)
t.goto(40,-210)
t.end_fill()

t.pencolor("#1B5E20")
t.fillcolor("#008000")

go(0, 245)

t.begin_fill()
t.goto(-105, 122.5)
t.goto(-70, 122.5)
t.goto(-140, 35)
t.goto(-105, 35)
t.goto(-210, -87.5)
t.goto(-175, -87.5)
t.goto(-245, -210)
t.goto(-105, -192.5)
t.goto(-140, -227.5)
t.goto(-0, -210)
t.goto(140, -227.5)
t.goto(105, -192.5)
t.goto(245, -210)
t.goto(175, -87.5)
t.goto(210, -87.5)
t.goto(105, 35)
t.goto(140, 35)
t.goto(70, 122.5)
t.goto(105, 122.5)
t.goto(0, 245)
t.end_fill()

t.pencolor("#F9A825")
t.fillcolor("#FFEE58")

go(0, 315)

t.begin_fill()
t.goto(-15, 280)
t.goto(-50, 280)
t.goto(-20, 258)
t.goto(-35, 225)
t.goto(0, 238)
t.goto(35, 225)
t.goto(20, 258)
t.goto(50, 280)
t.goto(15, 280)
t.goto(0, 315)
t.end_fill()

go(70, 175)

t.begin_fill()
t.goto(-98, 139)
t.goto(-77, 162)
t.goto(52.5, 192.5)
t.goto(70, 175)
t.end_fill()

go(105, 87.5)

t.begin_fill()
t.goto(-140, 38)
t.goto(-122.5, 59)
t.goto(87.5, 105)
t.goto(105, 87.5)
t.end_fill()

go(140, 0)

t.begin_fill()
t.goto(-194, -70)
t.goto(-175, -48)
t.goto(122.5, 17.5)
t.goto(140, 0)
t.end_fill()

go(192.5, -105)

t.begin_fill()
t.goto(-235, -180)
t.goto(-215, -157.5)
t.goto(175, -87.5)
t.goto(192.5, -105)
t.end_fill()

t.pencolor("#B71C1C")
t.fillcolor("#FF0000")

go(0, 192.5)

t.begin_fill()
t.circle(12)
go(0, 17.5)
t.circle(12)
t.end_fill()

go(-122.5, -122.5)

t.begin_fill()
t.circle(12)
go(122.5, -175)
t.circle(12)
t.end_fill()

t.pencolor("#880E4F")
t.fillcolor("#E91E63")

go(-35, 105)

t.begin_fill()
t.circle(12)
go(70, 38)
t.circle(12)
t.end_fill()

go(-17.5, -87.5)

t.begin_fill()
t.circle(12)
t.end_fill()

t.pencolor("#1A237E")
t.fillcolor("#0000FF")

go(52.5, 122.5)

t.begin_fill()
t.circle(12)
go(-87.5, -17.5)
t.circle(12)
t.end_fill()

go(-52.5, -192.5)

t.begin_fill()
t.circle(12)
t.end_fill()

go(87.5, -70)

t.begin_fill()
t.circle(12)
t.end_fill()

t.hideturtle()