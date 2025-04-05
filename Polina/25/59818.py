from fnmatch import fnmatch


def delit(n):
    deliteli = set()
    for i in range(1, int(n**0.5) + 1):
        if n%i == 0:
            deliteli.add(i)
            deliteli.add(n//i)

    for i in range(15):
        if len(deliteli) == 2**i:
            return True
    return False




for n in range(2031, 10**9 + 1, 2031):
    if (n%31 == 0) and fnmatch(str(n), "*31*65?") and delit(n):
        print(n, n//2031)



