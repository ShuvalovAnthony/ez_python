from turtle import *



"""
forward() fd() на Х пикселей
backward() bk()

left() lt() поворт на Х градусов
right() rt() 

up()
down()

tracer(0)
speed(0)
screensize(5000, 5000)

goto(x, y)
dot(SIZE, COLOR)

"""
tracer(0)
screensize(5000, 5000)
pensize(5)

lt(90)

k = 30


rt(90)

for _ in range(7):
    rt(45)
    fd(11*k)
    rt(45)


up()

for x in range(-10, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5, "red")





done()

