f = open("")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    sorted_row = sorted(row)
    povtor = []

    for num in row:
        if row.count(num) > 1:
            summa_cifr = sum([int(i) for i in str(num)])
            if summa_cifr%2 == 0:
                povtor.append(num)

    return (
        (row == sorted_row) and
        (povtor)
    )
    


for i in range(len(data)):
    row = data[i]

    if check(row):
        print(i + 1)