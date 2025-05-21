# # списки list


# # nums = [-2, 3, 5, -4, 7, 1, 0, -5, 3, 3]
# # # print(nums[3])

# # # print(nums.count(3))

# # nums.append(77)
# # nums.insert(3, 555)

# # nums = sorted(nums, reverse=True)

# # print(nums)


# board = [
#     ["A1", "B1", "C1", "D1", "E1"],
#     ["A2", "B2", "C2", "D2", "E2"],
#     ["A3", "B3", "C3", "D3", "E3"],
#     ["A4", "B4", "C4", "D4", "E4"],
#     ["A5", "B5", "C5", "D5", "E5"],
# ]


# # Заменить C3 на *
# # Заменить D5 на _
# # Заменить A1 на !
# # Заменить D5 на @
# # Заменить E5 на ? 

# board[2][2] = "*"

# for row in board:
#     print(*row)



# УСЛОВИЯ if/elif/else

# s = "BCDEFG"

# if "A" in s:
#     print("A in s")

# if "B" in s:
#     print("B in s")

# if "C" in s:
#     print("C in s")
# # else:
# #     print("else")



# Дается число от 1 до 100
# выделить 4 промежутка
# 1 - 25
# 26 - 50
# 51 - 75
# 76 - 100

# if num <= 25:
#     print("1 - 25")
# elif num <= 50:
#     ...
# elif num <= 75:



fruits = []
vegetables = []
berries = []

products = ["apple", "orange", "grape", "potato", "tomato", "lemon", "plum", "blueberries", "strawberries", "pumpkin"]


for product in products:
    print("Where should we put", product)
    number = int(input("1 - fruits, 2 - vegetables, 3 - berries "))

    if number == 1:
        fruits.append(product)
    elif number == 2:
        vegetables.append(product)
    elif number == 3:
        berries.append(product)
    else:
        print("Error")


print("fruits:", fruits)
print("vegetables:", vegetables)
print("berries:", berries)

