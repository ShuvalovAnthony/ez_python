from turtle import *

screensize(5000, 5000)
scale = 25
tracer(0)

x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x1, x2 = min(x1, x2), max(x1, x2)
y1, y2 = min(y1, y2), max(y1, y2)

up()

for x in range(x1 - 3, x2 + 3):
    for y in range(y1 - 3, y2 + 3):
        goto(x*scale, y*scale)
        dot(5, "green")

goto(x1*scale, y1*scale)

down()

goto(x2*scale, y2*scale)

up()



counter = 2
if y2 == y1:
    print(counter + (x2 - x1 - 1))
elif x2 == x1:
    print(counter + (y2 - y1 - 1))
else:
    k = (y2 - y1)/(x2 - x1)
    for x in range(x1 + 1, x2):
        for y in range(y1 + 1, y2):
            if (y - y1)/(x - x1) == k:
                goto(x*scale, y*scale)
                dot(5, "red")
                counter += 1
            else:
                goto(x*scale, y*scale)
                dot(5, "green")
    print(counter)



done()