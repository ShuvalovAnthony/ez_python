f = open(r"Mihail/9/12098/12098.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            uniq.append(num)


    return (
        (len(povtor) == 3) and
        (povtor[0]%2 == 1) and
        (uniq[0]%2 == 0)
    )


count = 0

for row in data:
    if check(row):
        count += 1


print(count)

