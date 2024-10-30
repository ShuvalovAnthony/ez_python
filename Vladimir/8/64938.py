from itertools import product

def checkRow(a, b):
    # a = 1 b = 3
    return (
        ((b > a) and ((a + b)%2 == 0)) or
        ((b < a) and (a + b)%2)
    )

def checkNum(num: str):
    for i in range(len(num) - 1):
        a, b = int(num[i]), int(num[i + 1])
        if not checkRow(a, b): return False
    return True

res = {
    i: 0 for i in range(2, 12)
}

for i in range(2, 7):
    counter = 0
    for num in product("012345678", repeat=i):
        if num[0] != "0":
            counter += checkNum("".join(num))
    res[i] = counter

print(res)

# 2 5
# 3 7
# 4 9
# 5 11
# 6 13
# 7 15
# 8 17
# 9 19
# 10 21
# 11 23
