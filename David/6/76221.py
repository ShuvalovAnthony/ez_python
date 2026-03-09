from turtle import *

screensize(5000, 5000)
tracer(0)
pensize(11)

k = 25

for i in range(4):
    fd(14*k)
    rt(90)

for i in range(5):
    fd(5*k)
    rt(45)


up()


for x in range(-30, 30):
    for y in range(-30 ,30):
        goto(x*k, y*k)
        dot(11, "red")

done()