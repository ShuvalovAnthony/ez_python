from itertools import product


index = 1

for word in product(sorted("СТРОКА"), repeat=5):
    word = ''.join(word)

    if (
        (index%2 == 1) and (word[0] not in "АЛ") and 
        (word.count("С") == 1)
    ):
        print(index, word)

    index += 1



