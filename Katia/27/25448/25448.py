from math import dist


# f = open("Katia/27/25448/27B_25448.txt")

# claster_1 = []
# claster_2 = []
# claster_3 = []

# for row in f:
#     x, y = [float(i) for i in row.replace(",", '.').split()]

#     if (25 <= x <= 35) and (5 <= y <= 15):
#         claster_1.append([x, y])
#     elif (10 <= x <= 20) and (10 <= y <= 16):
#         claster_2.append([x, y])
#     elif (15 <= x <= 25) and (15 <= y <= 25):
#         claster_3.append([x, y])


# def center(claster: list):
#     res_center = None
#     min_summ_rasst = 10**10

#     for start in claster:
#         temp_summ_rasst = 0

#         for end in claster:
#             temp_summ_rasst += dist(start, end)

#         if temp_summ_rasst < min_summ_rasst:
#             min_summ_rasst = temp_summ_rasst
#             res_center = start

#     return res_center



# def average_dist(claster: list):
#     vse_rasst = []

#     claster_center = center(claster)

#     for dot in claster:
#         if dot != claster_center:
#             vse_rasst.append(dist(claster_center, dot))
    
#     return sum(vse_rasst)/len(vse_rasst)


# print(int(average_dist(claster_3)*10000))
# print(int(average_dist(claster_1)*10000))


f = open("Katia/27/25448/27A_25448.txt")

claster_1 = []
claster_2 = []

for row in f:
    x, y = [float(i) for i in row.replace(",", '.').split()]

    if (0 <= x <= 5) and (4 <= y <= 10):
        claster_1.append([x, y])
    elif (0 <= x <= 10) and (14 <= y <= 20):
        claster_2.append([x, y])


def center(claster: list):
    res_center = None
    min_summ_rasst = 10**10

    for start in claster:
        temp_summ_rasst = 0

        for end in claster:
            temp_summ_rasst += dist(start, end)

        if temp_summ_rasst < min_summ_rasst:
            min_summ_rasst = temp_summ_rasst
            res_center = start

    return res_center


def average_dist(claster: list):
    vse_rasst = []

    claster_center = center(claster)

    for dot in claster:
        if dot != claster_center:
            vse_rasst.append(dist(claster_center, dot))
    
    return sum(vse_rasst)/len(vse_rasst)


px1, py1 = center(claster_1)
px2, py2 = center(claster_2)
dx, dy = px2 - px1, py2 - py1

print(int(dx * 10_000), int(dy * 10_000))

