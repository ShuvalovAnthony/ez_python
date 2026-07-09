# дано число - посчитать количество цифр, с числовым значением больше 4 в
# 16ти ричной системе счисления 

# 0123456789 ABCDEF


# fruits = []

# while True:
#     fruit = input("Введите фрукт: ")
    
#     if fruit == '0':
#         break

#     if fruit not in fruits:
#         fruits.append(fruit)

# print(fruits)


# for i in range(10):
#     for j in range(10):
#         print('i=', i, 'j=', j)


# написать цикл, который напечатает все числа, кратные 123456
# в промежутке от 10^10 до 2*10^10

# cmd+c
# for num in range(10000059456, 2*10**10 + 1, 123456):
#     print(num)
    



num = 789236
# num_hard = 9346573451234234

# дано число, необходимо найти:
# 1) сумму его цифр
# 2) все делители числа
# 3) простые множители числа
# задача посложнее - все тоже самое, с числом num_hard


# sum_cifr = 0

# for digit in str(num):
#     sum_cifr += int(digit)

# print(sum_cifr)

# deliteli = set()

# for i in range(1, int(num**0.5) + 1):
#     if num%i == 0:
#         deliteli.add(i)
#         deliteli.add(num//i)

# print(deliteli)


# def isPrime(num):
#     for i in range(2, int(num**0.5) + 1):
#         if num%i == 0:
#             return False
#     return True


# primeMnozh = set()

# for i in range(1, int(num**0.5) + 1):
#     if num%i == 0:
#         if isPrime(i)
#         primeMnozh.add(i)
#         primeMnozh.add(num//i)





# на вход будет подаваться 6 натуральных чисел через пробел
# они сохраняются в список nums (заранее неизвестны - я буду вводить любые
# ты для теста тоже можешь по 6 любых чисел вводить)

nums = [int(i) for i in input().split()] 

# print(nums)

# если одновременно выполняются все 3 условия - напечатать YES
# если нет - NO
# условия:
# 1) в списке есть повторяющиеся числа
# 2) в списке количество четных и количество нечетных чисел равно
# 3) в списке ровно 3 двузначных числа

# для пункта 2

def check2(nums):
    chet = 0
    nechet = 0

    for num in nums:
        if num%2 == 0:
            chet += 1
        else:
            nechet += 1
    
    return chet == nechet


# для пункта 3

def check3(nums):
    kolvo_dvuznach = 0

    for num in nums:
        if 10 <= num <= 99:
            kolvo_dvuznach += 1
    
    return kolvo_dvuznach == 2
        

if (
    (len(nums) != len(set(nums))) and
    check2(nums) and
    check3(nums)
):
    print("YES")
else:
    print("NO")