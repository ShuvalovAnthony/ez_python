from functools import lru_cache


@lru_cache
def f(n):
    if n == 0: return 0
    if n%2 == 0: return f(n//10) + n%10
    return f(n//10)


@lru_cache
def f2(n):
    n = str(n)
    for i in '3456789':
        if i in n: return 0
    return sum([int(i) for i in n if i in '2468'])


counter = 0

for k in range(10**9, 2*10**9 + 1):
    if f(k) == 2:
        counter += 1

    if k%10**6 == 0:
        print(k)

print(counter)
