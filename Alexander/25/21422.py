def check(num):
    deliteli = set()

    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            # первый делитель i
            if (i%10 == 7) and (i != 7):
                deliteli.add(i)

            # второй делитель - num//i
            if (num//i%10 == 7) and (num//i != num):
                deliteli.add(num//i)

    if deliteli: return min(deliteli)
    return False



limit = 5


for num in range(1_125_001, 10**10):
    res = check(num)
    if res:
        print(num, res)

        limit -= 1

        if limit == 0:
            break