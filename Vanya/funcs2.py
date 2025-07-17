text = """Привет привет привет как дела? Что делаешь? Что делаешь? Кошка и две собаки, попугай, еще кошка и собака.
Очень сильно Никита просит побольше домашней работы и еще Никита хочет делать двойное сальто. Ананасы"""


# Посчитать кол-во слов, в которых гласных больше чем согласных

def glasBolshSogl(word: str):
    counter_glas = 0
    for glas in "аоеуиэюяы":
        counter_glas += word.lower().count(glas)

    return counter_glas > len(word)//2
        

for symb in "?.!":
    text = text.replace(symb, '')

words = text.split()

counter = 0

for word in words:
    if glasBolshSogl(word):
        counter += 1
    

    
print(counter)
