def f(start, stop): # 
    if start == stop: return 1 #
    elif (start > stop) or (start == 35): 
        return 0 # где return 0 через or ИЗБЕГАЕМЫЙ ЭТАП

    moves = [
        f(start + 1, stop), #
        f(start + 2, stop),
        f(start*2, stop)
    ]

    return sum(moves) # возвращаем сумму ходов
                        # типичная ошибка - забываем слово sum  

# ОБЯЗАТЕЛЬНЫЕ этапы разбивают весь промежуток на отрезки
# от 7 до 51 включая числа 13 и 15
print(f(7, 13)*f(13, 15)*f(15, 51))