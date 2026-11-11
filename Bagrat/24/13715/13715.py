f = open("Bagrat/24/13715/24_13715.txt").read()


indexes = []

skipNext = False

for i in range(len(f)):
    if skipNext:
        skipNext = False
        continue

    slice = f[i: i + 2]
    if slice == "AB" or slice == "BA":
        indexes.append(i)
        skipNext = True

max_len = 0

for i in range(len(indexes) - 51):
    left = indexes[i]
    right = indexes[i + 51]

    sub = f[left: right + 2]

    max_len = max(max_len, len(sub) - 2)

print(max_len)


