from itertools import product


def check(word: str):
    if len(set(word)) != len(word): return False
    
    sogl = 0
    for letter in word:
        if letter in "РСЛВ":
            sogl += 1

    if sogl < 3: return False

    for glas in "ОА":
        word = word.replace(glas, "Я")

    return "ЯЯ" not in word


counter = 0


for word in product("ЯРОСЛАВ", repeat=5):
    word = ''.join(word)
    if check(word):
        counter += 1


print(counter)