f = open("Mihail/24/24_23281.txt").read()

indexes = [] # индексы Y в ФАЙЛЕ f

for i in range(len(f)):
    if f[i] == "Y":
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 81):
    left = indexes[i]
    right = indexes[i + 81]

    substr = f[left + 1:right]

    if substr.count("2025") >= 90:
        max_len = max(max_len, len(substr))

print(max_len)