# Завершить следующие функции проверки
# все функции возвращают либо True либо False

# Пример 1 - функция, проверяющая, можно ли
# составить треугольник из 3х заданных сторон

def is_triangle(a, b, c):
    a, b, c = sorted([a, b, c]) # распологаем a, b, c по возрастани
    # чтобы не делать много условий
    return a + b > c # проверяем, что сумма длин двух коротких сторон больше длинной


# Является ли число четным (пример 2)

def isEven(num):
    return num%2 == 0


# 1) Оканчивается ли число на нечетную цифру

def check1(num):
    return (num%10)%2!=0

# print(check1(12312))

# 2) Является ли число полным квадратом


def check2(num):
    return (num**0.5)%1==0 # int(num**0.5) == num**0.5

# print(check2(65))


# 3) Сумма чисел в списке кратна 5


def check3(nums: list):
    return sum(nums)%5 == 0


# 4) Строка является палиндромом


def check4(s: str):
    return s == s[::-1]

# print(check4("aboba"))

# 5) Является ли список чисел неубывающим


# def check5(nums: list):
#     return sorted(nums)==nums

# print(check5([1, 2, 3, 4, 4, 5]))

# 6) Является ли список чисел возрастающим


# def check6(nums: list):
#     return (sorted(nums) == nums) and (len(nums) == len(set(nums)))


# def check6(nums: list):
#     for i in range(len(nums) - 1):
#         if nums[i + 1] <= nums[i]:
#             return False

#     return True

# print(check6([1, 2, 3, 3, 4, 5]))



# 7) Написать функцию перевода числа в 7ричную систему счисления
# функция возвращает строку - запись числа в 7ричной СС


def to_7(num):
    res=''
    while num>0:
        res+=str(num%7)
        num//=7

    return res[::-1]