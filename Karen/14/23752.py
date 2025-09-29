num = 2*2187**2020 + 729**2021 - 2*243**2022 + 81**2023 - 2*27**2024 - 6561


counter = 0

while num > 0:
    if num%27 > 9:
        counter += 1

    num //= 27

print(counter)