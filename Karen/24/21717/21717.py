f = open("Karen/24/21717/24_21717.txt").read()


f = f.replace("RSQ", "_")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

min_len = 10**6

for i in range(len(indexes) - 130):
    left = indexes[i]
    right = indexes[i + 129]

    sub = f[left: right + 1]

    for j in range(right + 1, indexes[i + 130] + 3):
        if f[j] != "Q":
            sub += f[j]
            break
        else:
            sub += f[j]

    min_len = min(
        min_len,
        len(sub)
    )

print(min_len + 130*2)