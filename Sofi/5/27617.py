# 3 - мин расст

for n in range(1, 1000):
    n_2 = bin(n)[2:]

    if n%3 == 0:
        n_2 += n_2[-3:]
    else:
        n_2 += bin(n%3*3)[2:]

    r = int(n_2, 2)

    if abs(r - 130) == 3:
        print(n)
        break