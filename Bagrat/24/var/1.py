f = open("Bagrat/24/var/24.txt").read()

f = f.replace("MARYA", "*") + "*"

indexes = []

for i in range(len(f)):
    if f[i] == "*":
        indexes.append(i)


max_len = 0

for i in range(len(indexes) - 191):
    left = indexes[i]
    right = indexes[i + 191]

    sub = f[left + 1: right]

    # print(sub.count("*"))
    max_len = max(max_len, len(sub))


print(max_len + 190*4 + 4)