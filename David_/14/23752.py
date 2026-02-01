num = 2*2187**2020 + 729**2021 - 2*243**2022 + 81*2023 - 2*27**2024 - 6561

counter = 0


while num > 0:
    if num%27 > 9: 
        counter += 1

    num //= 27


print(counter)


# num = 4234535345
# counter = 0

# def convert(num: int, to_base):
#     res = []

#     if num == 0: return "0"

#     while num:
#         res.append(num%to_base)
#         num //= to_base

#     return res[::-1]

# num_27 = convert(num, 27)
# print(num_27)
# for digit in num_27:
#     if digit > 9:
#         counter += 1

# print(counter)