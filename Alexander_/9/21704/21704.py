f = open("Alexander_/9/21704/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    sorted_row = sorted(row, reverse=True)

    return (
        (row == sorted_row) and
        (
            (sorted_row[0] + sorted_row[-1])/2 >
            sum(sorted_row[1:-1])/5
        )
    )


for row in data:
    if check(row):
        print(sum(row))
        break