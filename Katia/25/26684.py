def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def primeDels(num):
    primeDeliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: # пара делителей
            if isPrime(i):
                primeDeliteli.add(i)
            if isPrime(num//i):
                primeDeliteli.add(num//i)
    
    return primeDeliteli


def check(num):
    if num%100 != 12:
        return False
    
    # initialNum = num
    primeDeliteli = primeDels(num)

    primeMnozh = []

    for delitel in primeDeliteli:
        while num%delitel == 0:
            primeMnozh.append(delitel)
            num //= delitel

    # proizvMnozh = 1
    # for mnozh in primeMnozh:
    #     proizvMnozh *= mnozh
    
    # if proizvMnozh != initialNum:
    #     return False

    for mnozh in sorted(set(primeMnozh)):
        if primeMnozh.count(mnozh) == 5:
            return mnozh
        
    return False


limit = 5

for num in range(5_000_001, 10**10):
    res = check(num)
    if res:
        print(num, res)
        limit -= 1

        if limit == 0:
            break