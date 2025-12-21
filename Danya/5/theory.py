# перевод из 10ой в любую СС от 2 до 9

# на примере 7ричной

def to_7(num):
    res = ''

    while num > 0:
        res += str(num%7)
        num //= 7

    return res[::-1]


# перевод из 10ой в любую СС от 11 до 36 (можно и от 2х до 36)

# на примере 23ричной

from string import digits, ascii_uppercase

alph = digits + ascii_uppercase[:13] # 10 цифр + 13 букв

def to_23(num):
    res = ''

    while num > 0:
        res += alph[num%23]
        num //= 23

    return res[::-1]

# print(to_23(132456789))
# print(int("KD7CKJ", 23))



summa_cifr = sum([int(i) for i in to_7(132123123)])

print(summa_cifr)