# Домашняя работа

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean vulputate est vitae purus consequat commodo."

# 1) Посчитать кол-во гласных в тексте
# 2) Найти кол-во слов в тексте
# 3) Убрать все знаки препинания (есть несколько способов - подумай каким проще)


# print(text.lower().count("a") + text.lower().count("e") + text.lower().count("y") + text.lower().count("u") + text.lower().count("o") + text.lower().count("i"))
# print(len(text.split()))
# text = text.replace(".", "").replace(",", "")
# print(text)


s = "QWERTY56789ASD0123"

# Получить следующие строки при помощи срезов:
# QWERTY56
# 9ASD01
# QR58
# Q
# SD0123
# 31D
# WERTY56789ASD012

print(s[::-1])