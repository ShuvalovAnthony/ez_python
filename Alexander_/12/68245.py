from itertools import product


def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True


res = []

for ones, twos, trees in product(range(20), repeat=3):
    a = '0' + '1'*ones + '2'*twos + '3'*trees + '0'

    while '00' not in a:
        a = a.replace('033', '21120', 1)
        a = a.replace('034', '22120', 1)
        a = a.replace('04', '220', 1)
        a = a.replace('030', '100', 1)

    if len(a) == 65:
        summa_cifr = sum([int(i) for i in a])
        if isPrime(summa_cifr):
            res.append(trees)
            
print(min(res))