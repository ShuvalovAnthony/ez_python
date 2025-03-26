f = open("Daniil/26/73881/26.txt")

n = int(f.readline())


data = [
    # id, summa, pluses, answs
    # [0], [1], [2], [3]
]

for row in f:
    row = [int(i) for i in row.split()]
    
    id = row[0]
    row = row[1:]

    summa = sum(row)
    pluses = sum([i for i in row if i > 0])
    answs = len([i for i in row if i != 0])

    if summa > 0:
        data.append([id, summa, pluses, answs])


data = sorted(data, key=lambda x:(
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

# second tour

first_in_second_tour = failed[0]

second_tour_participants = len(failed)//10

passed += failed[:len(failed)//10]
failed = failed[len(failed)//10:]


for student in failed:
    if student[1:] == passed[-1][1:]:
        passed.append(student)
        failed = failed[1:]
        second_tour_participants += 1

print(first_in_second_tour[0], second_tour_participants)


