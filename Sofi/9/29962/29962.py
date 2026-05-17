f = open("Sofi/9/29962/29962.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    uniq = []

    for num in row:
        if row.count(num) == 1:
            uniq.append(num)
        elif row.count(num) == 3:
            povtor.append(num)

    return (
        ((len(povtor) == 3) and (len(uniq) == 4)) and
        (sum(uniq)/4 > povtor[0])
    )


index = 1

for row in data:
    if check(row):
        print(index)

    index += 1