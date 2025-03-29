from itertools import product


index = 1


for word in product(sorted("КОМПЬТЕР"), repeat=5):
    word = ''.join(word)

    if ("К" not in word) and (word.count('Р') == 2):
        print(index, word)

    index += 1

    
