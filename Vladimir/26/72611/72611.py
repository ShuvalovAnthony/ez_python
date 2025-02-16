f = open("Vladimir/26/72611/26.txt")


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


# [77858, 14, 16, 6]

data = sorted(data, key= lambda x:(
    -x[1],
    -x[2],
    -x[3],
    x[0]
))


passed = data[:len(data)//4]
failed = data[len(data)//4:]

for student in failed:
    if student[1:] == passed[-1][1:]:
        passed.append(student)
        failed = failed[1:]



counter = 0
for student in passed:
    counter += student[1:] == passed[1699][1:]



print(failed[0][0], counter)