f = open("Katia/9/76224/76224.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    trizd = [i for i in row if row.count(i) == 3]
    uniq = [i for i in row if row.count(i) == 1]

    return (
        (len(trizd) == 3 and len(uniq) == 4) and
        (sum(uniq)/len(uniq) >= trizd[0]) and
        (max(row)%min(row) != 0)
    )


res = []
index = 1

for row in data:
    if check(row):
        res.append([sum(row), index])
    
    index += 1

res = sorted(res, key=lambda x: (x[0]))

for row in res:
    print(row[1])
    break