f = open("Mihail/26/28945/26_28945.txt")

n = int(f.readline())

data = []


for row in f:
    start, len_ = [int(i) for i in row.split()]

    data.append([start, start + len_])

data = sorted(data, key=lambda x: x[1])


last_stop = 0
counter = 0

used = []
unused = []

for start, stop in data:
    if start > last_stop:
        last_stop = stop
        counter += 1
        used.append([start, stop])
    else:
        unused.append([start, stop])

print(counter)

print(used[-5:])
print(unused[-5:])