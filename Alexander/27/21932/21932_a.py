from math import dist


f = open("Alexander/27/21932/27_A_21932.txt")


clasters = [[] for i in range(2)]


for row in f:
    x, y = [float(i) for i in row.split()]

    if y > 12:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])


print(len(clasters[0]), len(clasters[1]))


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


px = getCenter(clasters[0])[0]
py = getCenter(clasters[1])[1]

print(int(px*10000), int(py*10000))