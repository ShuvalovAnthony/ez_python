from itertools import *

words = set()

# перестановки!!!
for x in permutations('парижанка'):
    x=''.join(x)
    temp = x.replace("а", "и") # создаем временную переменную так как иначе в сете удалятся одинаковые слова, которые изначально были разные
    if ("иии" not in temp) and (temp.count('ии') == 1): # иии - значит есть 2 пары гласных
        words.add(x)

print(len(words))

