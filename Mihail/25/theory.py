# все делители числа


def deliteli(num):
    dels = set()

    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            dels.add(i) # число до корня которые идут
            dels.add(num//i) # их пары

            if len(dels) == 6:
                return sorted(dels)[-3:]

    return sorted(dels)[-3:]




for num in range(10**9, 10**9 + 1000):
    print(deliteli(num))