from turtle import *

screensize(5000,5000)
tracer(0)

pensize(3)

k=10

lt(90)

for i in range(4):
    fd(50*k)
    lt(90)

up()

fd(50*k)
lt(135)

down()

for i in range(2):
    fd(102*k)
    lt(120)
    fd(182*k)
    lt(60)

up()

for x in range(-100,100):
    for y in range(-100,100):
        goto(x*k,y*k)
        dot(3,'red')

done()