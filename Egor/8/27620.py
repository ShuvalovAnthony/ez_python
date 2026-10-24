from itertools import product


index = 1

for word in product(sorted("ЦИТРУС"), repeat=5):
    word = ''.join(word)

    if (
        # содержит ровно две буквы И
        (word.count("И") == 2) and
        # не содержит букв Ц, стоящих рядом
        ('ЦЦ' not in word)
    ):
        print(index, word)

    index += 1

    # if index == 10:
    #     break

