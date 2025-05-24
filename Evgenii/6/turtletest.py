from turtle import *


# tracer(0)
speed(0)
screensize(5000, 5000)

k = 20

dot(5, "red")

up()

down()
lt(90)
for i in range(180):
    fd(k/180)
    lt(1)

lt(90)
fd(k)


done()