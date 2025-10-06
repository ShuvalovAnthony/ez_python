f = open("Katia/26/20815/26_20815.txt")


data = []

n, k = [int(i) for i in f.readline().split()]

# print(n, k)

for row in f:
    row = [int(i) for i in row.split()]
    id_ = row[0]
    row = row[1:]

    data.append([id_, sum(row), row[-1]])


data = sorted(data, key=lambda x: [
    -x[1],
    -x[2],
    x[0]
])

passed = data[:k]
failed = data[k:]


# for row in passed:
#     print(row)

# print("-----")

# for row in failed[:5]:
#     print(row)


if passed[-1][1] == failed[0][1]:
    poluprohod = passed[-1][1]
else:
    poluprohod = 0


id_last_prohod = 0
cand_with_poluprohod = 0


if poluprohod:
    # первое число в ответе ищем
        
    # второе число
    for astro in passed:
        if astro[1] == poluprohod:
            cand_with_poluprohod += 1
        if astro[1] != poluprohod:
            id_last_prohod = astro[0]
    for astro in failed:
        if astro[1] == poluprohod:
            cand_with_poluprohod += 1
else:
    id_last_prohod = passed[-1][0]


print(id_last_prohod, cand_with_poluprohod)