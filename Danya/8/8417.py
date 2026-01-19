from itertools import product, permutations


def check(word: str):
    for i in "ЯО": # все гласные меняю на А
        word = word.replace(i, "А")
    for i in "РСЛ": # все согласные меняю на В
        word = word.replace(i, "В")

    return (
        ("АА" not in word) and # гласных не должно быть рядом
        (word.count("В") > word.count("А"))
    )


counter = 0

for word in product("ЯРОСЛАВ", repeat=5): # repeat - СКОЛЬКОБУКВЕННЫЕ слова
    word = ''.join(word)
    
    if (
        len(word) == len(set(word)) and # буквы в слове/цифры в числе
                                        # не повторяются
        check(word)
    ):
        counter += 1

print(counter)

