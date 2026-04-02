# from math import dist

# f = open("Karen/27/27637/27_A_27637.txt")


# claster_1 = []
# claster_2 = []


# for row in f:
#     x, y = [float(i) for i in row.replace(',', '.').split()]
    
#     if y < 15:
#         claster_1.append([x, y])
#     else:
#         claster_2.append([x, y]) 



# def getCenter(claster: list):
#     min_summa_rasst = 10**6
#     center = None

#     for potential_center in claster:
#         temp_summa_rasst = 0

#         for dot in claster:
#             temp_summa_rasst += dist(potential_center, dot)

#         if temp_summa_rasst < min_summa_rasst:
#             min_summa_rasst = temp_summa_rasst
#             center = potential_center

#     return center



# center_1 = getCenter(claster_1)
# center_2 = getCenter(claster_2)

# # # 301 - 1st answ

# summa_rasst = dist(center_1, [-1, 1.3]) + dist(center_2, [-1, 1.3])


# print(301)
# print(int(summa_rasst*10_000))






from math import dist

f = open("Karen/27/27637/27_B_27637.txt")


claster_1 = []
claster_2 = []
claster_3 = []


for row in f:
    x, y = [float(i) for i in row.replace(',', '.').split()]
    
    if y > 22:
        claster_1.append([x, y])
    else:
        if x < 24:
            claster_2.append([x, y])
        else:
            claster_3.append([x, y])



def getCenter(claster: list):
    min_summa_rasst = 10**6
    center = None

    for potential_center in claster:
        temp_summa_rasst = 0

        for dot in claster:
            temp_summa_rasst += dist(potential_center, dot)

        if temp_summa_rasst < min_summa_rasst:
            min_summa_rasst = temp_summa_rasst
            center = potential_center

    return center

# 1 - max       2 sredn          3 - min kolvo tochek
# print(len(claster_1), len(claster_2), len(claster_3))

# center_2 = getCenter(claster_2)
# count = 0
# for dot in claster_2:
#     if dot != center_2:
#         if dist(dot, center_2) <= 1.6:
#             count += 1
# print(count)
# 182 - 1st answ

center_1 = getCenter(claster_1)
max_dist = 0

for dot in claster_1:
    max_dist = max(max_dist, dist(center_1, dot))

print(int(max_dist*10_000))