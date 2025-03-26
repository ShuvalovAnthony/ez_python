# int float 

# + - * / // % **

# str

# text = "Hello world!"

# print(text.lower())

# # print(text.count("a"))
# # print(text.split())
# # print(text.replace("chto", "na chto", 1))
# # print(text.find("Н"))
# # print(text.zfill(100))

# text = text.replace("H", "A")

# print(text)

# str tuple (1, 2) set() int/float

# s = "0123456789ABCDEF"

# # 01234
# print(s[:5])
# # ECA8

# print(s[-2:-9:-2])

# print(s[::-1])

# bin()[2:]
# oct()[2:]


# text = "AaaaAAaaabbsdjndfgjkdfgndfjgldfngldfgdfg"

# print(text.lower().count("a"))

# nums = [-5, 0, 2, -3, -7, 4, 11]

# print(nums)

# nums.append(7)
# nums[3] = 8
# nums.insert(1, 0)

# print(nums.count(5))
    
# print(nums)

#                 # [-7, -5, -3, 0, 2, 4, 11]
# for num in nums: # [-5, 0, 2, -3, -7, 4, 11]
#     if num == 0:
#         nums = sorted(nums)
#         print([:3]) # [-7, -5, -3]
#     print(num)


# data = [
#     # 0   1   2
#     # mat rus inf
#     [80, 90, 90],
#     [90, 95, 85],
#     [85, 85, 85],
#     [85, 86, 85],
#     [80, 70, 90],
#     [85, 70, 90],
#     [30, 100, 40]
# ]

# # IT inf mat rus


# data = sorted(data, key=lambda row:(-row[2], row[0], -row[1]))

# for row in data:
#     print(row)



data = ["fdsfdsf", "afsdfdsf", 'fdsfdsfdsfdsfdsf', 'bsdfsdf', 'caddfdsf']

data = sorted(data, key=lambda s:(len(s)))

for row in data:
    print(row)

# генераторы, функции, библиотеки