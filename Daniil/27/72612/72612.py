from math import dist


f = open("Daniil/27/72612/27a.txt")


data = [
    [float(i) for i in row.replace(',', '.').split()] for row in f
]


claster_1 = [
    dot for dot in data if (
        (-1.5 <= dot[0] <= 1.5) and (-1 <= dot[1] <= 2)
        )
]
claster_2 = [
    dot for dot in data if (
        (0 <= dot[0] <= 3) and (2.5 <= dot[1] <= 5.5)
        )
]
# claster_3 = [
#     dot for dot in data if (
#         (-1 <= dot[0] <= 2) and (6 <= dot[1] <= 9)
#         )
# ]

clasters = [claster_1, claster_2]

def get_centroida(claster):
    centroida = None
    min_summ_rasst = 10**6
    for start in claster:
        temp_summa_rasst = 0
        for end in claster:
            temp_summa_rasst += dist(start, end)
        
        if temp_summa_rasst < min_summ_rasst:
            min_summ_rasst = temp_summa_rasst
            centroida = start

    return centroida


centroids = [get_centroida(claster) for claster in clasters]

center = [
    sum(i[0] for i in centroids)/len(centroids), 
    sum(i[1] for i in centroids)/len(centroids)
]

print(int(center[0]*10000), int(center[1]*10000))
