text = 'Hello world ABCdefg 0123456789' # str строка string


# print(text.upper())
# print(text.lower())
# print(text.count("o"))

# text = "AaaaAaaaAAAABCDEFbcd"

# посчитать все буквы A
# print(text.count("A") + text.count("a"))
# print(text.upper().count("A")) # chaining / цепочка методов
# text = text.replace("d", "D")
# print(text.replace("BCD", "___"))
# print(text.replace("a", "😁"))
# print(text)

# len() - функция подсчета элементов в коллекциях
# text = "abc ABC          qwe QEW 123 444"
# words = text.split()
# print(len(text))
# print(len(words))
# print(words)

# text2 = "AbAAAAbAAAA b b AAAA bAAA"
# words2 = text2.split("b")
# print(words2)
# print(len(words2))


# срезы

s = "0123456789ABCDEF"

# print(s[start:stop:step]) # 
# :stop - с самого начала
# start: - до конца
# stop - НЕ включается

# 012345
# print(s[:6])

# s = "0123456789ABCDEF"
# # 456789AB
# print(s[4:12])

# # 23456
# print(s[2:7])

# 13579B
# print(s[1:12:2])


# s = "0123456789ABCDEF"
# # CDEF
# print(s[12:])


# s = "0123456789ABCDEF"
# CDEF
# print(s[-4:])

