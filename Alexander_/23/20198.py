from functools import lru_cache


@lru_cache
def f(start, stop, k):
    if (start > stop) or (k > 3): return 0
    if start == stop: return 1

    moves = [f(start + 5, stop, 0),
             f(start * 2, stop, 0),
             f(start -1, stop, k + 1)
             ]

    return(sum(moves))

for i in range(34):
    f(1, 34)



print(f(5, 34, 0))



