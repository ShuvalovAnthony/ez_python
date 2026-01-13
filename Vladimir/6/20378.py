from turtle import *

screensize(5000, 5000)
tracer(0)
k = 50
pensize(5)

for _ in range(28):
    fd(49*k)
    rt(18)
    fd(69*k)
    rt(162)

up()

for x in range(-5, 150):
    for y in range(-60, 10):
        goto(x*k, y*k)

        if (-0.3249197*x*k < y*k) and (-0.3249197*x*k + 15.921 > y*k): # NE DODELANO
            dot(5, 'blue')
        else:
            dot(5, 'red')
        write(x, y)

done()