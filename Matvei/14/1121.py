for x in range(1, 10**6):
    num = 4**1014 - 2**x + 12

    if bin(num)[2:].count('0') == 2000:
        print(x)
        break