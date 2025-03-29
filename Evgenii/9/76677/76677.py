f = open("Evgenii/9/76677/9.txt")


data = [
    [int(i) for i in row.split()] for row in f
]


def check(row: list):
    avg = sum(row)/len(row)

    chet_zamet = 0
    nechet_zamet = 0

    for num in row:
        if num > avg:
            if (num%2 == 0): chet_zamet += 1
            else: nechet_zamet += 1

    summa_chet = sum([i for i in row if i%2 == 0])
    summe_nechet = sum([i for i in row if i%2 == 1])

    return (chet_zamet > nechet_zamet) and (summa_chet < summe_nechet)
    


counter = 0

for row in data:
    if check(row):
        counter += 1

print(counter)