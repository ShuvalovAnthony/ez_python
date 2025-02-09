from itertools import product


counter = 0

for word in product("ЕГЭ", repeat=5):
    word = ''.join(word)

    # counter += word[0] in "ЕЭ"
    if word[0] in 'ЕЭ': # (word[0] == "Е") or (word[0] == "Э")
        counter += 1


print(counter)