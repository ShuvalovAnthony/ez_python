from math import dist


f = open("Matvei/27/19715/b.txt")

clasters = [[] for _ in range(4)]


for row in f:
    x, y = [float(i) for i in row.split()]

    if x > 3 and y < -10:
        clasters[0].append([x, y])
    elif x > 2 and y > 2:
        clasters[1].append([x, y])
    elif x < -3 and y < -30:
        clasters[2].append([x, y])
    elif (x + 54)**2 + (y - 33)**2 <= 43**2:
        clasters[3].append([x, y])


print([len(i) for i in clasters])


def getCenter(claster: list):
    min_summa_rasst = 10**10
    center = None

    for start in claster:
        temp_summa_rasst = 0

        for end in claster:
            temp_summa_rasst += dist(start, end)

        if temp_summa_rasst < min_summa_rasst:
            min_summa_rasst = temp_summa_rasst
            center = start

    return center


centeres = [getCenter(claster) for claster in clasters]


px = sum(center[0] for center in centeres)/len(centeres)
py = sum(center[1] for center in centeres)/len(centeres)

print(int(abs(px*10000)), int(abs(py*10000)))