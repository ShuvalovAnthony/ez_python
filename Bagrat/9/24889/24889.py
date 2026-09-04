f = open(r"Bagrat/9/24889/24889.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 1:
            uniq.append(num)
        else:
            povtor.append(num)

    return (
        (max(row) in povtor) and
        (len(povtor) in (3, 4)) and
        (len(set(povtor)) == 1) and
        (min(uniq) + max(uniq) <= sum(uniq) - min(uniq) - max(uniq))
    )


counter = 0

for row in data:
    if check(row):
        print(row)
        counter += 1


print(counter)