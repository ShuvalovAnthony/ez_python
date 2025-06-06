from turtle import *


"""
forward() fd() вперед/назад на Х пикселей!!!
backward() bk() всегда умножаем на K

left() lt() нале напра во на Х градусов
right() rt() 

up() down() - поднять/опустить перо

goto(x*k, y*k)
dot(5, "red")


"""

# решение задачи
# 1) настройка холста
# 2) алгоритм из задачи
# 3) точки (коорд сетка)


tracer(0)
screensize(5000, 5000)
pensize(10)

lt(90)

k = 45

rt(90)

for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)


up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(10, "red")




done()