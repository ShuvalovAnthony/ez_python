for y in range(7):
    for x in range(7):
        left = int(str(y) + str(x) + "320", 7)
        right = int("1" + str(x) + '3' + str(y) + '3', 9)
        summa = left + right
        if summa%181 == 0:
            print(summa//181)
