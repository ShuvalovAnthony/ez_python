# from math import dist


# f = open("Mihail/27/25447/27A_25447.txt")


# claster_1 = []
# claster_2 = []


# for row in f:
#     x, y = [float(i) for i in row.replace(",", ".").split()]

#     if (5 < x < 15) and (-10 < y < 0):
#         claster_1.append([x, y])
#     elif (15 < x < 25) and (-10 < y < 5):
#         claster_2.append([x, y])



# def center(claster: list):
#     center = None
#     min_sum_rasst = 10**6

#     for start in claster:
#         temp_sum_rasst = 0

#         for end in claster:
#             temp_sum_rasst += dist(start, end)

#         if temp_sum_rasst < min_sum_rasst:
#             min_sum_rasst = temp_sum_rasst
#             center = start

#     return center



# # print(center(claster_1))
# # print(center(claster_2))

# px, py = center(claster_1)

# print(abs(int(px*10_000)), abs(int(py*10_000)))



from math import dist


f = open("Mihail/27/25447/27B_25447.txt")


claster_1 = []
claster_2 = []
claster_3 = []

for row in f:
    x, y = [float(i) for i in row.replace(",", ".").split()]

    if (5 < x < 15) and (7 < y < 13):
        claster_1.append([x, y])
    elif (15 < x < 25) and (10 < y < 20):
        claster_2.append([x, y])
    elif (15 < x < 25) and (-5 < y < 10):
        claster_3.append([x, y])



def findCenter(claster: list):
    center = None
    min_sum_rasst = 10**6

    for start in claster:
        temp_sum_rasst = 0

        for end in claster:
            temp_sum_rasst += dist(start, end)

        if temp_sum_rasst < min_sum_rasst:
            min_sum_rasst = temp_sum_rasst
            center = start

    return center



def avgDistFromCenter(claster: list):
    distances = []
    center = findCenter(claster)

    for dot in claster:
        if center != dot:
            distances.append(
                dist(center, dot)
            )

    return sum(distances)/len(distances)


q1 = avgDistFromCenter(claster_2) # min
q2 = avgDistFromCenter(claster_3) # max

print(int(q1*10_000), int(q2*10_000))