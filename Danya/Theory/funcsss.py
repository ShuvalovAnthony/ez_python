from turtle import *

# definition
def square(side_len):
    for i in range(4):
        fd(side_len)
        rt(90)


def goto_(x, y):
    up()
    goto(x, y)
    down()


#call
square(50)
