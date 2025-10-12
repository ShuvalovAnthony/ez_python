from turtle import *


screensize(5000, 5000)
tracer(0)
pensize(5)

k = 15

lt(90)


for i in range(9):
    fd(27*k)
    rt(90)
    fd(30*k)
    rt(90)

up()

fd(3*k)
rt(90)
fd(6*k)
lt(90)

down()

for i in range(9):
    fd(77*k)
    rt(90)
    fd(66*k)
    rt(90)


up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")

done()
