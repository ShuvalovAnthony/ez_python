f = open()


data = [
    [int(i) for i in row.split()] for row in f
]



def check(row: list):
    row = sorted(row)

    return (
        (row[-1] < sum(row[:3])) and
        (row[0] + row[-1] == row[1] + row[2])
    )



counter = 0


for row in data:
    if check(row): counter += 1


print(counter)
