def to_3(n: int):
    res = ''

    while n > 0:
        res += str(n%3)
        n //= 3

    return res[::-1]


answ = []

for n in range(1, 10000):
    n_3 = to_3(n) # str

    if n%3 == 0:
        n_3 += n_3[-2:]
    else:
        n_3 += to_3(n%3*5)

    r = int(n_3, 3) # перевод в десятичную ИЗ ТРОИЧНОЙ

    if r > 150:
        answ.append(r)


print(min(answ))