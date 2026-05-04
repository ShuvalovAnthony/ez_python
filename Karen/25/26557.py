def isPrime(num):
    for i in range(2, int(num**.5) + 1):
        if num%i == 0:
            return False
    return True


def m(num):
    primeDels = []

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            if isPrime(i):
                primeDels.append(i)

            if isPrime(num//i):
                primeDels.append(num//i)

    if not primeDels:
        return False

    min_plus_max = min(primeDels) + max(primeDels)

    if (
        ((min_plus_max)%len(set(primeDels)) == 0) and
        (min_plus_max%100 == 63)
    ):
        return min_plus_max
    
    return False

limit = 5

for num in range(7_800_001, 10**10):
    res = m(num)

    if res:
        print(num, res)
        limit -= 1

    if limit == 0:
        break