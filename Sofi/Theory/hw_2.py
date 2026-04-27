# Привет! Домашняя работа - 
# Написать следующие функции для проверки любой строки длиной 7 букв состоящей из букв "АБВГДЕЖ" на следующие условия:



# 1) Согласных букв больше, чем гласных

# def check(word: str):
#     for sogl in "БВГДЖ":
#         word = word.replace(sogl, "Б")
    
#     for glas in "АЕ":
#         word = word.replace(glas, "А")

#     return word.count("Б") > word.count("А")


# def check(word: str):
#     return (
#         (word.count("Б") + word.count("В") + 
#         word.count("Г") + word.count("Д") + 
#         word.count("Ж")) >
#         (word.count("А") +
#         word.count("Е"))
#     )




# 2) Строка начинается с гласной и в ней не более 3х согласных

# def check(word: str):
#     for sogl in "БВГДЖ":
#         word = word.replace(sogl, "Б")

#     return (word[0] in "АЕ") and (word.count("Б") <= 3)


# 3) В строке букв "А" меньше, чем согласных
# 4) Гласные и согласные буквы чередуются

def check(word: str):
    for sogl in "БВГДЖ":
        word = word.replace(sogl, "Б")
    
    for glas in "АЕ":
        word = word.replace(glas, "А")

    return ("АА" not in word) and ("ББ" not in word)


# 5) В строке только 1 согласная
# 6) В строке не более трех букв Г и одна гласная

# Написать функции, которые принимают на вход 2 целых числа - m и n и возвращают True если
# 1) m кратно n

# def check(m: int, n: int):
#     return m%n == 0


# 2) m является полным квадратом n

# def check(m: int, n: int):
#     return m == n**2

# 3) модуль разности m и n кратен 5
# def check(m: int, n: int):
#     return abs(m - n)%5 == 0

# 4) сумма m и n больше их произведения


# Это по желанию/если время будет:
# Написать функцию перевода числа из 10тиричной СС в 
# 1) 6тиричную СС
# 2) 14ти ричную СС