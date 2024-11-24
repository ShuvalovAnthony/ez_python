from functools import lru_cache

@lru_cache
def f(n):
    if n < 3: return 1
    elif n%2: return f(n - 1) + 3*f(n - 2)
    # summa = 0
    # for i in range(1, n):
    #     summa += f(i)
    # return summa
    return sum([f(i) for i in range(1, n)])
    

print(f(28))