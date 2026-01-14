f = open("Mihail/26/23383/26_23383.txt")

n = f.readline()


data = {}


for row in f:
    sportsman, point = [int(i) for i in row.split()]
    
    if not point in data:
        data[point] = set([sportsman])
    else:
        data[point].add(sportsman)


def find_max_podryad(sportsmen: set):
    sportsmen = sorted(sportsmen)

    max_podryad = 1
    temp_max_podryad = 1

    for i in range(1, len(sportsmen)):
        if sportsmen[i] == sportsmen[i - 1] + 1:
            temp_max_podryad += 1
        else:
            max_podryad = max(max_podryad, temp_max_podryad)
            temp_max_podryad = 1

    return max(max_podryad, temp_max_podryad)


min_point_itog = 10**10
max_podryad_itog = 0

for point, sportsmen in data.items():
    max_podryad = find_max_podryad(sportsmen)

    if max_podryad > max_podryad_itog:
        max_podryad_itog = max_podryad
        min_point_itog = point
    elif max_podryad == max_podryad_itog:
        min_point_itog = min(min_point_itog, point)


print(max_podryad_itog, min_point_itog)


