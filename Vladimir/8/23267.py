from itertools import product

def check(num: str):
    for i in "2468":
        num = num.replace(i, "0")
    for i in "3579":
        num = num.replace(i, "1")
    return ('00' not in num) and ('11' not in num)

counter = 0

for num in product("0123456789", repeat=4):
    num = ''.join(num)

    if (
        (num[0] != '0') and
        (len(num) == len(set(num))) and
        check(num)
    ):
        counter += 1

print(counter)




from itertools import product


index = 1


for word in product(sorted("СТРОКА"), repeat=5):
    word = ''.join(word)
    
    if (
        (index%2 == 1) and
        (word[0] not in "АЛ") and
        (word.count("С") == 1)
    ):
        print(index, word)


    index += 1

