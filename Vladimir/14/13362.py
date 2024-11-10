num = 125 + 25**3 + 5**9

digits = []

while num > 0:
    digits.append(num%5)
    num //= 5

print(digits.count(0))