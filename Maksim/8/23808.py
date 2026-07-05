from itertools import product, permutations

vars = set()

for word in permutations("КОТЕНОК"):
    word = ''.join(word)
    vars.add(word)


index = 1

for word in product(sorted("КОТЕНА"), repeat=7):
    word = ''.join(word)

    if (word in vars) and (index%2 == 1):
        print(index, word)

    index += 1