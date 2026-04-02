# from math import dist


# f = open("Karen/27/27592/27A_27592.txt")


# claster_1 = []
# claster_2 = []


# for row in f:
#     x, y = [float(i) for i in row.replace(',', '.').split()]

#     if x < 3:
#         claster_1.append([x, y])
#     else:
#         claster_2.append([x, y])

# # 1ый макс точек, 2ой - мин
# # print(len(claster_1), len(claster_2))



# def getCenter(claster: list):
#     min_summa_rasst = 10**6
#     center = None

#     for start in claster:
#         temp_summ_rasst = 0

#         for stop in claster:
#             temp_summ_rasst += dist(start, stop)

#         if temp_summ_rasst < min_summa_rasst:
#             min_summa_rasst = temp_summ_rasst
#             center = start

#     return center


# center_1 = getCenter(claster_1)
# center_2 = getCenter(claster_2)

# px = min(
#     dist(center_1, [2.1, 5]), 
#     dist(center_2, [2.1, 5])
# )


# x1, y1 = center_1
# x2, y2 = center_2

# seredina = [(x1 + x2)/2, (y1 + y2)/2]

# py = dist([2.1, 5], seredina)

# print(
#     int(px*10_000),
#     int(py*10_000)
# )



from math import dist


f = open("Karen/27/27592/27B_27592.txt")


claster_1 = []
claster_2 = []
claster_3 = []


for row in f:
    x, y = [float(i) for i in row.replace(',', '.').split()]

    if y > -2.5:
        if x < 3.5:
            claster_1.append([x, y])
        else:
            claster_2.append([x, y])
    else:
        claster_3.append([x, y])

# 1ый макс точек, 2ой - средн, 3ий мин
# print(len(claster_1), len(claster_2), len(claster_3))



def getCenter(claster: list):
    min_summa_rasst = 10**6
    center = None

    for start in claster:
        temp_summ_rasst = 0

        for stop in claster:
            temp_summ_rasst += dist(start, stop)

        if temp_summ_rasst < min_summa_rasst:
            min_summa_rasst = temp_summ_rasst
            center = start

    return center



# center_1 = getCenter(claster_1)

# count = 0

# for dot in (claster_1 + claster_2 + claster_3):
#     if dist(center_1, dot) <= 5:
#         count += 1

# print(count)


center_3 = getCenter(claster_3)

count = 0

for dot in (claster_1 + claster_2 + claster_3):
    if dist(center_3, dot) > 5:
        count += 1

print(count)