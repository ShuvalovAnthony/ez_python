def f(num):
    deliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    return sum(deliteli)


limit = 5


for num in range(500_001, 10**10):
    res = f(num)
    if res%10 == 9:
        print(num, res)
        limit -= 1

        if limit == 0:
            break
