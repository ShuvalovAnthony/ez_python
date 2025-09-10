from time import time

start = time()

def f(num: int):
    deliteli = set()

    for i in range(2, int(num**0.5) + 1):
        if num%i == 0:
            deliteli.add(i)
            deliteli.add(num//i)

    if len(deliteli) < 5: return 0

    deliteli = sorted(deliteli)
    return deliteli[-5]



limit = 1000

for num in range(46*10**10 + 1, 10**15):
    res = f(num)
    if res:
        # print(res)
        limit -= 1

    if not limit: break


print(time() - start)