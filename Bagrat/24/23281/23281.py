f = open("Bagrat/24/23281/24_23281.txt").read()

indexes = []

for i in range(len(f)):
    if f[i] == "Y":
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 81):
    left = indexes[i]
    right = indexes[i + 81]

    sub = f[left + 1: right]

    if sub.count("2025") >= 90:
        max_len = max(max_len, len(sub))

print(max_len)
