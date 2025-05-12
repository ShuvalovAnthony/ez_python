from math import dist


f = open("Alexander/27/20206/a.txt")

clasters = [[] for i in range(2)]


for row in f:
    x, y = [float(i) for i in row.split()]

    if y < 1.75*x - 0.35:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])


print([len(i) for i in clasters])


def getCenter(claster: list):
    min_dist = 10**10
    center = None

    for start in claster:
        temp_dist = 0
        for end in claster:
            temp_dist += dist(start, end)

        if temp_dist < min_dist:
            min_dist = temp_dist
            center = start

    return center


px = sum([getCenter(claster)[0] for claster in clasters])/len(clasters)
py = sum([getCenter(claster)[1] for claster in clasters])/len(clasters)

print(int(px*10000), int(py*10000))