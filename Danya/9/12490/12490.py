f = open("Danya/9/12490/12490.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            uniq.append(num)

    return (
        (len(povtor) == 2 and len(uniq) == 5) and
        (row.count(max(row)) == row.count(min(row)))
    )


counter = 0

for row in data:
    if check(row):
        counter += 1


print(counter)





