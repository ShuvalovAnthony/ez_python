f = open("Matvei/24/21717/24_21717.txt").read()


f = f.replace("RSQ", "_")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)


# min строка с 3мя RSQ
# max строка с 3мя RSQ


# FDF    _ FSDFDSF_FSDF_FDSF_FSDF _   SFDF_FSDF_SDF

min_len = 10**6

for i in range(len(indexes) - 130):
    left = indexes[i]
    right = indexes[i + 129]

    s = f[left:right + 1]

    for i in range(indexes[i + 130] - indexes[i + 129]):
        if f[i] == "Q":
            s += f[i]
        else:
            s += f[i]
            break


    if s[-1] != "Q":
        min_len = min(min_len, len(s) + 260)


print(min_len)
