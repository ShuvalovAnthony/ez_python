from turtle import *


screensize(5000, 5000)
tracer(0)

pensize(5)

k = 15

rt(90)



for i in range(2):
    fd(k*28)
    rt(90)
    fd(k*18)
    rt(90)

up()

fd(k*14)
rt(90)
fd(k*10)
lt(90)

down()

for i in range(2):
    fd(k*30)
    rt(90)
    fd(k*7)
    rt(90)


up()


for x in range(-40, 30):
    for y in range(-60, 30):
        goto(k*x, k*y)
        dot(5, "red")


done()