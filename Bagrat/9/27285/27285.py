f = open(r"Bagrat/9/27285/27285.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    chet = 0
    nechet = 0
    sorted_row = sorted(row)

    for num in row:
        if num%2 == 0:
            chet += 1
        else:
            nechet += 1

    return (
        (sorted_row == row) and # неубывание
        # (len(set(row)) == len(row)) and # + возрастание
        (chet > nechet)
    )


counter = 0

for row in data:
    counter += check(row)

print(counter)



# 4 числа в строке
# можно разбить 4 числа на две равных пары

def check(row: list):
    sorted_row = sorted(row)
    return (
        sorted_row[0] + sorted_row[-1] == sorted_row[1] + sorted_row[2]
    )


def treug(a, b, c):
    a, b, c = sorted([a, b, c])
    return a + b > c