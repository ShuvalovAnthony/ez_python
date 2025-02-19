from itertools import product


counter = 0

for word in product(sorted("ПЯТНИЦА"), repeat=5):
    word = ''.join(word)

    if (word[0] != "Н") and word.count("Я") == 1:
        counter += 1


print(counter)
