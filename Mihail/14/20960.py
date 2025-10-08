def to_5(num):
    res = ''

    while num > 0:
        res += str(num%5)
        num //= 5

    return res[::-1]


data = []

for x in range(1, 2006):
    num = 5**150 + 5**98 - x

    num_5 = to_5(num)

    data.append([num_5.count('0'), x])

data = sorted(data, key=lambda x:[
    -x[0],
    -x[1]
])

for row in data[:5]:
    print(row)




