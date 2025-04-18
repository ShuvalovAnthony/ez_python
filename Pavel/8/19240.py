from itertools import product


index = 1

for word in product(sorted("ЯНВАРЬ"), repeat=5):
    word = ''.join(word)

    if (
        (word[0] != 'Я') and
        (word.count('Ь') <= 1) and
        ('ЯЯ' not in word)
    ):
        print(index)

    index += 1