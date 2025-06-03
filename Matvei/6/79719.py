from turtle import *


# 1) настраиваем доску

screensize(5000, 5000)
tracer(0)
pensize(10)
lt(90)

k = 30

"""
forward() fd() - вперед на Х пксл
backward() bk()

left() lt() налево на Х град
right() rt()

up() down() поднять/опустить перо
goto(5*k, 5*k) перейти к точке X,Y
dot(5, "red") поставить точку 

"""

rt(90)

for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)

up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(10, 'red')




done() # либо input()