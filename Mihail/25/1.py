def isPrime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True


def check(num):
    mnozh = []

    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            if isPrime(i) and str(i).count("1") == 1:
                mnozh.append(i)
            if isPrime(num//i) and str(num//i).count("1") == 1:
                mnozh.append(num//i)

    if len(mnozh) == 3:
        return max(mnozh)
    return False


limit = 5

for num in range(15_381_264, 10**10):
    res = check(num)
    if res:
        print(num, res)
        limit -= 1

    if limit == 0:
        break