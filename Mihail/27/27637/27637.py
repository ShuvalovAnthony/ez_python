from math import *
f = open(r"Mihail/27/27637/27_A_27637.txt")
data = [[float(i) for i in row.replace(",",".").split()] for row in f]
claster1 = []
claster2 = []
for x, y in data:
    if 5 <= x <= 12 and 15 <= y <= 25:
        claster1.append([x, y])
    if 2.5 <= x <= 9 and 5.5 <= y <= 11:
        claster2.append([x, y])


def find_center(claster):
    center = None
    rast = 10**10
    for start in claster:
        temp_rast = 0
        for stop in claster:
            temp_rast += dist(start, stop)
        if temp_rast < rast:
            center = start
            rast = temp_rast
    return center

print(len(claster1))
print(len(claster2))
tochka = [-1, 1.3]
summa_rast = 0
center1 = find_center(claster1)
center2 = find_center(claster2)
summa_rast += dist(center1, tochka)
summa_rast += dist(center2, tochka)
print(summa_rast * 10000)
# from math import *
# f = open(r"27_B_27637.txt")
# data = [[float(i) for i in row.replace(",",".").split()] for row in f]
# claster1 = []
# claster2 = []
# claster3 = []
# for x, y in data:
#     if 14 <= x <= 21 and 23 <= y <= 32:
#         claster1.append([x, y])
#     if 17 <= x <= 23 and 14 <= y <= 20:
#         claster2.append([x, y])
#     if 25 <= x <= 32 and 11 <= y <= 19:
#         claster3.append([x, y])
#
#
# def find_center(claster):
#     center = None
#     rast = 10**10
#     for start in claster:
#         temp_rast = 0
#         for stop in claster:
#             temp_rast += dist(start, stop)
#         if temp_rast < rast:
#             center = start
#             rast = temp_rast
#     return center
#
# # claster2
# # rastt = 1.6
# # k = 0
# # center2 = find_center(claster2)
# # for start in claster2:
# #     if dist(start, center2) <= rastt and start != center2:
# #         k += 1
# # print(k)
# print(len(claster1))
# print(len(claster2))
# print(len(claster3))
#
# # claster3
# center1 = find_center(claster1)
# def max_rast(claster, center):
#     max_rastt = 0
#     for start in claster:
#         if dist(start, center) > max_rastt:
#             max_rastt = dist(start, center)
#     return max_rastt
# print(max_rast(claster1, center1) * 10000)