from itertools import product


counter = 0

for num in product("01234", repeat=6):
    num = ''.join(num) # str

    int_num = int(num, 5) # int


    if (int_num%2 == 0) and (num[0] == "3"):
        counter += 1


print(counter)
    