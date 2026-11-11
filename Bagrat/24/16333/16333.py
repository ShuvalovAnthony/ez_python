f = open("Bagrat/24/16333/24_16333.txt").read()

f = f.replace("R", "Q").replace("W", "Q").replace("2", "1").replace("4", "1")


res = []

temp_s = f[0]

for i in range(1, len(f)):
    if f[i] != temp_s[-1]:
        temp_s += f[i]
    else:
        res.append(len(temp_s))
        temp_s = f[i]

res.append(len(temp_s))

print(max(res))