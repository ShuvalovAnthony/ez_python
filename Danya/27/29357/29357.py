from math import dist


f = open("Danya/27/29357/27_B_29357.txt")


claster_1 = []
claster_2 = []
claster_3 = []



for row in f:
    row = [i for i in row.split()]
    x, y = float(row[0].replace(",", '.')), float(row[1].replace(",", '.'))
    extra = row[2]

    if y < 30:
        claster_1.append([x, y, extra])
    elif x < 16:
        claster_2.append([x, y, extra])
    else:
        claster_3.append([x, y, extra])

# 1170 393 288
# print(len(claster_1), len(claster_2), len(claster_3))


def getCenter(claster: list):
    center = None
    min_sum_rast = 10**6

    for start in claster:
        temp_sum_rast = 0

        for stop in claster:
            temp_sum_rast += dist(start[:2], stop[:2])

        if temp_sum_rast < min_sum_rast:
            min_sum_rast = temp_sum_rast
            center = start

    return center


# center_2 = getCenter(claster_2)
# kras_gig = None
# min_dist = 10**6

# for dot in claster_2:
#     if dot[2][0] == "M" and dot[2][2:] == "III":
#         temp_dist = dist(dot[:2], center_2[:2])
#         if temp_dist < min_dist:
#             min_dist = temp_dist
#             kras_gig = dot

# ax, ay = kras_gig[:2]
# print(int(abs(ax*10_000)), int(abs(ay*10_000)))



def countOrangeGigs(claster: list):
    counter = 0
    for dot in claster:
        if dot[2][0] == "K" and dot[2][2:] == "III":
            counter += 1

    return counter

# 87 28 25
# print(countOrangeGigs(claster_1), countOrangeGigs(claster_2), countOrangeGigs(claster_3),)

center_1 = getCenter(claster_1)
center_3 = getCenter(claster_3)

print(int(abs(dist(center_1[:2], center_3[:2])*10_000)))


def getMaxDistBetwYellowKarlik(claster: list):
    yellow_karliki = []
    max_dist = 0

    for dot in claster:
        if dot[2][0] == "G" and dot[2][2:] == "V":
            yellow_karliki.append(dot)

    for i in range(len(yellow_karliki)):
        for j in range(i + 1, len(yellow_karliki)):
            max_dist = max(
                max_dist,
                dist(yellow_karliki[i][:2], yellow_karliki[j][:2])
            )

    return max_dist
    

b2 = max(
    [getMaxDistBetwYellowKarlik(claster) for claster in [claster_1, claster_2, claster_3]]
)

print(int(abs(b2*10_000)))

