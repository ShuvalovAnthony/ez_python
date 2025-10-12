from turtle import *

"""
forward()/fd() - вперед назад на Х ПИКСЕЛЕЙ!!!!!
backward()/bk()

left() lt() налево / направо на Х ГРАДУСОВ!!!!!!
right() rt()

up()/down() поднять/опустить перо

goto(x, y)
dot(5, "red") - точка


pensize()
pencolor()
screensize(5000, 5000)
tracer(0) - мгновенная отрисовка 

done() - в конце!!!!
"""

tracer(0)
pensize(5)
screensize(5000, 5000)

# ЭТО УСЛОВИЕ ЗАДАЧИ ⬇️⬇️⬇️
k = 30 # коэффициент масштабирования

lt(90)

rt(90)

for i in range(7):
    rt(45)
    fd(11*k)
    rt(45)



# Рисуем сетку ⬇️⬇️⬇️
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(5, "red")


done()