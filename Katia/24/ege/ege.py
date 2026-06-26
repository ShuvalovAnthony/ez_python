from string import ascii_uppercase

f = open("Katia/24/ege/ege.txt").read()
original_f = f  # сохраняем оригинал, чтобы точно знать индексы символов

letters = {
    "CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4,
    "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1
}

# 1. Твоя очистка: убираем лишние буквы
valid_letters = "IVXLCDM"
for letter in ascii_uppercase:
    if letter not in valid_letters:
        f = f.replace(letter, ' ')

# Дополнительно убираем запрещенные повторения из условия задачи
for letter in "VLD":
    f = f.replace(letter * 2, ' ')  # V, L, D нельзя повторять
for letter in "IXCM":
    f = f.replace(letter * 4, ' ')  # I, X, C, M нельзя более 3 раз

# 2. Функция, которая проверяет одно слово из римских букв по твоему словарю
def check_and_sum(s):
    values = []
    i = 0
    while i < len(s):
        # Проверяем пары (CM, CD и т.д.)
        if i + 1 < len(s) and s[i:i+2] in letters:
            values.append(letters[s[i:i+2]])
            i += 2
        # Иначе берем одну букву
        else:
            values.append(letters[s[i]])
            i += 1
            
    # Твоя идея: проверяем, что всё идет по убыванию/равенству
    for k in range(len(values) - 1):
        if values[k] < values[k+1]:
            return None  # Порядок нарушен (например, после 10 идет 100 — ошибка)
            
    return sum(values)  # Возвращаем десятичное значение, если всё ок


# 3. Собираем ответ
max_len = 0
best_start_index = -1
min_decimal_value = float('inf')

# Бьем строку по пробелам на чистые слова из римских букв
for word in set(f.split()):
    dec_val = check_and_sum(word)
    
    if dec_val is not None:
        length = len(word)
        # Находим точную позицию слова в исходном файле (+1 для счета с 1)
        pos = original_f.find(word) + 1
        
        if length > max_len:
            max_len = length
            min_decimal_value = dec_val
            best_start_index = pos
        elif length == max_len:
            if dec_val < min_decimal_value:
                min_decimal_value = dec_val
                best_start_index = pos


print(f)