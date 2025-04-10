f = open("Daniil/24/17535/24_17535.txt").read()

f = f.replace("CD", "_")

indexes = []

for i in range(len(f)):
    if f[i] == '_':
        indexes.append(i)


max_len = 0

for i in range(len(indexes) - 161):
    left = indexes[i]
    right = indexes[i + 161]

    substring = f[left + 1:right]
    # print(substring[:10], substring[-10:], substring.count("_"))
    # print()

    if len(substring) > max_len:
        max_len = len(substring)



print(max_len + 160 + 2)