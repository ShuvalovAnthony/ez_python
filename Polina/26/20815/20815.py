f = open("Polina/26/20815/26_20815.txt")

n, crew_count = [int(i) for i in f.readline().split()]

cosmonavti = [
    # 0         1         2
    # id, summa_ballov, sobes
]


for row in f:
    row = [int(i) for i in row.split()]
    id = row[0]
    row = row[1:]
    summa_ballov = sum(row)
    sobes = row[-1]

    cosmonavti.append([id, summa_ballov, sobes])



cosmonavti = sorted(cosmonavti, key=lambda x:(
    -x[1],
    -x[2],
    x[0]
))


passed = cosmonavti[:crew_count]
failed = cosmonavti[crew_count:]


for cosm in passed[::-1]:
    if cosm[1] != passed[-1][1]:
        prohodnoi = cosm[1]
        break



for cosm in passed:
    if cosm[1] == prohodnoi:
        id = cosm[0]


counter = 0

for cosm in passed:
    if cosm[1] == passed[-1][1]:
        counter += 1

for cosm in failed:
    if cosm[1] == passed[-1][1]:
        counter += 1


print(id, counter)