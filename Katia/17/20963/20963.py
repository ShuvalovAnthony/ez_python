f = open("Katia/17/20963/17_20963.txt")

data = [int(i) for i in f]


for num in sorted(data):
    if (
        (1000 <= abs(num) <= 9999) and
        (abs(num)%17 == 0)
    ):
        min_el = num
        break



def check(triple: list):
    k = 0
    for num in triple:
        if (
        (1000 <= abs(num) <= 9999) and
        (abs(num)%100 == 27)
        ):
            k += 1
    
    return (
        (k >= 1) and
        (sum([i**2 for i in triple]) <= min_el**2)
        )


counter = 0
min_summ = 10**6


for i in range(len(data) - 2):
    row = data[i:i + 3]

    if check(row):
        counter += 1
        min_summ = min(min_summ, sum([abs(i) for i in row]))

print(counter, min_summ)





