f = open("Maksim/ege/9/19241/19241.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        elif row.count(num) == 1:
            uniq.append(num)

    return (
        (len(povtor) == 6) and
        (sum(povtor)/6 < uniq[0])
    )

index = 1

for row in data:
    if check(row):
        print(index)

    index += 1