from itertools import product, permutations


index = 1

# for word in permutations(sorted("ВИКТОР"), r=6):
#     word = ''.join(word)

#     if index == 170:
#         print(word)
#         break

#     index += 1


for word in product(sorted("ВИКТОР"), repeat=6):
    word = ''.join(word)

    if len(word) == len(set(word)):
        if index == 170:
            print(word)
            break

        index += 1