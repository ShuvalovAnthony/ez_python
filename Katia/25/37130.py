def check(n):
    deliteli_ok_na_7 = set()

    for i in range(2, int(n**0.5) + 1):
        if i == 7: continue

        if (n%i == 0): # нашли пару делителей и для каждого!! из них проверяем условия
            if i%10 == 7: deliteli_ok_na_7.add(i)
            if (n//i)%10 == 7: deliteli_ok_na_7.add(n//i)

    if not len(deliteli_ok_na_7): return False
    return min(deliteli_ok_na_7)


limit = 5

for n in range(6*10**5, 10**8):
    res = check(n)
    if res:
        print(n, res)
        limit -= 1

        if not limit:
            break