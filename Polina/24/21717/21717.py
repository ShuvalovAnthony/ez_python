f = open("Polina/24/21717/24_21717.txt").read()


f = f.replace("RSQ", "_")


indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)


min_len = 10**6


for i in range(len(indexes) - 130):
    left = indexes[i]
    right = indexes[i + 129]

    s = f[left:right + 2]

    for i in range(indexes[i + 130] - indexes[i + 129]):
        if s[-1] == "Q":
            s += f[indexes[i + 129] + i + 1]

    if s[-1] != "Q":
        min_len = min(min_len, len(s) + 260)

print(min_len)
