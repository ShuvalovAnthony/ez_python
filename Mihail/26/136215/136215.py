f = open("Mihail/26/136215/26_2024.txt")

n = int(f.readline())

data = [
    [int(i) for i in row.split()] for row in f
]


data = sorted(data, key= lambda x: (
    x[1]
))

used = []
unused = []

for start, stop in data:
    if not used:
        used.append([start, stop])
        continue

    if start >= used[-1][-1]:
        used.append([start, stop])
    else:
        unused.append([start, stop])


# print(len(used)) # 32

print(used[-3:])

print([i for i in unused if i[0] >= 1273])