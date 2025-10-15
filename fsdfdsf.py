from time import time

start = time()


from functools import reduce as red
from itertools import combinations as com
from operator import mul


def f(n):
    s = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            s.append(i)
            n //= i
        i += 1
    if n > 1:
        s.append(n)
    d = []
    for i in range(1, len(s)):
        for j in com(s, r=i):
            m = red(mul, j)
            if m in d:
                continue
            d.append(m)
    return sorted(d)

s = 10e4 * 7 + 1
k = 0
while True:
    if k >= 5000:
        break
    q = f(s)
    if not q:
        s += 1
        continue
    m = min(q) + max(q)
    if m % 10 == 8:
        k += 1
        # print(int(s), int(m))
    s += 1


print(time() - start)