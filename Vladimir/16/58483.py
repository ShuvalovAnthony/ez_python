from functools import lru_cache


@lru_cache
def f(n):
    if n > 10**6: return n
    return (n + f(2*n))

@lru_cache
def g(n):
    return f(n)/n


counter = 0

for n in range(1, 3000):
    if g(n) == g(1000):
        counter += 1
        print(n)

print(counter)