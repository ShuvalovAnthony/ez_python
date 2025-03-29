from itertools import product, permutations, combinations



# 0 1 2 3 4 5 6 7 8 9 10 = A   11 = B

counter = 0

for num in product(range(12), repeat=6):
    temp_counter = 0
    for digit in num:
        if digit > 9:
            temp_counter += 1

    if (num[0] != 0) and (num.count(7) == 1) and (temp_counter <= 3):
        counter += 1



print(counter)