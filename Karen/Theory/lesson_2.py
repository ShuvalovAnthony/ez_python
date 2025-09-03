text = "Apple grape orange BANANA. How are you?"

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

