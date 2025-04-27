f = open("Alexander_/9/19117/data.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


counter = 0


def check(row: list):
    povtor = []
    unique = []
    sum_chet = 0
    sum_nechet = 0

    for num in row:
        if num%2 == 0: sum_chet += num
        else: sum_nechet += num

        if row.count(num) == 2:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

    return (
        ((len(povtor) == 2) and (len(unique) == 3)) or
        (   
            sum_chet and sum_nechet and
            (sum_chet > sum_nechet)
        )
    )

for row in data:
    if check(row):
        counter += 1


print(counter)