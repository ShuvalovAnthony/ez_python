from itertools import product, permutations


counter = 0
index = 1

for word in product(sorted("МУЖЧИНА"), repeat=6):
    word = ''.join(word)

    if (
        (index%2 == 0) and
        (word[0] != "Ж") and
        (word.count("Ч") <= 1)
    ):
        counter += 1

    index += 1

print(counter)