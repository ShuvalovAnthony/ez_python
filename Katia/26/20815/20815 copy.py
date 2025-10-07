f = open("Katia/26/20815/26_20815.txt")

n, k = [int(i) for i in f.readline().split()]
data = []
for row in f:
    row = [int(i) for i in row.split()]
    id_can = row[0]
    sum_ball_imp = sum(row[1:])
    ball_sobes = row[-1]
    data.append([id_can, sum_ball_imp, ball_sobes] )


data = sorted( data,key= lambda x:[
    -x[1],
    -x[2],
    x[0]
])

passed = data[:k]
failed = data[k:]
counter = 0 
izgoy = 0
if passed[-1][1] == failed[0][1]:
    poluprohod = passed[-1][1]
else:
    poluprohod = 0

if poluprohod:
    for student in passed:
        if student [1] == poluprohod:
            counter += 1
        if student[1] != poluprohod:
            izgoy = student[0]
    for student in failed:
        if student[1] == poluprohod:
            counter += 1
else:
    counter = 0

print(izgoy, counter)