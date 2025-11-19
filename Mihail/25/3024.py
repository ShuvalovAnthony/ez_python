def d(n):
    deliteli = set()

    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli.add(i)
            deliteli.add(n//i)

    if len(deliteli) < 6:
        return 0
    return sorted(deliteli)[-6]



limit = 5


for num in range(300_000_001, 10**9):
    res = d(num)

    if res > 0:
        print(num, res)
        limit -= 1

    if limit == 0: break