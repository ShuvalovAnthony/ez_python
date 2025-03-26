from itertools import product


counter = 0

for word in product("ГЕПАРД", repeat=5):
    word = ''.join(word)

    if (word.count("Г") == 1) and (word[0] != 'А') and (word[-1] != 'Е'):
        counter += 1

print(counter)