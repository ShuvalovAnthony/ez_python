# Условная конструкция - это блоки из 1-3 инструкций
# Один if
# Сколько угодно elif
# Один else
# Из блока может быть ТОЛЬКО ОДИН выход


# if 
# elif
# elif...
# elif
# else
  
# if

# if
# else


# if
# elif
# elif


# text = "abab_____"

# if "a" in text:
#     print("a in text")
# if "b" in text:
#     print("a not in text and b in text")





# Проверьте, что число нечетное

# num = 235

# if num%2 != 0: # pythonic way
#     print(num, 'is odd')


# nums = [4234, 4235, 5436]

# if nums:
#     print(min(nums))


# print(any([5 > 3, True, 0 > 7])) # 5 > 3 or True or 0 > 7
# print(all([5 > 3, True, 0 > 7])) # 5 > 3 and True and 0 > 7



# Функции 

# def function_name(param_1, param_2):
#     # function_body

#     return



# def root_with_rounding(num, power):
#     return num**(1/power)


# print(root_with_rounding(27, 3))




# Пишем функцию суммирующую 2 числа


# def summa_dvuh(a, b):
#     return a + b


# # Если нужно сложить 3 число при помощи этой функции

# print(
#     summa_dvuh(5, summa_dvuh(6, 7))
# )


# Рекурсия 


# Последовательность Фибоначчи - первые два элемента это единицы, каждый следующий - сумма двух предыдущих

# 1, 1, 2, 3, 5, 8, 13, 21...

# from functools import lru_cache


# @lru_cache
# def fibo(n): # n - номер числа Фибо
#     if n <= 2:
#         return 1
    
#     return fibo(n - 1) + fibo(n - 2)


# for i in range(1, 1000):
#     # print(f"{i}ое число Фибоначчи равно", fibo(i))
#     ...

# print("done")



