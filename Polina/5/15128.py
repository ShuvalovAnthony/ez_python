for n in range(9999, 999, -1):
    n = str(n) # "1234"

    summa_12 = int(n[0]) + int(n[1])
    summa_23 = int(n[1]) + int(n[2])
    summa_34 = int(n[2]) + int(n[3])

    summi = sorted([summa_12, summa_23, summa_34])[1:]

    res = str(summi[0]) + str(summi[1])

    if res == "1315":
        print(n)
        break