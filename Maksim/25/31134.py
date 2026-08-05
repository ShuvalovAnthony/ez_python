from functools import lru_cache



def isFiveSixSeven(num):
    return str(num).count('567') == 1

@lru_cache
def isPrime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            return False
    return True

def check(num):
    delit = set()
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            if isPrime(i):
                delit.add(i)
            if isPrime(num//i):
                delit.add(num//i)

    if len(delit) >= 2:
        return max(delit) + min(delit)
    return 0



limit = 5

for num in range(8_007_494_155, 10**10):
    m = check(num)
    if m and m > 80_000 and isPrime(m) and isFiveSixSeven(m) :
        print(num, m)
        limit -= 1
    if limit == 0:
        break

print(check(8007495062))