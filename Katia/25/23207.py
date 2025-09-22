def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
        
    return True


def cont_only_one_5(n):
    return str(n).count('5') == 1


def check(n: int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            mnozh1 = i
            mnozh2 = n//i

            if (
                isPrime(mnozh1) and isPrime(mnozh2) and
                cont_only_one_5(mnozh1) and cont_only_one_5(mnozh2)
            ):
                return mnozh2
            
    return False


limit = 5

for n in range(1_324_728, 10**10):
    res = check(n)
    if res:
        print(n, res)
        limit -= 1

    if limit == 0:
        break