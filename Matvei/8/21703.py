from itertools import product, permutations, combinations


index = 1

for word in product(sorted("ПОБЕДА"), repeat=6):
    word = ''.join(word)

    if (
        (index%2 == 0) and
        (word[0] == 'О') and
        (len(set(word)) == 6)
    ):
        print(index, word)

    index += 1
