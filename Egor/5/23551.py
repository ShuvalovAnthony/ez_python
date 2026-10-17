answ = []

for n in range(1, 1000):
    n_2 = bin(n)[2:] # ! срез обязательно

    if n%2 == 0:
        n_2 = '10' + n_2
    else:
        n_2 = '1' + n_2 + '01'

    r = int(n_2, 2)

    if r < 30:
        answ.append(n)

print(max(answ))

