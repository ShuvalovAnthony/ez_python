f = open("Sofi/24/29354/24_29354.txt").read()


f = f.replace("BC", "_")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)


max_len = 0


for i in range(len(indexes) - 191):
    left = indexes[i]
    right = indexes[i + 191]
    sub = f[left + 1: right]

    max_len = max(max_len, len(sub))
        


print(max_len + 190 + 2)