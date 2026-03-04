f = open("Karen/24/23381/24_23381.txt").read()


for i in "02468":
    f = f.replace(i, ' ')


exps = f.split()
exps = sorted(exps, key=lambda x: -len(x))

# print(len(exps[0]) + 2)

max_len = 0

for exp in exps:
    if len(set(exp)) == 1:
        max_len = max(max_len, len(exp) + 2)


print(max_len)