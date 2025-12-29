# snake_case_hello_world
# camelCaseHelloWorld


# перевод из 10ой СС в систему счисления от 2 до 9

# перевод в 7ричную
# *args - неименованный аргумент, **kwargs - именованный аргумент
# def convertFrom10(num, to_base): # параметр - это локальная переменная
#     res = ''

#     while num > 0:
#         res += str(num%to_base)
#         num //= to_base

#     return ( res[::-1])


# print(convertFrom10(100, 2))
# print(convertFrom10(100, 3))
# print(convertFrom10(100, 8))

# def test(a, b, c):
#     return f"a = {a}, b = {b}, c = {c}"



# рекурсия

# последовательность Фибоначчи

# 1, 1, 2, 3, 5, 8, 13, 21, 34...
# 1  2  3  4  5  6  7   8   9 - n


# from functools import lru_cache


# @lru_cache
# def fibo(n): # n - НОМЕР элемента
#     if n <= 2:
#         return 1
    
#     return fibo(n - 1) + fibo(n - 2)


# for n in range(1, 100000):
#     print(f"{n}ое число Фибоначчи равно", fibo(n))


# print("done")



# сделать функцию удаляющую из текста слово


# def removeWordFromText(text: str, word: str):
#     return text.replace(word, '')



# print(removeWordFromText("hello hello fskjdbfnsdjk nfgkdjb gdfb gdfg", "hello"))

def summOf2Words(word1: str, word2: str):
    return word1 + " " + word2


print(summOf2Words(10, 10))


print("fsdfsdf".__add__("AAAAA"))