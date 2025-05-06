def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def primeDivs(num):
    primes = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # i - первый делитель
            if isPrime(i) and (i%1000 == 777):
                primes.add(i)
            # num//i - второй делитель
            if isPrime(num//i) and (num//i%1000 == 777):
                primes.add(num//i)
    
    if primes: return min(primes)
    return False



limit = 4

for num in range(55_000_001, 10**10):
    res = primeDivs(num)
    if res:
        print(num, res)

        limit -= 1

        if limit == 0:
            break