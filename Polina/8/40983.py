from itertools import permutations


def check(word: str):
    for letter in word:
        if letter*2 in word: return False
    return True


unique_words = set()


for word in permutations("ГЕОРГИЙ", r=7):
    word = ''.join(word)
    if check(word):
        unique_words.add(word)

print(len(unique_words))