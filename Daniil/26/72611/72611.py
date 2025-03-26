f = open("Daniil/26/72611/72611.txt")

n = int(f.readline())


data = []


for row in f:
    row = [int(i) for i in row.split()]

    id = row[0]

    row = row[1:]

    summa = sum(row)
    pluses = sum([i for i in row if i > 0])
    answs = len([i for i in row if i != 0])

    data.append([id, summa, pluses, answs])


data = sorted(data, key=lambda x: (
    -x[1],
    -x[2],
    -x[3],
    x[0]
))


passed = data[:len(data)//4]
failed = data[len(data)//4:]


for row in failed:
    if row[1:] == passed[-1][1:]:
        passed.append(row)
        failed = failed[1:]

first_failed = failed[0]


counter = 0
for row in passed:
    if row[1:] == passed[1699][1:]:
        counter += 1

print(first_failed[0], counter)