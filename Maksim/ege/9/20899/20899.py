f = open(r"Maksim/ege/9/20899/20899.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    sorted_row = sorted(row)

    povtor = []

    for num in row:
        if row.count(num) == 2:
            povtor.append(num)

    return (
        (sorted_row[-1] < sum(sorted_row[:3])) and
        (len(povtor) == 2)
    )


counter = 0

for row in data:
    if check(row):
        counter += 1

print(counter)