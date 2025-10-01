from itertools import product


index = 1

# четырёхбуквенные слова в алфавитном порядке!!!!
for word in product(sorted("АРГУМЕНТ"), repeat=4):
    word = ''.join(word)

    if (
        (len(set(word)) == len(word)) and
        (list(word) == sorted(word))
    ):
        print(index, word)

    index += 1

