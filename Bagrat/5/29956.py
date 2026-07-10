def to_3(num):
    res = ''

    while num > 0:
        res += str(num%3)
        num //= 3

    return res[::-1]

res = []

for n in range(1, 10_000):
    tri_n = to_3(n)

    if n%3 == 0:
        tri_n = "1" + tri_n + "02"
    else:
        tri_n += to_3((n%3)*5)

    r = int(tri_n, 3)

    if r >= 177:
        print(n, r)
        # break

# Если ищем n
# min     max
# break   последнее что напечатает

# Если ищем R - создаем список res перед циклом
# добавляем в него все прошедшие условие R
# min     max
# min(res) max(res)
 