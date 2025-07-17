n = 555

result = ""

while n > 0:
    result += str(n%3)
    n //= 3

result = result[::-1]

print(result)
print(int(result, 3))