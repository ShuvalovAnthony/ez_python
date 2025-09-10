# function - функции

# Функция это кусок кода, который можно переиспользовать
# функции в программировании имеют как общие черты с мат функциями
# так и сильные различия


# def to_3(n):
#     res = ''

#     while n > 0:
#         res += str(n)
#         n //= 3
    
#     return res[::-1]


# for n in range(1, 1000):
#     tri_n = to_3(n)

#     if n%3 == 0:
#         ...
#     else:
#         tri_n += to_3(n%3 * 5)




# Дают текст, надо убрать из него запрещенные слова

# def - создать функцию
# def ИМЯ_ФУНКЦИИ(ПАРАМЕТРЫ_ФУНКЦИИ):
#     ТЕЛО_ФУНКЦИИ

# def banWordsInText(text: str, banList: list):
#     for banWord in banList:
#         text = text.replace(banWord, '')
#     return text


# print(banWordsInText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo.", ["sit", "amet", "durak"]))

# print(banWordsInText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo.", ["elit", "consectetur", "purus"]))


# print(banWordsInText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo.", ["Aenean", "vulputate", "vitae"]))



# тривиальные делители - включая 1 и само число
# для поиска нетривиальных (кроме 1 и числа) 
# в range() стартуем c 2
def deliteli(n: int):
    delit = {1}

    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            delit.add(i)
            delit.add(n//i)

        if len(delit) >= 10:
            break

    max_five = sorted(delit)[-5:]

    if len(max_five) != 5:
        return 0

    return sum(max_five)



limit = 7

for num in range(4_000_001, 10**16):
    res = deliteli(num)

    if (res%10 == 0) and (res > 0):
        print(num, res)

        limit -= 1

    if limit == 0:
        break