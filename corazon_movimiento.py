from turtle import *
bgcolor(0, 0, 0), setup(500, 500)
hideturtle(), tracer(0), penup()
from math import sin, cos
from time import perf_counter
def _loop():
    update(), clear()
    t = perf_counter()
    X, Y = 0, 0
    for i in range(1, 400):
        if cos(i)<0: continue
        X = sin(2-0.2*sin(3*t+X/20)**8+i/2)
        X = 200*cos(i)*X
        Y = 200*sin(i + 0.7**cos(i)**0.05)-30
        goto(X, Y)
        dot(20, (1, 0, sin(i+t+sin(t/2))/2+.5))
    ontimer(_loop, 10)
_loop()
mainloop()