
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
    return num%2!=0


# 2) Является ли число полным квадратом

def check2(num):
    return int(num**0.5)==num**0.5


# 3) Сумма чисел в списке кратна 5


def check3(nums: list):
    return sum(nums)%5==0


# 4) Строка является палиндромом


def check4(s: str):
    return s == s[::-1]


# 5) Является ли список чисел неубывающим


def check5(nums: list):
    return nums == sorted(nums)

# print(check5([1, 2, 3, 3, 4, 5, 6, 6, 7]))

# 6) Является ли список чисел возрастающим


def check6(nums: list):
    return (nums == sorted(nums)) and (len(nums) == len(set(nums)))

def check6(nums: list):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False

    return True

# print(check6([1, 2, 3, 3, 4, 5, 6, 6, 7]))



# 7) Написать функцию перевода числа в 7ричную систему счисления
# функция возвращает строку - запись числа в 7ричной СС


def to_7(num):
    answer = ""

    while num != 0:
        answer += str(num%7)
        num = num//7
    
    return answer[::-1]


num = 42352347862354234872348
num_7 = to_7(num)

print(int(num_7, 7))