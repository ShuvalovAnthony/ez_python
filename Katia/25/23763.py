def m(n: int):
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return i + n//i
    
    return 0


limit = 5

for n in range(800_001, 10**10):
    res = m(n)
    if res%10 == 4:
        print(n, res)

        limit -= 1

    if limit == 0:
        break