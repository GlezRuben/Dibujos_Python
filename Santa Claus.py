import turtle
t = turtle.Turtle()
t.pensize(5)

turtle.bgcolor("black")

def go(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t.pencolor("#B71C1C")
t.fillcolor("#FF0000")

go(-140, 105)

t.begin_fill()
t.goto(-75, 210)
t.goto(0,262.5)
t.goto(75, 210)
t.goto(140, 105)
t.end_fill()

t.pencolor("#F5CBA7")
t.fillcolor("#F5CBA7")

go(-157.5, 87.5)

t.begin_fill()
t.goto(157.5, 87.5)
t.goto(157.5, -35)
t.goto(-157.5, -35)
t.end_fill()

t.pencolor("#1C2833")
t.fillcolor("#1C2833")

go(-85, 18)

t.begin_fill()
t.goto(-85, 35)
t.seth(90)
t.circle(-12, 180)
t.goto(-61, 18)
t.seth(270)
t.circle(-12, 180)
t.end_fill()

go(85, 18)

t.begin_fill()
t.goto(85, 35)
t.seth(90)
t.circle(12, 180)
t.goto(61, 18)
t.seth(270)
t.circle(12, 180)
t.end_fill()

t.pencolor("#BDC3C7")
t.fillcolor("#ECF0F1")

go(0, 0)

t.begin_fill()
t.goto(-52.5, 0)
t.goto(-105, -11.5)
t.goto(-157.5, 35)
t.goto(-175, 0)
t.goto(-157.5, -70)
t.goto(-140, -70)
t.goto(-140, -105)
t.goto(-122.5, -140)
t.goto(-105, -140)
t.goto(-55, -180.5)
t.goto(55, -180.5)
t.goto(105, -140)
t.goto(122.5, -140)
t.goto(140, -105)
t.goto(140, -70)
t.goto(157.5, -70)
t.goto(175, 0)
t.goto(157.5, 35)
t.goto(105, -11.5)
t.goto(52.5, 0)
t.goto(0, 0)
t.end_fill()

go(-105, 70)

t.begin_fill()
t.goto(-105, 58)
t.goto(-35, 75.5)
t.goto(-35, 87.5)
t.goto(-105, 70)
t.end_fill()

go(105, 70)

t.begin_fill()
t.goto(105, 58)
t.goto(35, 75.5)
t.goto(35, 87.5)
t.goto(105, 70)
t.end_fill()

t.pencolor("#BDC3C7")
t.fillcolor("#FDFEFE")

go(0, 280)

t.begin_fill()
t.goto(0, 245)
t.goto(35, 210)
t.goto(70, 210)
t.goto(105, 245)
t.goto(105, 280)
t.goto(70, 315)
t.goto(35, 315)
t.goto(0, 280)
t.end_fill()

go(0, 140)

t.begin_fill()
t.goto(-70, 140)
t.goto(-157.5, 100)
t.goto(-157.5, 35)
t.goto(-105, 70)
t.goto(-35, 87.5)
t.goto(0, 87.5)
t.goto(35, 87.5)
t.goto(105, 70)
t.goto(157.5, 35)
t.goto(157.5, 100)
t.goto(70, 140)
t.goto(0, 140)
t.end_fill()

t.pencolor("#FDFEFE")
t.fillcolor("#FDFEFE")

go(80, 35)

t.begin_fill()
t.circle(5)
t.end_fill()

go(-70, 35)

t.begin_fill()
t.circle(5)
t.end_fill()

t.pencolor("#17202A")

go(-35, -33.5)
t.goto(-17.5, -50)
t.goto(17.5, -50)
t.goto(35, -33.5)

t.pencolor("#F39C12")
t.fillcolor("#F8C471")

go(0, 23)

t.begin_fill()
t.goto(-17.5, 23)
t.goto(-35, 17.5)
t.goto(-35, 0)
t.goto(0, -17.5)
t.goto(35, 0)
t.goto(35, 17.5)
t.goto(17.5, 23)
t.goto(0, 23)
t.end_fill()


