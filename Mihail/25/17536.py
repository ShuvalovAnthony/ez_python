def delit(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return i + num//i

    return 0


limit = 5

for num in range(800_001, 10**10):
    res = delit(num)

    if (res%10 == 4):
        print(num, res)

        limit -= 1

    if limit == 0:
        break