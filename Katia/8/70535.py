from string import digits, ascii_uppercase
from itertools import product, permutations, combinations


alph = digits + ascii_uppercase[:2]


def check(word: str):
    if (word.count('7') != 1) or (word[0] == '0'): return False

    digit_counter = 0
    for i in "9AB":
        digit_counter += word.count(i)

    return digit_counter <= 3


counter = 0

for word in product(alph, repeat=5):
    word = ''.join(word)

    counter += check(word)


print(counter)


