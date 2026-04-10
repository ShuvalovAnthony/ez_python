# from math import dist

# f = open("Katia/27/28766/27_A_28766.txt")


# claster_1 = []
# claster_2 = []


# for row in f:
#     x, y, info = [i for i in row.replace(",", ".").split()]
#     x, y = float(x), float(y)
#     color, light, size = info[0], info[1], info[2:]

#     if y < 10:
#         claster_1.append([x, y, color, light, size])
#     else:
#         claster_2.append([x, y, color, light, size])


# # 131 92
# print(len(claster_1), len(claster_2))

# print(claster_1[0])

# def getCenter(claster: list):
#     min_sum_dist = 10**6
#     center = None

#     for start in claster:
#         temp_sum_dist = 0
#         for stop in claster:
#             temp_sum_dist += dist(start[:2], stop[:2])

#         if temp_sum_dist < min_sum_dist:
#             min_sum_dist = temp_sum_dist
#             center = start

#     return center


# center_2 = getCenter(claster_2)

# # min_dist = 10**6

# # # [x, y, color, light, size]
# # for stop in (claster_1 + claster_2):
# #     if (stop[2] == "Y") and (stop[-1] == "III"):
# #         min_dist = min(
# #             min_dist,
# #             dist(center_2[:2], stop[:2])
# #         )

# # print(int(min_dist*10_000))


# # max_dist = 0

# # # [x, y, color, light, size]
# # for stop in (claster_1 + claster_2):
# #     if (stop[2] == "Y") and (stop[-1] == "III"):
# #         max_dist = max(
# #             max_dist,
# #             dist(center_2[:2], stop[:2])
# #         )

# # print(int(max_dist*10_000))






from math import dist

f = open("Katia/27/28766/27_B_28766.txt")


claster_1 = []
claster_2 = []
claster_3 = []


for row in f:
    x, y, info = [i for i in row.replace(",", ".").split()]
    x, y = float(x), float(y)
    color, light, size = info[0], info[1], info[2:]

    if y > 23:
        claster_1.append([x, y, color, light, size])
    elif y > 15:
        claster_2.append([x, y, color, light, size])
    else:
        claster_3.append([x, y, color, light, size])


# 74 100 451
print(len(claster_1), len(claster_2), len(claster_3))



def getCenter(claster: list):
    min_sum_dist = 10**6
    center = None

    for start in claster:
        temp_sum_dist = 0
        for stop in claster:
            temp_sum_dist += dist(start[:2], stop[:2])

        if temp_sum_dist < min_sum_dist:
            min_sum_dist = temp_sum_dist
            center = start

    return center

# [x, y, color, light, size]
def getMinDistYelGigants(claster: list):
    filteredClaster = [star for star in claster if (
        (star[2] == "Z") and (star[-1] == "I")
        )]
    

    min_dist = 10**6

    for start in filteredClaster:
        for stop in filteredClaster:
            if start != stop:
                min_dist = min(
                    min_dist,
                    dist(start[:2], stop[:2])
                )

    return min_dist


def countYelGigants(claster: list):
    return len([star for star in claster if ((star[2] == "Z") and (star[-1] == "I"))])


b1 = min(
    getMinDistYelGigants(claster_1),
    getMinDistYelGigants(claster_2),
    getMinDistYelGigants(claster_3)
)


print(
    countYelGigants(claster_1),
    countYelGigants(claster_2), # min
    countYelGigants(claster_3) # max
)

b2 = dist(
    getCenter(claster_2)[:2],
    getCenter(claster_3)[:2]
)


print(int(b1*10_000))
print(int(b2*10_000))