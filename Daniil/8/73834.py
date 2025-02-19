from string import ascii_uppercase
from itertools import product


index = 1


for k in range(1, 7):
    for word in product(ascii_uppercase, repeat=k):
        word = ''.join(word)

        if word == "FEDABC":
            print(index)
            break

        index += 1