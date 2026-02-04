f = open("Mihail/24/19254/24_19254.txt").read()


f = f.replace("FSRQ", "_")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)



max_len = 0


for i in range(len(indexes) - 81):
    left = indexes[i]
    right = indexes[i + 81]

    substring = f[left + 1: right]

    max_len = max(max_len, len(substring) + 3*80 + 6)


print(max_len)