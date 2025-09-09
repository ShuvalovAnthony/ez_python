for i in [638, 442, 357, 123]:
    summa_cifr = sum([int(i) for i in str(i)]) # ВЫУЧИТЬ!!!!

    if (
        (not (i//100%2 == 0)) and (summa_cifr%2 == 0)
    ):
        print(i)