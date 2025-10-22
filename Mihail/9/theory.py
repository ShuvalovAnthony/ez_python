f = "FILE"

# # одномерный массив
# nums = [1, 2, 3, 4, 5]
# nums = [int(i) for i in f]


# двумерный массив
# data = [
#     [1, 2, 3],
#     [5, 6, 7],
#     [8, 9, 0]
# ]

# data = [
#     [int(i) for i in row.split()] for row in f
# ]






row = [5, 9, 0, 5, 13, 2, 3, 3] # 8 элементов

# 1) все числа в строке уникальны
len(row) == len(set(row))


# 2) все числа по возрастанию/убыванию
sorted_row = sorted(row)

sorted_row == row # начальная УЖЕ была по возрастанию


# 3) в строке есть два числа, повторяющихся дважды
povtor = []

for num in row:
    if row.count(num) == 2:
        povtor.append(num)

len(povtor) == 4


# 4) произведение всех повторяющихся чисел строки
# более чем вдвое превосходит произведение неповторяющихся чисел

povtor = [1, 1, 5, 5, 5, 7, 7]
uniq = [9, 0, 2, 4]

povtor_mult = 1
uniq_mult = 1

for num in povtor_mult:
    povtor_mult *= num


#5) оканчиваются на цифру 5
num = 4567
str(num)=[-1] == "5"
num%10 == 5


# abs() модуль - если нужно взять остаток/трех значное число

# 6) число является трехзначным
100 <= abs(num) <= 999
abs(num) in range(100, 1000)
len(str(abs(num))) == 3

# 7) максимальное число не повторяется
max(row) not in povtor # список povtor сделаешь заранее
row.count(max(row)) == 1



# 7) максимум меньше суммы трех других
row = [1, 2, 3, 4]

max(row) < sum(row) - max(row)

sorted_row = sorted(row)
sorted_row[-1] < sum(sorted_row[:3])