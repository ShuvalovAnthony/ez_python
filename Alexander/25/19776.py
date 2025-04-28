def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: return False
    return True


def check(num):
    deliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            if isPrime(i): deliteli.add(i)
            if isPrime(num//i): deliteli.add(num//i)

    if len(deliteli) >= 2: return min(deliteli) + max(deliteli)
    return 0



limit = 6


for num in range(23_600_001, 10**10):
    m = check(num)
    if m and (m%213 == 171):
        print(num, m)

        limit -= 1

        if limit == 0:
            break