def m(n):
    deliteli = {n}

    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli.add(i)
            deliteli.add(n//i)

    if len(deliteli) < 5: return 0

    proizved = 1
    for delit in sorted(deliteli)[:5]:
        proizved *= delit

    return proizved



limit = 5

for n in range(5*10**8 + 1, 10**10):
    res = m(n)
    if 0 < res < n:
        print(res)
        limit -= 1

        if limit == 0: break
    

