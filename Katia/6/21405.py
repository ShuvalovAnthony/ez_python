from turtle import *


pensize(5)
tracer(0)
screensize(5000, 5000)

k = 35

lt(90)
rt(30)

for i in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, 'red')

done()