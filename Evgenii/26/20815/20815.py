f = open("Evgenii/26/20815/26_20815.txt")

n, k = [int(i) for i in f.readline().split()]


data = []

for row in f:
    row = [int(i) for i in row.split()]

    id = row[0]
    row = row[1:]
    summa = sum(row)
    sobes = row[-1]

    data.append([id, summa, sobes])


# id - 0, summa - 1, sobes - 2

data = sorted(data, key=lambda x:(
    -x[1],
    -x[2],
    x[0]
))


# for student in data[:20]:
#     print(student)


passed = data[:k]
failed = data[k:]


if passed[-1][1] == failed[0][1]:
    poluprohod = passed[-1][1]
else:
    poluprohod = 0


# for cosm in passed:
#     if cosm[1] != poluprohod:
#         print(cosm)

# id 45539


counter = 0

for cosm in passed:
    if cosm[1] == poluprohod:
        counter += 1

for cosm in failed:
    if cosm[1] == poluprohod:
        counter += 1

print(counter)