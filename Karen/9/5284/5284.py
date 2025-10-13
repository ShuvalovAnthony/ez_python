f = open("Karen/9/5284/5284.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []
    sorted_row = sorted(row)

    for num in row:
        if row.count(num) == 3:
            povtor.append(num)
        if row.count(num) == 1:
            uniq.append(num)

    return (
        ((sorted_row[0] + sorted_row[-1])**2 > sum([i**2 for i in sorted_row[1:-1]])) or
        (len(povtor) == 3 and len(uniq) == 3)
    )
    

count = 0

for row in data:
    if check(row):
        count += 1


print(count)