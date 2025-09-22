# data = [
#     # student_id, rus, math, inf
#     [117, 87, 99, 100],
#     [101, 87, 99, 100],
#     [102, 85, 99, 89],
#     [105, 85, 78, 95],
#     [107, 86, 78, 95],
#     [111, 70, 70, 70],
#     [112, 87, 99, 100],   
# ]

# # Сортировка по информатике
# # если инф равна то по математике
# # если оба этих равны то по русскому
# # при равенстве баллов егэ сортируем по id

# data = sorted(data, key=lambda x: [
#     -x[3],
#     -x[2],
#     -x[1],
#     x[0]
# ])

# for student in data:
#     print(student)


nums = ['ABCABCABC', 'ABCABC', 'AAAAAAAA', 'ABCAAA']

nums = sorted(nums, key=lambda x: [
    -x.count("A"),
    x.count("C")
])

print(nums)