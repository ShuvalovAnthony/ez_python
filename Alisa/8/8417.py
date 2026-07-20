from itertools import product


counter = 0


def check1(word: str):
    sogl = 0
    glas = 0

    for letter in word:
        if letter in "ЯОА":
            glas += 1
        else:
            sogl += 1

    return sogl > glas


def check2(word: str):
    for glas in "ЯОА":
        word = word.replace(glas, "_")
    
    return "__" not in word


for word in product(sorted("ЯРОСЛАВ"), repeat=5):
    word = ''.join(word)

    if (
        (len(word) == len(set(word))) and
        check1(word) and
        check2(word)
    ):
        counter += 1

print(counter)