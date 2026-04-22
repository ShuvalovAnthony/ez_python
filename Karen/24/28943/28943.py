f = open("Karen/24/28943/24_28943.txt").read()

f = f.replace("20", "_")
for i in "EYUIO":
    f = f.replace(i, "A")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

min_len = 10**6

for i in range(len(indexes) - 25):
    left = indexes[i]
    right = indexes[i + 25]

    sub = f[left: right + 1 + 1]

    if (sub[-1] == "A" and sub.count("A") == 1):
        min_len = min(min_len, len(sub))

print(min_len+26)