
def count_zeros(num):
    counter = 0

    while num > 0:
        if num%27 == 0:
            counter += 1
        
        num //= 27

    return counter


for x in range(1, 27_001):
    exp = 3*27**9 + 2*27**6 + 27**3 - x

    if count_zeros(exp) == 6:
        print(x)
        break

