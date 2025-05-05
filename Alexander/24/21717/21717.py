f = open("Alexander/24/21717/24_21717.txt").read()


f = f.replace("RSQ", "_")


indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

min_len = 10**10

for i in range(len(indexes) - 129):
    left = indexes[i] # в f
    right = indexes[i + 129]

    subs = f[left:right + 2]
    try:
        for j in range(indexes[i + 130] - indexes[i + 129]):
            if f[j] == "Q":
                subs += f[indexes[i + 129] + 2 + j]
            else:
                min_len = min(min_len, len(subs) + 260 + j)
    except:
        ...
    # if subs[-1] != "Q":
    #     min_len = min(min_len, len(subs) + 260)

print(min_len)