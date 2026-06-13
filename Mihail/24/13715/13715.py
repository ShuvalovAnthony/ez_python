f = open("Mihail/24/13715/24_13715.txt").readline()

f = f.replace("AB", "*")

indexes = []

for i in range(len(f)):
    if f[i] == "*":
        indexes.append(i)

max_len = 0

for i in range(len(indexes) - 51):
    left = indexes[i]
    right = indexes[i + 51]
    sub = f[left + 1: right]

    max_len = max(max_len, len(sub))

print(max_len + 52) # 50 - от замены + 2 символа по краям
