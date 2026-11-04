f = open("Bagrat/24/27634/24_27634.txt").read()

indexes = []

for i in range(len(f)):
    if f[i] == "Z":
        indexes.append(i)

max_len = 0

for i in range(len(indexes)- 271):
    left = indexes[i]
    right = indexes[i + 271]

    sub = f[left + 1:right]

    # print(sub.count("Z"), sub[:10], sub[-10:])

    max_len = max(max_len, len(sub))

print(max_len)