def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def deli(num):
    del1 = set()
    for i in range(2,int(num**0.5) + 1):
        if num%i == 0:
            del1.add(i)
            del1.add(num//i)
    
    for d in sorted(del1):
        if isPrime(d) and (d%1000 == 777) and (d != num):
            return d

limit = 0

for num in range(55_000_000,10**10):
    if deli(num):
        print(num,deli(num))
        limit += 1
        if limit == 4:
            break