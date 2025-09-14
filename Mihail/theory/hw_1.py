from string import digits, ascii_lowercase, punctuation, ascii_letters

# alph = digits + ascii_lowercase[:18]

# print(alph)

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo."
# count = 0

# # 1) Посчитать кол-во гласных в тексте
# spisok = "aoeyui"
# for letter in spisok:
#     count += text.lower().count(letter)
# # print(text.lower().count("a")) # chaining цепочка методов
# print(count)

# 2) Найти кол-во слов в тексте
# text = text.split()
# print(text)
# print(len(text))

# 3) Убрать все знаки препинания (есть несколько способов - подумай каким проще)

# spisok = [",", ".", "?", "!", ">", "<", "_", "-", ":", ";"]
# #
# for letter in text.lower():
#     if letter in spisok:
#         text = text.replace(letter, " ")
# print(text)

s = "QWERTY56789ASD0123"

# Получить следующие строки при помощи срезов:
# QWERTY56
print(s[:8])
# 9ASD01
print(s[-8:-2])
# QR58
print(s[0:11:3])
# Q
print(s[:1])
# SD0123
print(s[-6:-1])
# 31D
print(s[-1:-6:-2])
# WERTY56789ASD012
print(s[1:-1])

# print(s[::-1])



# Дан список чисел - заполнить параметры методов, чтобы получился следующий список
nums = [90, 78, 75, 55, 90]
nums.append(10)
nums.insert(1, 22)
nums.append(77)
nums.insert(4, 51)

print(nums)
[90, 22, 78, 75, 51, 55, 90, 10, 77]