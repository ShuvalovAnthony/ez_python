from itertools import product


index = 1


for word in product(sorted("ПОБЕДА"), repeat=6):
    word = ''.join(word)

    if (
        (index%2 == 0) and
        (word[0] == 'О') and
        (len(set(word)) == len(word))
    ):
        print(index, word)

    index += 1
