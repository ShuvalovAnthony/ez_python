f = open(r"Bagrat/17/28938/17_28938.txt")

data = [int(i) for i in f]

for num in sorted(data):
    if abs(num)%100 == 28: # str(num)[-2:] == '28'
        max_na_28 = num

def check(row: list):
    kolvo_trehzn = 0 # колво трехзначных
    avg = sum(row)/len(row)

    for num in row:
        if 100 <= abs(num) <= 999:
            kolvo_trehzn += 1

    return (
        (kolvo_trehzn >= 1) and
        (avg > 0) and
        (avg < max_na_28)
    )


counter = 0
max_sum = 0


for i in range(len(data) - 2):
    row = data[i: i + 3]

    if check(row):
        counter += 1
        max_sum = max(max_sum, sum(row))

print(counter, max_sum)