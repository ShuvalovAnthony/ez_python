def m(n):
    deliteli = set()
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli.add(i)
            deliteli.add(n//i)

        if len(deliteli) >= 10:
            return sorted(deliteli)[-5]
        
    if len(deliteli) < 5: return 0
    
    return sorted(deliteli)[-5]



limit = 5

for n in range(46*10**7 + 1, 10**10):
    res = m(n)
    if res > 0:
        print(res)
        limit -= 1

        if limit == 0:
            break

