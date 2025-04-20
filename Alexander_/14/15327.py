n = 3*2187**2020 + 3*729**2021 - 2*81**2022 + 27**2023 - 4*3**2024 - 2029


digits = []

while n > 0:
    digits.append(n%27)
    n //= 27

digits = digits[::-1]

print(len([i for i in digits if i > 9]))
