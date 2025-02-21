for n in range(4, 10**4):
    s = "5" + "2"*n
    
    while ("52" in s) or ("1122" in s) or ('2222' in s):
        if '52' in s:
            s = s.replace('52', '11', 1)
        if '2222' in s:
            s = s.replace('2222', '5', 1)
        if '1122' in s:
            s = s.replace('1122', '25', 1)

    summa_cifr = sum([int(i) for i in s])

    if summa_cifr == 64:
        print(n)