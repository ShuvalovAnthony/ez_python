from turtle import *


tracer(0)
# speed(0)
screensize(5000, 5000)

k = 100

# forward() fd() px
# backward() bk() px
# left() lt() grad
# right() rt() grad
# up()
# down()
# speed()
# tracer()
# circle()
# dot()
# goto()

lt(90)

pensize(10)

rt(30)
for _ in range(3):
    rt(150)
    fd(6*k)
    rt(30)
    fd(12*k)


# up()

# for x in range(-10, 10):
#     for y in range(-20, 20):
#         goto(x*k, y*k)
#         dot(10, "red")



input()