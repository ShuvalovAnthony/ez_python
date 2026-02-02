def deliteli(num: int):
    delit = set()

    for i in range(1, int(num**0.5) + 1): # 1264537489234235345
        if num%i == 0:
            delit.add(i)
            delit.add(num//i)

    return delit



print(deliteli(1234567890))
