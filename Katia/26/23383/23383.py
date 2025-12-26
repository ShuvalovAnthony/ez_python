f = open("Katia/26/23383/26_23383.txt")

n = int(f.readline())

data = {}

for row in f:
    sportsman_num, point_num = [int(i) for i in row.split()]

    if point_num not in data:
        data[point_num] = set()
    
    data[point_num].add(sportsman_num)


def maxPodryad(point_num):
    sportsmen = sorted(data[point_num])
    max_podryad = 0

    temp_max_podryad = 1

    for i in range(1, len(sportsmen)):
        previous_man, current_man = sportsmen[i - 1], sportsmen[i]
        if current_man - previous_man == 1:
            temp_max_podryad += 1
        else:
            max_podryad = max(max_podryad, temp_max_podryad)
            temp_max_podryad = 1

    return max(max_podryad, temp_max_podryad)

res = []

for point_num in data:
    res.append([point_num, maxPodryad(point_num)])


res = sorted(res, key=lambda x: (
    -x[1],
    x[0]
))


for row in res[:10]:
    print(row)