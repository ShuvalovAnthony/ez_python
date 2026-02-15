from itertools import product


index = 1

for word in product(sorted("АЛГОРИТМ"), repeat=5):
    word = ''.join(word)

    if (
        (index%2 == 0) and
        (word[0] not in "АГ") and
        (word.count("Р") >= 2)
    ):
        print(index, word)
        break

    index += 1
