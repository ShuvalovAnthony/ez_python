f = open("Matvei/26/20815/26_20815.txt")

n, k = [int(i) for i in f.readline().split()]

data = []


for row in f:
    row = [int(i) for i in row.split()]

    id_ = row[0]
    row = row[1:]
    summa = sum(row)
    sobes = row[-1]

    data.append([id_, summa, sobes])


data = sorted(data, key=lambda x:(
    -x[1],
    -x[2],
    x[0]
))



passed = data[:k]
failed = data[k:]


if passed[-1][1] == failed[0][1]:
    poluprohod = passed[-1][1]
else:
    poluprohod = 0


if poluprohod:
    for cosm in passed:
        if cosm[1] != poluprohod:
            id_with_prohod = cosm[0]
else:
    id_with_prohod = passed[-1][0]


if poluprohod:
    counter = 0
    for cosm in passed:
        if cosm[1] == poluprohod:
            counter += 1
    for cosm in failed:
        if cosm[1] == poluprohod:
            counter += 1
else:
    counter = 0


print(id_with_prohod, counter)