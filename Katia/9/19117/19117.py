f = open("Katia/9/19117/data.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


counter = 0


def check(row):
    chet = []
    nechet = []

    for num in row:
        if num%2 == 0:
            chet.append(num)
        else:
            nechet.append(num)

    return (
        chet and nechet and
        (
            sum(chet) > sum(nechet)
        )
    ) or (len(set(row)) == 4)


for row in data:
    if check(row):
        counter += 1


print(counter)