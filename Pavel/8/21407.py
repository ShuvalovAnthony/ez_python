from itertools import product


counter = 0

for word in product("ДГИАШЭ", repeat=5):
    word = ''.join(word)
    
    if (
        (word[0] not in "ИАЭ") and
        (word[-1] not in "ДГШ")
    ):
        counter += 1

print(counter)


