from string import digits, ascii_uppercase
from sys import set_int_max_str_digits

set_int_max_str_digits(10**5)


def convert(num: str, from_base: int, to_base: int):
    alph = digits + ascii_uppercase

    num_10 = int(num, from_base)

    res = ''

    while num_10 > 0:
        res += alph[num_10%to_base]
        num_10 //= to_base

    return res[::-1]


num = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561


res = convert(
        str(num), 10, 27
        )

count = 0

for i in res:
    if int(i, 27) > 9:
        count += 1

print(count)