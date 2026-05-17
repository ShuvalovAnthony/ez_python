f = open("Sofi/17/29971/17_29971.txt")

data = [int(i) for i in f]

for num in sorted(data):
    if abs(num)%100 == 33:
        max_ok_na_33 = num



def check(row: list):
    k = 0 # кол-во двузначных
    for num in row:
        if 10 <= abs(num) <= 99:
            k += 1

    return (
        (k == 2) and
        (sum(row)**2 < max_ok_na_33)
    )


counter = 0
max_sum = 0

for i in range(len(data) - 2): # тройка -2, пара -1
    row = data[i: i + 3]

    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))


print(counter, max_sum)
