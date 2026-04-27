# from math import dist

# f = open("Danya/27/27780/27A_27780.txt")

# claster_1 = []
# claster_2 = []

# for row in f:
#     x, y = [float(i) for i in row.replace(",", ".").split()]

#     if y > 15:
#         claster_1.append([x, y])
#     else:
#         claster_2.append([x, y])

# # 344 301
# # print(len(claster_1), len(claster_2))


# def getCenter(claster: list):
#     center = None
#     min_sum_rasst = 10**6

#     for start in claster:
#         temp_sum_rasst = 0

#         for stop in claster:
#             temp_sum_rasst += dist(start, stop)

#         if temp_sum_rasst < min_sum_rasst:
#             min_sum_rasst = temp_sum_rasst
#             center = start

#     return center


# a1 = 344

# center_1 = getCenter(claster_1)
# center_2 = getCenter(claster_2)

# a2 = dist(center_1, [1, 1.5]) + dist(center_2, [1, 1.5])

# print(a1, int(abs(a2*10_000)))



from math import dist

f = open("Danya/27/27780/27B_27780.txt")

claster_1 = []
claster_2 = []
claster_3 = []

for row in f:
    x, y = [float(i) for i in row.replace(",", ".").split()]

    if y > 22:
        claster_1.append([x, y])
    elif x < 24:
        claster_2.append([x, y])
    else:
        claster_3.append([x, y])

# 902 200 148
# print(len(claster_1), len(claster_2), len(claster_3))


def getCenter(claster: list):
    center = None
    min_sum_rasst = 10**6

    for start in claster:
        temp_sum_rasst = 0

        for stop in claster:
            temp_sum_rasst += dist(start, stop)

        if temp_sum_rasst < min_sum_rasst:
            min_sum_rasst = temp_sum_rasst
            center = start

    return center



center_2 = getCenter(claster_2)

b1 = 0

for stop in (claster_1 + claster_2 + claster_3):
    if stop != center_2:
        if dist(center_2, stop) <= 1.2:
            b1 += 1



center_1 = getCenter(claster_1)
b2 = 10**6

for stop in claster_1:
    if stop != center_1:
        b2 = min(b2, dist(center_1, stop))


print(b1, int(abs(b2 * 10_000)))