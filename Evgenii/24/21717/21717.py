f = open("Evgenii/24/21717/24_21717.txt").read()


f = f.replace("RSQ", "_")

indexes = []

for i in range(len(f)):
    if f[i] == "_":
        indexes.append(i)

substrings = []


for i in range(len(indexes) - 129):
    left = indexes[i]
    right = indexes[i + 129]
    substring = f[left: right + 1]
    
    for j in range(right + 1, right + 50):
        try:
            if f[j] == "Q":
                substring += "Q"
            else:
                substring += f[j]
                break
        except:
            ...

    substrings.append(substring)


substrings = sorted(substrings, key=lambda x: len(x))

print(len(substrings[0]) + 260)
