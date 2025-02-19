from itertools import permutations


words = set()

def check(word: str):
    for i in "СМХ": word = word.replace(i, "Р")
    word = word.replace("О", "А")

    return ("РР" not in word) and ("АА" not in word)



for word in permutations("РОСОМАХА", r=8):
    word = ''.join(word)
    if check(word):
        words.add(word)


print(len(words))

