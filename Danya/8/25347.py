from itertools import product


index = 1

for word in product(sorted("ГРАНИТ"), repeat=6):
    word = ''.join(word)

    if (
        (index%2 == 1) and
        (word[0] not in "АИГ") and
        (word.count("А") == 1)
    ):
        print(index, word)
        break

    index += 1
