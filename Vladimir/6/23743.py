from turtle import *


screensize(2000, 2000)
tracer(0)
pensize(5)


k = 40


for i in range(2):
    fd(14*k)
    lt(270)
    bk(12*k)
    rt(90)

up()

fd(9*k)
rt(90)
bk(7*k)
lt(90)

down()

for i in range(2):
    fd(13*k)
    rt(90)
    fd(6*k)
    rt(90)



up()

for x in range(-30, 30):
    for y in range(-30, 30):
        goto(x*k, y*k)
        dot(5, "red")


done()