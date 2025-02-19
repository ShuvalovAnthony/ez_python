for n in range(1000, 9999 + 1):
    str_n = str(n)
    summa_12 = int(str_n[0]) + int(str_n[1])
    summa_23 = int(str_n[1]) + int(str_n[2])
    summa_34 = int(str_n[2]) + int(str_n[3])

    summs = sorted([summa_12, summa_23, summa_34])

    res = str(summs[1]) + str(summs[2])

    if res == "1215":
        print(n)
        break