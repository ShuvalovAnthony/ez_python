num = 3*1024**75 + 2*256**76 - 16**77 - 2023
counter = 0

while num:
    if num%32 == 0:
        counter += 1
    num //= 32

print(counter)