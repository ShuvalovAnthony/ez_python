def check(num):
    deliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            # первый делитель i
            deliteli.add(i)
            # второй делитель - num//i
            deliteli.add(num//i)

    if deliteli: return sum(deliteli)
    return False



limit = 5


for num in range(500_001, 10**10):
    res = check(num)
    if res and (res%10 == 9):
        print(num, res)

        limit -= 1

        if limit == 0:
            break