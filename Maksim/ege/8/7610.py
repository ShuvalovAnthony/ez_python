from itertools import product


index = 1

for word in product(sorted("АКЛМНЯ"), repeat=5): # пятибуквенные
    word = ''.join(word)

    if word[:2] == "КМ":
        print(index, word)
        break

    index += 1