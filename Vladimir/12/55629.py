def algo(s: str):
    while '00' not in s:
        s = s.replace('02', '101', 1)
        s = s.replace('11', '2', 1)
        s = s.replace('12', '21', 1)
        s = s.replace('010', '00', 1)

    return s


def summaCifr(num):
    num = int(num)
    summa = 0
    while num > 0:
        summa += num%10
        num //= 10
    return summa


def prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num%i == 0: return False
    return True


for i in range(100, 110):
    a = '0' + '12'*i + '0'
    b = algo(a)
    if prime(summaCifr(b)):
        print(i)