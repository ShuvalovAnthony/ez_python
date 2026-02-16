f = open("Danya/9/24344/24344.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    row = sorted(row)

    return (
        ((row[0] + row[-1])**2 > (row[1]**3 + row[2]**3)) and
        (row[0] + row[-1] != row[1] + row[2])
    )


index = 1
summa = 0


for row in data:
    if check(row):
        summa += index


    index += 1

print(summa)