from math import dist


f = open("Polina/27/21425/27b.txt")


claster_1 = []
claster_2 = []
claster_3 = []


for row in f:
    x, y = [float(i) for i in row.split()]
    if (x < 0):
        claster_1.append([x, y])
    elif (y > 0):
        claster_2.append([x, y])
    else:
        claster_3.append([x, y])


def getClasterCenter(claster: list):
    center = None
    min_summa_rasst = 10**6

    for start_dot in claster:
        temp_summa_rasst = 0

        for finish_dot in claster:
            temp_summa_rasst += dist(start_dot, finish_dot)

        if temp_summa_rasst < min_summa_rasst:
            min_summa_rasst = temp_summa_rasst
            center = start_dot

    return center


clasters = [claster_1, claster_2, claster_3]
clasters_centers = [getClasterCenter(i) for i in clasters]

px = sum([center[0] for center in clasters_centers])/len(clasters_centers)
py = sum([center[1] for center in clasters_centers])/len(clasters_centers)

print(int(px*10000), int(py*10000))




# from math import dist


# f = open("Polina/27/21425/27a.txt")


# claster_1 = []
# claster_2 = []


# for row in f:
#     x, y = [float(i) for i in row.split()]
#     if (4 <= x <= 15) and (-18 <= y <= -7):
#         claster_1.append([x, y])
#     else:
#         claster_2.append([x, y])


# def getClasterCenter(claster: list):
#     center = None
#     min_summa_rasst = 10**6

#     for start_dot in claster:
#         temp_summa_rasst = 0

#         for finish_dot in claster:
#             temp_summa_rasst += dist(start_dot, finish_dot)

#         if temp_summa_rasst < min_summa_rasst:
#             min_summa_rasst = temp_summa_rasst
#             center = start_dot

#     return center


# clasters = [claster_1, claster_2]
# clasters_centers = [getClasterCenter(i) for i in clasters]

# px = sum([center[0] for center in clasters_centers])/len(clasters_centers)
# py = sum([center[1] for center in clasters_centers])/len(clasters_centers)

# print(int(px*10000), int(py*10000))