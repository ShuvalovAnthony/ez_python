data = [
    # ID 4⬆️, Матем 2⬇️, Рус 3⬇️, Инф 1⬇️
    [1001, 70, 70, 85],
    [995, 70, 90, 80],
    [992, 70, 92, 80,],
    [1002, 60, 100, 90],
    [1007, 70, 70, 85],
]



data = sorted(data, key=lambda el: [
    -sum(el[1:]),
    
])


for row in data:
    print(*row)




# passed = [
#     [1, 100, 5],
#     [4, 99, 2],
#     [112, 98, 3],
#     [332, 97, 7],
#     [444, 97, 10],
# ]


# failed = [
#     [555, 97, 1],
#     [666, 97, 2],
#     [11, 96, 7],
#     [22, 80, 10],
# ]


# for row in failed:
#     if row[1] == passed[-1][1]:
#         passed.append(row)
#         failed = failed[1:]



# for row in failed:
#     print(row)