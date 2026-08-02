# 2 .. 9

def to_6(num: int):
    res = '' # любое число не в 10чной это строка

    while num > 0:
        res += str(num%6)
        num //= 6

    return res[::-1]



# 2 .. 36 
from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:12]

def to_22(num: int):
    res = '' # любое число не в 10чной это строка

    while num > 0:
        res += alph[num%22]
        num //= 22

    return res[::-1]

num_22 = to_22(345345345345345)

# сколько цифр с числовым значением больше 12
counter = 0
for digit in num_22:
    if int(digit, 22) > 12:
        counter += 1
        print(digit)

print(counter)




num = 345345345345345

counter = 0

while num > 0:
    if num%22 > 12:
        counter += 1
    num //= 22

print(counter)