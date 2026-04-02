from turtle import *
tracer(0)
screensize(2500, 2500)
pensize(20)
k = 40
for i in range(3):
    fd(20*k)
    rt(120)
up()
fd(5 * k)
rt(60)
fd(8 * k)
lt(60)
down()
for i in range(4):
    fd(30*k)
    rt(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(20, "red")
done()