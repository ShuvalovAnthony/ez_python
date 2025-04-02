for n in range(100, 1000):
    n = str(n)

    summa_12 = int(n[0]) + int(n[1])
    summa_23 = int(n[1]) + int(n[2])

    summi = sorted([summa_12, summa_23])

    res = str(summi[0]) + str(summi[1])

    if res == "812":
        print(n)
        break