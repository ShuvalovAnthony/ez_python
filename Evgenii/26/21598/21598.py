f = open("Evgenii/26/21598/26_21598.txt")


n = int(f.readline())


data = [
    [int(i) for i in row.split()] for row in f
]

data = sorted(data, key=lambda x:(x[0], x[1]))


def countWorkersOnThisMin(minute: int):
    counter = 0

    for start, stop in data:
        if start <= minute <= stop:
            counter += 1

    return counter


workersEveryMin = []

for minute in range(60*24):
    workersEveryMin.append(countWorkersOnThisMin(minute))


max_time = 0
temp_time = 1


for i in range(1, len(workersEveryMin)):
    if workersEveryMin[i] == workersEveryMin[i - 1]:
        temp_time += 1
        print(i, workersEveryMin[i], temp_time)
    else:
        max_time = max(max_time, temp_time)
        print(workersEveryMin[i], temp_time, max_time, "NEW")
        temp_time = 1
max_time = max(max_time, temp_time)

print(max_time)