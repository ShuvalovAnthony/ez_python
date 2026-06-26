from itertools import product


counter = 0
index = 1

def check(word: str):
    for i in "АБВГД":
        if i*2 in word:
            return False
    
    return True


def count_let(word: str):
    k = 0
    for i in "ПРСТЛ":
        k += word.count(i)

    return k <= 3


for word in product(sorted("СИНЕРГЯ"), repeat=6):
    word = ''.join(word)

    if (
        "ГИРЯ" in word
    ):
        counter += 1
        print(index, word)
        # break
        

    index += 1

    # if index == 10:
    #     break

print(counter)