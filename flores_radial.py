import turtle as t
import colorsys

t.bgcolor("black")
t.tracer(968)

def draw():
    h = 0
    n = 20
    t.up()
    t.goto(0, 0)
    t.down()
    t.pensize()
    for i in range(73):
        c = colorsys.hsv_to_rgb(h,1,1)
        h += 1/n
        t.color(c)
        t.fd(10)
        t.circle(i, 4.5)
        for j in range(550):
            t.lt(971)
            t.circle(i*.1, j , steps=2)
            t.circle(i,2)
draw()
t.done()