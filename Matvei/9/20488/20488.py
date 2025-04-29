f = open("Matvei/9/20488/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    povtor = []
    unique = []

    for num in row:
        if row.count(num) > 1:
            povtor.append(num)
        elif row.count(num) == 1:
            unique.append(num)

    return (
        povtor and unique and
        (max(row) not in povtor) and
        (sum(unique) >= sum(povtor)*3)
    )
    


counter = 0

for row in data:
    if check(row):
        counter += 1


print(counter)