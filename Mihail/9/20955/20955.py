f = open(r"Mihail/9/20955/20955.txt")

data = [[int(i) for i in row.split()] for row in f]


def check(row: list):
    uniq = []
    povtor = []
    for i in row:
        if row.count(i) == 1:
            uniq.append(i)
        if row.count(i) == 2:
            povtor.append(i)

    return(
        (len(povtor) == 4 and len(uniq) == 4) and (sum(povtor) >= sum(uniq)*2)
    )

count = 0
for row in data:
    # print(row)
    if check(row):
        count += 1
print(count)
#мой ответ - 115