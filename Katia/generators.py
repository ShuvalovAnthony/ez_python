nums = [16, 57, 7, 3, 89, 27, 16, 20, 64, 44, 7, 89, 25, 53, 17, 52, 12, 44,
        67, 1, 88, 87, 21, 94, 61, 16, 90, 89, 57, 65, 35, 8, 99, 27, 97, 51,
        50, 89, 27, 76, 59, 21, 56, 84, 81, 15, 49, 47, 5, 169]


# Найти число оканчивающееся на 9 и являющееся полный квадратом
# 16 -> "16" -> "11231231236"[-1] -> "6" == "9"

# for num in nums:
#     if (
#         (num%10 == 9) and
#         (num**0.5 == int(num**0.5))
#     ):
#         print(num)
        



print([num**2 for num in nums if (num%10 == 9 and num**0.5 == int(num**0.5))])


# # найти самое длинное слово в тексте
# def find_longest_word(text: str):
#     return max([len(word) for word in text.split()])
    


# text = "Abc abbbc abbbbbbc qwertyqwert"

# print(find_longest_word(text)) # -> qwertyqwert


# найти наибольший общий делитель
# def greatest_common_divisor(num1: int, num2: int):
#     for i in range(min(num1, num2), 0, -1):
#         if (num1%i == 0) and (num2%i == 0):
#             return i

# print(greatest_common_divisor(17, 7)) # -> 6
