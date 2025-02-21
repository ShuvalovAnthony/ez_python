from itertools import permutations, product

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0: return False
    return True


# 127 !!!!
res = set()
for ed, dv in product(range(100), range(100)):

    s = '0' + '1'*ed + '2'*dv
    summa_cifr_ishod = sum([int(i) for i in s])
    if len(s) > 40:
        while ('01' in s) or ('02' in s):
            s = s.replace('02', '1110', 1)
            s = s.replace('01', '220', 1)

        summa_cifr = sum([int(i) for i in s])


        if isPrime(summa_cifr):
            res.add(summa_cifr_ishod)

print(min(res))

