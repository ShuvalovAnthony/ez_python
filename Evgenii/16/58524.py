from functools import lru_cache


@lru_cache
def f(n):
    if n > 10**6: return n
    return n + f(2*n)


def g(n):
    return f(n)/n


res = g(2000)

counter = 0


for n in range(1, 10**6):
    if g(n) == res:
        counter += 1

    # if n%10**6 == 0:
    #     print(n)

print(counter)