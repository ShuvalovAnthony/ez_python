f = open("Mihail/24/21717/24_21717.txt").read()


f = f.replace('RSQ', '_')

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

spisok = []

k = 0

for i in range(len(indexes) - 130):
    left = indexes[i]
    right = indexes[i + 129]

    substring = f[left:right + 1]


    for j in range(right + 1, indexes[i + 130]):
        if f[j] != "Q":
            spisok.append(len(substring) + 1)
        else:
            substring += f[j]

    

    

print(min(spisok) + 260)