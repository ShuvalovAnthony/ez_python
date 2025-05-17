f = open("Evgenii/26/19752/26_19752.txt")

n = int(f.readline())


data = []


for row in f:
    row = [int(i) for i in row.split()]

    id = row[0]
    row = row[1:]

    summa = sum(row)
    pluses = sum([i for i in row if i > 0])
    answs = len([i for i in row if i != 0])

    if summa > 0:
        data.append([id, summa, pluses, answs])


data = sorted(data, key=lambda x: (
    -x[1],
    -x[2],
    -x[3],
    x[0]
))


passed = data[:len(data)//3]
failed = data[len(data)//3:]

for student in failed:
    if student[1:] == passed[-1][1:]:
        passed.append(student)
        failed = failed[1:]


# dop tur
print(failed[0])
start_len = len(passed)
passed += failed[:len(failed)//10]
failed = failed[len(failed)//10:]

for student in failed:
    if student[1:] == passed[-1][1:]:
        passed.append(student)
        failed = failed[1:]

finish_len = len(passed)
print(finish_len - start_len)
