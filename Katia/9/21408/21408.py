f = open("Katia/9/21408/data.txt")



data = [
    [int(i) for i in row.split()] for row in f
]

counter = 0


def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

    return (
        (len(povtor) == 6) and
        (len(unique) == 1) and
        (max(povtor) > unique[0])
    )


for row in data:
    if check(row):
        counter += 1


print(counter)