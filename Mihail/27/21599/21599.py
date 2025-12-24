f = open("Mihail/27/21599/27_B_21599.txt")


claster_1 = []
claster_2 = []
claster_3 = []
claster_4 = []
claster_5 = []
claster_6 = []


for row in f:
    x, y = [float(i) for i in row.replace(",", ".").split()]

    if y < -5:
        claster_1.append([x, y])
    elif y <= 2/3*x:
        claster_2.append([x, y])