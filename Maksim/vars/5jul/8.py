from itertools import product


index = 1


for word in product(sorted("ЦИТРУС"), repeat=5):
    word = ''.join(word)
    
    if (
        word.count("И") == 2 and
        "ЦЦ" not in word
    ):
        print(index, word)

    index += 1

    # if index == 10:
    #     break
    