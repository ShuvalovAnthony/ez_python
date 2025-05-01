from turtle import *


tracer(9)
screensize(5000, 5000)
pensize(5)
k = 50

left(90)


right(270)
for _ in range(2):
    fd(8*k)
    right(120)

right(120)

for _ in range(2):
    right(120)
    fd(3*k)
    right(240)

right(240)

for _ in range(2):
    fd(14*k)
    right(120)




up()

for x in range(-15, 15):
    for y in range(-15, 15):
        goto(x*k, y*k)
        dot(5, "red")


done()