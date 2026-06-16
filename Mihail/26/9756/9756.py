f = open(r"Mihail/26/9756/26_9756.txt")
n = f.readline()
data = [[int(i) for i in row.split()] for row in f]

data = sorted(data, key=lambda x: (
    x[1],
))

used = []
unused = []


for start, stop in data:
    if not used or start >= used[-1][-1]:
        used.append([start, stop])
    else:
        unused.append([start, stop])


print(len(used), used[-3:]) # 16

unused = [i for i in unused if i[0] >= 991]
print(unused) # 1345