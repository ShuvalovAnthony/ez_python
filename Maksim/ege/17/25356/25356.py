f = open("Maksim/ege/17/25356/17_25356.txt")

data = [int(i) for i in f]

# максимального элемента последовательности,
# оканчивающегося на 30

for num in sorted(data, reverse=True):
    if abs(num)%100 == 30:
        max_ok_na_30 = num
        break


def check(row: list):
    k = 0 # колво четырехзначных
    for num in row:
        if 1000 <= abs(num) <= 9999:
            k += 1

    return (
        (k == 0) and
        (sum(row) > max_ok_na_30)
    )


counter = 0
max_sum = 0

for i in range(len(data) - 2):
    row = data[i: i + 3] # тройка

    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))


print(counter, max_sum)