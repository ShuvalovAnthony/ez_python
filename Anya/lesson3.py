# Циклы
# Условия


# a = 1

# while True:
#     print(a)
#     a += 1
#     if a == 10:
#         break

# for - итератор (цикл который проходит по итерируемым объектам - коллекциям)

# text = "Hello"
# nums = [1, 2, 3, 4, [1, 2, 3], "hello"]
# range_ = range(1, 15, 4)


# for el in range_:
#     print(el)


# range(105, 1000, 7)

# from itertools import product, combinations, permutations


# for left, right in product("ABCDEF", "012345"):
#     print(left, right)

#     if right == "2": break


# data = [
#     # x y z
#     (0, -7, 9),
#     (-5, 4, 8),
#     (11, 9, -3)
# ]

# for x, y, z in data:
#     print(x, y, z)


text = "Hello world banana good Apple bad day weather Tomato city"

# Вывести все слова по отдельности 1
# Вывести слова, в которых гласных букв, больше либо равно, чем согласных✅
# Посчитать количество слов, начинающихся с заглавной буквы 3
# Посчитать количество слов, в которых меньше 5 букв 2
# Заменить слова из бан листа на ***** 4

words = text.split()

for word in words:
    first_letter = word[0]
    if first_letter == first_letter.upper():
        print(word)


    # # Посчитать количество гласных
    # # Посчитать кол-во согласных
    # # Сравнить

    # count_glas = 0

    # for glas in "aeyuio":
    #     count_glas += word.lower().count(glas)
    # # 2 sposob
    # # for letter in word:
    # #     if letter in "aeyuioAEYUIO":
    # #         count_glas += 1

    # if count_glas >= len(word)/2:
    #     print(word)




