f = open("Katia/24/20909/24_20909.txt").read()

f = f.replace("AB", "_")


indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

max_len = 0


# 0123456789

for i in range(len(indexes) - 102):
    left = indexes[i]
    right = indexes[i + 101]

    res = f[left + 1:right]

    max_len = max(max_len, len(res) + 100 + 2)

print(max_len)

    