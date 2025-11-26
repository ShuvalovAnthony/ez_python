from turtle import *


# forward() / fd() вперед/назад на Х ПИКСЕЛЕЙ
# backward() / bk()

# left() / lt() налево/направо на Х ГРАДУСОВ
# right() / rt()

# up()/down() поднять/опустить перо

# dot() - точка
# goto() - идти к координате

screensize(5000, 5000)
pensize(10)
tracer(0)

k = 35
# задание
for i in range(2):
    fd(13*k)
    rt(30)
    fd(18*k)
    rt(90)

up()
fd(5*k)
rt(90)
fd(9*k)
lt(90)

down()

for i in range(2):
    fd(11*k)
    rt(90)
    fd(7*k)
    rt(90)

# сетка

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(10, "red")



done()