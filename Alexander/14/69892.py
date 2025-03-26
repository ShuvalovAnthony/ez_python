num = 3*289**2024 + 81*49**121 - 9*16**81 - 6011

digits = []

while num > 0:
    digits.append(num%31)
    num //= 31

print(sum([i for i in digits if i <= 17]))