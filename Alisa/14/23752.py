from string import digits, ascii_uppercase

# функция перевода в 27ричную
alph = digits + ascii_uppercase[:17]

def to_27(num: int):
    res = '' # любое число не в 10чной это строка

    while num > 0:
        res += alph[num%27]
        num //= 27

    return res[::-1]


# число которое дано в задаче
num = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561
# число в 27ричной (перевели при помощи функции)
num_27 = to_27(num)
# счетчик цифр с числовым значением больше 9
counter = 0

for digit in num_27:
    if digit not in "0123456789": # int(digit, 27) > 9 проверка
        counter += 1

print(counter)