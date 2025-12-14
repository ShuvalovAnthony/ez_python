# типы данных

# числовые
# int целые числа
# float вещественные/с плавающей точкой МЫ СТАРАЕМСЯ НИКОГДА НЕ ИСПОЛЬЗОВАТЬ float

# действия с числами

# + - * - сложение вычитание умножение

# ** возведение в степень
# print(2**3)

# # деление
# 1) / обычное
# 2) // целочисленное (отбрасывается дробная часть БЕЗ ОКРУГЛЕНИЯ)
# 3) % остаток от деления modulo
# модуль числа abs()

# num_of_teams = 5

# for i in range(100, 145):
#     print(i, i%num_of_teams)


# корень n степени
# print(81**0.25)

# приведение типов - при делении и возведении в дробную степень результат всегда float

# num = 234234
# bin_num = bin(num)[2:]

# print(bin_num, type(bin_num))


# bool - логический тип
# True и 1 одно и тоже
# False и 0 также


# коллекции

# str - строки (записываются в "", '')

# print("Толстой \"Война и мир\"")

# list, tuple, set, dict списки кортежи множества и словари



# Строковый тип - string
# ‼️‼️‼️СТРОКИ ЭТО НЕИЗМЕНЯЕМЫЙ ТИП‼️‼️‼️


# функции и методы
# методы - это функции, применимые только к определенному классу


# cat = Cat()
# dog = Dog()


# feed(cat)
# feed(dog)


# cat.meow()
# dog.bark()


# Строковые методы

# text = "Hello world 123456 hello hello FSDNMFJK"
# верхний/нижний регистр

# print(text.upper())
# print(text.lower())

# print(text)

# считаем кол-во подстрок в строке
# print(text.count("l"))

# посчитать количество h в строке

# print(text.count("h") + text.count("H"))
# print(text.lower().count("h")) # chaining/цепочка методов

# элемент строки можно взять по его индексу (начиная с 0 !!!) в том числе и отрицательному
# print(text[-3])
# индекс первого вхождения подстроки
# print(text.find("&"))
# print(text.index("&"))


# проверка наличия подстроки в строке

# ПЛОХОЙ СПОСОБ (никогда так не делаем)
# if text.find("h") >= 0:
#     print("YES")

# if "&" in text:
#     print("YES")

# text = "Hello world 123456 hello asdas hello FSDNMFJK"

# # заменить подстроку в строке на другую подстроку
# # print(text.replace("o", "_", 3))

# # разбить строку по разделителю -> результат список подстрок

# print(text.split())
# print(text.split(" ")) # НИКОГДА НЕ ИСПОЛЬЗУЕМ ЕСЛИ НЕ ПОНИМАЕМ ТОЧНО ЗАЧЕМ

# print(text.split("hello"))

# соединить список строк по разделителю

# words = ["apple", 'banan', 'leaf', 'orange']

# print(" ".join(words))


# срезы = [start:stop:step] STOP не входит!!!!!!!


s = "0123456789ABCDEFGHIJKL"


# print(s[5])


# 012345
# 456789ABCDEFG
# CDEFG
# EFGHIJKL
# 2468
# KIGE

# print(s[:6])
# print(s[4:-5])
# print(s[12:-5])
# print(s[14:]) # print(s[-8:])
# print(s[2:10:2])
# print(s[-2:-10:-2])


# перевод из 10ой в 2ую 8ричную и 16ричную

num = 234535

print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:])


# сумма цифр в двоичном числе - колво единиц

print(bin(num)[2:].count("1"))

# сумма цифр в любом числе до 10тиричной СС включительно

oct_num = oct(num)[2:]



sum_cifr = sum([int(i) for i in oct_num])

# summa_cifr = 0
# for i in oct_num:
#     summa_cifr += int(i)


print(sum_cifr)