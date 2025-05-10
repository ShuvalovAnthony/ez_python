from math import dist

f = open("Daniil/27/21599/27_B_21599.txt")


clasters = [[] for i in range(6)]


for row in f:
    x, y = [float(i) for i in row.split()]

    if y < 7/27*x - 17*7/27:
        clasters[0].append([x, y])
    elif y < 0.8*x + 1:
        clasters[1].append([x, y])
    elif y < 2*x + 13:
        clasters[2].append([x, y])
    elif x > -10:
        clasters[3].append([x, y])
    elif y > -2.5*x - 32:
        clasters[4].append([x, y])
    else:
        clasters[5].append([x, y])
    


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
    abs(sum(i[0] for i in centroids))/len(centroids), 
    abs(sum(i[1] for i in centroids))/len(centroids)
]

print(int(center[0]*10000), int(center[1]*10000))



