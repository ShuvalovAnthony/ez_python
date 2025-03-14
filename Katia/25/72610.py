def m(n):
    deliteli = set()

    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            deliteli.add(i)
            deliteli.add(n//i)
        
        if len(deliteli) >= 4:
            return sum(sorted(deliteli)[-2:])%10000 == 1214

    if len(deliteli) < 2: return 0

    return sum(sorted(deliteli)[-2:])%10000 == 1214


for n in range(112_500_000, 112_550_000 + 1):
    if m(n):
        print(n)