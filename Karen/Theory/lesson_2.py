# text = "Apple grape orange BANANA. How are you?"

# Строковые методы работают с ПОДСТРОКАМИ (1 и БОЛЕЕ символов)
# Все функции и методы имеют скобки (либо пустые, либо с параметрами внутри)

# print(text.upper()) # верхний регистр
# print(text.lower()) # нижний регистр
# print(text.count("A")) # посчитать количество подстрок в строке
# print(text.split()) # разбить строку по подстроке (умолчание - пробелы)
# print(text.split(" "))
# text = text.replace(" ", "_") # !!!!
# print(text.replace(" ", "_"))

# print(text.find("*")) # вернет индекс ПЕРВОГО вхождения в строке данной подстроки
# print(text.index("*"))



# ПРИМЕР


# Посчитать сколько в тексте букв A

# text = "aoifsdAIOUFNsdaflnsfojnISDJFNKSDF"

# print(text.count("a") + text.count("A")) # не лучший способ

# chaining - цепочка методов - применение методов один за другим
# работает слева направо!!!

# print(text.lower().count("a"))



# Срезы/slices



# Индексы - любой элемент строки можно получить
# по индексу (номеру буквы в строке)
# ОТСЧЕТ ИДЕТ С НУЛЯ !!!!!!!
# Индексы записываются к вадратных скобках
 
# Срезы - часть строки по правилу
# [start=0:stop:step=1] STOP не входит!!!
s = "0123456789ABCDEF"

print(s[:7]) # первые 7 символов
print(s[2:]) # начиная со 2ого и до конца

# 3456789AB
# ABCDE
# 01234
# 579B
# FC9
# print(s[3:12])
# print(s[10:-1])
# print(s[:5])
# print(s[5:12:2])
# print(s[-1:8:-3])



# # start=0, stop, step=1
# for i in range(5, 16, 1):
#     print(i)







s = "0123456789ABCDEF"

# 4567
# 0123456789AB
# 3456789ABCDEF
# 1234
# 3579
# ACE
# BDF