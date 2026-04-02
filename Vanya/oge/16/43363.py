counter = 0
summa = 0

n = int(input())

for i in range(n):
    number = int(input())
    start_number = number

    res = []

    while number > 0:
        res.append(number%7)
        number //= 7

    res = res[::-1]

    if res[-1]%2 == 1:
        summa += start_number
        counter += 1

if counter > 0:
    print(summa/counter)
else:
    print("NO")
