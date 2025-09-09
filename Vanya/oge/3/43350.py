for x in range(100, 1000): # трехзначные числа
    if (
        (not (x//100%2 == 1)) and (not (x%3 == 0))
    ):
        print(x)