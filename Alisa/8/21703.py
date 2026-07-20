from itertools import product


index = 1

for word in product(sorted("ПОБЕДА"), repeat=6):
    word = ''.join(word)
    
    if (
        (index%2 == 0) and
        (word[0] == "О") and
        (len(word) == len(set(word)))
    ):
        print(index, word)
        # break

    index += 1

    # if index == 10:
    #     break

