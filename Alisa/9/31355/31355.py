f = open(r"Alisa/9/31355/31355.txt")

# На win r"""

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    uniq = []
    povtor = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            uniq.append(num)

    return (
        (len(povtor) == 3) and
        (len(uniq) == 3) and
        (povtor[0]**3 < uniq[0]*uniq[1]*uniq[2])
    )


counter = 0

for row in data:
    if check(row):
        counter += 1


print(counter)