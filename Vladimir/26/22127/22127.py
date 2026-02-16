f = open("Vladimir/26/22127/26_22127.txt")

n = f.readline()

data = [
    [int(i) for i in row.split()] for row in f
]

data = sorted(data, key=lambda x: x[0])

total = data[0][0] - 1
counter = 2

last_stop = data[0][1]

for start, stop in data[1:]:
    if start <= last_stop:
        last_stop = max(last_stop, stop)
    else:
        total += start - last_stop - 1
        counter += 1
        last_stop = stop

total += 24*60*60*1000 - last_stop

print(counter, total)