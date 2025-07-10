from functools import lru_cache

@lru_cache()
def prime(n:int):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True

@lru_cache()
def all_delit(n:int):
    deliteli = []
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            deliteli += [i, n//i]
    return sorted(set(deliteli))

@lru_cache()
def prime_mnozh(n:int):
    prime_delit = []
    for delitel in all_delit(n):
        if prime(delitel): prime_delit.append(delitel)
    return prime_delit

@lru_cache()
def check(num: int):
    answ = []
    primes_counter = 0
    for mnozh in prime_mnozh(num):
        while num%mnozh == 0:
            primes_counter += 1
            num //= mnozh
            if (str(mnozh).count('1') == 1):
                answ.append(mnozh)
    if (len(answ) == 3) and (primes_counter == 3):
        return max(answ)
    return False



limit = 5

for num in range(15_381_265, 10**10):
    res = check(num)
    if res:
        print(num, res)

        limit -= 1
        if limit == 0:
            break