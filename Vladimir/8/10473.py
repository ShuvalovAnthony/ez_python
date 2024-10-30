# _ _ _ _ _ 1..4
from itertools import product, combinations, permutations
from string import ascii_uppercase, digits

alph = ascii_uppercase[:12]

# ABCDEFGHIJKL
# 012345678

# ord() chr()

def check(num):
    count = 0
    for digit in num:
        if digit in "JKL":
            count += 1
    return count <= 3

counter = 0

for word in product(alph, repeat=5):
    word = ''.join(word)
    if (
        (word.count("H") == 1) and
        check(word) and
        (word[0] != "A")
    ):
        counter += 1

print(counter)