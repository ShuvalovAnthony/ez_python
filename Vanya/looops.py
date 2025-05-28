# Циклы
# while
# for

# nums = [1, 2, 3, 4, 5, 6, 7]

# while nums:
#     print(nums)

#     nums = nums[1:]


# s = "GIJNgjksgndfgIOGFNG gf sg2343"
# nums = [-5, 6, 7, -1, 2, 0]
# r = range(10, 100, 6)

# coords = [
#     (1, 2),
#     (5, 7),
#     (0, 4),
#     (6, 8)
# ]

# for x, y in coords:
#     print(x, y)



text = """Привет привет привет как дела? Что делаешь? Что делаешь? Кошка и две собаки, попугай, еще кошка и собака.
Очень сильно Никита просит побольше домашней работы и еще Никита хочет делать двойное сальто."""

ban_list = ["привет", "кошка"]

# Посчитать кол-во слов, в которых гласных столько же сколько согласных
# Удалить все слова из бан листа
# Посчитать количество слов в предложении
# Посчитать количество знаков препинания
# Посчитать количество предложений
# Заменить слова из бан листа на *%^&#
# Записать весь текст задом наперед (слова идут в обратном порядке) без знаков препинания
# Выписать все слова, которые начинаются с заглавной буквы



# РЕШЕНИЕ

# for symb in "?.!":
#     text = text.replace(symb, '')

# words = text.split()


# counter = 0

# for word in words:
#     counter_glas = 0
#     for glas in "аоеуиэюяы":
#         counter_glas += word.lower().count(glas)

#     if (len(word)%2 == 0) and (len(word)//2 == counter_glas):
#         counter += 1

    
# print(counter)







# for n in range(4, 10000):
#     s = "1" + "9"*n

#     while ("19" in s) or ("399" in s) or ("999" in s):
#         if "19" in s:
#             s = s.replace("19", "9", 1)
#         if "399" in s:
#             s = s.replace("399", "91", 1)
#         if "999" in s:
#             s = s.replace("999", "3", 1)

#     summa_cifr = sum([int(i) for i in s])

#     if summa_cifr == 33:
#         print(n)
#         break
    




