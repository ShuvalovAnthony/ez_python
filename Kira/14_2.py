counter = 0

num = 14**1402 + 28**501 - 14**51 - 1400

while num > 0:
    if num%14 == 12:
        counter += 1

    num //= 14

print(counter)

