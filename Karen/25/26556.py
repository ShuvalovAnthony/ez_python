def prime(num: int):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def deliteli(num: int):
    prime_delit = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # first = i
            # second = num//i 

            if prime(i):
                prime_delit.add(i)
            if prime(num//i):
                prime_delit.add(num//i)

    if not prime_delit:
        return 0
    return max(prime_delit) + min(prime_delit)

limit = 5

for num in range(5_700_001, 10**10):
    m = deliteli(num)

    if (m > 70_000) and (m**0.5 == int(m**0.5)):
        print(num, m)

        limit -= 1

    if limit == 0:
        break
