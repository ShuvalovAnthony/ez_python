def to_3(n: int):
    res = ''

    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]


res = []

for n in range(1, 1000): # int
    n_3 = to_3(n) # str

    if n%3 == 0:
        n_3 += n_3[-2:] # n_3 = n_3 + n_3[-2:]
    else:
        summa_cifr = sum([int(i) for i in n_3])
        n_3 += to_3(summa_cifr)

    r = int(n_3, 3)

    if (r%2 == 0) and (r > 220):
        res.append(r)

print(min(res))
