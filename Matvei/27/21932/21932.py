from math import dist 


f = open("Matvei/27/21932/27_A_21932.txt")


clasters = [[] for i in range(2)]



for row in f:
    x, y = [float(i) for i in row.split()]
    
    if y > 10:
        clasters[0].append([x, y])
    else:
        clasters[1].append([x, y])

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


px = getCenter(clasters[0])[0]
py = getCenter(clasters[1])[1]



print(int(px*10000), int(py*10000))
