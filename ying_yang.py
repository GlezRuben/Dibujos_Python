from turtle import *

goto(0, -205)
width(10)
circle(200, 360)
width(2)
home()
begin_fill()
seth(180)
circle(100, 180)
home()
circle(100, 180)
seth(0)

for i in range(181):
    fd(3.5)
    rt(1)
    
end_fill()
pu()
goto(-10, 100)
dot(50)
goto(10, -100)
color('white')
dot(50)

done()