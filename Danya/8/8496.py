from itertools import product


index = 1

# sorted - для алфавитного порядка
for word in product(sorted("АВОРТ"), repeat=6):
    word = ''.join(word)

    if (
        word == "ВОРОТА"
    ):
        print(index, word)

    index += 1

    # if index == 10: break