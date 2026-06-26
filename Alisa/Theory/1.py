# Типы данных

# 1) int, float - целые и вещественные числа (числа с плавающей точкой)

# +, -, *  как в математике

# деление - 
# / обычное деление
# // - целочисленное деление
# % остаток от деления


# ** возведение в степень/ в том числе извлечение корня степени n


# приведение типов/type casting



# 2) строки/string/str
# записываются в кавычках одинарных или двойных
# неизменяемый тип‼️‼️

# s = "Hello world! 12345"

# + строки можно сложить (слепить) - конкатенация
# * строки можно умножить


# Функция - дейтсвие над объектом
# print()
# int()
# len()
# range()

# Метод - это функция, которая работает ТОЛЬКО с определенным типом данных


# feed(cat) - функция
# feed(dog) - функция


# cat.meow() - метод
# dog.bark() - метод


# Строковые методы - функции, которые работают ТОЛЬКО со строками

# text = "HHHHHHHHELLO world! 12345"
#       01234
# 1) .lower() .upper() нижний/верхний регистр
# print(text.lower())
# print(text)

# 2) .find() .index()

# print(text.find("Q")) мы используем find()
# print(text.index("Q"))

# 3) .replace()

# print(text.replace("H", "_", 1))

# 4) .count() - посчитать количество ПОДСТРОК в строке

# text = "ABAAAABBBB abababab world! 12345"
# # посчитать сколько в тексте буква A и B
# print(text.count("A") + text.count("B") + text.count("a") + text.count("b"))

# # chaining - цепочка методов
# # методы выполняются СЛЕВА НАПРАВО

# print(text.upper().count("A") + text.upper().count("B"))

# text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo."

# 5) .split() - разделить строку по подстроке

# print(text.split())
# print(len(text.split(" ")))


s = 'ABC'

print(s.zfill(50))