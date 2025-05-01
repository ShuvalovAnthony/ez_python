from turtle import *


# forward() fd() - вперед x пикселей
# backward() bk() - назад
# left() lt() поворот на градус
# right() rt()
# up() down() поднять/опустить перо
# speed(0)
# screensize() - позволяет сделать прокрутку
# goto() - идти к координате
# dot() точка

tracer(0)
screensize(5000, 5000)

k = 50

left(90)

pensize(5)
right(90)

for _ in range(7):
    right(45)
    fd(11*k)
    right(45)


up()

for x in range(-10, 20):
    for y in range(-20, 20):
        goto(x*k, y*k)
        dot(5, "red")



input()



