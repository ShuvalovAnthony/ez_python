from itertools import product


counter = 0
index = 1


for word in product(sorted("ТЕРМИН"), repeat=10):
    word = ''.join(word)

    if (
        (index%3 == 0) and
        (word[0] in "ЕИ") and
        (word.count("Т") == 1)
    ): 
        counter += 1

    index += 1


print(counter)