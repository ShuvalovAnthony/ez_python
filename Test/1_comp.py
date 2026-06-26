# Перечислить основные типы данных, написать какие из них изменяемые и какие неизменяемые


text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo."

# 1) Посчитать кол-во гласных в тексте
# counter = 0

# for letter in "aeyuio":
#     counter += text.lower().count(letter)

# print(counter)


# 2) Найти кол-во слов в тексте
# print(len(text.split()))


# 3) Убрать все знаки препинания (есть несколько способов - подумай каким проще)

# for sign in ",.:/!@*":
#     text = "Lorem ipsum dolor sit amet consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo.".replace(sign, '')

# print(text)


s = "QWERTY56789ASD0123"

# # Получить следующие строки при помощи срезов:
# # QWERTY56
# # 9ASD01
# # QR58
# # Q

# print(s[8:])



# Дан список чисел - заполнить параметры методов, чтобы получился следующий список
# [90, 78, 75, 55, 90, 12, 34]
# nums = [90, 78, 75, 55, 90]
# nums.append(12)
# nums.append(34)

# print(nums)

# # Отсортировать список по возрастанию


# # Имеется список покупок
# basket = ["apple", "banana", "orange", "apple", "kiwi", "banana", "banana"]
# print(basket, set(basket))
# # Выведи количество (!) уникальных фруктов в корзине
# # Добавь в этот список "pineapple" и удали из списка дубли (конечный тип данных - list)



# Вывести 1ую, 2ую, 3юю цифры трехзначного числа не используя строки, а только
# математические операции
# + - * ** / // %
# num = 587

# print(num//100)
# print(num//10%10)
# print(num%10)


# # Написать функцию перевода из 10ой в 7ую СС

# def to_7(num):
#     ...


# # Написать функцию, которая проверяет является ли число простым

# def isPrime(num):
#     ...