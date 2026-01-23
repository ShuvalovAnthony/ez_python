# сначала просто берем все слова
str_1 = input()
str_2 = input()
str_3 = input()

# соединяем все слова и при помощи set() удаляем повторы
# это будет просто кортеж (список) всех букв
all_letters = set(str_1 + str_2 + str_3)

# здесь будет строка для ответа со всеми буквами
res = ''

# перебираем все буквы
for letter in all_letters:
    # counter - сколько слов содержит эту букву
    counter = (
        # letter in str_1 - вернет либо True, либо False
        # обернув в int мы делаем True единицей, False - нулем
        # таким образом мы просто посчитаем, сколько раз было True
        int(letter in str_1) +
        int(letter in str_2) +
        int(letter in str_3)
    )

    # если количество слов содержащих букву хотя бы 2
    # добавляем эту букву в ответ
    if counter >= 2:
        res += letter

print(res)

