def f(start, stop):
    # если мы зашли за стоп (внимательно со знаком!!!)
    if (start < stop) or (start == 7): # не содержит 7 !!!
        return 0
    # пришли в нужное место
    elif start == stop:
        return 1


    
    # продолжаем движение (действия)
    # не забываем f и плюсы!!!!!!
    return (
        f(start - 1, stop) + # A. Вычесть 1
        f(start - 4, stop) + # B. Вычесть 4
        f(start//3, stop) # C. Найти целую часть от деления на 3
    )


print(f(19, 13)*f(13, 2))
