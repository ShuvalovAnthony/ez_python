# https://pythonworld.ru/moduli/modul-itertools.html

# from itertools import permutations, combinations, product


# for word in combinations("ABC", r=3):
#     word = ''.join(word)
#     print(word)



# не содержит идущих подряд цифр

def check(num: str):
    for digit in num:
        if digit*2 in num:
            return False
        
    return True



# Число никогда не начинается с 0
# Но числа в 8ой задачи мы пишем как строки!!!
# поэтому проверка num[0] != '0'


# Алфавитный порядок - sorted("БУКВЫ") внутри product()


# Обязательно печатаем начало списка, чтобы сверить с условием!!!!