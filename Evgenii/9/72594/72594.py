f = open("Evgenii/9/72594/9.txt")

data = [
    [int(i) for i in row.split()] for row in f
]

counter = 0


def check(row: list):
    unique = []
    non_unique = []
    triple = False

    for num in row:
        if row.count(num) == 1:
            unique.append(num)
        else:
            non_unique.append(num)

        if row.count(num) >= 3: triple = True

    return bool(triple and unique and (
        sum(non_unique)/len(non_unique) < sum(unique)/len(unique) 
    ))



for row in data:
    if check(row):
        counter += 1

print(counter)