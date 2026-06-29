# from itertools import product


# counter = 0
# index = 1


# for word in product(sorted("ДЕКОР"), repeat=4):
#     word = ''.join(word)

#     if word[0] == "К":
#         print(index, word)
#         break


#     index += 1



for a in range(1, 10_000):
    flag = True

    for x in range(1, 10_000):
        if not (
            (x%a == 0) or
            (
                (x in range(50, 71)) <=
                (not (x%16 == 0))
            )
        ):
            flag = False
            break

    if flag:
        print(a)