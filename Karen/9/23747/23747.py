f = open("Karen/9/23747/23747.txt") # r перед кавычками для винды

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
        povtor and uniq and
        (len(povtor) == 3) and
        (sum(uniq)/len(uniq) <= povtor[0])
    )


for row in data:
    if check(row):
        print(sum(row))