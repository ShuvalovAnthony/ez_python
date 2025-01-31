from string import digits, ascii_uppercase


num = 47646578908763214234
to_base = 16

result = []

while num > 0:
    result.append(num%to_base)
    num //= to_base

result = result[::-1]

print(*result)