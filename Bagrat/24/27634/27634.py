f = open("Bagrat/24/27634/24_27634.txt").read()

indexes = []

for i in range(len(f)):
    if f[i] == "Z":
        indexes.append(i)

min_len = 10**6

for i in range(len(indexes)- 269):
    left = indexes[i]
    right = indexes[i + 269]

    sub = f[left:right + 1]

    # print(sub.count("Z"), sub[:10], sub[-10:])

    min_len = min(min_len, len(sub))

print(min_len)