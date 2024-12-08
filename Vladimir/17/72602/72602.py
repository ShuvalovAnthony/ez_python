f = open("17/72602/17.txt")


data = [int(i) for i in f]


max_el = max(data)
min_el = min(data)
counter = 0
max_sum = -10**6


def check(num1, num2):
    return (
        (
            (num1%3 == max_el%3) or
            (num2%3 == max_el%3)
        ) and
        (
            (num1%7 == min_el%7) or
            (num2%7 == min_el%7)
        )
    )


for i in range(len(data) - 1):
    num1, num2 = data[i], data[i + 1]
    if check(num1, num2):
        counter += 1
        max_sum = max(max_sum, num1 + num2)

print(counter, max_sum)