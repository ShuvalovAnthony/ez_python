from string import digits, ascii_uppercase

alf = digits + ascii_uppercase[:2]
def to_12(num):
    res = ''
    while num > 0:
        res += alf[num % 12]
        num //= 12
    return res[::-1]

for n in range(1, 10*810):
    num = to_12(n)
    if n % 4 == 0:
        num = 'A' + num + 'B'
    if n % 4 != 0:
        num = '1' + num + '0'

    r = int(num, 12)
    if r > 2025:
        print(r)
        break