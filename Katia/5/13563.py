def check(n):
    for digit in str(n):
        if digit in "02468":
            return False
    return True


counter = 0

for n in range(1000, 10000):
    if not check(n): continue

    n = str(n)

    summa_12 = int(n[0]) + int(n[1])
    summa_34 = int(n[2]) + int(n[3])

    if summa_12 > summa_34:
        res = str(summa_34) + str(summa_12)
    else:
        res = str(summa_12) + str(summa_34)

    if res == "616":
        counter += 1

print(counter)



