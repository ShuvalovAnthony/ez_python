f = open("Sofi/9/27284/27284.txt")

data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor_2 = []
    povtor_3 = []
    uniq = []

    for num in row:
        if row.count(num) == 2:
            povtor_2.append(num)
        elif row.count(num) == 3:
            povtor_3.append(num)
        elif row.count(num) == 1:
            uniq.append(num)

    uniq = sorted(uniq)

    return (
        (
            (min(row) in povtor_2 and len(uniq) == 5) or
            (min(row) in povtor_3 and len(uniq) == 4)
        ) and
        (
            uniq[0] + uniq[-1] > sum(uniq[1:-1])
            # min(uniq) + max(uniq) > sum(uniq) - min(uniq) - max(uniq)
        )
    )


counter = 0

for row in data:
    if check(row):
        counter += 1



print(counter)