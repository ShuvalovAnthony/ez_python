# Списки list / array / massive
# [] list()
# списки - коллекции любых типов данных
# списки - изменяемый тип данных!!!!!!!!!!!!


# spisok = [1312, 534.5345, -234, 0, True, False, "Hello", [1, 2, 3]]

# print(spisok)

# nums = [-7, 8, 9, 0, 0, 0, -4, -2, 11]
# #       0   1  2  3  4   5    6
# # Списковые методы
# # print(nums.count(8))
# # print(nums)

# # nums.append(4)
# # # nums += [6] # ‼️☢️
# # nums.insert(3, 555)

# # nums.remove(0)

# # print(nums)
# nums = sorted(nums, reverse=True)

# print(nums)


# Двумерные массивы (матрицы)
# row col

board = [
#   ⬇️ - 0ой столб
    [1, 2, 3, 4, 5], # 0ая строка
    [11, 12, 13, 14, 15], # 1ая строка
    [21, 22, 23, 24, 25],
    [31, 32, 33, 34, 35],
    [41, 42, 43, 44, 45],
]

# 1 -> A
# 15 -> B
# 31 -> C
# 44 -> D
# 45 -> E
# 23 -> F
# 5 -> G
# 21 -> H

board[0][3] = "U"

for row in board: print(*row)






# Срезы/slices индексы

# s = "hello world"
#    01234...

# print(s[-2])



# range(start, stop, step) start - incl stop - excl step=1

# s = "0123456ABCDEFG"
#    0123456789....

# 0123456ABC
# 234
# 56ABC
# GFE
# 6420
# ACEG
# 036C
# FDB642

# EB52
# print(s[11:1:-3])
# print(s[-3:1:-3])


# 01234
# 6ABCDEFG
# 6BDF
# print(s[6::2])

# print(s[0:5:1])
# print(s[:5])


# num = "248344234" # -> "778344234"

# num = "77" + num[2:]

# print(num)