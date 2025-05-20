from math import*
f=open('oppu.txt')
clasters=[[] for _ in range (2)]
for row in f:
    x, y=[float(i.replace(',', '.')) for i in row.split()]
    if y > 12:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])
print([len(i) for i in clasters])


def getCenter(claster: list):
    center = None
    min_summa = 10 ** 10
    for start in claster:
        temp_summa = 0
        for end in claster:
            temp_summa += dist(start, end)
        if (temp_summa <
                min_summa):
            min_summa = temp_summa
            center = start
    return center


centeres = [getCenter(claster) for claster in clasters]
px = sum(center[0] for center in centeres) / len(centeres)
py = sum(center[1] for center in centeres) / len(centeres)

print(int(px * 10000), int(py * 10000))