def summaDel(num: int):
    deliteli = set()

    for i in range(1, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    return sum(deliteli)


def sumdiv(n):
    return sum(i for i in range(1, n + 1)
               if n % i == 0)


def f(start, stop):
    if start == stop: return 1

    if start > stop: return 0

    moves = [
        f(start + 1, stop),
        f(summaDel(start), stop)
    ]

    return sum(moves)


print(f(2, 24))
